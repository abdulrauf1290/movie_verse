# Movie Subtitle Search Engine

![Movie Subtitle Search Engine Logo](https://your-website.com/movie-subtitle-search-engine-logo.png)

## Introduction

The Movie Subtitle Search Engine is a powerful tool designed to help users find movie subtitles quickly and efficiently. This project consists of two main parts: ingesting documents and retrieving documents.

## Part 1: Ingesting Documents

1. **Read Data**: Read the given database file containing movie subtitles.
2. **Database Inspection**: Examine the README.txt file to understand the contents of the database.
3. **Data Decoding**: Take care to decode the files inside the database.
4. **Data Sampling**: If compute resources are limited, randomly sample 30% of the data.
5. **Text Cleaning**: Apply appropriate cleaning steps to preprocess the subtitle documents.
6. **Text Vectorization**:
   - **BOW / TFIDF**: Generate sparse vector representations for the subtitle documents.
   - **BERT-based SentenceTransformers**: Generate embeddings to encode semantic information.
7. **Document Chunker**: Implement a document chunker to address the challenge of embedding large documents. This involves dividing large documents into smaller, more manageable chunks.
   - Set token windows and overlapping windows to handle large documents effectively.
8. **ChromaDB Integration**: Store the generated embeddings in a ChromaDB database for efficient retrieval.

## Part 2: Retrieving Documents

1. **User Query**: Take the user's search query as input.
2. **Query Preprocessing**: Preprocess the user query if required.
3. **Query Embedding**: Create an embedding for the user query.
4. **Document Retrieval**:
   - **Cosine Similarity**: Calculate the similarity score between the query embedding and the embeddings of documents using cosine distance.
   - Return the most relevant candidate documents based on cosine similarity scores.

## Usage

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Follow the steps outlined in the README to ingest and retrieve documents.
4. Enjoy fast and efficient movie subtitle search capabilities!

## Feedback

We welcome your feedback and suggestions! If you have any questions, concerns, or ideas for improvement, please don't hesitate to reach out.

## License

This project is licensed under the [MIT License](LICENSE).

Happy searching! 🎬🔍
