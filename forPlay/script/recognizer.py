import speech_recognition as sr
import time
r = sr.Recognizer()

def callback(recognizer,audio):
    try:
        print("Google pienza que tu quieres decir : {}".format(recognizer.recognize_google(audio)))
    except:
        print("error")


m = sr.Microphone()

with m as source:
    r.adjust_for_ambient_noise(source)

stop_listening = r.listen_in_background(m,callback)
for _ in range(50): time.sleep(0.1)  # we're still listening even though the main thread is doing other things
stop_listening(wait_for_stop=False)


while True: time.sleep(0.1)  