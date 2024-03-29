import cv2

def chitra(picture):
    image = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
    image_blur=cv2.GaussianBlur(image,(5,5),0)
    canny=cv2.Canny(image_blur,10,70)
    ret, mask = cv2.threshold(canny,70,255,cv2.THRESH_BINARY_INV)
    return mask

capture=cv2.VideoCapture(0)

while (True):
    ret, frame = capture.read()
    cv2.imshow('Live sketcher (developed by SHIVAM SHARMA)',chitra(frame))

    if cv2.waitKey(2) == 13:
        break

capture.release()
cv2.destroyAllWindows()