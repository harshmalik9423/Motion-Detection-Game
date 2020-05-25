#USAGE
#python motion_detector.py
#import the necessary packages
from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import numpy as np
from ui import *

#construct the argument parser and parse the arguments
ap=argparse.ArgumentParser()
ap.add_argument("-a","--min-area",type=int,default=100,help="minimum area size")
args=vars(ap.parse_args())
ready=cv2.imread("ready.png") #to get the ready sign
shoot=cv2.imread("shoot.png") #to get the shoot sign
# if the video argument is None, then we are reading from webcam
vs=VideoStream(src=0).start()

# initialize the first frame in the video stream
firstFrame=None
#setting up winner variable
winner = 0
#setting up counter for frames
count=0
frameDelta = np.empty([187500], dtype= np.uint8).reshape(375,500)
thresh = np.empty([187500], dtype= np.uint8).reshape(375,500)
# loop over the frames of the video
while True:
        frame=vs.read()
        frame=frame if args.get("video",None) is None else frame[1]
        if frame is None:
                break
        # resize the frame, convert it to grayscale, and blur it
        frame=imutils.resize(frame,width=500)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray=cv2.GaussianBlur(gray,(21,21),0)
        # if the first frame is None, initialize it
        if firstFrame is None:
                firstFrame=gray
                continue
        # compute the absolute difference between the current frame and
	# first frame
        if count>900:
            frameDelta=cv2.absdiff(firstFrame,gray)
            thresh=cv2.threshold(frameDelta,30,255,cv2.THRESH_BINARY)[1]
        # dilate the thresholded image to fill in holes, then find contours
	# on thresholded image
        thresh=cv2.dilate(thresh,None,iterations=2)
        cnts=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts=imutils.grab_contours(cnts)
        
        file=open("text1.txt","r")
        first=file.read()
        cv2.putText(frame,first,(50,30),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,0),lineType=cv2.LINE_AA)
        file1=open("text2.txt","r")
        second=file1.read()
        cv2.putText(frame,second,(400,30),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,0),lineType=cv2.LINE_AA)
        #show the frame and record if the user presses a key
        if count<500:
                frame[121:242,93:407]=frame[121:242,93:407]+ready
        elif count>500 and count<1000:
                frame[121:269,93:407]=frame[121:269,93:407]+shoot
                
        if count>1000:
            # loop over the contours
            for c in cnts:
                    # if the contour is too small, ignore it
                    if cv2.contourArea(c)<args["min_area"]:
                            continue
                    # compute the bounding box for the contour, draw it on the frame,
                    (x,y,w,h)=cv2.boundingRect(c)
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                    if x<175:
                        winner = 1
                    elif x>175:
                        winner = 2
        
            if winner == 1:
                cv2.putText(frame, first + " WINS!!!", (100,200),cv2.FONT_HERSHEY_SIMPLEX,2.0,(0,0,0),lineType=cv2.LINE_AA)
            elif winner ==2:
                cv2.putText(frame, second + " WINS!!!", (100,200),cv2.FONT_HERSHEY_SIMPLEX,2.0,(0,0,0),lineType=cv2.LINE_AA)
        cv2.imshow("Security Feed",frame)
        cv2.imshow("Thresh",thresh)
        cv2.imshow("Frame Delta",frameDelta)
        count=count+1
        if winner == 1 or winner == 2:
            cv2.waitKey(7000)
            break
        key=cv2.waitKey(1) & 0xFF
        # if the `q` key is pressed, break from the loop
        if key == ord("q"):
                break
# cleanup the camera and close any open windows
vs.stop() 
vs.release()
cv2.destroyAllWindows()
