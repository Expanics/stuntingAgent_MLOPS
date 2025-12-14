import sys
import os
import json
from app import app

def test_api():
    print("Testing Flask API...")
    client = app.test_client()
    
    # Test 1: Home Page
    print("\nTest 1: GET /")
    response = client.get('/')
    if response.status_code == 200 and b"Edukator Stunting Indonesia" in response.data:
        print("PASS: Home page loaded")
    else:
        print(f"FAIL: Home page status {response.status_code}")

    # Test 2: Chat API
    print("\nTest 2: POST /api/chat")
    payload = {"message": "Berapa angka stunting 2024?"}
    response = client.post('/api/chat', 
                          data=json.dumps(payload),
                          content_type='application/json')
    
    if response.status_code == 200:
        data = response.get_json()
        print(f"Response: {data.get('response')[:100]}...")
        if "19.8%" in data.get('response', ''):
            print("PASS: API returned correct data")
        else:
            print("FAIL: API returned unexpected data")
    else:
        print(f"FAIL: API status {response.status_code}")
        print(response.data)

if __name__ == "__main__":
    test_api()
