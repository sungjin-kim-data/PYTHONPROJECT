# STT (Speech To Text)
# pip install SpeechRecognition
# pip install PyAudio

import speech_recognition as sr

# Get voice from Mike
r = sr.Recognizer() 
with sr.Microphone() as source:
  print('듣고 있어요') # Loader
  audio = r.listen(source) # Listening to voices from Mike.

# Get voice from file (Wav, aiff/aiff-c, flac is possible, mp3 is not possible)
# r = sr.Recognizer()
# with sr.AudioFile('file_name.wav') as source:
#   audio = r.record(source)

try:
  # google API (a limit of 50 times a day)
  text = r.recognize_google(audio, language='ko-KR')
  print(text)
except sr.UnknownValueError: # Speech Recognition Failed
  print('인식 실패')
except sr.RequestError as e: # Reason for request failure (API key Error, network is unreachable etc...)
  print('요청 실패 : {0}'.format(e))