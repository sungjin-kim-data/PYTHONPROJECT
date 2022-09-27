AI-Speaker
Implemented Artificial Intelligent Speaker.

Used API
Speech to Text : Google Streaming Speech Recognition API, Google Speech Recognition
Conversaion : Watson, Aibril(korean)
Text to Speech : gTTS, Naver Clova TTS, AWS Polly TTS

Requirements
Ubuntu 16.04
Python 3.5
Dependencies
sudo apt-get install python3-dev virtualenv
sudo apt-get install portaudio19-dev
sudo apt-get install ffmpeg
Setting Environment
Google Streaming Speech Recognition

export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/credentials-key.json
Aibril Conversation

export watson_username=YOUR_USER_NAME
export watson_password=YOUR_PASSWORD
export watson_workspace=YOUR_WORKSPACE
export watson_url=YOUR_URL
export watson_version=YOUR_VERSION
Naver Clova TTS

export naver_tts_client_id=YOUR_CLIENT_ID
export naver_tts_client_secret=YOUR_CLIENT_SECRET
AWS Polly TTS