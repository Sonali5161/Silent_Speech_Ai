from gtts import gTTS

def text_to_speech(text, filename="static/output_audio.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    return filename
