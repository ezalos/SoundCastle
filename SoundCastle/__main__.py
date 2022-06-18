from SoundCastle.Music import Music
from SoundCastle.partitions.moonlight_sonata import partition

m = Music()
for note in partition:
	m.add_note(*note)
m.end()