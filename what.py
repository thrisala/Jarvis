import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
from email.mime.text import MIMEText
import smtplib
from translate import Translator
import webbrowser as wb
import os
import pyautogui
import language_translate
import psutil
import pyjokes
import imdb
import requests
import random
import cv2
import google.generativeai as genai
from PIL import Image, ImageDraw, ImageFont
import streamlit as st
from fpdf import FPDF
from time import sleep
import urllib
import pyowm
import voices
import pywhatkit
import codecs 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
r=sr.Recognizer()

os.environ["GOOGLE_CLOUD_QUOTA_PROJECT"] = "elemental-axle-409816"

# Openweather API key
owm_api_key = "f012fd2800189fe3721d83d75bb5b89a"
owm = pyowm.OWM(owm_api_key)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    speak("The time is: ")
    t=datetime.datetime.now().strftime("%I:%M:%S")
    print(t)
    speak(t)

def virtual_travel_guide(city):
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{city}"
        response = requests.get(url)
        data = response.json()

        title = data.get('title', '')
        extract = data.get('extract', '')

        if title and extract:
            print(f"Welcome to {title}!")
            speak(f"Welcome to {title}!")
            print(extract)
            speak(extract)
        else:
            print(f"Sorry, I couldn't find information about {city}.")
    except Exception as e:
        print(f"An error occurred while fetching information. {e}")

def assignment(t,n):

    # A4 page in pixels (300 DPI)
    A4_WIDTH = 2480
    A4_HEIGHT = 3508

    # Blank image of A4 size
    image = Image.new("RGB", (A4_WIDTH, A4_HEIGHT), "white")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(r"D:\\jarvis\handwritten_3\Handwritten.otf", size=70)  # Font File

    user_title = t

    try:
        page = wikipedia.page(user_title)
        print("Title: ", page.title)

        # number of lines
        num_lines = int(n)

        lines = page.content.split('\n')[:num_lines]
        text =  "\n"+page.title + "\n" +"\n"+"\n".join(lines)
        # text=lines

    except wikipedia.exceptions.DisambiguationError as e:
        print("Please be more specific with your title.")
    except wikipedia.exceptions.PageError as e:
        print("The page does not exist. Please try another title.")
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print("An error occurred: ", e)

    position = (50, 50)

    # Split the text into lines
    lines = text.split('\n')

    current_line = 0
    current_width = 0
    current_height = 50
    current_page = 1

    for line in lines:
        words = line.split()
        for word in words:
            word_bbox = draw.textbbox(position, word, font=font)
            word_width = word_bbox[2] - word_bbox[0]
            word_height = word_bbox[3] - word_bbox[1]
            if current_width + word_width > A4_WIDTH - 100:
                position = (50, position[1] + 100)
                current_width = 0
                current_line += 1
                if position[1] > A4_HEIGHT - 100:
                    image.save(fr"D:\jarvis\handwritten\handwritten_text_page_{current_page}.png")
                    current_page += 1
                    image = Image.new("RGB", (A4_WIDTH, A4_HEIGHT), "white")
                    draw = ImageDraw.Draw(image)
                    position = (50, 50)
            draw.text(position, word, fill="black", font=font)
            word_width_with_space = word_width + 20   # word spacing
            position = (position[0] + word_width_with_space, position[1])   # space between words
            current_width += word_width_with_space

        position = (50, position[1] + 100)
        current_line += 1
        current_width = 0

    image.save(fr"D:\jarvis\handwritten\handwritten_text_page_{current_page}.png")
    image_directory = r"D:\jarvis\handwritten"

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)     

    for image_file in os.listdir(image_directory):
        if image_file.endswith(".png"):
            pdf.add_page()
            pdf.image(os.path.join(image_directory, image_file), x=0, y=0, w=210, h=297)

    # To Save PDF
    pdf.output(fr"D:\jarvis\handwritten\handwritten_text.pdf", "F")
    
    file_path = r"D:\jarvis\handwritten\handwritten_text.pdf"
    os.startfile(file_path)

def date():
    now = datetime.datetime.now()
    current_date = now.strftime("%B %d, %Y")
    print(f"Today's date is {current_date}")
    speak(f"Today's date is {current_date}")

def get_weather(city_name):
    try:
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city_name)
        weather = observation.weather
        temperature = weather.temperature('celsius')['temp']
        status = weather.status
        print(f"The weather in {city_name} is {status} with a temperature of {temperature:.2f} degrees Celsius.")
        speak(f"The weather in {city_name} is {status} with a temperature of {temperature:.2f} degrees Celsius.")
    except Exception as e:
        print(f"An error occurred while fetching the weather. {e}")

def play_music(song):
    pywhatkit.playonyt(song)
    speak(f"Playing {song} on YouTube")

def get_movie_info(movie_title):
    try:
        a = imdb.IMDb()
        movies = a.search_movie(movie_title)
        if movies:
            movie = movies[0]
            a.update(movie)
            print(f"Here is some detailed information about {movie_title}:\n"
                f"Title: {movie['title']}\n"
                f"Year: {movie['year']}\n"
                f"Genres: {', '.join(movie['genres'])}\n"
                f"Plot: {movie.get('plot')}\n"
                f"Director(s): {', '.join([director['name'] for director in movie['directors']])}\n"
                f"Rating: {movie.get('rating')}")
            speak(f"Here is some detailed information about {movie_title}:\n"f"Title: {movie['title']}\n"f"Year: {movie['year']}\n"f"Genres: {', '.join(movie['genres'])}\n"f"Plot: {movie.get('plot')}\n"f"Director(s): {', '.join([director['name'] for director in movie['directors']])}\n"f"Rating: {movie.get('rating')}")
        else:
            print(f"Sorry, I couldn't find information about {movie_title}.")
            speak(f"Sorry, I couldn't find information about {movie_title}.")
    except Exception as e:
        print(f"An error occurred while fetching movie information. {e}")


