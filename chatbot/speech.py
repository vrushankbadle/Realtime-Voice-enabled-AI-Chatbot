import speech_recognition as sr 
import pyttsx3

engine = pyttsx3.init()

# Assigning language and voice

voc = engine.getProperty('voices')[0].id

engine.setProperty('voice', voc)

# Speech to text

def get_transcript(lang):

    ''' 
    input : 
        lang : language of voice input
        
    output : transcript, bool
        if no error, returns transcript of given voice input and true.
        else, returns error message and false.
    '''

    recognizer = sr.Recognizer()
    audio = ' '
    transcript = ' '

    print("\nListening ......\n")
    
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        transcript = recognizer.recognize_google(audio, language=lang)
        # print(transcript)
        return  transcript, True
    
    except sr.UnknownValueError:
        print("Could not understand audio")
        return "Could not understand audio", False
    
    except sr.RequestError as e:
        print("Could not request results")
        return "Could not request results", False
 
# Text to speech

def speak(response):
    
    '''
    input : response 
        text to be converted to speech
    '''

    engine.say(response)
    engine.runAndWait()

