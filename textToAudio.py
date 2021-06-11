from gtts import gTTS
import os

metin = 'Merhaba Dünya!'

dil = 'tr'

speech = gTTS(text=metin,lang=dil,slow=False)
speech.save("output.mp3")

os.system("start output.mp3")