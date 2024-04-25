import streamlit as st
import chromadb
from chromadb.utils import embedding_functions
import re
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import nltk

# Set Streamlit page configuration
st.set_page_config(
    page_title="Movie Verse",
    page_icon=":clapper:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dark background and white/red colors
custom_css = """
<style>
body {
    background-color: #000000;
    color: #FFFFFF;
    font-family: Arial, sans-serif;
}
.stTextInput > div > div > div > input {
    border-radius: 20px;
    border: 2px solid #FFFFFF;
    padding: 10px;
    outline: none;
    color: #FFFFFF;
}
.stButton>button {
    border-radius: 20px;
    background-color: #FF0000;
    color: #FFFFFF;
    font-weight: bold;
    padding: 10px 20px;
}
.stButton>button:hover {
    background-color: #FF4500;
}
.stDataFrame {
    color: #FF0000;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Initialize ChromaDB client
chroma_client = chromadb.PersistentClient(path="C:/Users/hp/my_chromadb2")

# DistilBERT model for embedding function
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# Get or create the collection
collection = chroma_client.get_or_create_collection(name="my_collection", embedding_function=sentence_transformer_ef, metadata={"hnsw:space": "cosine"})

# Download stopwords if not already downloaded
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

def preprocess(text):
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    # Remove special characters
    text = re.sub(r'[^A-Za-z\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Remove stopwords
    text = ' '.join(word for word in text.split() if word not in stop_words)
    # Remove extra spaces and line breaks
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def main():
    st.title("🎬 Movie Verse 🎥")

    # Getting the user input
    user_query = st.text_input("Hey buddy, type your query and I will search movies for you:")

    if st.button("Search"):
        if user_query:
            # Preprocess the user query
            user_query = preprocess(user_query)

            # Query the collection
            results = collection.query(
                query_texts=[user_query],
                n_results=10,
                include=['documents', 'distances', 'metadatas']
            )

            # Display user input
            st.write(f"Your search query: {user_query}")

            # Display output documents
            st.write("Search Results:")
            for i, (document, metadata) in enumerate(zip(results['documents'][0], results['metadatas'][0]), 1):
                item_id = metadata.get('item_id', 'Not available')
                st.write(f"{i}. Item ID: {item_id}, Document: {document}")

if __name__ == "__main__":
    main()

