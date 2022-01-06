import cv2
def take_snapshot():
    cvo=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frames=cvo.read()
        cv2.imwrite("image1.jpg",frames)
        result=False
    cvo.release()
    cv2.destroyAllWindows()
take_snapshot()