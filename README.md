Rachel - AI Audio Chat

Stack: Python (Backend), React (Frontend), ChatGPT API, Fast API, ElevenLabs API, Tailwind.

Commands for development

cd backend
source venv/bin/activate
uvicorn main:app --reload (for dev)
http://localhost:8000/
uvicorn main:app (for prod)

cd frontend
yarn dev
yarn start (for prod)

Backend tasks and purposes:
1. Save audio input
2. Convert audio to text (OpenAI Whisper)
3. Get Chatbot response (OpenAI ChatGPT)
4. Add to Chat Histiory
5. Convert Text to Speech (ElevenLabs AI)