def command():
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("couldn't hear you, say thet again please...")
        command()
        return "None"
    return query

def send_email(subject,body):
    try:
        sender_email = 'summa@gmail.com'
        receiver_email = 'suma@gmail.com'

        message = MIMEText(body)
        message['Subject'] = subject
        message['From'] = sender_email
        message['To'] = receiver_email

        smtp_server = 'smtp-relay.brevo.com'
        smtp_port = 587
        smtp_username = 'navinking2305@gmail.com'
        smtp_password = 'xycACpLTFgz8MWEf'

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        print("Email sent successfully!")
        speak("Email sent successfully!")
    except Exception as e:
        print(f"Sorry, I couldn't send the email. Error: {e}")

def screenshot():
    img=pyautogui.screenshot()
    img.save(r"D:\jarvis\ss.png")

def fun(query):
    genai.configure(api_key="AIzaSyAU2IgOs9oZackY49au2pCC61Wd4c87viE")
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(query)
    print(response.text)
    speak(response.text)

def cpu():
    usage=str(psutil.cpu_percent())
    speak("cpu is at"+usage)
    battery=psutil.sensors_battery()
    speak("Battery is")
    speak(str(battery.percent)+"percentage")

def joke():
    a=pyjokes.get_joke()
    print(a)
    speak(a)

def take_picture():
    cam=cv2.VideoCapture(0)
    cv2.namedWindow("Navin webcam")
    c=0
    while True:
        ret,frame=cam.read()
        if not ret:
            print("failed")  
            break
        cv2.imshow("test",frame)
        k=cv2.waitKey(1)
        q=command()
        if "close" in q:
            print("Closing the camera")
            speak("Camera closed")
            break
        elif "take" in q or "picture" in q:
            img="pic{}.png".format(c)
            cv2.imwrite(img,frame)
            print("Picture taken")
            c+=1
            speak("Picture captured!")
        elif "offline" in q:
            quit()

def what():
    import pywhatkit as kit
    import pyautogui as auto
    import time
    import app

    phone_number = '+919941520375'
    speak("What message you want to send")
    msg=command()
    kit.sendwhatmsg_instantly(phone_number, msg)

def get_news(api_key, category='general'):
    url = 'https://newsapi.org/v2/top-headlines'

    params = {
        'country': 'in',
        'category': category,
        'apiKey': api_key,
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get('articles', [])
        random.shuffle(articles)

        for index, article in enumerate(articles[:2], start=1):
            print(f"News {index}:")
            print(f"Title: {article.get('title')}")
            print(f"URL: {article.get('url')}")
            print("-" * 30)
            speak(article.get('title'))

    else:
        print(f"Error: {response.status_code}")

if __name__ =="__main__":
    speak('Hello I am your Virtual Buddy ')
    speak('How can i help you')

    while True:
        query=command()
        if query is not None:
            query = query.lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query or 'wiki' in query:
            speak("What should I search in wikipedia")
            a=command()
            speak("Searching...")
            result=wikipedia.summary(a,sentences=2)
            print(result)
            speak(result)

        elif 'chrome' in query:
            speak('What should I search in chrome')
            search=command().lower()
            wb.open(search+'.com')

        elif "Notes" in query or "note" in query:
            speak("Please mention your title.")
            t=command()
            assignment(t,100)

        elif "tell" in query and "city" in query:
            speak("Tell the name of the city you want to know: ")
            a=command()
            virtual_travel_guide(a)

        elif "youtube" in query:
            speak("Which video do i need to play:")
            song=command()
            play_music(song)

        elif 'mail' in query or 'email' in query:
            speak("What is the subject of the email ?")
            sub=command()
            speak("What is the content ?")
            body=command()
            send_email(sub,body)

        elif 'songs' in query or 'song' in query:
            dir="D:\\music"
            songs=os.listdir(dir)
            os.startfile(os.path.join(dir,songs[1]))

        elif "language" in query and ("translate" in query or "translator" in query):
            language_translate.translate_text()

        elif 'remember' in query:
            speak("what should I remember ?")
            data=command()
            speak("you said me to remember "+data)
            remember=open('remember.txt','w')
            remember.write(data)
            remember.close()
            
        elif "whatsapp" in query:
            what()

        elif 'forget' in query:
            with open('remember.txt','w') as file:
                pass
            speak('I forgot the text you said me to remember')

        elif 'know' in query:
            remember=open('remember.txt','r')
            speak("I remember "+remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("Done!")

        elif "review" in query and "movie" in query:
            speak("For which movie?")
            movie_title = command()
            get_movie_info(movie_title)

        elif 'mapping' in query:
            url = r"D:\\jarvis\\image mapping\\Project.html"
            wb.open(url)

        elif 'cpu' in query:
            cpu()

        elif "weather" in query:
            speak("Which city do i need to tell?")
            city = command().lower()
            get_weather(city)

        elif 'joke' in query:
            joke()

        elif 'capture' in query:
            take_picture()

        elif 'news' in query:
            speak("Sure, which category would you like to know about?")
            speak("Categories include: general, business, entertainment, health, science, sports, technology")
            category = command().lower()
            get_news('d3c4d9066d3e4cc6a3af7fb4e1226dbb', category)

        elif 'logout' in query:
            os.system('shutdown -l')

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system('shutdown /r /t 1')

        elif 'offline' in query:
            quit()

        else:
            if query:
                fun(query) 
        print()