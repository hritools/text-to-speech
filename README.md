# Text to Speech
A speech synthesis library with a primary use for Russian language.

### Installation

First, you need to install the library.
```
$ pip install .
```

Second, you need to install your solutions of interest.
- RHVoice [installation guide](texttospeech/rhvoice/INSTALL.md).
- Google Translate Speech Synthesis [installation guide](texttospeech/gtts/INSTALL.md)


### Simple Example
```
from texttospeech import TextToSpeech

# Use default text synthesis solution
tts       = TextToSpeech()

# Return an instance of speechrecongition.AudioData that can be used further
audiodata = tts.synthesize("привет мир, этот текст был синтезирован!")

# Write to disk so you can listen to the synthesized data
with open("out.wav", mode="wb") as f:
    f.write(audiodata.get_wav_data())
```

### Supported audio formats
- RAW
- WAV
- AIFF
- FLAC

### Supported solutions
- RHVoice
- Google Translate Speech Synthesis