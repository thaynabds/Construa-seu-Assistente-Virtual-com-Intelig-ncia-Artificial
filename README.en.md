<div align="center">

## 🌐 Language / Idioma

[![Português](https://img.shields.io/badge/🇧🇷_Português-click_here-lightgrey?style=for-the-badge)](./README.md)
[![English](https://img.shields.io/badge/🇺🇸_English-selected-2ea44f?style=for-the-badge)](./README.en.md)

</div>

---

# Build-Your-Virtual-Assistant-with-Artificial-Intelligence

<div align="center">

# 💰 FIN — Virtual Financial Assistant with Generative AI

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5%20Turbo-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
[![HTML5](https://img.shields.io/badge/Frontend-HTML5%20%2B%20JS-E34F26?style=for-the-badge&logo=html5&logoColor=white)](./index.html)
[![Google Colab](https://img.shields.io/badge/Google%20Colab-Notebook-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](./assistente_fin_colab.ipynb)
[![DIO](https://img.shields.io/badge/DIO-Project%20Challenge-E91E63?style=for-the-badge&logo=dio&logoColor=white)](https://dio.me/)

<br/>

> **DIO Project Challenge** — Build Your Virtual Assistant with Artificial Intelligence  
> A digital financial-relationship experience guided by Generative AI,  
> with good UX practices, Prompt Engineering, and real-time simulations.

<br/>

![Assistant Preview](https://via.placeholder.com/800x400/0a0f0d/00c96e?text=FIN+%E2%80%94+Virtual+Financial+Assistant)

</div>

---

## 📌 About the Project

**FIN** is an intelligent virtual financial assistant that integrates:

- 🤖 **Generative AI (OpenAI GPT)** for natural-language understanding and contextualized responses
- 🧮 **Real-time financial simulations** (compound interest, loans, emergency fund)
- 💬 **Context persistence** for more personalized, continuous conversations
- 📚 **Smart FAQs** on banking and financial products
- 🎨 **Modern web interface** with refined, responsive design
- 🛡️ **Security best practices** and financial disclaimers

---

## 🏗️ Solution Architecture

```
  👤 User
      │
      ▼  natural-language question
  ┌─────────────────────────────────┐
  │        Interface (Web / CLI)    │
  └──────────────┬──────────────────┘
                 │
         ┌───────▼────────┐
         │  Pre-processing    │
         │  Detects calculations │
         └───────┬────────┘
                 │
    ┌────────────▼────────────────┐
    │                             │
    ▼                             ▼
┌──────────────┐         ┌─────────────────────┐
│  Financial   │         │  OpenAI GPT API      │
│  Calculation │         │  (Generative AI)     │
│  Engine      │         │  + System Prompt     │
│  (local)     │         │  + History           │
└──────┬───────┘         └──────────┬──────────┘
       │                            │
       └──────────┬─────────────────┘
                  │  contextualized response
                  ▼
            👤 User receives
            a clear, educational answer
```

---

## ✨ Features

| Feature | Description |
|---|---|
| 💬 Smart Chat | Contextualized responses via Generative AI |
| 🧮 Compound Interest | Simulation with principal, rate, and period |
| 🏦 Loan Financing | Installment calculation using the Price system |
| 🛡️ Emergency Fund | Personalized goal based on monthly income |
| 📚 Financial FAQs | Selic rate, CDI, FGC, CDB, Treasury bonds, and more |
| 💾 History | Export the conversation as JSON |
| 🌐 Web Interface | Modern chat with dark theme and animations |
| ⚡ Quick Shortcuts | Chips for quick access to main topics |

---

## 📁 Repository Structure

```
assistente-financeiro-ia/
│
├── 🌐 index.html                      # Web interface (works without a backend)
├── 🐍 assistente.py                   # Terminal assistant (Python)
├── 📓 assistente_fin_colab.ipynb      # Notebook for Google Colab
├── 📋 requirements.txt                # Python dependencies
├── 🔒 .env.example                    # Environment variables template
├── 🚫 .gitignore                      # Files ignored by Git
└── 📖 README.md                       # Project documentation
```

---

## 🚀 How to Run

### 🌐 Option 1 — Web Interface (easiest, zero install)

1. Download or clone the repository
2. Open `index.html` in your browser
3. *(Optional)* Add your `OPENAI_API_KEY` at the top of `index.html` to enable AI-powered responses
4. Use the **quick shortcuts** or type your question — it works with local responses even without an API key!

---

### 📓 Option 2 — Google Colab

1. Upload `assistente_fin_colab.ipynb` to [Google Colab](https://colab.research.google.com/)
2. Go to **🔑 Secrets** (key icon in the sidebar) and add `OPENAI_API_KEY`
3. Run the cells in order — done!

---

### 💻 Option 3 — Local Execution (Terminal)

**Prerequisites:** Python 3.9+

```bash
# 1. Clone the repository
git clone https://github.com/thaynabds/assistente-financeiro-ia.git
cd assistente-financeiro-ia

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate       # Linux/macOS
.venv\Scripts\activate          # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up the API Key
cp .env.example .env
# Edit .env and add your key

# 5. Run the assistant
python assistente.py
```

---

## 🔑 Setting Up the API Key

1. Go to [platform.openai.com](https://platform.openai.com/)
2. Click **API Keys → Create new secret key**
3. Copy the key and add it to `.env`:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> ⚠️ **Never commit the `.env` file with your real key!**

---

## 🧠 Prompt Engineering

The assistant uses a **structured System Prompt** with:

```
PERSONA      → FIN: empathetic, educational, positive
CAPABILITIES → clear list of features
RULES        → safety constraints (no return guarantees)
LANGUAGE     → always Brazilian Portuguese
CONTEXT      → keeps the last 10 messages of history
```

This technique ensures **consistent**, **safe**, and **personalized** responses regardless of the user's question.

---

## 🧮 Usage Examples

**Compound Interest Simulation:**
```
You: Simulate compound interest of R$10,000 at 1% per month for 36 months

FIN: 📊 Simulation — Compound Interest
     Initial principal: R$ 10,000.00
     Monthly rate:            1.00%
     Period:                36 months
     ──────────────────────────────
     Final amount:      R$ 14,307.69
     Interest earned:   R$  4,307.69  (+43.1%)
```

**Smart FAQ:**
```
You: What's the difference between a CDB and a savings account?

FIN: Great question! Let me explain the main differences...
     [educational, personalized response via GPT]
```

---

## 🛠️ Technologies Used

- **[Python 3.9+](https://www.python.org/)** — Backend and business logic
- **[OpenAI API](https://platform.openai.com/docs/)** — Generative AI (GPT-3.5 Turbo)
- **[HTML5 + CSS3 + JavaScript](https://developer.mozilla.org/)** — Web interface
- **[Google Colab](https://colab.research.google.com/)** — Cloud execution environment
- **Prompt Engineering** — Structured System Prompt for consistent responses

---

## 📚 References

| Resource | Link |
|---|---|
| 🌐 DIO Platform | [dio.me](https://dio.me/) |
| 📖 OpenAI Documentation | [platform.openai.com/docs](https://platform.openai.com/docs/) |
| 📓 OpenAI Cookbook | [cookbook.openai.com](https://cookbook.openai.com/) |
| 💰 Brazilian Treasury Direct | [tesourodireto.com.br](https://www.tesourodireto.com.br/) |
| 🏦 FGC — Credit Guarantee Fund | [fgc.org.br](https://www.fgc.org.br/) |

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
