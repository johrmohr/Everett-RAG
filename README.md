# About This Project

This project is designed to explore the intellectual history of **Hugh Everett III**, the physicist who fundamentally changed our understanding of reality. By combining modern OCR technology with Retrieval-Augmented Generation (RAG), this system allows you to converse with Everett's private manuscripts, drafts, and personal correspondence.

## Hugh Everett III & the Many-Worlds Interpretation

[**Hugh Everett III**](https://en.wikipedia.org/wiki/Hugh_Everett_III) (1930–1982) was an American physicist who, as a graduate student at Princeton in 1956, proposed the Relative State formulation of quantum mechanics.

In an era dominated by the Copenhagen Interpretation, which argued that the act of observation "collapses" a quantum wave into a single reality, Everett proposed something radical: the wave function never collapses. Instead, it continues to evolve, and every possible outcome of a quantum event occurs in a branching series of relative states.

While his theory was largely ignored or ridiculed during his life, leading him to leave academia for a career in military defense analysis, it was later popularized as the **Many-Worlds Interpretation (MWI)**. Today, it is considered one of the most important and controversial pillars of modern physics.

## The Archive

For decades, many of Everett's original thoughts were hidden from the public. In 2007, investigative journalist **Peter Byrne** discovered a trove of documents in the Los Feliz basement of Everett's son, Mark Oliver Everett (the lead singer of the band Eels).

These documents were digitized and organized by [**Professor Jeffrey Barrett**](https://faculty.sites.uci.edu/jeffreybarrett/) (UC Irvine), the leading scholar on Everett's work. The collection includes:

- **The Long Thesis:** The original, 137-page unedited draft of Everett's work, which contains philosophical metaphors and mathematical proofs that were sanitized or removed for his final 1957 publication.
- **Handwritten minipapers:** Early, raw notes where Everett first wrestled with the problem of probability and observers.
- **Correspondence:** Private letters between Everett, his advisor John Wheeler, and other physicists like Niels Bohr and Bryce DeWitt.

## What is this RAG System?

**Retrieval-Augmented Generation (RAG)** is an AI architecture that gives a Large Language Model (LLM) a long term memory composed of specific documents: in this case, the Everett Manuscripts.

## DeepSeek-OCR

The primary challenge of this project was the nature of the source material: 1950s-era handwritten notes, faded typewritten drafts, and complex mathematical notation. Traditional OCR tools often fail on these documents due to noise, low contrast, and non-standard layouts.

To solve this, I utilized [**DeepSeek-OCR**](https://huggingface.co/deepseek-ai/DeepSeek-OCR), a cutting-edge Vision-Language Model (VLM). Unlike standard OCR, DeepSeek-OCR treats the entire page as a visual context, allowing it to "read" Everett's unique cursive and technical shorthand with high fidelity. It was specifically chosen for its ability to recognize and format scientific notation (LaTeX), ensuring that Everett's crucial derivations for the "Universal Wavefunction" remained intact during transcription. The model outputs Markdown, preserving the logical structure of the manuscripts including headers, bullet points, and equations, which is essential for the RAG system to understand the relationship between different ideas.

## Google Colab for Students

This project used free Google Colab for students for compute to process over 5,000 pages of high-resolution manuscript images. For more information, see [**here**](https://blog.google/outreach-initiatives/education/colab-higher-education/?s=09).
