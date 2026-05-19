# Construa-seu-Assistente-Virtual-com-Intelig-ncia-Artificial

<div align="center">

# 💰 FIN — Assistente Financeira Virtual com IA Generativa

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5%20Turbo-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
[![HTML5](https://img.shields.io/badge/Frontend-HTML5%20%2B%20JS-E34F26?style=for-the-badge&logo=html5&logoColor=white)](./index.html)
[![Google Colab](https://img.shields.io/badge/Google%20Colab-Notebook-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](./assistente_fin_colab.ipynb)
[![DIO](https://img.shields.io/badge/DIO-Desafio%20de%20Projeto-E91E63?style=for-the-badge&logo=dio&logoColor=white)](https://dio.me/)

<br/>

> **Desafio de Projeto DIO** — Construa seu Assistente Virtual com Inteligência Artificial  
> Uma experiência digital de relacionamento financeiro guiada por IA Generativa,  
> com boas práticas de UX, Engenharia de Prompt e simulações em tempo real.

<br/>

![Preview do Assistente](https://via.placeholder.com/800x400/0a0f0d/00c96e?text=FIN+%E2%80%94+Assistente+Financeira+Virtual)

</div>

---

## 📌 Sobre o Projeto

A **FIN** é uma assistente financeira virtual inteligente que integra:

- 🤖 **IA Generativa (OpenAI GPT)** para compreensão de linguagem natural e respostas contextualizadas
- 🧮 **Simulações financeiras** em tempo real (juros compostos, financiamentos, reserva de emergência)
- 💬 **Persistência de contexto** para conversas mais personalizadas e contínuas
- 📚 **FAQs inteligentes** sobre produtos bancários e financeiros
- 🎨 **Interface Web moderna** com design refinado e responsivo
- 🛡️ **Boas práticas de segurança** e disclaimers financeiros

---

## 🏗️ Arquitetura da Solução

```
  👤 Usuário
      │
      ▼  pergunta em linguagem natural
  ┌─────────────────────────────────┐
  │        Interface (Web / CLI)    │
  └──────────────┬──────────────────┘
                 │
         ┌───────▼────────┐
         │  Pré-processamento │
         │  Detecta cálculos  │
         └───────┬────────┘
                 │
    ┌────────────▼────────────────┐
    │                             │
    ▼                             ▼
┌──────────────┐         ┌─────────────────────┐
│  Motor de    │         │  OpenAI GPT API      │
│  Cálculo     │         │  (IA Generativa)     │
│  Financeiro  │         │  + System Prompt     │
│  (local)     │         │  + Histórico         │
└──────┬───────┘         └──────────┬──────────┘
       │                            │
       └──────────┬─────────────────┘
                  │  resposta contextualizada
                  ▼
            👤 Usuário recebe
            resposta clara e didática
```

---

## ✨ Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| 💬 Chat Inteligente | Respostas contextualizadas via IA Generativa |
| 🧮 Juros Compostos | Simulação com capital, taxa e período |
| 🏦 Financiamento | Cálculo de parcelas pelo sistema Price |
| 🛡️ Reserva de Emergência | Meta personalizada pela renda mensal |
| 📚 FAQs Financeiros | Selic, CDI, FGC, CDB, Tesouro Direto e mais |
| 💾 Histórico | Exportação da conversa em JSON |
| 🌐 Interface Web | Chat moderno com tema escuro e animações |
| ⚡ Atalhos Rápidos | Chips de acesso rápido aos tópicos principais |

---

## 📁 Estrutura do Repositório

```
assistente-financeiro-ia/
│
├── 🌐 index.html                      # Interface Web (funciona sem backend)
├── 🐍 assistente.py                   # Assistente via terminal (Python)
├── 📓 assistente_fin_colab.ipynb      # Notebook para Google Colab
├── 📋 requirements.txt                # Dependências Python
├── 🔒 .env.example                    # Modelo de variáveis de ambiente
├── 🚫 .gitignore                      # Arquivos ignorados pelo Git
└── 📖 README.md                       # Documentação do projeto
```

---

## 🚀 Como Executar

### 🌐 Opção 1 — Interface Web (mais fácil, zero instalação)

1. Faça download ou clone o repositório
2. Abra `index.html` no navegador
3. *(Opcional)* Insira sua `OPENAI_API_KEY` no início do arquivo `index.html` para habilitar respostas via IA
4. Use os **atalhos rápidos** ou digite sua pergunta — funciona com respostas locais mesmo sem API Key!

---

### 📓 Opção 2 — Google Colab

1. Faça upload de `assistente_fin_colab.ipynb` para o [Google Colab](https://colab.research.google.com/)
2. Vá em **🔑 Secrets** (ícone de chave no menu lateral) e adicione `OPENAI_API_KEY`
3. Execute as células em ordem — pronto!

---

### 💻 Opção 3 — Execução Local (Terminal)

**Pré-requisitos:** Python 3.9+

```bash
# 1. Clone o repositório
git clone https://github.com/thaynabds/assistente-financeiro-ia.git
cd assistente-financeiro-ia

# 2. Crie e ative um ambiente virtual
python -m venv .venv
source .venv/bin/activate       # Linux/macOS
.venv\Scripts\activate          # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure a API Key
cp .env.example .env
# Edite .env e adicione sua chave

# 5. Execute o assistente
python assistente.py
```

---

## 🔑 Configurando a API Key

1. Acesse [platform.openai.com](https://platform.openai.com/)
2. Clique em **API Keys → Create new secret key**
3. Copie a chave e adicione ao `.env`:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> ⚠️ **Nunca faça commit do arquivo `.env` com sua chave real!**

---

## 🧠 Engenharia de Prompt

O assistente utiliza um **System Prompt estruturado** com:

```
PERSONA      → FIN: empática, didática, positiva
CAPACIDADES  → listagem clara das funcionalidades
REGRAS       → restrições de segurança (sem garantias de retorno)
IDIOMA       → sempre português brasileiro
CONTEXTO     → mantém as últimas 10 mensagens do histórico
```

Esta técnica garante respostas **consistentes**, **seguras** e **personalizadas** independente da pergunta do usuário.

---

## 🧮 Exemplos de Uso

**Simulação de Juros Compostos:**
```
Você: Simule juros compostos de R$10000 a 1% ao mês por 36 meses

FIN: 📊 Simulação — Juros Compostos
     Capital inicial:   R$ 10.000,00
     Taxa mensal:            1,00%
     Período:               36 meses
     ──────────────────────────────
     Montante final:    R$ 14.307,69
     Juros ganhos:      R$  4.307,69  (+43,1%)
```

**FAQ Inteligente:**
```
Você: Qual a diferença entre CDB e poupança?

FIN: Boa pergunta! Vou explicar as principais diferenças...
     [resposta didática e personalizada via GPT]
```

---

## 🛠️ Tecnologias Utilizadas

- **[Python 3.9+](https://www.python.org/)** — Backend e lógica de negócio
- **[OpenAI API](https://platform.openai.com/docs/)** — IA Generativa (GPT-3.5 Turbo)
- **[HTML5 + CSS3 + JavaScript](https://developer.mozilla.org/)** — Interface Web
- **[Google Colab](https://colab.research.google.com/)** — Ambiente de execução em nuvem
- **Engenharia de Prompt** — System Prompt estruturado para respostas consistentes

---

## 📚 Referências

| Recurso | Link |
|---|---|
| 🌐 Plataforma DIO | [dio.me](https://dio.me/) |
| 📖 Documentação OpenAI | [platform.openai.com/docs](https://platform.openai.com/docs/) |
| 📓 OpenAI Cookbook | [cookbook.openai.com](https://cookbook.openai.com/) |
| 💰 Tesouro Direto Oficial | [tesourodireto.com.br](https://www.tesourodireto.com.br/) |
| 🏦 FGC — Fundo Garantidor | [fgc.org.br](https://www.fgc.org.br/) |

---

## 👩‍💻 Autora

<div align="center">

**Thayná Batista da Silva**  
Aluna de Análise e Desenvolvimento de Sistemas  
Faculdade Senac Recife-PE · Turma 2025 · Formação prevista: 2027

</div>

---

## 📬 Contato

<div align="center">
  <a href="https://br.linkedin.com/in/thaynabds" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a href="https://www.instagram.com/thaynabdstec/" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" />
  </a>
</div>

📧 Email: [thaynabdstec@gmail.com](mailto:thaynabdstec@gmail.com)  
📱 Telefone: +55 (81) 97912-6121

<div align="center">

![Cartão TEC Thayná](https://raw.githubusercontent.com/thaynabds/AppMedSmart/refs/heads/main/Cart%C3%A3o%20TEC%20Thayn%C3%A1%20Batista%20da%20Silva.png)

</div>

---

<div align="center">

Feito com 💜 por **Thayná Batista da Silva** durante o Bootcamp da **DIO**

</div>
