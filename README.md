<div align="center">

<br/>

```
        ███╗   ███╗███████╗██████╗ ██╗██████╗  ██████╗ ████████╗
        ████╗ ████║██╔════╝██╔══██╗██║██╔══██╗██╔═══██╗╚══██╔══╝
        ██╔████╔██║█████╗  ██║  ██║██║██████╔╝██║   ██║   ██║   
        ██║╚██╔╝██║██╔══╝  ██║  ██║██║██╔══██╗██║   ██║   ██║   
        ██║ ╚═╝ ██║███████╗██████╔╝██║██████╔╝╚██████╔╝   ██║   
        ╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝╚═════╝  ╚═════╝    ╚═╝   
```

**Your AI-powered medical assistant, available 24/7**

<br/>

[![Live App](https://img.shields.io/badge/🌐%20Live%20App-medibot--1.streamlit.app-2563eb?style=for-the-badge&logoColor=white)](https://medi-bott.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain.com)
[![Groq](https://img.shields.io/badge/Groq-F55036?style=for-the-badge&logo=groq&logoColor=white)](https://groq.com)

<br/>

---

## 🩺 What is MediBot?

**MediBot** is a polite, conversational AI medical assistant built with **Streamlit**<br/>
and powered by **Groq's LLaMA 3.1 8B** model via **LangChain**.<br/>
It listens to your health concerns and offers calm, concise, practical advice —<br/>
like having a knowledgeable friend on call, anytime.

<br/>

> ⚠️ MediBot is an informational assistant only. It does **not** replace professional medical advice.<br/>Always consult a licensed healthcare provider for serious concerns.

---

## ✨ Features

| Feature | Description |
|:---:|:---|
| 💬 **Conversational Memory** | Full multi-turn chat — MediBot remembers your conversation context |
| 🧠 **LLM-Powered** | Backed by `llama-3.1-8b-instant` via Groq for fast, intelligent responses |
| 🎯 **Medical Focus** | Politely redirects off-topic queries back to health-related discussions |
| ⚡ **Real-time Streaming UI** | Clean chat bubbles with a responsive Streamlit interface |
| 🔄 **Session Management** | Clear chat anytime via the sidebar |
| 🔒 **Secure Key Handling** | API keys loaded via `.env` locally or `st.secrets` on deployment |

---

## 🖼️ Preview

```
┌─────────────────────────────────────────────────────┐
│  🤖 MediBot                                          │
├─────────────────────────────────────────────────────┤
│                                                      │
│  ╭──────────────────────────────────────────╮       │
│  │ Hello, I am a medical assistant.         │  🤖   │
│  │ How can I help you?                      │       │
│  ╰──────────────────────────────────────────╯       │
│                                                      │
│        ╭──────────────────────────────────╮         │
│   👤   │ I have a fever and a headache.   │         │
│        ╰──────────────────────────────────╯         │
│                                                      │
│  ╭──────────────────────────────────────────╮       │
│  │ For fever and headache, Paracetamol can  │  🤖   │
│  │ help relieve both symptoms.              │       │
│  ╰──────────────────────────────────────────╯       │
│                                                      │
│  [ Type your message...                    ] [Send] │
└─────────────────────────────────────────────────────┘
```

---

## 🚀 Getting Started

### Prerequisites

Python 3.10+ &nbsp;|&nbsp; A [Groq API key](https://console.groq.com/) *(free tier available)*

<br/>

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/shreya/medibot.git
cd medibot
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 4️⃣ Run the App

```bash
streamlit run app.py
```

Visit `http://localhost:8501` in your browser — MediBot is live! 🎉

---

## 📁 Project Structure

```
medibot/
│
├── app.py           # Streamlit UI — chat interface, session state, styling
├── main.py          # LangChain + Groq LLM integration, get_response()
├── .env             # Local secrets (not committed)
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

```
Frontend       →  Streamlit   (chat UI, session state, sidebar controls)
LLM            →  Groq API    (llama-3.1-8b-instant — ultra-fast inference)
Orchestration  →  LangChain   (SystemMessage / HumanMessage / AIMessage)
Secrets        →  python-dotenv + st.secrets (local + cloud)
```

---

## ⚙️ How It Works

```
User types a message
        │
        ▼
app.py appends message to session_state.messages
        │
        ▼
get_response(messages) called in main.py
        │
        ▼
LangChain formats the full conversation history
  ┌─────────────────────────────────────┐
  │  SystemMessage  (MediBot persona)   │
  │  HumanMessage   (user turn 1)       │
  │  AIMessage      (bot turn 1)        │
  │  HumanMessage   (user turn 2)       │
  │  ...                                │
  └─────────────────────────────────────┘
        │
        ▼
Groq LLaMA 3.1 8B generates a response
        │
        ▼
Reply is trimmed and displayed in the chat UI
```

---

## 🌐 Deployment (Streamlit Cloud)

**1.** Push your code to a **public GitHub repository**<br/>
**2.** Go to [streamlit.io/cloud](https://streamlit.io/cloud) and connect your repo<br/>
**3.** In **App Settings → Secrets**, add:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

**4.** Deploy! Your app will be live at `https://your-app.streamlit.app` 🚀

---

## 📦 Requirements

```txt
streamlit
langchain-groq
langchain-core
python-dotenv
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

**1.** Fork the repository<br/>
**2.** Create your feature branch — `git checkout -b feature/amazing-feature`<br/>
**3.** Commit your changes — `git commit -m 'Add amazing feature'`<br/>
**4.** Push to the branch — `git push origin feature/amazing-feature`<br/>
**5.** Open a Pull Request

---

## 👩‍💻 Author

**Shreya Ghorui** — Created MediBot as a conversational AI health assistant project.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<br/>

Made with ❤️ and a dash of 🩺

<br/>

**[Try MediBot Live →]([https://medi-bott.streamlit.app/])**

<br/>

</div>
