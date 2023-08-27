import IPython
from IPython.display import Audio, display
from transformers import pipeline
from IPython.display import Audio

class Stt:
  def STT(self):
    Speech = 'Speech.mp3'
    #display(Audio(Speech, autoplay = True))
    whisper = pipeline('automatic-speech-recognition', model = 'openai/whisper-base')
    query = whisper(Speech)
    print("Question : ", query)
    return query
