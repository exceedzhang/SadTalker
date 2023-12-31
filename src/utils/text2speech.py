import os
import tempfile
from TTS.api import TTS


class TTSTalker():
    def __init__(self) -> None:
        model_name = "tts_models/multilingual/multi-dataset/xtts_v2"
        self.tts = TTS(model_name=model_name, progress_bar=True, gpu=True)

    def test(self, text, audio, language='zh'):

        tempf  = tempfile.NamedTemporaryFile(
                delete = False,
                suffix = ('.'+'wav'),
            )

        self.tts.tts_to_file(text, speaker_wav=audio, language=language, file_path=tempf.name)

        return tempf.name
