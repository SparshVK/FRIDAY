<h1 align="center">🤖 FRIDAY: My Personal AI Assistant</h1>
<p align="center"><i>A voice-controlled futuristic AI, inspired by pop culture and driven by real-time intelligence.</i></p>

<p align="center">
  <img src="https://img.shields.io/badge/AI_Model-Grok_1.5V-blueviolet" />
  <img src="https://img.shields.io/badge/Voice_Control-Enabled-brightgreen" />
  <img src="https://img.shields.io/badge/NLP-Google_Cloud-yellow" />
  <img src="https://img.shields.io/badge/Image_Generation-HuggingFace-orange" />
  <img src="https://img.shields.io/badge/Developer-Sparsh_Kumar-informational" />
</p>

---

## 🎬 Live Demo

> 🎥 Coming Soon: Video demo showcasing real-time voice commands, web data fetching, and app control.
> 

---

## 📸 UI Preview

![FRIDAY Screenshot](https://github.com/your-username/FRIDAY-AI/assets/ui-preview.png)  
> Replace with actual screenshot or interface preview.

---

## 🚀 Features

- 🎙️ **Voice Recognition:** 98% accurate command parsing
- 🧠 **Conversational AI:** Context-aware replies powered by Grok 1.5V and Google NLP
- 🌐 **Real-Time Web Access:** Fetches news, weather, traffic, and more
- 💻 **System-Level Control:** Opens apps, websites, manages basic hardware tasks
- 🖼️ **Image Generation:** Uses HuggingFace APIs to generate AI-based images
- 🔊 **Text-to-Speech (TTS):** Emotionally expressive and natural sounding output
- 🛠️ **Wake Word Detection:** Custom trigger word “Hey FRIDAY”
- 🧠 **Context Memory:** Remembers past interactions for better continuity
- 🔐 **Noise Filtering:** Smooth operation in noisy environments

---

## 🧠 Architecture Overview

1. **Voice Interface Layer**
   - Wake word detection
   - Voice input capture (microphone)
   - Noise filtering
2. **AI & NLP Processing**
   - Grok 1.5V for chat
   - Google Cloud NLP for language parsing
3. **System Interaction Layer**
   - Python-based automation (PyAutoGUI / OS hooks)
   - Custom command execution
4. **Web & Image Layer**
   - Google Search API
   - HuggingFace for image generation
   - Weather/news API integration
5. **TTS Output**
   - pyttsx3 / gTTS for natural voice feedback

---

## 📦 Installation Guide

### 🖥️ Manual Setup

```bash
git clone https://github.com/your-username/FRIDAY-AI.git
cd FRIDAY-AI
pip install -r requirements.txt
python main.py
````

> ⚠️ Ensure microphone & speaker permissions are enabled.

---

## 📄 `requirements.txt`

```text
speechrecognition
pyttsx3
gtts
pyautogui
requests
openai
transformers
bs4
pyjokes
playsound
pyaudio
```

---

## 🔧 Packaging with PyInstaller (Windows)

To create a standalone `.exe` file:

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --icon=friday_icon.ico main.py
```

> Output will be in the `/dist` folder. Customize your icon accordingly.

---

## 🐳 Docker Support (Optional)

**Dockerfile:**

```Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]
```

To build and run:

```bash
docker build -t friday-ai .
docker run -it --rm --device /dev/snd friday-ai
```

> Docker containers don’t handle microphones easily. For Linux, consider PulseAudio or pipe input.

---

## 🔮 Roadmap

* 📱 Android/iOS integration with mobile wake-word detection
* 📊 Local database for personal memory (custom knowledge base)
* 🏠 Smart Home automation integration (Home Assistant, Zigbee)
* 🧠 Personalized response tuning using user profiling
* 👀 Visual object detection with OpenCV & webcam

---

## 🧗 Challenges Overcome

* 🔄 Real-time latency optimization
* 🔊 Background noise mitigation for cleaner command capture
* 🧩 Third-party API compatibility (Google, HuggingFace)
* 💬 Maintaining personality and context over long sessions
* 🛠️ Controlling desktop apps from within Python

---

## 📫 Contact & Credits

**Developer:** Sparsh Kumar
📧 Email: [sparsh.devmail@gmail.com](mailto:sparsh.devmail@gmail.com)
🔗 GitHub: [github.com/sparsh-ai](https://github.com/sparsh-ai)
🌐 Portfolio: [www.sparshkumar.dev](https://www.sparshkumar.dev)

---

## 🧠 Inspired By

* J.A.R.V.I.S. & F.R.I.D.A.Y. from Marvel Universe
* OpenAI Assistants
* Real-time interaction needs in modern productivity tools

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for full details.

---

> *“FRIDAY isn’t just another AI — it’s your virtual assistant reimagined with intelligence, personality, and purpose.”*

```
