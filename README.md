<div align="center">

## 🌐 Language / Idioma

[![Português](https://img.shields.io/badge/🇧🇷_Português-click_here-lightgrey?style=for-the-badge)](./README.md)
[![English](https://img.shields.io/badge/🇺🇸_English-selected-2ea44f?style=for-the-badge)](./README.en.md)

</div>

---

# Talking-by-Voice-With-ChatGPT-Using-Whisper-OpenAI-and-Python
---
<div align="center">

# 🎙️ Voice ChatGPT
### Talking by Voice with ChatGPT using Whisper (OpenAI) and Python

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-Whisper%20%2B%20GPT-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
[![gTTS](https://img.shields.io/badge/gTTS-Text--to--Speech-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://pypi.org/project/gTTS/)
[![Google Colab](https://img.shields.io/badge/Google%20Colab-Notebook-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](https://colab.research.google.com/)
[![DIO](https://img.shields.io/badge/DIO-Project%20Challenge-E91E63?style=for-the-badge&logo=dio&logoColor=white)](https://dio.me/)

<br/>

> Project developed as part of the **DIO (Digital Innovation One)** Project Challenge —
> combining **Speech-to-Text**, **Artificial Intelligence**, and **Text-to-Speech** into a multi-language voice solution.

</div>

---

## 📌 About the Project

This project implements an intelligent voice assistant that combines three powerful modern AI technologies:

| Technology | Function |
|---|---|
| 🎤 **Whisper (OpenAI)** | Converts your speech into text (*Speech-to-Text*) with support for multiple languages |
| 🤖 **ChatGPT (OpenAI)** | Processes the question and generates an intelligent response via the API |
| 🔊 **gTTS (Google)** | Converts the response into natural-sounding speech (*Text-to-Speech*) |

The full flow lets you **talk to ChatGPT using only your voice**, also receiving responses as audio — creating a truly immersive dialogue experience.

---

## 🏗️ Solution Architecture

```
  🎤 Microphone
      │
      ▼
  Audio Capture (SpeechRecognition / JavaScript)
      │
      ▼
  ┌─────────────────────────┐
  │  Whisper API (OpenAI)   │  ◄── Speech-to-Text
  │  Audio transcription    │
  └─────────────┬───────────┘
                │  transcribed text
                ▼
  ┌─────────────────────────┐
  │  ChatGPT API (OpenAI)   │  ◄── NLP Processing
  │  gpt-3.5-turbo          │
  └─────────────┬───────────┘
                │  text response
                ▼
  ┌─────────────────────────┐
  │  gTTS (Google)          │  ◄── Text-to-Speech
  │  Voice synthesis        │
  └─────────────┬───────────┘
                │
                ▼
            🔊 Audio response
```

---

## 📁 Repository Structure

```
voice-chatgpt/
│
├── 📓 voice_chatgpt_colab.ipynb   # Full notebook for Google Colab
├── 🐍 voice_chatgpt.py            # Script for local execution
├── 📋 requirements.txt            # Project dependencies
├── 🔒 .env.example                # Example environment variables
├── 🚫 .gitignore                  # Files ignored by Git
└── 📖 README.md                   # Project documentation
```

---

## 🚀 How to Run

### ☁️ Option 1 — Google Colab (Recommended)

1. Open the notebook: **[`voice_chatgpt_colab.ipynb`](./voice_chatgpt_colab.ipynb)**
2. Upload it to [Google Colab](https://colab.research.google.com/) or use the course's official link
3. Enter your `OPENAI_API_KEY` in the setup cell
4. Run the cells in order and click **"Allow microphone"** when prompted
5. Speak when the recording cell is active 🎤

> 💡 **Original course Colab link:** [bit.ly/41XfKaM](https://bit.ly/41XfKaM)

---

### 💻 Option 2 — Local Execution

**Prerequisites:** Python 3.9+, pip, working microphone

```bash
# 1. Clone the repository
git clone https://github.com/thaynabds/voice-chatgpt.git
cd voice-chatgpt

# 2. Create and activate a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate       # Linux/macOS
.venv\Scripts\activate          # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up your API key
cp .env.example .env
# Edit the .env file and add your OPENAI_API_KEY

# 5. Run
python voice_chatgpt.py
```

---

## 🔑 Setting Up the API Key

1. Go to [platform.openai.com](https://platform.openai.com/)
2. Navigate to **API Keys → Create new secret key**
3. Copy the key and add it to the `.env` file:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> ⚠️ **Never share your API Key or commit the `.env` file!**

---

## 🛠️ Technologies Used

- **[Python 3.9+](https://www.python.org/)** — Main language
- **[OpenAI Whisper](https://openai.com/research/whisper)** — Audio transcription (Speech-to-Text)
- **[OpenAI ChatGPT](https://platform.openai.com/docs/)** — `gpt-3.5-turbo` language model
- **[gTTS](https://pypi.org/project/gTTS/)** — Google Text-to-Speech for voice synthesis
- **[SpeechRecognition](https://pypi.org/project/SpeechRecognition/)** — Local audio capture
- **[Google Colab](https://colab.research.google.com/)** — Cloud execution environment

---

## 📚 References and Resources

| Resource | Link |
|---|---|
| 📄 Full project article | [Conversando Por Voz Com o ChatGPT](https://web.dio.me/articles/conversando-por-voz-com-o-chatgpt-utilizando-whisper-openai-e-python) |
| 📓 Notebook on Google Colab | [bit.ly/41XfKaM](https://bit.ly/41XfKaM) |
| 🎥 DIO YouTube live | [bit.ly/44e9Nrw](https://bit.ly/44e9Nrw) |
| 🌐 DIO Platform | [dio.me](https://dio.me/) |
| 📖 OpenAI documentation | [platform.openai.com/docs](https://platform.openai.com/docs/) |
| 📖 gTTS documentation | [gtts.readthedocs.io](https://gtts.readthedocs.io/) |

---

## 👩‍💻 Author

<div align="center">

**Thayná Batista da Silva**  
Systems Analysis and Development student  
Faculdade Senac Recife-PE · 2025 cohort · Expected graduation: 2027

</div>

---

## 📬 Contact

<div align="center">
  <a href="https://br.linkedin.com/in/thaynabds" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a href="https://www.instagram.com/thaynabdstec/" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" />
  </a>
</div>

📧 Email: [thaynabdstec@gmail.com](mailto:thaynabdstec@gmail.com)  
📱 Phone: +55 (81) 97912-6121

<div align="center">

![Thayná's business card](https://raw.githubusercontent.com/thaynabds/AppMedSmart/refs/heads/main/Cart%C3%A3o%20TEC%20Thayn%C3%A1%20Batista%20da%20Silva.png)

</div>

---

<div align="center">

Made with 💜 by **Thayná Batista da Silva** during the **DIO** Bootcamp

</div>
