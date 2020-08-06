#This Virtual Assistance will gets the date, current time,respond back with a random greeting

import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

warnings.filterwarnings('ignore')

#record audio

def recordAudio():
    r=sr.Recognizer()

    #open the mic and start recording

    with sr.Microphone() as source:
        print('Say Something')
        audio= r.listen(source)

    #Google Speech Recognition
    data=''
    try:
        data=r.recognize_google(audio)
        print('You Said: '+data)
    except sr.UnknownValueError:
        print('Google Speech Recognition could not understand the audio')
    except sr.RequestError as e:
        print('Request results from Google Speech Recognition Server Error'+e)

    return data

#A Function to get the virtual assistance response
def assistanceresponse(text):

    print(text)

    #converting text into speech
    myobj=gTTS(text=text,lang='en', slow=False)

    #save the converted audio to a file
    myobj.save('assistance_response.mp3')

    #Play the converted file
    os.system('Start assistance_response.mp3')

# text='This is a test'
# assistanceresponse(text)

#A function for Wake word
def wakeWord(text):
    WAKE_WORDS=['yo dude', 'sir ji','hey siri','siri','anvi']

    text=text.lower()

    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
    #If the wake word is not found
    return False

#A Function to get the current date
def getDate():
    now=datetime.datetime.now()
    my_date=datetime.datetime.today()
    weekday=calendar.day_name[my_date.weekday()]
    monthnum=now.month
    dayNum=now.day
    month_names=['January','February','March','April','May','June','July','August','September','October','November','December']
    ordinalNumbers=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th','11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th','29th', '30th', '31st']

    return 'Today is '+weekday+' '+month_names[monthnum-1] + ' '+ ordinalNumbers[dayNum-1]+'.'

print(getDate())

def greeting(text):
    GREETING_INPUTS=['hi','hey','hola','greetings','wassup','hello']

    GREETING_RESPONSE=['howdy','whats good','hello','hey there']

    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSE)+'.'

    return ''

#A function to get a person first and last name from the text

def getperson(text):

    wordlist=text.split()

    for i in range(0,len(wordlist)):
       if i+3<=len(wordlist)-1 and wordlist[i].lower()=='who' and wordlist[i+1].lower()=='is':
        return wordlist[i+2] + ' '+wordlist[i+3]

# print(getperson('who is Aditya Pandey'))

while True:

    #Record the Audio
    text=recordAudio()
    response=''

    #Check for the wake word
    if(wakeWord(text)==True):

      #Cheeck for greeting by the user
        response=response+greeting(text)

        if('date' in text):
            get_date=getDate()
            response=response+' '+get_date
      #check if the user said who is

        if('time' in text):
            now=datetime.datetime.now()
            meridiem=''
            if now.hour>=12:
                meridiem='p.m.'
                hour=now.hour-12

            else:
                 meridiem='a.m.'
                 hour=now.hour

            if now.minute<10:
                 minute='0'+str(now.minute)
            else:
                 minute=str(now.minute)
                 response=response+' '+'It is '+str(hour)+':'+minute+' '+meridiem+' Mister Pandey.'

        if('who is' in text):
            person=getperson(text)
            print(person)
            wiki=wikipedia.summary(person,auto_suggest=False,sentences=2)
            response=response+' '+wiki

           #Have the assistance respond back using audio and the text from response
        assistanceresponse(response)

