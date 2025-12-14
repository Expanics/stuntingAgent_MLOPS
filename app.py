import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai
from stunting_agent.agent import root_agent, retrieve_stunting_data

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), "stunting_agent", ".env"))

app = Flask(__name__)

# Configure Gemini
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("Warning: GOOGLE_API_KEY not found in environment.")
else:
    genai.configure(api_key=api_key)

# In-memory session storage
# Format: {session_id: [{"role": "user", "parts": [...]}, ...]}
chat_sessions = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    session_id = data.get('session_id')
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
        
    if not session_id:
        return jsonify({"error": "No session_id provided"}), 400

    try:
        # Initialize session if not exists
        if session_id not in chat_sessions:
            chat_sessions[session_id] = []
            
        # 1. Retrieve Context using RAG
        context = retrieve_stunting_data(user_message)
        
        # 2. Construct Prompt with History
        # We append the history to the prompt to maintain context
        history = chat_sessions[session_id]
        
        system_instruction = root_agent.instruction
        
        # Build conversation history string for the prompt
        conversation_history_str = ""
        for msg in history:
            role = "User" if msg["role"] == "user" else "Agent"
            content = msg["parts"][0]
            conversation_history_str += f"{role}: {content}\n"

        full_prompt = f"""{system_instruction}

DATA PENDUKUNG (RAG):
{context}

RIWAYAT PERCAKAPAN:
{conversation_history_str}

PERTANYAAN USER SAAT INI: {user_message}

INSTRUKSI TAMBAHAN:
Jawab pertanyaan user secara langsung berdasarkan DATA PENDUKUNG dan RIWAYAT PERCAKAPAN.
"""
        
        # 3. Generate Response
        model = genai.GenerativeModel(root_agent.model)
        response = model.generate_content(full_prompt)
        
        # 4. Update History
        chat_sessions[session_id].append({"role": "user", "parts": [user_message]})
        chat_sessions[session_id].append({"role": "model", "parts": [response.text]})
        
        return jsonify({"response": response.text})
        
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Use PORT environment variable for Railway, default to 8080 for local
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host='0.0.0.0', port=port)
