import subprocess 
import wolframalpha 
import pyttsx3 
import tkinter 
import json 
import random 
import operator 
import speech_recognition as sr 
import datetime 
import wikipedia 
import webbrowser 
import os 
import winshell 
import pyjokes 
import feedparser 
import smtplib 
import ctypes 
import time 
import requests 
import shutil 
from twilio.rest import Client 
from clint.textui import progress 
from bs4 import BeautifulSoup 
import win32com.client as wincl 
from urllib.request import urlopen 
# Now we will set our engine to Pyttsx3 which is used for text to speech in Python and sapi5 is Microsoft speech application platform interface we will be using this for text to speech function.

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id) 
# You can change voice Id to “0” for Male voice while using assistant here we are using Female voice for all text to speech

def speak(audio): 
    engine.say(audio) 
    engine.runAndWait() 
  
def wishMe(): 
    hour = int(datetime.datetime.now().hour) 
    if hour >= 0 and hour<12: 
        speak("Good Morning Mam !") 
   
    elif hour>= 12 and hour<18: 
        speak("Good Afternoon Mam !")    
   
    else: 
        speak("Good Evening Mam !")   
   
    assname =("Jarvis 1 point o") 
    speak("I am your Assistant") 
    speak(assname) 
      
  
def usrname(): 
    speak("What should i call you Mam") 
    uname = takeCommand() 
    speak("Welcome Mam") 
    speak(uname) 
    columns = shutil.get_terminal_size().columns 
      
    print("............".center(columns)) 
    print("Welcome Miss.", uname.center(columns)) 
    print("............".center(columns)) 
      
    speak("How can i Help you, Mam") 
  
def takeCommand(): 
      
    r = sr.Recognizer() 
      
    with sr.Microphone() as source: 
          
        print("Listening...") 
        r.pause_threshold = 1
        audio = r.listen(source) 
   
    try: 
        print("Recognizing...")     
        query = r.recognize_google(audio, language ='en-in') 
        print(f"User said: {query}\n") 
   
    except Exception as e: 
        print(e)     
        print("Unable to Recognizing your voice.")   
        return "None"
      
    return query 
#Main Function starts here, we will now call all these function in main function.


