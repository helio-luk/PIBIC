import cv2
import numpy as np

class Data(object):
    """docstring for Data"""

    def __init__(self, arquivo_video, arquivo_label, labels = [], image_matrix = []):
        self.arquivo_video = arquivo_video #cv2.VideoCapture(arquivo_video)
        self.arquivo_label = arquivo_label
        self.labels = labels
        self.image_matrix = image_matrix


    def setArquivoVideo(self, arquivo):
        self.arquivo_video = arquivo
    def setArquivoLabel(self, label):
        self.arquivo_label = label

    #def getNumFrames(self):
#        last = self.arquivo_label.readlines()
#        num_frames = last[-1].split(';')[1]
        #return self.num_frames

    def getLabels(self):
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

        a = open(self.arquivo_label)
        last = a.readlines()
        num_frames = last[-1].split(';')[1]

        self.labels = np.zeros((int(int(num_frames))), dtype=np.uint8)
        for line in a:
            ini, fin, label, _ = line.split(';')
            self.labels[int(ini)-1:int(fin)-1] = f(label)
        return self.labels

    def getVideoMatrix(self):
        #v = cv2.VideoCapture('../videos/test/012609_A29_Block1_C57fe1_t.avi')
        #frames = int(v.get(cv2.CAP_PROP_FRAME_COUNT))

        video = cv2.VideoCapture(self.arquivo_video)
        a = open(self.arquivo_label)
        last = a.readlines()
        num_frames = last[-1].split(';')[1]

        h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))



        tam = h*w
        self.image_matrix = np.zeros((int(num_frames),tam), dtype=np.uint8)

        for i in range(0, 1):

            ret, frame = video.read()

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            x = np.array(image, dtype=np.uint8)
            p = x.flatten().reshape(1,tam)
            self.image_matrix[i,:] = p[:]
        return self.image_matrix
