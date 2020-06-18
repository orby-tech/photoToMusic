import numpy as np
import librosa
import cv2

filename = 're.wav'
photoName = 'jupiter.png'
y, sr = librosa.load(filename)

img = cv2.imread(photoName)

arrayOfLinePic = np.array(1)
for j in img:
    for i in j:
        arrayOfLinePic = np.append(arrayOfLinePic, sum(i)/600)
librosa.output.write_wav('jupiter.wav', arrayOfLinePic, sr)