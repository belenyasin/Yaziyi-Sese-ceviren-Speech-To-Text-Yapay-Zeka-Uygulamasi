import speech_recognition as sr
sesTanima = sr.Recognizer()
with sr.AudioFile('input.wav') as src:
    metin = sesTanima.listen(src)
    try:
        txt = sesTanima.recognize_google(metin, language="tr-TR")
        print('Sesteki metin : ')
        print(txt)
    except:
        print('Bir hata oluştu!')
