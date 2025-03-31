from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from cue_system import CUESystem  # Ensure this module is installed and available

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variable
api_key = "Unique API"
if not api_key:
    raise ValueError("API key not found. Set the OPENAI_API_KEY environment variable.")

# Initialize the OpenAI client using the updated package
client = OpenAI(api_key=api_key)

# Initialize the cue system (this is a hypothetical module; adjust as needed)
cue_system = CUESystem()

# Flask App Configuration
TEMPLATE_DIR = os.getenv("TEMPLATE_DIR", "/Users/Kwach/Downloads/LLM Update. Final update 2/Template")
STATIC_DIR = os.getenv("STATIC_DIR", "/Users/Kwach/Downloads/LLM Update. Final update 2/static")

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
socketio = SocketIO(app)

# ================== ROUTES ==================
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def query():
    """Processes user commands and returns execution results or AI-generated responses."""
    data = request.get_json()

    # Validate request data
    if not data or "instruction" not in data:
        return jsonify({"error": "Invalid request. No instruction provided."}), 400

    instruction = data["instruction"].strip()

    if not instruction:
        return jsonify({"error": "Instruction is empty."}), 400

    try:
        print(f"✅ Received Instruction: {instruction}")

        # Check if it's a valid command in CUESystem
        if hasattr(cue_system, "is_command") and cue_system.is_command(instruction):
            execution_result = cue_system.execute(instruction)
            response = {"instruction": instruction, "execution_result": execution_result}
        else:
            # Use OpenAI to generate a response
            generated_response = client.invoke(instruction)
            response = {"instruction": instruction, "ai_response": generated_response}

        print(f"✅ Response: {response}")

        # Emit real-time updates to the frontend via WebSocket
        socketio.emit("update", response)

        return jsonify(response)

    except Exception as e:
        print(f"❌ Error Processing Request: {e}")
        return jsonify({"error": str(e)}), 500


# ================== RUN SERVER ==================
if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5002, debug=True)