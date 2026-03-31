"""
StudyBuddy Mini - Flask API Server
MindGarden Learning Systems

Routes:
  GET  /           → Serves the frontend HTML
  POST /api/vocab  → Accepts { "words": [...] }, returns vocab + quiz JSON
"""
from flask import Flask, request, jsonify, send_from_directory
from vocab import process_vocabulary
import os

app = Flask(__name__, static_folder="static")


# ------------------------------------------------------------
# Serve the frontend
# ------------------------------------------------------------
@app.route("/")
def index():
    return send_from_directory("static", "index.html")


# ------------------------------------------------------------
# API: Generate vocabulary set + quiz
# ------------------------------------------------------------
@app.route("/api/vocab", methods=["POST"])
def generate_vocab():
    data = request.get_json(silent=True)

    # --- input validation ---
    if not data or "words" not in data:
        return jsonify({"error": "Request body must include a 'words' array."}), 400

    words = data["words"]

    # Strip whitespace and filter out blank entries
    words = [w.strip() for w in words if isinstance(w, str) and w.strip()]

    if len(words) == 0:
        return jsonify({"error": "No valid words provided. Please enter at least one word."}), 400

    if len(words) > 30:
        return jsonify({"error": "Please enter 30 words or fewer for the demo."}), 400

    try:
        result = process_vocabulary(words)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": f"Something went wrong: {str(e)}"}), 500


# ------------------------------------------------------------
# Run
# ------------------------------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"\n🌱 StudyBuddy Mini is running at http://localhost:{port}\n")
    app.run(debug=True, port=port)
