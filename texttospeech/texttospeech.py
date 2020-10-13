import io
import speech_recognition as sr

from .rhvoice   import RHVoice
from gtts       import gTTS
from pydub      import AudioSegment


SOLUTION_RHVOICE  = {"name": "rhvoice", "voice": "aleksandr"}
SOLUTION_GOOGLE   = {"name": "google"}


class TextToSpeech:
    def __init__(self, solution=SOLUTION_RHVOICE):
        self._solution = solution

    def synthesize(self, text: str, solution=None) -> sr.AudioData:
        # Switch to default solution
        if solution is None:
            solution = self._solution

        if solution["name"] == SOLUTION_RHVOICE["name"]:
            voice = solution["voice"]
            synthesizer = RHVoice(default_voice=voice)
            return sr.AudioData(synthesizer.get_audio(text), sample_rate=24000, sample_width=2)
        elif solution["name"] == SOLUTION_GOOGLE["name"]:
            with io.BytesIO() as audiodata:
                # Read the mp3 file from the google translate
                gTTS(text, lang="ru").write_to_fp(audiodata)
            
                # Convert it to raw format so it is compatible with the speech recognition library
                audiodata.seek(0)
                song = AudioSegment.from_mp3(audiodata)

            with io.BytesIO() as audiodata:
                song.export(audiodata, format="raw")
                audiodata.seek(0)
                return sr.AudioData(audiodata.read(), sample_rate=song.frame_rate, sample_width=song.sample_width)
        else:
            raise Exception("There is no such solution.")