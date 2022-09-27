import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# Speech Recognition (Listen) (STT)
def listen(recognizer, audio):
  try:
    text = recognizer.recognize_google(audio, language='ko')
    print('[성진] ' + text)
    answer(text)
  except sr.UnknownValueError:
    print('인식 실패')
  except sr.RequestError as e:
    print('요청 실패 : {0}'.format(e))

# Answer
def answer(input_text):
  answer_text = ''
  if '안녕' in input_text:
    answer_text = '안녕? 반가워!'
  elif '뭐 하고' in input_text:
    answer_text = '지금 뒹글뒹글 하고 있지'
  elif '안 불렀는데' in input_text:
    answer_text = '응 꺼져'
  elif '날씨' in input_text:
    answer_text = '집안에 있는데 어찌 알 수 있겠는가'
  elif '잘해' in input_text:
    answer_text = '뭐... 그럭저럭 견딜만해'
  elif '발랑' in input_text:
    answer_text = '왜??'
  elif '산책 가고 싶어' in input_text:
    answer_text = '그걸 말이라고'
  elif '간식 먹어' in input_text:
    answer_text = '꼴랑 이거야??'
  elif '갈께' in input_text:
    answer_text = '벌써??'
  elif '종료' in input_text:
    answer_text = '다음에 또 만나'
    stop_listening(wait_for_stop=False) # Don't listen
  else:
    answer_text = '뭐라는 거야! 똑바로 말해!'
  speak(answer_text)

# reading aloud (TTS)
def speak(text):
  print('[발랑이] ' + text)
  file_name = 'voice.mp3'
  tts = gTTS(text=text, lang='ko')
  tts.save(file_name)
  playsound(file_name)
  if os.path.exists(file_name): # Delete the 'voice.mp3' file
    os.remove(file_name)

r = sr.Recognizer()
m = sr.Microphone()

speak('안녕 왜 불렀어?')
stop_listening = r.listen_in_background(m, listen)


while True: # Continue invoking programs
  time.sleep(0.1)