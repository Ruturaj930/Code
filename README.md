# Arvi Life Coach Agent

A simple personal AI agent that provides life coaching advice via a FastAPI endpoint.

## Features
- Speech-to-text (can be integrated with Whisper)
- LangChain/LangGraph orchestration placeholder
- Governor rate limiting
- Exposes a REST API

## Quick Start

```bash
git clone https://github.com/Ruturaj930/Code.git
cd Code
python -m venv .venv
source .venv/bin/activate  # or .\.venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app:app --reload
```

Then POST to `http://localhost:8000/advice` with JSON:

```json
{ "text": "How can I improve my career?" }
```

Response:

```json
{ "advice": "Based on your question about 'How can I improve my career?', here's some life coaching advice: take a deep breath, stay focused, and remember that every step forward counts." }
```

## Extending the Agent

- Integrate Whisper for audio input.
- Replace the mock `get_advice` with a LangChain pipeline using an LLM and a vector store of your career profile.
- Use LangGraph to manage conversation history.
- Add more sophisticated Governor policies (token limits, content filters).

## License

MIT