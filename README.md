Jarvis – Your Personal Virtual Assistant 🤖
    Jarvis is an AI-powered virtual assistant built in Python that can perform a wide range of tasks using speech recognition, natural language processing, and automation tools. It can talk, search, automate daily tasks, fetch data, and even generate handwritten assignments.

✨ Features

* 🎤 Voice Commands – Speak naturally, Jarvis listens and responds.
* ⏰ Date & Time – Tells current time and date.
* 📚 Wikipedia Search – Fetches summaries of topics.
* 🌍 Virtual Travel Guide – Learn about any city.
* 🌦️ Weather Updates – Real-time weather using OpenWeather API.
* 🎵 Music & YouTube – Plays songs locally or from YouTube.
* 🎬 Movie Info – Fetches movie details using IMDb.
* 📧 Send Emails – Automated email sending.
* 📝 Handwritten Assignment Generator – Creates handwritten PDFs from Wikipedia articles.
* 📸 Screenshots & Camera Capture – Capture screen or webcam pictures.
* 💬 WhatsApp Messaging – Instantly send messages via WhatsApp.
* 📰 Latest News – Fetches headlines from NewsAPI.
* 🖥️ System Stats – CPU usage and battery level.
* 😂 Jokes – Lighten up with a random joke.
* 🔊 AI Chat Mode – Uses Google Generative AI for custom queries.
* 💻 System Control – Shutdown, restart, logout directly via commands.


🛠️ Tech Stack

* Programming Language: Python 3.x
* Libraries:

  * `speech_recognition`, `pyttsx3`, `wikipedia`, `pywhatkit`
  * `psutil`, `pyjokes`, `imdbpy`, `cv2 (OpenCV)`
  * `pyowm`, `requests`, `streamlit`, `fpdf`, `PIL`
  * `google.generativeai` (Gemini), `pyautogui`, `smtplib`, etc.



🚀 Getting Started

1. Clone this repository

```bash
git clone https://github.com/Thrisala K/jarvis.git
cd what
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

(You’ll need Python 3.9+ recommended)

3. Setup API Keys

* Google Generative AI – Replace with your Gemini API key.
* OpenWeather – Replace `owm_api_key` with your API key.
* NewsAPI – Replace with your News API key.
* Email (SMTP) – Configure your email credentials.

4. Run Jarvis

```bash
python what.py
```


🎤 Example Commands

* "What is the time?"
* "Tell me today's date"
* "Search Wikipedia for Artificial Intelligence"
* "Tell me the weather in Chennai"
* "Play Believer on YouTube"
* "Tell me a joke"
* "Take a screenshot"
* "Review movie Interstellar"
* "Send a WhatsApp message"
* "What's the news in technology?"
* "Shutdown the system"



📂 Project Structure

│── what.py # Main Python file (entry point)
│── README.md # Documentation
│
└── handwritten_3/ # Fonts folder
    │── Handwritten.ttf
    │── Handwritten.otf
    │── Handwritten - Italic.ttf
    │── Handwritten - Italic.otf
    │── More Info.txt


⚠️ Disclaimer

* This project is for educational purposes only.
* Be careful with system commands like shutdown/restart.
* Do not hardcode or share sensitive API keys & passwords.


 💡 Future Improvements

* Add GUI with Streamlit
* Integrate calendar & reminders
* More natural conversations with LLMs
* Smarter memory & personal context awareness


 👩‍💻 Author

Developed by Thrisala K
