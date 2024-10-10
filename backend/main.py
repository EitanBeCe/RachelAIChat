# cd backend
# source venv/bin/activate
# uvicorn main:app --reload
# http://localhost:8000/
# http://localhost:8000/docs

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

from functions.open_requests import convert_audio_to_text

# Initiate App
app = FastAPI()

# CORS - Origins (what can be accessed)
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000",
]

# CORS - Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def check_health():
    return {"message": "healthy"}

# Get audio
@app.get("/post-audio-get/")
async def get_audio():

    # Get saved audio
    audio_input = open("voice.mp3", "rb")

    # Decode audio
    message_decoded = convert_audio_to_text(audio_input)

    print(message_decoded)

    return "Text from audio: " + message_decoded 


# Post bot response
# Note: Not playing audio answer in browser when using post request
# @app.post("/post-audio/")
# async def post_audio(file: UploadFile = File(...)):

#     print("Hello Audio")