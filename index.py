import cv2
import os
import time

RTSP_URL = 'rtsp://192.168.43.1:1935/'

os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp' # Use tcp instead of udp if stream is unstable

cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)

if not cap.isOpened():
    print('Cannot open RTSP stream')
    exit(-1)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = 15

video_codec = cv2.VideoWriter_fourcc(*'MJPG')
video_output = cv2.VideoWriter('filename.avi', video_codec, fps, (frame_width, frame_height))

while True:
    ret, frame = cap.read()

    if ret == True:
        video_output.write(frame)
        cv2.imshow("Video Recording", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
video_output.release()
cv2.destroyAllWindows()
