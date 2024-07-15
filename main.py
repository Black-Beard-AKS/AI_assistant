import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import random

# Define your OpenAI API key here
apikey = 'your_openai_api_key_here'

def ai(prompt):
    openai.api_key = apikey
    text = f"Openai response from prompt : {prompt} \n *******************\n\n"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "i want to change the job location write an email regarding the topic\n"},
                {"role": "user", "content": ""}
            ],
            prompt=prompt,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        print(response["choices"][0]["text"])
        text += response["choices"][0]["text"]
    except Exception as e:
        print(f"Error: {e}")
        text += f"\nError: {e}"

    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    with open(f"Openai/{' '.join(prompt.split('intelligenge')[1:])}.txt", "w") as f:
        f.write(text)

def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print(f"Error: {e}")
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print('PyCharm')
    say("Hello I am Jarvis ")
    while True:
        print("Listening...")
        query = takeCommand()

        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Sir...")
                webbrowser.open(site[1])

        if "open music" in query.lower():
            musicPath = "kjsv/dknoks/mp3"
            os.system(f"open {musicPath}")

        if "the time" in query.lower():
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir the time is {hour} hours and {min} minutes")

        if "open camera" in query.lower():
            os.system("start microsoft.windows.camera:")

        if "open chrome" in query.lower():
            os.system("start chrome")

        if "using artificial intelligence" in query.lower():
            ai(prompt=query)
