import pyaudio
import numpy as np

from SoundCastle import notes

class Music():
	def __init__(self, fs:int=44100, volume:float=0.5) -> None:
		self.fs = fs               # sampling rate, Hz, must be integer
		self.volume = volume       # range [0.0, 1.0]

		self.p = pyaudio.PyAudio()
		self.stream = self.p.open(format=pyaudio.paFloat32,
						channels=1,
						rate=self.fs,
						output=True)


	def add_note(self, note, duration=1.0):
		duration = duration   # in seconds, may be float
		f = notes.notes[note]
		samples = (np.sin(2*np.pi*np.arange(self.fs*duration)*f/self.fs)).astype(np.float32)
		print(f"{samples.shape = }")
		self.stream.write(self.volume*samples)


	def end(self):
		# generate samples, note conversion to float32 array

		# for paFloat32 sample values must be in range [-1.0, 1.0]
		# play. May repeat with different volume values (if done interactively) 
		self.stream.stop_stream()
		self.stream.close()
		self.p.terminate()
