import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os
text=''
'''
This is where you specify the target language for speech translation. 
In this example, it's set to Japanese, but you can select from 
a variety of languages. Refer to the 'language.tex' file 
to view and choose different languages. Note that not all 
languages may be supported. 
'''
language='ja'
def text_to_speech(text,ulang):
    tts = gTTS(text=text, lang=ulang)
    tts.save("output.mp3")
    playsound("output.mp3")
    os.remove("output.mp3")
   

def text_translator(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

thing = sr.Recognizer()
run = True


while run:
    with sr.Microphone() as source:
        # Two try-except blocks are added: one handles errors when the sound source isn't recognized,
        # and the other manages failures in playing the MP3 audio file.
        try:
            print("Working")
            audio_text = thing.listen(source, timeout=15, phrase_time_limit=15)
            print("Done")
        
            text=thing.recognize_google(audio_text)
        
                
            if text != "":
                
                try:
                    #This piece of code here prints out the recongize and translated text
                    print("Recognized Text:")
                    print(text)
                    ctext=text_translator(text,language)
                    print(ctext)
                    #This piece of code usings gTTs library to play translated text
                    text_to_speech(ctext,language)
                
                
                    if "quit" in text or "bye" in text:
                        break


                except Exception as e:
                    print("Audio was not playable")

        except Exception as e:
            print("No audio detected")   

    
    

   
      

    
