import codecs
import speech_recognition as sr

flag = True

while flag:

    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    inp = r.recognize_google(audio)
    print(inp)

    if inp == "bye":
        
        flag = False
    else:
        infile=codecs.open("text.txt", "r", encoding="UTF-8")
        for data in infile.readlines():
            one=data.split(':')

            if(inp==one[1]):
                
                for mean in one:
                    
                    if(mean==one[1]):
                        continue
                    else:
                        print(mean)
                break
        else:
            print("Not matched,Try Another")
    inp = ""
