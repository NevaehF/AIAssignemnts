# 📚 StudyBuddy Mini — Prototype
**MindGarden Learning Systems**

A lightweight vocabulary-study web app for K–8 students.  
Teachers paste a word list → the app generates definitions, example sentences, and a quick quiz.

---

## Project Structure

```
studybuddy-mini/
├── app.py            ← Flask API server (routes + error handling)
├── vocab.py          ← Backend module (definition / sentence / quiz generation)
├── requirements.txt  ← Python dependencies (just Flask)
├── static/
│   └── index.html    ← Student-facing frontend (HTML + CSS + JS, single file)
└── README.md
```

---

## How to Run Locally

### 1 — Prerequisites
- Python 3.8 or higher
- pip

### 2 — Install dependencies

```bash
cd studybuddy-mini
pip install -r requirements.txt
```

### 3 — Start the server

```bash
python app.py
```

You should see:

```
🌱 StudyBuddy Mini is running at http://localhost:5000
```

### 4 — Open the app

Visit **http://localhost:5000** in your browser.

---

## Using the App

1. Type vocabulary words into the text box, separated by commas  
   *(e.g. `brave, curious, observe, compare, bright`)*
2. Click **✨ Generate Study Set**
3. Review the vocabulary cards (word, definition, example sentence)
4. Scroll down to take the auto-generated quiz
5. Click **🎯 Submit Quiz** to see your score with instant feedback

---

## API Reference

### `POST /api/vocab`

**Request body**
```json
{ "words": ["brave", "curious", "observe"] }
```

**Response (200)**
```json
{
  "words": [
    {
      "word": "brave",
      "definition": "Brave means something related to 'brave' in a simple way.",
      "example": "The student used the word 'brave' in a sentence to show they understood it."
    }
  ],
  "quiz": [
    {
      "question": "What is the meaning of 'brave'?",
      "options": ["...", "...", "..."],
      "answer": "Brave means something related to 'brave' in a simple way."
    }
  ]
}
```

**Error response (400 / 500)**
```json
{ "error": "Human-readable error message" }
```

---

## Error Handling

| Scenario | Behaviour |
|---|---|
| Empty word list | 400 + friendly message shown in UI |
| More than 30 words | 400 + friendly message shown in UI |
| Server crash | 500 + generic error shown in UI |
| Network failure | Frontend shows "Could not reach the server" message |

---

## Notes for Demo

- This prototype uses **rule-based generation** (no AI API calls).  
  In production these would be replaced with real LLM-generated definitions and sentences.
- The quiz randomly samples 3–4 words per run; re-generating gives a different quiz.
- No database — all state lives in memory per request. Progress tracking would be added in a later sprint.

---

*Built for the MindGarden Learning Systems 3-minute video demo.*
