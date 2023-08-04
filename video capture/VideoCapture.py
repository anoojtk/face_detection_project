import cv2
vid = cv2.VideoCapture(0)
i = 0
while True:
    ret, frame = vid.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imwrite('photo' + str(i) + '.jpg', frame)
    i += 1
    if i == 10:
        break
vid.release()
cv2.destroyAllWindows()
