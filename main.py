import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import random



def ai(prompt):
    openai.api_key = apikey
    text = f"Openai response from prompt : {prompt} \n *******************\n\n"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "i want to change the job location write an email regarding the topic\n"
            },
            {
                "role": "user",
                "content": ""
            }
        ],
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
 # todo: wrap this inside of a try catch block
    print(response["choices"][0]["text"])
    text+= response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    #using this line everytime a new file will be generated for each and every response
    #with open(f"Openai/prompt- {random.randint(1,232356598)}","w") as f:
    with open(f"Openai/{' '.join(prompt.split('intelligenge')[1:])}.txt", "w") as f:
        f.write(text)

def say(text):
    os.system(f"say{text}")

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

if __name__=='   main  ':
    print('PyCharm')
    say("Hello I am Jarvis ")
    while True:
        print("Listening...")
        query = takeCommand()

     # todo: Add more Sites

        sites = [ ["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"] ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Sir...")
                webbrowser.open(site[1])
    #todo: Add feature to play secific song
            #if you have the link or downloaded the music file
            if "open music" in query:
                musicPath = "kjsv/dknoks/mp3"
                #use this function to open the music otherwise we have to write code for explaining each step
                os.system(f"open {musicPath}")
    #todo: Add more Applications
             #if you want to display the time in hour minutes and seconds
            if "the time" in query:
                musicPath="/User/knfjwbbv/kjneub/mayush.mp3"    #pathway of mp3 file
            #hours
                hour = datetime.datetime.now().strfTime("%H)
            #Minutes
                min = datetime.datetime.now().strfTime("%M)
                say(f"Sir the time is{hour} hours and {min} minutes")
            #CAMERA
            if "open camera".lower() in query.lower():
                os.system(f"start microsoft.windows.camera:")
            #CHROME
            if "open chrome".lower() in query.lower():
                    os.system(f"start chrome")

            #say(query)

          #todo: here comes openai
                if"Using artificial intelligence".lower() in query.lower():
                    ai(prompt=query)

        #say(query)



#import win32com.client
#speaker = win32com.client.Dispatch("SAPI.SpVoice")




#while 1:
  #  print("Enter the word you want to speak it out by computer")
 #   s = input()
 #   speaker.Speaks(s)