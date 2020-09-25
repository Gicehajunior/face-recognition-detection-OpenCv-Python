from gtts import gTTS
import os

#text to convert to audio speech
speechToSpeak = "There is someone outside, Kindly go and Open the door"

# Language in which you want to convert 
language = 'en'

# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
gTTSInstance = gTTS(text=speechToSpeak, lang=language, slow=False)

# Saving the converted audio in a mp3 file
gTTSInstance.save("openDoorAlert.mp3") 

# to play the audio
os.system("openDoorAlert.mp3")
