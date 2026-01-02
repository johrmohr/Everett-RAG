// ===== CONFIGURATION =====
// When served from FastAPI, use relative URLs (same origin)
// When developing separately, use localhost:8000
const API_URL = '';

// ===== STATE =====
let messages = [];
let sources = {};
let documents = [];
let selectedDoc = null;

// ===== DOM ELEMENTS =====
const views = document.querySelectorAll('.view');
const navLinks = document.querySelectorAll('.nav-link');
const chatMessages = document.getElementById('chat-messages');
const chatInput = document.getElementById('chat-input');
const clearBtn = document.getElementById('clear-btn');
const chatActions = document.querySelector('.chat-actions');
const sampleQuestions = document.getElementById('sample-questions');
const loading = document.getElementById('loading');

// ===== NAVIGATION =====
navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const viewId = link.dataset.view;
        switchView(viewId);
    });
});

function switchView(viewId) {
    // Update nav links
    navLinks.forEach(link => {
        link.classList.toggle('active', link.dataset.view === viewId);
    });

    // Update views
    views.forEach(view => {
        view.classList.toggle('active', view.id === `${viewId}-view`);
    });

    // Scroll to top when switching views
    window.scrollTo(0, 0);

    // Load archive documents if switching to archive
    if (viewId === 'archive' && documents.length === 0) {
        loadDocuments();
    }
}

// ===== CHAT FUNCTIONALITY =====
chatInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});

clearBtn.addEventListener('click', clearConversation);

document.querySelectorAll('.sample-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const question = btn.dataset.question;
        chatInput.value = question;
        sendMessage();
    });
});

