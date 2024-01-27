import cv2

class VideoCamera(object):
    def __init__(self):
      self.video = cv2.VideoCapture(0)
    def __del__(self):
      self.video.release()
    def get_frame(self):
      ret, frame = self.video.read()
      #We might need to change whether we're reading into jpg or not
      ret, jpeg = cv2.imencode('.jpg', frame)
      return jpeg.tobytes()