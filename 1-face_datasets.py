from tkinter import *
import cv2
import os

#Method for checking existence of path i.e the directory

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

def save_info():
    firstname_info = firstname.get()
    id_info = id.get()
    #id_info = str(id_info)

    file = open("studata.txt", "a")
    file.write(firstname_info+"\n")
    #======================================
    # Starting the web cam by invoking the VideoCapture method
    vid_cam = cv2.VideoCapture(0)

    # For detecting the faces in each frame we will use Haarcascade Frontal Face default classifier of OpenCV
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Set unique id for each individual person
    #face_id = input("enter face id:")

    # Variable for counting the no. of images
    count = 0

    #checking existence of path
    assure_path_exists("training_data/")

    # Looping starts here
    while(True):

        # Capturing each video frame from the webcam
        _, image_frame = vid_cam.read()

        # Converting each frame to grayscale image
        gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

        # Detecting different faces
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        # Looping through all the detected faces in the frame
        for (x,y,w,h) in faces:

            # Crop the image frame into rectangle
            cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
            
            # Increasing the no. of images by 1 since frame we captured
            count += 1

            # Saving the captured image into the training_data folder
            cv2.imwrite("training_data/Person." + str(id_info) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

            # Displaying the frame with rectangular bounded box
            cv2.imshow('frame', image_frame)

        # press 'q' for at least 100ms to stop this capturing process
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break

        #We are taking 100 images for each person for the training data
        # If image taken reach 100, stop taking video
        elif count>50:
            break

    # Terminate video
    vid_cam.release()

    # Terminate all started windows
    cv2.destroyAllWindows()
    #===============================================
    firstname_entry.delete(0, END)
    id_entry.delete(0, END)


#============================================================
screen = Tk()
screen.geometry("250x200")
screen.title("Recognizer")
heading = Label(text = "Face Detector", bg = "grey", fg = "black", width = "500", height = "3")
heading.pack()
 
firstname_text = Label(text = "Firstname * ",)
id_text = Label(text = "Id * ",)
id_text.place(x = 15, y = 70)
firstname_text.place(x = 15, y = 100)

firstname = StringVar()
id = IntVar()

firstname_entry = Entry(textvariable = firstname)
id_entry = Entry(textvariable = id)

id_entry.place(x = 100, y = 70)
firstname_entry.place(x =100, y = 100)

register = Button(screen,text = "Register", width = "10", height = "1", command = save_info, bg = "grey")
register.place(x = 90, y = 150)

screen.mainloop()
