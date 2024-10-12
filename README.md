# 📰 K-Nearest Neighbor (kNN) Semantic Search with ElasticSearch and OpenAI Embeddings

Welcome to the **kNN Semantic Search Model**! This project demonstrates how to implement a powerful k-Nearest Neighbor (kNN) search using **ElasticSearch (local)** and OpenAI's **text-embedding-ada-002** model. The project focuses on semantic search using a small dataset of news articles.

## 🌟 Project Overview

In this project, we leverage OpenAI's advanced embedding model to convert text from news articles into vector embeddings. These embeddings are then indexed in ElasticSearch, allowing for fast and efficient kNN-based semantic search. The steps involve:

1. **Input Data**: We use a dataset of news articles (`news_1.csv`).
2. **Embeddings Generation**: Text data is processed through OpenAI's `text-embedding-ada-002` model to generate embeddings, stored in `embedded_1.csv`.
3. **ElasticSearch Integration**: We use ElasticSearch to index the embeddings and perform semantic search using k-Nearest Neighbors (kNN).

## 🔧 Technologies Used

- **ElasticSearch** (Local): For indexing and performing the kNN search.
- **OpenAI's `text-embedding-ada-002` model**: To convert raw text into semantic embeddings.
- **Python**: For data processing, embedding generation, and ElasticSearch integration.

## 📂 Project Structure

- `news_1.csv`: The dataset containing news articles used as input data.
- `embedded_1.csv`: The generated embeddings from OpenAI's embedding model.
- `knn_search.py`: The script that integrates ElasticSearch and performs kNN search queries.
- `README.md`: This file, explaining the project details and setup instructions.

## 🚀 Getting Started

To get this project up and running on your local machine, follow these steps:

### Prerequisites

- Python 3.x
- ElasticSearch installed locally (for instructions, visit the [ElasticSearch Setup Guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html)).
- OpenAI API key (you can obtain this by signing up at [OpenAI's platform](https://platform.openai.com)).

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/knn-semantic-search.git
   cd knn-semantic-search
