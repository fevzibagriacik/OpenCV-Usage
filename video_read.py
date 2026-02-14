import cv2

video = cv2.VideoCapture("resources/demo.mp4")

fps = video.get(cv2.CAP_PROP_FPS) #If video is too fast, you can modify delay with fps
delay = int(1000 / fps)

while True:
    success, img = video.read()
    cv2.imshow("Video", img)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break