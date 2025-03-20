# SearchRelevance
Estimates and ranks search results based on semantic similarity to the query.
# Dynamic Bing Search Relevance Evaluator

This project implements a search relevance evaluator that dynamically retrieves live search results from Bing and ranks them based on semantic similarity to a user’s query. By integrating **Beautiful Soup for web scraping**, and **Sentence Transformers**, this tool demonstrates modern techniques in search relevance and real-time data processing.

## Watch a Demo
[Demo](https://drive.google.com/file/d/1htw3360nwyYCtiBVDgrMpVhKBTsQ5Ej7/view?usp=sharing)

## Technical Challenges Solved
- **Dynamic Data Integration:** Fetches up-to-date search results from Bing and extracts useful content with **Beautiful Soup**.
- **Web Scraping for Contextual Data:** Extracts page titles, metadata, and summaries from search result URLs to enrich the ranking process.
- **Semantic Similarity Ranking:** Utilizes **pre-trained Sentence Transformers** to compute and rank search results based on similarity to the input query.
- **Interactive Interface:** Leverages **Gradio** to build a responsive web interface that displays ranked search results in real time.

## Features
- **Live Search Results:** Retrieves real-time search results from Bing for any given query.
- **Web Scraping for Additional Context:** Extracts relevant content snippets from search result pages using **Beautiful Soup**.
- **Relevance-Based Ranking:** Ranks search results using **cosine similarity** between query and result embeddings.
- **User-Friendly Interface:** Provides a simple, interactive web app built with **Gradio**.
- **Modular Architecture:** Easily extendable to include additional features or alternative ranking algorithms.

## Installation
Ensure you have Python installed, then install the necessary dependencies:

```bash
python3 -m pip install gradio sentence-transformers requests beautifulsoup4 lxml
