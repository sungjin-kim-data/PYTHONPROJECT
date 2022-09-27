# TTS (Text To Speech)
# install gTTs
# install playsound==1.2.2

from gtts import gTTS
from playsound import playsound

file_name = 'sample.mp3'

# text = 'Imagine that you have just arrived at a hotel after a tiring 7-hour overnight flight.'
# tts_en = gTTS(text=text, lang='en')
# tts_en.save(file_name)

# text = '안녕하세요 성진님 좋은 밤입니다. 무엇을 도와드릴까요?'
# tts_ko = gTTS(text=text, lang='ko')
# tts_ko.save(file_name)

# playsound(file_name)

with open('sample.txt', 'r', encoding='utf8') as f:
  text = f.read()

tts_ko = gTTS(text=text, lang='ko')
tts_ko.save(file_name)

playsound(file_name)