#
#
#
# Steps for install
# pip install SpeechRecognition
# This installs speech recognition
# sudo apt-get install python-pyaudio python3-pyaudio
# This installs microphone support
#
# TODO
# Add audio recordings
# Check for people
# Keep going forever
# Add firmata support
# Write script: https://voicechanger.io/
# Hello my name is thankful bot 37, I am a simple robot who reminds you to be t
# thankful for what you already have. Please press my red button and tell me what you are th
# thankful for and I will give you a small treat. If you want to hear what other people
# are thankful for please press the green button. Make sure you use the word thank or thankful
#  so I can make sure you are telling me something good.

# Sounds like you used a pretty bad word there, the year is 2018
# and even though our president might be racist, I don't think we should be


import speech_recognition as sr
import pygame as pygame

print("Firing up thankful bot")
print(sr.__version__)

# pygame.mixer.init()
# pygame.mixer.music.load("harvard.wav")
# pygame.mixer.music.play()


r = sr.Recognizer()

def check_for_thankfulness(a):
  print("They said:")
  print(a)
  if "thank" in a:
    print("Thank you")
  else:
    print("Please say something with the word thank or thankful")


def save_audio_file(a):
  with open("microphone-results.wav", "wb") as f:
    f.write(a.get_wav_data())
# Test with recorded file
# harvard = sr.AudioFile('harvard.wav')
# with harvard as source:
#   audio = r.record(source)
#   r.adjust_for_ambient_noise(source)
#   print(r.recognize_google(audio))

#Microphone Firing up
mic = sr.Microphone(device_index=0)
# print(sr.Microphone.list_microphone_names())

with mic as source:
  r.adjust_for_ambient_noise(source)
  audio = r.listen(source)
  save_audio_file(audio)
  check_for_thankfulness(r.recognize_google(audio))

