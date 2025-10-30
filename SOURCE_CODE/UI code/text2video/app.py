# app.py
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env (not committed to git)
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")  # safe default, change if needed
OPENAI_MAX_TOKENS = int(os.getenv("OPENAI_MAX_TOKENS", "500"))
OPENAI_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0.7"))

if not OPENAI_API_KEY:
    raise RuntimeError("Missing OPENAI_API_KEY. Create a .env file with OPENAI_API_KEY=<your key>")

# Initialize OpenAI client (new SDK)
client = OpenAI(api_key=OPENAI_API_KEY)

# Initialize Flask app
app = Flask(__name__, static_folder="static")
CORS(app)

@app.route("/video")
def video():
    return send_from_directory("static", "video.html")

# Serve static files (your HTML, CSS, JS)
@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/api/generate_prompt", methods=["POST"])
def generate_prompt():
    try:
        data = request.get_json(silent=True) or {}
        text = (data.get("text") or "").strip()

        if not text:
            return jsonify({"error": "No text provided"}), 400

        # Chat Completions using the new client
        completion = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Generate fitness-related captions and a script for a short social media video. "
                        "Use this format:\n\n"
                        "Captions: Provide short, clear descriptions for each video clip (one per line).\n"
                        "Script: Motivational, informative voiceover that ties the clips together.\n\n"
                        "Example:\n"
                        "Captions:\n"
                        "- Man lifting weights\n"
                        "- Woman skipping rope outside\n"
                        "- Man performing squats in gym\n"
                        "- Person holding a plank position\n"
                        "- Man doing pushups\n"
                        "- Woman running in park\n\n"
                        "Script:\n"
                        "Lifting builds strength—each rep brings you closer to your goals. "
                        "Skipping rope boosts your cardio—keep moving! "
                        "Squats power up your legs—own the burn. "
                        "Hold that plank and feel your core. "
                        "Pushups challenge your upper body—push your limits. "
                        "Finish strong with a confident run!"
                    ),
                },
                {"role": "user", "content": f'prompt: "{text}"'},
            ],
            max_tokens=OPENAI_MAX_TOKENS,
            temperature=OPENAI_TEMPERATURE,
        )

        generated_prompt = completion.choices[0].message.content
        return jsonify({"prompt": generated_prompt})

    except Exception as e:
        app.logger.error(f"Error generating prompt: {e}")
        return jsonify(
            {"error": "Failed to generate prompt", "details": str(e) if app.debug else None}
        ), 500

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error", "details": str(e) if app.debug else None}), 500

if __name__ == "__main__":
    app.run(
        debug=os.getenv("FLASK_DEBUG", "False").lower() == "true",
        port=int(os.getenv("PORT", 5000)),
    )
