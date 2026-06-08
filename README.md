# About This Project

The model was trained on original documents including draft and final versions of Everett's long and short Ph.D. theses, his early notes that led to these published works, his correspondence regarding his relative state formulation of pure wave mechanics, and miscellaneous biographical material. These documents were discovered by investigative journalist [**Peter Byrne**](https://www.peterbyrne.info), Petaluma, CA in 2007 in the Los Angeles basement of Everett's son, Mark Everett. The original documents were digitized with support from National Science Foundation Grant #0924135. The collection is edited by [**Jeffrey A. Barrett**](https://faculty.sites.uci.edu/jeffreybarrett/), Peter Byrne, and [**James O. Weatherall**](https://jamesowenweatherall.com). It is housed at the University of California Calisphere and can be found at https://calisphere.org/collections/28/. This project is designed to explore the intellectual history of Hugh Everett III via Retrieval-Augmented Generation (RAG) by allowing you to converse with his private manuscripts, drafts, and personal correspondence.

## How It Works

Retrieval-Augmented Generation (RAG) is an AI architecture that gives Large Language Models (LLMs) access to specific documents at query time: in this case, the Everett Manuscripts. The responses are generated with Claude Haiku 4.5 by retrieving relevant information directly from Everett's manuscripts before answering. The manuscripts are split into sections called chunks—small passages of roughly 250 tokens each that preserve semantic coherence.

These chunks are converted into numerical representations called embeddings using Amazon Titan Embed Text v2, a model that encodes text as 1024-dimensional vectors. These vectors capture semantic meaning: chunks about similar topics will have vectors that are close together in this high-dimensional space. All 4,221 chunk embeddings are stored in a FAISS index, an efficient similarity search library.

When you ask a question, that question is also converted into an embedding using the same Titan model. FAISS then finds the chunks whose embeddings are most similar to your question's embedding using cosine similarity. The most relevant chunks—those that pass a similarity threshold—are then passed to Claude Haiku 4.5 as context, along with your question. Claude reads this context and generates an answer grounded in Everett's actual words, citing the specific manuscripts where the information was found.

## Hugh Everett III & the Many-Worlds Interpretation

[**Hugh Everett III**](https://en.wikipedia.org/wiki/Hugh_Everett_III) (1930–1982) was an American physicist who, as a graduate student at Princeton in 1956, proposed the Relative State formulation of quantum mechanics.

In an era dominated by the Copenhagen Interpretation, which argued that the act of observation "collapses" a quantum wave into a single reality, Everett proposed something radical: the wave function never collapses. Instead, it continues to evolve, and every possible outcome of a quantum event occurs in a branching series of relative states.

While his theory was largely ignored or ridiculed during his life, leading him to leave academia for a career in military defense analysis, it was later popularized as the **Many-Worlds Interpretation**. Today, it is considered one of the most important and controversial pillars of modern physics.

## The Archive

The digital collection includes:

- **The Long Thesis:** The original, 137-page unedited draft of Everett's work, which contains philosophical metaphors and mathematical proofs that were sanitized or removed for his final 1957 publication.
- **Handwritten minipapers:** Early, raw notes where Everett first wrestled with the problem of probability and observers.
- **Correspondence:** Private letters between Everett, his advisor John Wheeler, and other physicists like Niels Bohr and Bryce DeWitt.

## DeepSeek-OCR

The primary challenge of this project was the nature of the source material: 1950s-era handwritten notes, faded typewritten drafts, and complex mathematical notation. Traditional OCR tools often fail on these documents due to noise, low contrast, and non-standard layouts.

To solve this, I utilized [**DeepSeek-OCR**](https://huggingface.co/deepseek-ai/DeepSeek-OCR), a cutting-edge Vision-Language Model (VLM). Unlike standard OCR, DeepSeek-OCR treats the entire page as a visual context, allowing it to "read" Everett's unique cursive and technical shorthand with high fidelity. It was specifically chosen for its ability to recognize and format scientific notation (LaTeX), ensuring that Everett's crucial derivations for the "Universal Wavefunction" remained intact during transcription. The model outputs Markdown, preserving the logical structure of the manuscripts including headers, bullet points, and equations, which is essential for the RAG system to understand the relationship between different ideas.

## Google Colab for Students

This project used free Google Colab for students for compute to process over 5,000 pages of high-resolution manuscript images. For more information, see [**here**](https://blog.google/outreach-initiatives/education/colab-higher-education/?s=09).
