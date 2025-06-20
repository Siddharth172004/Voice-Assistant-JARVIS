
# 🧠 Jarvis - Python Voice Assistant

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Open Source](https://img.shields.io/badge/Open%20Source-Yes-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-blue)

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

## 🧪 Quick Test Instructions

If you're testing this project, follow these quick steps:

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/Siddharth172004/Voice-Assistant-JARVIS.git
cd Voice-Assistant-JARVIS
```

### ✅ 2. Make Sure Python and pip Are Installed

Check if Python and pip are installed:

```bash
python --version
pip --version
```

If not, please install [Python](https://www.python.org/downloads/) (3.8 or higher), which includes pip.

### ✅ 3. Install Required Libraries

```bash
pip install speechrecognition
pip install pyttsx3
pip install requests
```

### ✅ 4. Run the Assistant

```bash
python main.py
```

Say `Jarvis` to activate, then speak a command like:

- `Open Google`
- `Play knock`
- `News`
- Or say anything, and AI will respond

> ℹ️ No need to use a virtual environment for simple testing.

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
