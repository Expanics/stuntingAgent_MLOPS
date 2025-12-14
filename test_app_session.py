import sys
import os
import json
from app import app

def test_sessions():
    print("Testing Session Management...")
    client = app.test_client()
    
    # Test 1: Missing Session ID
    print("\nTest 1: Missing Session ID")
    payload = {"message": "Hello"}
    response = client.post('/api/chat', 
                          data=json.dumps(payload),
                          content_type='application/json')
    if response.status_code == 400:
        print("PASS: Rejected request without session_id")
    else:
        print(f"FAIL: Status {response.status_code}")

    # Test 2: Session A Context
    print("\nTest 2: Session A Context")
    session_a = "session_a"
    
    # A1: My name is Reza
    payload_a1 = {"message": "Nama saya Reza", "session_id": session_a}
    client.post('/api/chat', data=json.dumps(payload_a1), content_type='application/json')
    
    # A2: Who am I?
    payload_a2 = {"message": "Siapa nama saya?", "session_id": session_a}
    response_a2 = client.post('/api/chat', data=json.dumps(payload_a2), content_type='application/json')
    data_a2 = response_a2.get_json()
    print(f"Session A Response: {data_a2.get('response')}")
    
    if "Reza" in data_a2.get('response', ''):
        print("PASS: Session A remembers name")
    else:
        print("FAIL: Session A forgot name")

    # Test 3: Session B Isolation
    print("\nTest 3: Session B Isolation")
    session_b = "session_b"
    
    # B1: Who am I? (Should NOT know Reza)
    payload_b1 = {"message": "Siapa nama saya?", "session_id": session_b}
    response_b1 = client.post('/api/chat', data=json.dumps(payload_b1), content_type='application/json')
    data_b1 = response_b1.get_json()
    print(f"Session B Response: {data_b1.get('response')}")
    
    if "Reza" not in data_b1.get('response', ''):
        print("PASS: Session B does not know Session A's name")
    else:
        print("FAIL: Session Leakage detected!")

if __name__ == "__main__":
    test_sessions()
