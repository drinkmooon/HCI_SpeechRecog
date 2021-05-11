# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import speech_recognition as sr
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    r = sr.Recognizer()
    speech = sr.AudioFile('./f1lcapae.wav')
    with speech as source:
        audio = r.record(source)
    print((r.recognize_sphinx(audio)))
    # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
