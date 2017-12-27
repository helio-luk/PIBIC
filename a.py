import numpy as np
import cv2
import tensorflow as tf

video = cv2.VideoCapture('../videos/test/012609_A29_Block1_C57fe1_t.avi')
print(video.read())

'''
approach   - 0
attack     - 1
copulation - 2
chase      - 3
circle     - 4
drink      - 5
eat        - 6
clean      - 7
human      - 8
sniff      - 9
up         - 10
walk_away  - 11
other      - 12


def f(x):
    return {
        'approach': 0,
        'attack': 1,
        'copulation': 2,
        'chase': 3,
        'circle': 4,
        'drink': 5,
        'eat': 6,
        'clean': 7,
        'human': 8,
        'sniff': 9,
        'up': 10,
        'walk_away': 11,
        'other': 12,
    }[x]

arquivo = open('../videos/test/012609_A29_Block1_C57fe1_t.txt', 'r')

last = arquivo.readlines()
num_frames = last[-1].split(';')[1]

labels = np.zeros((int(num_frames)), dtype=np.uint8)

arquivo = open('../videos/test/012609_A29_Block1_C57fe1_t.txt', 'r')
for line in arquivo:
    ini, fin, label, _ = line.split(';')
    labels[int(ini)-1:int(fin)-1] = f(label)
'''
