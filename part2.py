


#need pyautogui, speechrecognition, pyaudio, pyttsx3
import pyautogui
import speech_recognition as recordAudio
import pyttsx3

def moveMouse(xCoord, yCoord):
    pyautogui.moveTo(xCoord, yCoord, duration = 0)
def clickMouse(xCoord, yCoord):
    pyautogui.click(xCoord, yCoord)

def speechToText(writeText):
    r = recordAudio.Recognizer()
    while (writeText):
        try:
            with recordAudio.Microphone() as audioSource:
                #noise level
                r.adjust_for_ambient_noise(audioSource, duration = 0.2)

                userSpeech = r.listen(audioSource)

                text = r.recognize_google(userSpeech)
                text = text.lower()
                if(text == "delete"):
                    pyautogui.press("backspace")
                elif (text == "period"):
                    pyautogui.typewrite(".")
                else:
                    print(text)
                    pyautogui.typewrite(text)
        except recordAudio.RequestError as e:
            print("error\n")
        except recordAudio.UnknownValueError:
            print("error\n")
        except KeyboardInterrupt:
            print("error\n")

if __name__ == '__main__':
    speechToText(True)


