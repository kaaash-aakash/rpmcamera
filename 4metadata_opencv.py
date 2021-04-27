# import module
import cv2
import datetime
  
# create video capture object
data = cv2.VideoCapture(r'res/fidget.mp4')
  
# count the number of frames
frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
fps = float(data.get(cv2.CAP_PROP_FPS))

print(f"frames in video are: {frames}")
print(f"fps of video is: {fps}")

  
# calculate dusration of the video
seconds = int(frames / fps)
video_time = str(datetime.timedelta(seconds=seconds))
print("duration in seconds:", seconds)
print("video time:", video_time)