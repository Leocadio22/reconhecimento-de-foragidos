import cv2
webcam = cv2.VideoCapture(2)
while True:
  check, img = camera.read()
  cv2.imshow('web cam',img)
  if cv2.waitKey(1) & 0xFF == ord('q')
    break
