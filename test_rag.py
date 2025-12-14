import sys
import os
from dotenv import load_dotenv

# Load .env from stunting_agent directory
load_dotenv(os.path.join(os.getcwd(), "stunting_agent", ".env"))

# Add current directory to path
sys.path.append(os.getcwd())

# Add stunting_agent directory to path
sys.path.append(os.path.join(os.getcwd(), "stunting_agent"))

try:
    import rag as rag_module
    RAGEngine = rag_module.RAGEngine
    print("Successfully imported RAGEngine")
except ImportError as e:
    print(f"Failed to import RAGEngine: {e}")
    sys.exit(1)

def test_rag():
    print("Initializing RAGEngine...")
    rag = RAGEngine(data_dir="data")
    
    print("\nTest 1: Query Stunting Data")
    query1 = "Berapa angka stunting 2024?"
    result1 = rag.retrieve(query1)
    print(f"Query: {query1}")
    print(f"Result: {result1[:200]}...") # Show first 200 chars
    
    if "19.8%" in result1:
        print("PASS: Found 19.8%")
    else:
        print("FAIL: Did not find 19.8%")

    print("\nTest 2: Query Food Prices")
    query2 = "Berapa harga beras premium?"
    result2 = rag.retrieve(query2)
    print(f"Query: {query2}")
    print(f"Result: {result2[:200]}...")
    
    if "13.112" in result2 or "Beras Premium" in result2:
        print("PASS: Found price data")
    else:
        print("FAIL: Did not find price data")

if __name__ == "__main__":
    test_rag()
