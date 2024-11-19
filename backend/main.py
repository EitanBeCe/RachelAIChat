# cd backend
# source venv/bin/activate
# uvicorn main:app --reload
# http://localhost:8000/docs
# http://localhost:8000/

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

from functions.open_requests import convert_audio_to_text, get_chat_response
from functions.database import store_messages, reset_messages
from functions.text_to_speech import convert_text_to_speech

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


# Reset messages
@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"message": "conversation reset"}


# Get audio
@app.get("/post-audio-get/")
async def get_audio():

    # Get saved audio
    audio_input = open("voice.mp3", "rb")

    # Decode audio
    message_decoded = convert_audio_to_text(audio_input)

    if not message_decoded:
        return HTTPException(status_code=400, detail="Failed to decode audio")
    
    # Get Chat Response
    chat_response = get_chat_response(message_decoded)

    if not chat_response:
        return HTTPException(status_code=400, detail="Failed to chat response")
    
    print(chat_response)

    # Store messages
    store_messages(message_decoded, chat_response)

    # Convert chat response to audio
    audio_output = convert_text_to_speech(chat_response)

    if not audio_output:
        return HTTPException(status_code=400, detail="Failed to Eleven Labs audio response")
    
    # Create a generator that yields chunks data
    def iterfile():
        yield audio_output

    # return "Text from audio: " + message_decoded
            
    return StreamingResponse(iterfile(), media_type="audio/mpeg")


# Post bot response
# Note: Not playing audio answer in browser when using post request
# @app.post("/post-audio/")
# async def post_audio(file: UploadFile = File(...)):

#     print("Hello Audio")