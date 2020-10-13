from texttospeech import TextToSpeech
    
tts = TextToSpeech()
audiodata = tts.synthesize("привет мир, меня зовут Александр!")
with open("out.wav", mode="wb") as f:
    f.write(audiodata.get_wav_data())