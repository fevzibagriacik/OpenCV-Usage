import cv2

video = cv2.VideoCapture(0) #0 parameter represents default webcam
video.set(cv2.CAP_PROP_EXPOSURE, -4) #If it is too small, brightness is too low
video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

fps = video.get(cv2.CAP_PROP_FPS) #If video is too fast, you can modify delay with fps
delay = int(1000 / fps)

while True:
    success, img = video.read()
    cv2.imshow("Video", img)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break