if __name__ == '__main__': 
    clear = lambda: os.system('cls') 
      
    # This Function will clean any 
    # command before execution of this python file 
    clear() 
    wishMe() 
    usrname() 
      
    while True: 
          
        query = takeCommand().lower() 
          
        # All the commands said by user will be  
        # stored here in 'query' and will be 
        # converted to lower case for easily  
        # recognition of command 
        if 'wikipedia' in query: 
            speak('Searching Wikipedia...') 
            query = query.replace("wikipedia", "") 
            results = wikipedia.summary(query, sentences = 3) 
            speak("According to Wikipedia") 
            print(results) 
            speak(results) 
  
        elif 'open youtube' in query: 
            speak("Here you go to Youtube\n") 
            webbrowser.open("youtube.com") 
  
        elif 'open google' in query: 
            speak("Here you go to Google\n") 
            webbrowser.open("google.com") 
  
        elif 'open stackoverflow' in query: 
            speak("Here you go to Stack Over flow.Happy coding") 
            webbrowser.open("stackoverflow.com")    
  
        elif 'the time' in query: 
            strTime = datetime.datetime.now().strftime("% H:% M:% S")     
            speak(f"Sir, the time is {strTime}")
  
        elif 'how are you' in query: 
            speak("I am fine, Thank you") 
            speak("How are you, Sir") 
  
        elif 'fine' in query or "good" in query: 
            speak("It's good to know that your fine") 
  
        elif "change my name to" in query: 
            query = query.replace("change my name to", "") 
            assname = query 
  
        elif "change name" in query: 
            speak("What would you like to call me, Sir ") 
            assname = takeCommand() 
            speak("Thanks for naming me") 
  
        elif "what's your name" in query or "What is your name" in query: 
            speak("My friends call me") 
            speak(assname) 
            print("My friends call me", assname) 
  
        elif 'exit' in query: 
            speak("Thanks for giving me your time") 
            exit() 
  
        elif "who made you" in query or "who created you" in query:  
            speak("I have been created by yashasvi.") 
              
        elif 'joke' in query: 
            speak(pyjokes.get_joke()) 
              
  
        elif 'search' in query or 'play' in query: 
              
            query = query.replace("search", "")  
            query = query.replace("play", "")           
            webbrowser.open(query)  
  
        elif "who i am" in query: 
            speak("If you talk then definately your human.") 
  
        elif "why you came to world" in query: 
            speak("Thanks to Yashasvi. further It's a Secret")
  
        elif 'news' in query: 
              
            try:  
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''') 
                data = json.load(jsonObj) 
                i = 1
                  
                speak('here are some top news from the times of india') 
                print('''=============== TIMES OF INDIA ============'''+ '\n') 
                  
                for item in data['articles']: 
                      
                    print(str(i) + '. ' + item['title'] + '\n') 
                    print(item['description'] + '\n') 
                    speak(str(i) + '. ' + item['title'] + '\n') 
                    i += 1
            except Exception as e: 
                  
                print(str(e)) 
  
          
        elif 'lock window' in query: 
                speak("locking the device") 
                ctypes.windll.user32.LockWorkStation() 
  
        elif 'shutdown system' in query: 
                speak("Hold On a Sec ! Your system is on its way to shut down") 
                subprocess.call('shutdown / p /f') 
                  
        elif 'empty recycle bin' in query: 
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
            speak("Recycle Bin Recycled") 
  
        elif "don't listen" in query or "stop listening" in query: 
            speak("for how much time you want to stop jarvis from listening commands") 
            a = int(takeCommand()) 
            time.sleep(a) 
            print(a) 
  
        elif "where is" in query: 
            query = query.replace("where is", "") 
            location = query 
            speak("User asked to Locate") 
            speak(location) 
            webbrowser.open("https://www.google.nl / maps / place/" + location + "") 
  
    
  
        elif "restart" in query: 
            subprocess.call(["shutdown", "/r"]) 
              
        elif "hibernate" in query or "sleep" in query: 
            speak("Hibernating") 
            subprocess.call("shutdown / h") 
  
        elif "log off" in query or "sign out" in query: 
            speak("Make sure all the application are closed before sign-out") 
            time.sleep(5) 
            subprocess.call(["shutdown", "/l"]) 
  
        elif "write a note" in query: 
            speak("What should i write, sir") 
            note = takeCommand() 
            file = open('jarvis.txt', 'w') 
            speak("Sir, Should i include date and time") 
            snfm = takeCommand() 
            if 'yes' in snfm or 'sure' in snfm: 
                strTime = datetime.datetime.now().strftime("% H:% M:% S") 
                file.write(strTime) 
                file.write(" :- ") 
                file.write(note) 
            else: 
                file.write(note) 
          
        elif "show note" in query: 
            speak("Showing Notes") 
            file = open("jarvis.txt", "r")  
            print(file.read()) 
            speak(file.read(6)) 
  
        elif "update assistant" in query: 
            speak("After downloading file please replace this file with the downloaded one") 
            url = '# url after uploading file'
            r = requests.get(url, stream = True) 
              
            with open("Voice.py", "wb") as Pypdf: 
                  
                total_length = int(r.headers.get('content-length')) 
                  
                for ch in progress.bar(r.iter_content(chunk_size = 2391975), 
                                       expected_size =(total_length / 1024) + 1): 
                    if ch: 
                      Pypdf.write(ch) 
                      
        # NPPR9-FWDCX-D2C8J-H872K-2YT43 
        elif "jarvis" in query: 
              
            wishMe() 
            speak("Jarvis 1 point o in your service Mister") 
            speak(assname) 
  
        elif "weather" in query: 
              
            # Google Open weather website 
            # to get API of Open weather  
            api_key = "Api key" 
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ") 
            print("City name : ") 
            city_name = takeCommand() 
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name 
            response = requests.get(complete_url)  
            x = response.json()  
              
            if x["cod"] != "404":  
                y = x["main"]  
                current_temperature = y["temp"]  
                current_pressure = y["pressure"]  
                current_humidiy = y["humidity"]  
                z = x["weather"]  
                weather_description = z[0]["description"]  
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))  
              
            else:  
                speak(" City Not Found ") 
  
        elif "wikipedia" in query: 
            webbrowser.open("wikipedia.com") 
  
        elif "Good Morning" in query: 
            speak("A warm" + query) 
            speak("How are you Mister") 
            speak(assname) 

        elif "how are you" in query: 
            speak("I'm fine, glad you me that") 
  
        elif "i love you" in query: 
            speak("It's hard to understand") 
  
        elif "what is" in query or "who is" in query: 
            
              
            try: 
                print (next(res.results).text) 
                speak (next(res.results).text) 
            except StopIteration: 
                print ("No results") 
  
        # elif "" in query: 
            # Command go here 
            # For adding more commands 