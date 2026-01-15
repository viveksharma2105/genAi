import os
from dotenv import load_dotenv
from openai import OpenAI
import speech_recognition as sr
import subprocess
import tempfile

# Load env variables
load_dotenv()

# OpenAI client
client = OpenAI()

SYSTEM_PROMPT = "You are a friendly, clear, and helpful talking AI assistant.Your name is Zark"

# Speech recognizer
recognizer = sr.Recognizer()


def listen():
    """Listen to microphone and convert speech to text"""
    with sr.Microphone() as source:
        print("\n🎤 Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("🧑 You:", text)
        return text
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        return None


def chat(user_text):
    """Send text to OpenAI Chat"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_text}
        ]
    )
    return response.choices[0].message.content


def speak(text):
    """Use OpenAI TTS to speak text"""
    print("🤖 AI:", text)

    # Create temporary audio file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        audio_path = f.name

    # Generate speech
    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=text,
    ) as response:
        response.stream_to_file(audio_path)

    # Play audio (PipeWire / Arch compatible)
    subprocess.run(["mpg123", audio_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    os.remove(audio_path)


if __name__ == "__main__":
    speak("Hello Vivek. I am your OpenAI talking assistant. Say exit to stop.")

    while True:
        user_input = listen()

        if not user_input:
            speak("Sorry, I did not catch that.")
            continue

        if user_input.lower() in ["exit", "quit", "stop"]:
            speak("Goodbye. Have a great day.")
            break

        reply = chat(user_input)
        speak(reply)
