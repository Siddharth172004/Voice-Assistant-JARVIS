"# Voice-Assistant-JARVIS"

Jarvis is a simple voice assistant built using Python. It can recognize your voice commands, open websites, fetch the latest news headlines, play selected YouTube music, and even interact with an AI model to generate smart responses.

---

## 📁 Project Structure

```
📦Jarvis
 ┣ 📜main.py              # Main script to activate Jarvis and process voice commands
 ┣ 📜client.py            # Handles API requests to AI model
 ┣ 📜musiclibrary.py      # Stores a dictionary of songs with their YouTube links
 ┣ 📜README.md            # Project overview and setup instructions
```

---

## ⚙️ Features

- 🔊 Voice recognition using `speech_recognition`
- 🎤 Text-to-speech with `pyttsx3`
- 🌐 Opens common websites via voice command
- 📰 Fetches latest Indian news using NewsAPI
- 🎶 Plays predefined music from YouTube
- 💬 AI-based response system using OpenRouter (or DeepSeek)

---

## 🔧 Requirements

Install the following Python packages:

```bash
pip install speechrecognition
pip install pyttsx3
pip install requests
```

---

## 🚀 How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/jarvis-voice-assistant.git
   cd jarvis-voice-assistant
   ```

2. Run the assistant:
   ```bash
   python main.py
   ```

3. Say **"Jarvis"** to activate the assistant and then give your command (e.g., "open YouTube", "news", "play joint").

---

## 🧠 AI Integration

`client.py` connects to OpenRouter API or DeepSeek AI to provide intelligent responses when a command is not predefined. Make sure you set your API key inside `client.py`.

---

## 🔐 Note

- Do **not** share your API key publicly.
- You can add more songs to `musiclibrary.py` and expand functionality in `main.py`.

---

## 👤 Author

**Siddharth Dhole**

---

## 📜 License

This project is licensed under the MIT License.

