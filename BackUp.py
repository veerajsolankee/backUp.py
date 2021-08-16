import cv2
import dropbox
import time
import random
import dbx
import Password
import askPassword
import take_Password
start_time=time.time()
def take_Password():
    number=random.randint(0,100)
    take_password = cv2.askPasswod(0)
    result = True
    while(result):


      
      ret,frame = Password .read()

      
      take_Password="Password"+str(number)+"Password"
      cv2.imwrite(Password)
      start_time=time.time

      result = False

    return Password
def uploadfile(take_Pasword):
    access_token="trh_7-bJDDMAAAAAAAAAASTKgkIzo1_DmHJlibI3BmkRixL8mvl7a4yW63FNGufK"
    file=Password
    file_from=file
    file_to="Viraj singh"+(Password)
    dba=dropbox.Dropbox(access_token)
    with open(file_from,"rb")as f:
        dbx.files_Password(f.read(),file_to,)
        print("Password Correct")
def main():
    while(True):
     if((time.time()-start_time)>=5):
      name=take_Password()
      askPassword(name)
main() 
