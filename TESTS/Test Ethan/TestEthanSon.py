






















import sounddevice as sd
from scipy.io.wavfile import write
import random
import pygame
# import time

pygame.init()
pygame.mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')

fs = 44100  # Sample rate
seconds = 00.1  # Duration of recording

def main():
   for x in range(10000):
      number = random.randint(1,9999999)


      myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
      sd.wait()  # Wait until recording is finished
      write(f'audio.mp3', fs, myrecording)  # Save as WAV file

      import soundfile as sf
      import soundcard as sc

      default_speaker = sc.default_speaker()
      samples, samplerate = sf.read(f'audio.mp3')
      default_speaker.play(samples, samplerate=samplerate)
      print("True")
      # PLAY MIC SOUND HERE
      #pygame.mixer.music.load(f'audio.mp3') #Load the mp3
      #pygame.mixer.music.play() #Play it
      #time.sleep(00.1)
main()

