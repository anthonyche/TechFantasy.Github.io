import numpy as np
import pandas as pd
import ffmpeg
import pydub
from pydub import AudioSegment
import os
import re
from pydub.utils import which

AudioSegment.converter = which("ffmpeg")
path = 'out.csv'

#pandas test
df = pd.read_csv(path, header= None, sep=',')
#print(df)
ogg01 = AudioSegment.from_ogg("OGG001.ogg")



#pandas extract the the second column

print(df.iloc[1:,0])
timestamps = []
for i in df.iloc[1:,0]:
    
    min = i[0] + i[1]
    #minutes
    sec = i[3] + i[4]
    #seconds
    
    
    total_seconds = int(min)*60 + int(sec)
    total_time = total_seconds * 1000
    #print(total_time)
    timestamps.append(total_time)

print(timestamps)
#Horray! now we have the array for the timestamps and they are in milliseconds!!

for i, timestamp in enumerate(timestamps):
    filename = "audio_{}.wav".format(i)
    #print(filename)
    if i+1 < len(timestamps):
        output = ogg01[timestamps[i]:timestamps[i+1]]

    output.export(filename,format = 'wav')



# pydub does things in milliseconds
'''ten_seconds = 10 * 1000

first_10_seconds = ogg01[:ten_seconds]

last_5_seconds = ogg01[-5000:]

first_10_seconds.export('try.mp4',format='mp4')
last_5_seconds.export('try01.mp4',format='mp4')'''




