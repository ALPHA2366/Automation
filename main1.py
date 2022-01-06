import cv2
import dropbox
import time
import random
start_time=time.time()
def take_snapshot():
    number=random.randint(0,100)
    cvo=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=cvo.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time()
        result=False
    return img_name
    print("snapshot taken")
    cvo.release()
    cv2.destroyAllWindows()
def upload_file(img_name):
    access_token="sl.A_i5Hwm9YnfDZ4-7CRhEK0WPIDlXnezQ3sli6GUbr9Z5cT2aP8W93LO6X5Rf7Dw0H3sJWoHq6b7Uf4RUKADUrt4zP1N7IqqLwTs54ZlZ-kXtdrP1hRICoVe5CJjMxIIY_n7y3XJnLEcV"
    file=img_name
    file_from=file
    file_to="/102/"+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")
def main():
    while(True):
      if((time.time()-start_time)>=5):
          name=take_snapshot()
          upload_file(name)
main()
