import cv2

videofeed = cv2.VideoCapture('rtsp://192.168.43.1:1935/')

# my phone IP address rtsp://10.85.217.28:8080/h264_ulaw.sdp
while True:

    # print('About to start the Read command')
    _, frame = videofeed.read()
    # print('About to show frame of Video.')
    cv2.imshow("Capturing", frame)
    print('Running..')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

videofeed.release()
cv2.destroyAllWindows()