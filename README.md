
---

# 🎙️ AI Vocal — Predizione & Chat Vocale con Machine Learning

Un progetto Python che combina **Machine Learning**, **API REST**, **CLI** e **Chat Vocale AI**.
Allenato su un dataset sintetico (età, stipendio, esperienza) con modello **Logistic Regression**.

---

## ✨ Funzionalità principali

* 📊 **Predizione acquisto** in base a:

  * Età
  * Stipendio
  * Anni di esperienza
* 🖥️ **CLI**:

  * Addestramento modello
  * Predizione diretta da terminale
* 🌐 **API REST (FastAPI)**:

  * Endpoint `/predict` con input JSON
* 🎤 **Chat Vocale AI**:

  * Input tramite microfono (SpeechRecognition)
  * Risposte AI con voce sintetizzata (gTTS + pygame)
* 📂 **Dataset automatico**:

  * Generato e salvato in `dataset.csv`
  * Modello salvato in `model.joblib`

---

## 🗂️ Architettura del progetto

```mermaid
graph TD
    A[Dataset sintetico CSV] --> B[Training Logistic Regression]
    B -->|Salva| C[model.joblib]

    subgraph CLI
        D1[python ai_vocal.py train] --> B
        D2[python ai_vocal.py predict] --> C
    end

    subgraph API REST
        E1[FastAPI Server] --> C
        E2[/predict endpoint] --> C
    end

    subgraph Voice Chat
        F1[Microfono 🎤] --> F2[SpeechRecognition]
        F2 --> F3[OpenAI GPT]
        F3 --> F4[gTTS + pygame 🔊]
    end
```

---

## 📦 Installazione

### 1. Clona il progetto

```bash
git clone https://github.com/tuonome/ai_vocal.git
cd ai_vocal
```

### 2. Crea un virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
```

### 3. Installa le dipendenze

```bash
pip install -r requirements.txt
```

### 4. Configura OpenAI API Key

Crea un file `.env` nella root:

```ini
OPENAI_API_KEY=la_tua_chiave_api
```

---

## 🚀 Utilizzo

### 🔹 1. Addestramento modello

```bash
python ai_vocal.py train
```

### 🔹 2. Predizione da CLI

```bash
python ai_vocal.py predict --eta 44 --stipendio 4600 --esperienza 18
```

Output:

```
🔮 Predizione: Sì (compra) — Probabilità 72.5%
```

### 🔹 3. API REST

Avvia server:

```bash
python ai_vocal.py serve --host 0.0.0.0 --port 8000
```

Richiesta:

```http
POST /predict
Content-Type: application/json
{
  "eta": 44,
  "stipendio": 4600,
  "esperienza": 18
}
```

Risposta:

```json
{
  "prediction": 1,
  "probability": 0.725
}
```

### 🔹 4. Chat Vocale AI

Esegui senza argomenti:

```bash
python ai_vocal.py
```

* Parla 🎤
* L’AI risponde 🔊
* Esci dicendo **"exit"**

---

## ⚙️ Requisiti extra

Su **Windows**:

```bash
pip install pipwin
pipwin install pyaudio
```

Su **Linux/macOS**:

```bash
sudo apt-get install portaudio19-dev
pip install pyaudio
```

---

## 📂 Struttura progetto

```
ai_vocal/
│── ai_vocal.py        # Script principale
│── dataset.csv        # Dataset generato
│── model.joblib       # Modello ML salvato
│── requirements.txt   # Dipendenze
│── README.md          # Documentazione
│── .env               # Chiave API OpenAI
```

---

## 🛠️ Tecnologie usate

* [Python 3.10+](https://www.python.org/)
* [scikit-learn](https://scikit-learn.org/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
* [OpenAI](https://platform.openai.com/)
* [gTTS](https://pypi.org/project/gTTS/)
* [pygame](https://www.pygame.org/)

---

## 📜 Licenza

MIT License © 2025 — *Anton Morosi*

---


