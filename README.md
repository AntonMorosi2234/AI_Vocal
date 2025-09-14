#AI VOCAL
---

# 📢 Chatbot Vocale Offline in Italiano

Un semplice chatbot vocale **offline** in italiano.
Funziona senza API esterne (quindi senza costi o limiti), usando:

* 🎙️ **SpeechRecognition** → per ascoltare la voce e trascriverla (Google STT gratuito).
* 🗣️ **pyttsx3** → per sintetizzare voce in italiano (voce del sistema operativo).
* 📚 **responses.py** → archivio di risposte divise per categorie.
* 🤖 **main\_chatbot.py** → programma principale che gestisce microfono, logica e conversazione.

---

## 📂 Struttura progetto

```
chatbot_offline/
│
├── main_chatbot.py     # programma principale
├── responses.py        # archivio frasi (stile dizionario)
└── README.md           # questo file
```

---

## ⚙️ Installazione

1. Clona o scarica questa cartella.
2. Assicurati di avere **Python 3.9+** installato.
3. Installa le dipendenze:

```bash
pip install SpeechRecognition pyttsx3 pyaudio
```

⚠️ Nota:

* Su Windows, se `pyaudio` dà errore, scarica la [ruota già compilata](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) e installala con `pip install nomefile.whl`.
* Su Linux potrebbe essere necessario installare anche `portaudio`:

  ```bash
  sudo apt-get install portaudio19-dev
  ```

---

## ▶️ Avvio

Nella cartella del progetto esegui:

```bash
python main_chatbot.py
```

---

## 🧑‍💻 Utilizzo

* Quando appare il messaggio **🎙️ Parla ora...**, puoi parlare al microfono.
* Il chatbot riconosce parole chiave e risponde con frasi prelevate da `responses.py`.
* Per chiudere la conversazione, puoi dire **"esci"**, **"stop"** o **"basta"**.

---

## ✨ Funzionalità

* ✅ Saluti e frasi di cortesia
* ✅ Risposte su tempo/meteo (simboliche)
* ✅ Barzellette
* ✅ Curiosità
* ✅ Frasi motivazionali
* ✅ Proverbi italiani
* ✅ Indovinelli semplici
* ✅ Archivio frasi separato in `responses.py` (facile da ampliare)

---

## 📚 Come aggiungere nuove frasi

Apri `responses.py` e aggiungi nuove categorie o nuove frasi.
Esempio:

```python
RESPONSES = {
    "saluti": [
        "Ciao! Come stai?",
        "Bentornato, amico!"
    ],
    "musica": [
        "Adoro la musica! Qual è la tua canzone preferita?",
        "La musica rende la vita più bella."
    ]
}
```

Poi aggiorna `main_chatbot.py` per gestire la nuova categoria:

```python
elif "musica" in user_input:
    return get_response("musica")
```

---

## 📌 Esempio di conversazione

```
🎤 Chatbot vocale offline in Italiano (di' 'esci' per chiudere)
🎙️ Parla ora...
🧑 Tu: ciao
🤖 AI: Salve! Che piacere sentirti!
🎙️ Parla ora...
🧑 Tu: raccontami una barzelletta
🤖 AI: Sai cosa fa un pomodoro timido? Diventa rosso.
🎙️ Parla ora...
🧑 Tu: esci
🤖 AI: Arrivederci, alla prossima!
```

---

## 🔮 Idee future

* Integrazione con **Vosk** per riconoscimento vocale offline.
* Aggiunta di un file **JSON esterno** per le risposte (modificabile senza toccare il codice).
* Uso di un piccolo modello NLP open-source per risposte più naturali.

---

✍️ **Autore:** progetto dimostrativo creato per sperimentare un assistente vocale offline in italiano.

---

