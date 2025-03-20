from sentence_transformers import SentenceTransformer, util
from getSearch import scrape_bing_search
import gradio as gr

#simple pretrained semantic similarity model
model = SentenceTransformer('all-MiniLM-L6-v2')
search_results = [
    "Example result one.",
    "Another sample result.",
    "black man."
]
import os
import requests

#scrape bing search results for a given query

#determine similarity of results to query using embeddings
def rank_search_results(query):

    search_results = scrape_bing_search(query)
    titles = [result['title'] for result in search_results]

    # Extract summaries from the search results
    summaries = [result['summary'] for result in search_results]
    print(summaries)
    
    #compute embeddings for the query and the search results
    query_embedding = model.encode(query, convert_to_tensor=True)
    results_embeddings = model.encode(summaries, convert_to_tensor=True)
    
    #get cosine similarities
    cosine_scores = util.cos_sim(query_embedding, results_embeddings)[0]
    
    ranked_results = sorted(
        zip(titles, cosine_scores.tolist()),
        key=lambda x: x[1],
        reverse=True
    )

    return "\n".join([f"{text} (score: {score:.2f})" for text, score in ranked_results])



iface = gr.Interface(
    fn=rank_search_results,
    inputs="text",
    outputs="text",
    title="Mini Search Relevance Evaluator",
    description="Enter a search query to see how search results are ranked based on semantic similarity between summaries."
)

iface.launch(debug=True)