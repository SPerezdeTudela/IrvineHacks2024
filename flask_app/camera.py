import cv2
import mediapipe as mp
import numpy as np
import time

from tensorflow import keras
from keras.models import load_model
from collections import Counter


class VideoCamera:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.count = 0
        self.current = ''
        self.sentence = []
        self.model = load_model('asl_cnn.h5')
        self.tracker = 0

    def get_frame(self):
        hands = self.mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)
        labels = {0: 'A', 1: 'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'K', 10:'L', 11:'M', 12:'N', 13:'O', 14:'P', 15:'Q', 16:'R', 17:'S', 18:'T', 19:'U', 20:'V', 21:'W', 22:'X', 23:'Y'}
        data = []
        ret, frame = self.cap.read()
        h, w, c, = frame.shape
        focus = frame
        #self.current = ''
        #self.tracker = 0
            
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frame_rgb)
        rland = result.multi_hand_landmarks
        
        if rland:
            
            for hand_landmarks in rland:
                x_max = 0
                y_max = 0
                x_min = w
                y_min = h
                
                for i in range(len(hand_landmarks.landmark)):
                    x = int(hand_landmarks.landmark[i].x * w)
                    y = int(hand_landmarks.landmark[i].y * h)
                    
                    if x > x_max:
                        x_max = x
                    if x < x_min:
                        x_min = x
                    if y > y_max:
                        y_max = y
                    if y < y_min:
                        y_min = y
                        
                y_min -= 20
                y_max += 20
                x_min -= 20
                x_max += 20
                
                cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
                self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                
                focus = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                focus = focus[y_min:y_max, x_min:x_max]
                val_x, val_y = focus.shape
                
                if (val_x > 0 and val_y > 0):
                    #print(focus.shape)
                    #cv2.imwrite('original.png', focus)
                    focus = cv2.resize(focus,(28,28))
                    #cv2.imwrite('resized.png', focus)
                    
        
                    row, col = focus.shape
                    for i in range(row):
                        for j in range(col):
                            k = focus[i,j]
                            data.append(k)


                    #print(len(data))
                    
                    
                    
            
                    pixels = np.asarray(data[:784])
                    pixels = pixels/255
                    pixels = pixels.reshape(-1,28,28,1)    
                    
                    
                    prediction_list = list(self.model.predict(pixels)[0])
                    i = prediction_list.index(max(prediction_list))
                    letter = labels[i]
                    
                    self.sentence.append(letter)
                    
                    
                #time.sleep(0.5)
            
                
            
        
            self._predictor()
            font = cv2.FONT_HERSHEY_SIMPLEX
            print(self.current)
            cv2.putText(frame, self.current, (50, 50), font, 1, (0, 0, 255), 4, cv2.LINE_4)   

        else:
            #might be a problem
            self.current = ''
            self.tracker = 0
        
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
    
    
    def _predictor(self):
        #take most common letter every 2 seconds

        #print(self.sentence)

        #truncated = ''

        print(self.sentence)
        while self.tracker < len(self.sentence):
            temp = self.sentence[self.tracker:self.tracker+10]
            self.current += (self._most_frequent(temp))
            self.tracker += 10
            

        print(self.current)

    
 
    def _most_frequent(self, sub):
        occurence_count = Counter(sub)
        return occurence_count.most_common(1)[0][0]
    

            
    
    def __del__(self):
        self.cap.release()

#cv2.destroyAllWindows()