async function sendMessage() {
    const message = chatInput.value.trim();
    if (!message) return;

    // Add user message
    messages.push({ role: 'user', content: message });
    renderMessages();
    chatInput.value = '';

    // Hide sample questions
    sampleQuestions.style.display = 'none';

    // Show inline loading indicator
    const loadingEl = document.createElement('div');
    loadingEl.className = 'loading-inline';
    loadingEl.innerHTML = '<div class="spinner-small"></div><span>Searching the archives...</span>';
    chatMessages.appendChild(loadingEl);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    try {
        const response = await fetch(`${API_URL}/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message, include_sources: true })
        });

        if (!response.ok) throw new Error('API request failed');

        const data = await response.json();

        // Add assistant message
        const msgIndex = messages.length;
        messages.push({ role: 'assistant', content: data.answer });
        sources[msgIndex] = data.sources || [];

        renderMessages();
    } catch (error) {
        messages.push({
            role: 'assistant',
            content: `⚠️ Error: ${error.message}. Make sure the backend server is running.`
        });
        renderMessages();
    } finally {
        // Remove inline loading (renderMessages will have replaced the content)
        loadingEl.remove();
    }
}

function renderMessages() {
    if (messages.length === 0) {
        chatMessages.innerHTML = '';
        sampleQuestions.style.display = 'block';
        chatActions.style.display = 'none';
        return;
    }

    sampleQuestions.style.display = 'none';
    chatActions.style.display = 'block';
    
    chatMessages.innerHTML = messages.map((msg, index) => {
        if (msg.role === 'user') {
            return `<div class="user-msg">${escapeHtml(msg.content)}</div>`;
        } else {
            const msgSources = sources[index] || [];
            let sourcesHtml = '';
            
            if (msgSources.length > 0) {
                sourcesHtml = `
                    <div class="sources-toggle">
                        <button class="sources-btn" onclick="toggleSources(${index})">
                            View ${msgSources.length} sources
                        </button>
                        <div class="sources-list" id="sources-${index}">
                            ${msgSources.map(s => `
                                <div class="source-item">
                                    <div class="source-title">${escapeHtml(s.title)} <span class="source-relevance">— ${(s.relevance * 100).toFixed(0)}%</span></div>
                                    <div class="source-excerpt">${escapeHtml(s.excerpt.substring(0, 200))}...</div>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                `;
            }
            
            return `
                <div class="assistant-msg">
                    ${formatMarkdown(msg.content)}
                    ${sourcesHtml}
                </div>
            `;
        }
    }).join('');
    
    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function toggleSources(index) {
    const sourcesList = document.getElementById(`sources-${index}`);
    sourcesList.classList.toggle('open');
}

async function clearConversation() {
    messages = [];
    sources = {};
    renderMessages();
    
    try {
        await fetch(`${API_URL}/conversation/clear`, { method: 'POST' });
    } catch (e) {
        // Ignore errors
    }
}

// ===== ARCHIVE FUNCTIONALITY =====
async function loadDocuments() {
    try {
        const response = await fetch(`${API_URL}/documents`);
        if (!response.ok) throw new Error('Failed to load documents');

        documents = await response.json();
        renderDocumentList();
        populateYearFilter();
    } catch (error) {
        document.getElementById('doc-count').textContent = 'Error loading documents. Make sure the backend is running.';
    }
}

function renderDocumentList() {
    const typeFilter = document.getElementById('filter-type').value;
    const yearFilter = document.getElementById('filter-year').value;
    const searchFilter = document.getElementById('filter-search').value.toLowerCase();
    
    const filtered = documents.filter(doc => {
        const matchType = typeFilter === 'All' || doc.type === typeFilter;
        const matchYear = yearFilter === 'All' || doc.year === yearFilter;
        const matchSearch = !searchFilter || doc.title.toLowerCase().includes(searchFilter);
        return matchType && matchYear && matchSearch;
    }).sort((a, b) => {
        // Sort by year (documents without year go to end)
        const yearA = a.year === '—' ? 9999 : parseInt(a.year);
        const yearB = b.year === '—' ? 9999 : parseInt(b.year);
        if (yearA !== yearB) return yearA - yearB;
        // Secondary sort by title
        return a.title.localeCompare(b.title);
    });
    
    document.getElementById('doc-count').textContent = `Showing ${filtered.length} of ${documents.length} documents`;
    
    const docList = document.getElementById('doc-list');
    docList.innerHTML = filtered.map(doc => `
        <button class="doc-list-item ${selectedDoc?.filename === doc.filename ? 'active' : ''}"
                data-filename="${escapeHtml(doc.filename)}">
            ${escapeHtml(doc.title)}
        </button>
    `).join('');
    
    // Add click handlers
    docList.querySelectorAll('.doc-list-item').forEach(item => {
        item.addEventListener('click', () => {
            const filename = item.dataset.filename;
            const doc = documents.find(d => d.filename === filename);
            if (doc) selectDocument(doc);
        });
    });

}

async function selectDocument(doc) {
    selectedDoc = doc;

    // Update active state in list
    document.querySelectorAll('.doc-list-item').forEach(item => {
        item.classList.toggle('active', item.dataset.filename === doc.filename);
    });
    
    const viewer = document.getElementById('doc-viewer');
    viewer.innerHTML = '<div class="doc-viewer-placeholder">Loading...</div>';
    
    try {
        const response = await fetch(`${API_URL}/documents/${encodeURIComponent(doc.filename)}`);
        if (!response.ok) throw new Error('Failed to load document');
        
        const data = await response.json();
        
        viewer.innerHTML = `
            <div class="doc-viewer-inner">
                <div class="doc-viewer-header">
                    <div class="doc-viewer-title">${escapeHtml(doc.title)}</div>
                    <div class="doc-viewer-meta">Type: ${doc.type} | Year: ${doc.year}</div>
                </div>
                <div class="doc-viewer-content">${formatMarkdown(data.content)}</div>
                <button class="btn-secondary doc-download-btn" onclick="downloadDocument('${doc.filename}')">
                    Download
                </button>
            </div>
        `;

        // Render math notation
        const contentEl = viewer.querySelector('.doc-viewer-content');
        if (contentEl) renderMath(contentEl);
    } catch (error) {
        viewer.innerHTML = `<div class="doc-viewer-placeholder">Error loading document: ${error.message}</div>`;
    }
}

function downloadDocument(filename) {
    const doc = documents.find(d => d.filename === filename);
    if (!doc) return;
    
    fetch(`${API_URL}/documents/${encodeURIComponent(filename)}`)
        .then(r => r.json())
        .then(data => {
            const blob = new Blob([data.content], { type: 'text/markdown' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            a.click();
            URL.revokeObjectURL(url);
        });
}

function populateYearFilter() {
    const years = [...new Set(documents.map(d => d.year).filter(y => y !== '—'))].sort();
    const select = document.getElementById('filter-year');
    select.innerHTML = '<option value="All">All Years</option>' + 
        years.map(y => `<option value="${y}">${y}</option>`).join('');
}

// Filter event listeners
document.getElementById('filter-type')?.addEventListener('change', renderDocumentList);
document.getElementById('filter-year')?.addEventListener('change', renderDocumentList);
document.getElementById('filter-search')?.addEventListener('input', renderDocumentList);

// ===== UTILITIES =====
function showLoading() {
    loading.classList.remove('hidden');
}

function hideLoading() {
    loading.classList.add('hidden');
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function formatMarkdown(text) {
    // Use marked.js if available, otherwise fallback to simple formatting
    if (typeof marked !== 'undefined') {
        // Protect LaTeX from marked by temporarily replacing it
        const mathPlaceholders = [];

        // Protect display math \[...\]
        text = text.replace(/\\\[([\s\S]*?)\\\]/g, (match) => {
            mathPlaceholders.push(match);
            return `%%MATH_DISPLAY_${mathPlaceholders.length - 1}%%`;
        });

        // Protect inline math \(...\)
        text = text.replace(/\\\(([\s\S]*?)\\\)/g, (match) => {
            mathPlaceholders.push(match);
            return `%%MATH_INLINE_${mathPlaceholders.length - 1}%%`;
        });

        // Protect display math $$...$$
        text = text.replace(/\$\$([\s\S]*?)\$\$/g, (match) => {
            mathPlaceholders.push(match);
            return `%%MATH_DISPLAY_${mathPlaceholders.length - 1}%%`;
        });

        // Protect inline math $...$
        text = text.replace(/\$([^\$\n]+?)\$/g, (match) => {
            mathPlaceholders.push(match);
            return `%%MATH_INLINE_${mathPlaceholders.length - 1}%%`;
        });

        marked.setOptions({
            breaks: true,
            gfm: true
        });

        let html = marked.parse(text);

        // Restore math
        html = html.replace(/%%MATH_(DISPLAY|INLINE)_(\d+)%%/g, (match, type, index) => {
            return mathPlaceholders[parseInt(index)];
        });

        return html;
    }
    // Fallback: simple markdown formatting
    return text
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/\*(.*?)\*/g, '<em>$1</em>')
        .replace(/`(.*?)`/g, '<code>$1</code>')
        .replace(/\n/g, '<br>');
}

function renderMath(element) {
    // Render KaTeX math if available
    if (typeof renderMathInElement !== 'undefined') {
        renderMathInElement(element, {
            delimiters: [
                {left: '$$', right: '$$', display: true},
                {left: '$', right: '$', display: false},
                {left: '\\[', right: '\\]', display: true},
                {left: '\\(', right: '\\)', display: false}
            ],
            throwOnError: false,
            ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
        });
    }
}

// ===== INITIALIZATION =====
document.addEventListener('DOMContentLoaded', () => {
    renderMessages();
});

