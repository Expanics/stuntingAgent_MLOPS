import os
import chromadb
from chromadb.utils import embedding_functions
from typing import List, Optional

class RAGEngine:
    def __init__(self, data_dir: str = "data", collection_name: str = "stunting_knowledge_local"):
        self.data_dir = data_dir
        self.collection_name = collection_name
        
        # Initialize ChromaDB Client
        # Using persistent client to save data to disk
        self.client = chromadb.PersistentClient(path="./chroma_db")
        
        # Setup Local SentenceTransformer Embedding Function
        # "all-MiniLM-L6-v2" is a small, fast, and effective model for general purpose
        print("Loading local embedding model (sentence-transformers/all-MiniLM-L6-v2)...")
        self.embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
        
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            embedding_function=self.embedding_fn
        )
        
        # Check if collection is empty, if so, load data
        if self.collection.count() == 0:
            print("Collection empty. Loading documents...")
            self.load_documents()
        else:
            print(f"Collection loaded with {self.collection.count()} documents.")

    def load_documents(self):
        """Reads text files from data_dir and adds them to ChromaDB."""
        if not os.path.exists(self.data_dir):
            print(f"Data directory {self.data_dir} not found.")
            return

        documents = []
        metadatas = []
        ids = []
        
        file_count = 0
        for filename in os.listdir(self.data_dir):
            if filename.endswith(".txt"):
                file_path = os.path.join(self.data_dir, filename)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        
                    # Simple chunking by paragraphs
                    chunks = [c.strip() for c in content.split('\n\n') if c.strip()]
                    
                    for i, chunk in enumerate(chunks):
                        documents.append(chunk)
                        metadatas.append({"source": filename, "chunk_id": i})
                        ids.append(f"{filename}_{i}")
                    
                    file_count += 1
                except Exception as e:
                    print(f"Error reading {filename}: {e}")

        if documents:
            self.collection.add(
                documents=documents,
                metadatas=metadatas,
                ids=ids
            )
            print(f"Successfully indexed {len(documents)} chunks from {file_count} files.")

    def retrieve(self, query: str, n_results: int = 3) -> str:
        """Retrieves relevant context for a query."""
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        
        # Flatten results
        retrieved_texts = []
        if results['documents']:
            for doc_list in results['documents']:
                retrieved_texts.extend(doc_list)
        
        return "\n\n".join(retrieved_texts)

if __name__ == "__main__":
    # Test run
    rag = RAGEngine(data_dir="../data") 
    print("Testing Retrieval:")
    print(rag.retrieve("Berapa angka stunting 2024?"))
