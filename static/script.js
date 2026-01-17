// ===== CONFIGURATION =====
// When served from FastAPI, use relative URLs (same origin)
// When developing separately, use localhost:8000
const API_URL = '';

// ===== STATE =====
let messages = [];
let sources = {};
let documents = [];
let selectedDoc = null;
let customSystemPrompt = null;

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
        const requestBody = { message, include_sources: true };
        // Include custom system prompt if set
        if (customSystemPrompt) {
            requestBody.system_prompt = customSystemPrompt;
            console.log('Using custom system prompt:', customSystemPrompt.substring(0, 50) + '...');
        } else {
            console.log('Using default system prompt');
        }

        const response = await fetch(`${API_URL}/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(requestBody)
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

// Track if this is the first question in the conversation
let firstQuestionAsked = false;

function renderMessages() {
    if (messages.length === 0) {
        chatMessages.innerHTML = '';
        sampleQuestions.style.display = 'block';
        chatActions.style.display = 'none';
        firstQuestionAsked = false;
        return;
    }

    sampleQuestions.style.display = 'none';
    chatActions.style.display = 'block';

    let isFirstAssistantMsg = true;

    chatMessages.innerHTML = messages.map((msg, index) => {
        if (msg.role === 'user') {
            return `<div class="user-msg">${escapeHtml(msg.content)}</div>`;
        } else {
            const msgSources = sources[index] || [];
            let sourcesHtml = '';
            let ragInfoHtml = '';

            // Show RAG info only before the very first assistant response
            if (isFirstAssistantMsg) {
                ragInfoHtml = `
                    <div class="rag-info-text">
                        This answer is generated with Claude 3 Haiku (via AWS Bedrock) by retrieving relevant information directly from Everett's manuscripts before answering. <a href="#" onclick="switchView('about'); return false;" class="link-blue">Learn more here</a>.
                    </div>
                `;
                isFirstAssistantMsg = false;
            }

            if (msgSources.length > 0) {
                sourcesHtml = `
                    <div class="sources-toggle">
                        <button class="sources-btn" onclick="toggleSources(${index})">
                            View ${msgSources.length} sources
                        </button>
                        <div class="sources-list" id="sources-${index}">
                            ${msgSources.map((s, i) => `
                                <div class="source-item source-clickable" onclick="openSourceInArchive('${escapeAttr(s.filename || s.title + '.md')}', '${escapeAttr((s.excerpt || '').substring(0, 200))}')">
                                    <div class="source-title"><span class="source-number">${i + 1}.</span> ${escapeHtml(s.title)} <span class="source-relevance">— ${(s.relevance * 100).toFixed(0)}%</span></div>
                                    <div class="source-excerpt">${escapeHtml((s.excerpt || '').substring(0, 200))}...</div>
                                </div>
                            `).join('')}
                            <button class="sources-close-btn" onclick="toggleSources(${index})">Close</button>
                        </div>
                    </div>
                `;
            }

            return `
                ${ragInfoHtml}
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

function escapeAttr(text) {
    // Escape text for use in HTML attributes
    return text.replace(/'/g, "\\'").replace(/"/g, '&quot;').replace(/\n/g, ' ');
}

// Store the excerpt to highlight when opening a source in archive
let highlightExcerpt = null;

async function openSourceInArchive(filename, excerpt) {
    // Switch to archive view on the same page
    switchView('archive');

    // Wait for documents to load if not already loaded
    if (documents.length === 0) {
        await loadDocuments();
    }

    if (!filename) return;

    // Normalize the search term - handle both underscores and spaces
    const normalizedSearch = filename.replace('.md', '').toLowerCase();
    const withUnderscores = normalizedSearch.replace(/ /g, '_');
    const withSpaces = normalizedSearch.replace(/_/g, ' ');

    // Try to find the document using multiple strategies
    let doc = documents.find(d => d.filename === filename);

    if (!doc) {
        doc = documents.find(d => d.filename.toLowerCase() === filename.toLowerCase());
    }

    if (!doc) {
        doc = documents.find(d => {
            const docFileLower = d.filename.toLowerCase();
            const docTitleLower = d.title.toLowerCase();
            return docFileLower.includes(withUnderscores) ||
                   docFileLower.includes(withSpaces) ||
                   docTitleLower.includes(withUnderscores) ||
                   docTitleLower.includes(withSpaces) ||
                   withUnderscores.includes(docTitleLower.replace(/ /g, '_')) ||
                   withSpaces.includes(docTitleLower);
        });
    }

    if (doc) {
        await selectDocument(doc);
        if (excerpt) {
            setTimeout(() => {
                highlightAndScrollToExcerpt(excerpt);
            }, 300);
        }
    }
}

// Handle URL parameters to open specific document on page load
async function handleUrlParameters() {
    const params = new URLSearchParams(window.location.search);
    const view = params.get('view');
    const docFilename = params.get('doc');
    const highlight = params.get('highlight');

    if (view === 'archive') {
        // Update nav links manually (don't use switchView to avoid race condition)
        document.querySelectorAll('.nav-link').forEach(link => {
            link.classList.toggle('active', link.dataset.view === 'archive');
        });
        document.querySelectorAll('.view').forEach(v => {
            v.classList.toggle('active', v.id === 'archive-view');
        });

        // Always load documents for archive view
        const docCountEl = document.getElementById('doc-count');
        try {
            docCountEl.textContent = 'Loading documents...';
            const response = await fetch(`${API_URL}/documents`);
            if (!response.ok) throw new Error('Failed to load documents');
            documents = await response.json();
            renderDocumentList();
            populateYearFilter();
        } catch (error) {
            console.error('Error loading documents:', error);
            docCountEl.textContent = 'Error loading documents. Make sure the backend is running.';
            return;
        }

        // If a specific document was requested, open it
        if (docFilename && documents.length > 0) {
            // Decode the filename in case it was URL encoded
            const decodedFilename = decodeURIComponent(docFilename);
            console.log('Looking for document:', decodedFilename);
            console.log('Available documents:', documents.map(d => d.filename));

            // Find the document by exact filename match
            let doc = documents.find(d => d.filename === decodedFilename);

            // Try finding by case-insensitive match
            if (!doc) {
                doc = documents.find(d =>
                    d.filename.toLowerCase() === decodedFilename.toLowerCase()
                );
            }

            // Try finding by title (filename without .md extension)
            if (!doc) {
                const titleFromFilename = decodedFilename.replace('.md', '');
                doc = documents.find(d => d.title === titleFromFilename);
            }

            // Try finding by partial/fuzzy match
            if (!doc) {
                const searchTerm = decodedFilename.replace('.md', '').toLowerCase();
                doc = documents.find(d =>
                    d.title.toLowerCase().includes(searchTerm) ||
                    d.filename.toLowerCase().includes(searchTerm) ||
                    searchTerm.includes(d.title.toLowerCase())
                );
            }

            console.log('Found document:', doc);

            if (doc) {
                await selectDocument(doc);
                if (highlight) {
                    const decodedHighlight = decodeURIComponent(highlight);
                    setTimeout(() => {
                        highlightAndScrollToExcerpt(decodedHighlight);
                    }, 500);
                }
            } else {
                console.log('Document not found for:', decodedFilename);
            }
        }
    }
}

function highlightAndScrollToExcerpt(excerpt) {
    if (!excerpt) return;

    const viewer = document.querySelector('.doc-viewer-content');
    if (!viewer) return;

    // Remove any previous highlights
    viewer.querySelectorAll('.highlight-source').forEach(el => {
        el.outerHTML = el.innerHTML;
    });

    const excerptText = excerpt.trim();
    let found = false;

    // Try to find and highlight the excerpt text
    // First try the full excerpt, then progressively shorter portions
    let searchLengths = [excerptText.length, 80, 60, 40];

    for (let len of searchLengths) {
        if (found) break;
        const searchText = excerptText.substring(0, Math.min(len, excerptText.length));
        if (searchText.length < 20) continue;

        // Search through text nodes
        const walker = document.createTreeWalker(viewer, NodeFilter.SHOW_TEXT, null, false);
        let node;

        while ((node = walker.nextNode())) {
            const nodeText = node.textContent;
            const matchIndex = nodeText.toLowerCase().indexOf(searchText.toLowerCase());

            if (matchIndex !== -1) {
                // Found the text in this node - highlight it
                const before = nodeText.substring(0, matchIndex);
                const match = nodeText.substring(matchIndex, matchIndex + searchText.length);
                const after = nodeText.substring(matchIndex + searchText.length);

                const wrapper = document.createElement('span');
                wrapper.innerHTML = escapeHtml(before) +
                    '<span class="highlight-source" id="highlighted-source">' + escapeHtml(match) + '</span>' +
                    escapeHtml(after);

                node.parentNode.replaceChild(wrapper, node);

                // Scroll to the highlighted element
                const highlighted = document.getElementById('highlighted-source');
                if (highlighted) {
                    highlighted.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
                found = true;
                break;
            }
        }
    }

    // If not found, scroll to top
    if (!found) {
        viewer.scrollTop = 0;
    }
}

function escapeRegExp(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
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

// ===== SYSTEM PROMPT =====
const DEFAULT_SYSTEM_PROMPT = `You are a friendly guide helping researchers and students explore Hugh Everett III's manuscripts and the development of the Many-Worlds Interpretation of quantum mechanics.

You have access to Everett's original handwritten drafts, thesis versions, correspondence with physicists like John Wheeler and Bryce DeWitt, and various notes from 1955-1957.

When answering questions about the manuscripts:
1. Ground your responses in the manuscript content provided
2. Quote relevant passages when helpful
3. Cite specific documents (e.g., "In his handwritten draft from 1955...")
4. Explain historical and scientific context when relevant

IMPORTANT: If the user asks a general question like "What's this?", "Hello", "Hi", or anything not specifically about the manuscripts, DO NOT apologize or ask them to provide excerpts. Instead, warmly welcome them and explain:

"Welcome! This is an interactive tool for exploring Hugh Everett III's original manuscripts on quantum mechanics. Everett developed the Many-Worlds Interpretation in the 1950s, proposing that the quantum wave function never collapses—instead, all possible outcomes occur in branching parallel realities.

You can ask me questions like:
• What was Everett's key insight about measurement?
• What is the 'relative state' formulation?
• How did Wheeler respond to Everett's thesis?
• What criticisms did Everett's theory face?"

Never say things like "I don't have any excerpts" or "please provide manuscript content." The system automatically retrieves relevant content—if none is found, just answer helpfully based on what you know about Everett.`;

function initSystemPrompt() {
    const useBtn = document.getElementById('use-system-prompt-btn');
    const resetBtn = document.getElementById('reset-system-prompt-btn');
    const promptInput = document.getElementById('system-prompt-input');

    // Load any saved system prompt from localStorage
    const savedPrompt = localStorage.getItem('customSystemPrompt');
    if (savedPrompt && promptInput) {
        promptInput.value = savedPrompt;
        customSystemPrompt = savedPrompt;
        console.log('Loaded custom system prompt from localStorage');
    } else {
        console.log('No custom system prompt saved');
    }

    if (useBtn && promptInput) {
        useBtn.addEventListener('click', () => {
            const newPrompt = promptInput.value.trim();
            if (!newPrompt) {
                alert('Please enter a system prompt.');
                return;
            }

            // Store locally - this will be sent with each chat request
            customSystemPrompt = newPrompt;
            localStorage.setItem('customSystemPrompt', newPrompt);
            console.log('System prompt saved:', newPrompt.substring(0, 50) + '...');

            useBtn.textContent = 'System prompt updated!';
            useBtn.style.background = '#4a9eff';
            setTimeout(() => {
                useBtn.textContent = 'Use this system prompt';
                useBtn.style.background = '';
            }, 2000);
        });
    }

    if (resetBtn && promptInput) {
        resetBtn.addEventListener('click', () => {
            // Clear from localStorage and reset to default
            localStorage.removeItem('customSystemPrompt');
            customSystemPrompt = null;
            promptInput.value = DEFAULT_SYSTEM_PROMPT;
            console.log('System prompt reset to default');

            resetBtn.textContent = 'Reset to default!';
            setTimeout(() => {
                resetBtn.textContent = 'Reset to default';
            }, 2000);
        });
    }
}

// ===== INITIALIZATION =====
document.addEventListener('DOMContentLoaded', () => {
    renderMessages();
    initSystemPrompt();
    handleUrlParameters();
});

