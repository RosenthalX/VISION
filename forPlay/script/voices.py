import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")
print(len(voices))
ix=0
for voice in voices:
    engine.setProperty('voice',voice.id)
    engine.say("Buenas noches chiquito hermoso")
    #engine.save_to_file("Hello world","voice{}.mp3".format(ix))
    ix += 1
    engine.runAndWait()