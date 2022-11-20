import time
import cv2

while True:
    
    cap = cv2.VideoCapture('rtsp://192.168.43.1:1935/', cv2.CAP_GSTREAMER)
    if cap.isOpened():
        print('Cam opened')
        break
    print('Waiting for camera')
    time.sleep(1)
    

    writer = cv2.VideoWriter("appsrc ! queue ! multipartmux ! tcpserversink port=8089 ", cv2.CAP_GSTREAMER, 0, 30.0, (640,480)) 
    if not writer.isOpened():
        print('Error: failed to open Writer')
        exit()
    print('Streaming camera')


    while True:
       ret_val, img = cap.read();
       if not ret_val:
          print('Failed to read from camera')
          break

       writer.write(img);
       cv2.waitKey(1)

    writer.release()
    cap.release()