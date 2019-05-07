import os
from pydub import AudioSegment
import re

wav_list = []
for root, dirs, files in os.walk('music/'):
    for filename in files:
        wav_list.append(re.split('mp3',filename)[0])
#Sometimes MacOS adds a DS_Store file. Thus we removed it here. 
try:
    wav_list.remove('.DS_Store')
except:
    print('No DS_Store to remove! All ok!')
nr = 1
for name in wav_list:
    print('Number {} of {}.'.format(nr,len(wav_list)))
    src = 'music/' + name + 'mp3'
    dst = '/Volumes/LaCie/power_metai/wav/'+name + 'wav'
    sound = AudioSegment.from_mp3(src)
    sound.export(dst,format='wav')
    nr += 1
