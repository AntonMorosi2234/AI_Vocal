import speech_recognition as sr
import pyttsx3
from responses import get_response

# === TTS (sintesi vocale) ===
engine = pyttsx3.init()
engine.setProperty("rate", 160)
engine.setProperty("volume", 1.0)

# Imposta voce italiana se disponibile
voices = engine.getProperty("voices")
for voice in voices:
    if "italian" in voice.name.lower():
        engine.setProperty("voice", voice.id)
        break

def speak(text):
    print("🤖 AI:", text)
    engine.say(text)
    engine.runAndWait()

# === STT (riconoscimento vocale) ===
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Parla ora...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="it-IT")
        print("🧑 Tu:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("❌ Non ho capito.")
        return ""
    except sr.RequestError:
        print("❌ Errore nel servizio di riconoscimento vocale.")
        return ""

# === Chatbot ===
def chatbot_response(user_input):
    if "ciao" in user_input or "salve" in user_input or "buongiorno" in user_input:
        return get_response("saluti")
    elif "come stai" in user_input or "come va" in user_input:
        return get_response("come_stai")
    elif "nome" in user_input or "chi sei" in user_input:
        return get_response("nome")
    elif "tempo" in user_input or "meteo" in user_input:
        return get_response("tempo")
    elif "barzelletta" in user_input or "scherzo" in user_input:
        return get_response("barzellette")
    elif "curiosità" in user_input or "curioso" in user_input:
        return get_response("curiosita")
    elif "motivami" in user_input or "motivazione" in user_input or "incoraggiami" in user_input:
        return get_response("motivazione")
    elif "proverbio" in user_input:
        return get_response("proverbi")
    elif "indovinello" in user_input:
        return get_response("indovinelli")
    elif "esci" in user_input or "quit" in user_input or "basta" in user_input or "stop" in user_input:
        return get_response("uscita")
    else:
        return get_response("default")

# === Main loop ===
def main():
    print("🎤 Chatbot vocale offline in Italiano (di' 'esci' per chiudere)")
    while True:
        user_input = listen()
        if not user_input:
            continue
        reply = chatbot_response(user_input)
        speak(reply)
        if "arrivederci" in reply.lower() or "alla prossima" in reply.lower():
            break

if __name__ == "__main__":
    main()
