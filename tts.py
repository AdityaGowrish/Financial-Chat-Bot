from gtts import gTTS
from IPython.display import Audio

class Tts:
  def TTS(self,ans):
    tts = gTTS(ans)
    tts.save('1.mp3')
    sound_file = '1.mp3'
    return (sound_file)
