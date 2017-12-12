# -*- coding:utf-8 -*- 

import sys,getopt
import cv2
import os
import numpy as np

global Const_Image_Format
Const_Image_Format = [".jpg",".jpeg",".bmp",".png"]
Const_Video_Format = [".mp4",".avi"]

class FileFilt:
    
    def __init__(self):
        self.fileList = []
        self.counter = 0
    def FindFile(self,dirr,fileformat,filtrate = 1):
        
        for s in os.listdir(dirr):
            newDir = os.path.join(dirr,s)
            if os.path.isfile(newDir):
                if filtrate:
                    if newDir and(os.path.splitext(newDir)[1] in fileformat):
                        self.fileList.append(newDir)
                        self.counter+=1
                else:
                    self.fileList.append(newDir)
                    self.counter+=1

def imgprocess(imglist):
    
    for picd in imglist:
       
                    
        thispic = cv2.imdecode(np.fromfile(picd, dtype=np.uint8), 1)
        thispic=cv2.resize(thispic,(500,400))
        cv2.imshow("play",thispic)
        cv2.waitKey(1000)
    
def vidprocess(vidlist):
    for vid in vidlist:
       
        videoCapture = cv2.VideoCapture(vid)
        fps = videoCapture.get(cv2.CAP_PROP_FPS)
        success, frame = videoCapture.read()
        
        display=cv2.resize(frame,(500,400))
        
        while success:
            display=cv2.resize(frame,(500,400))
            
            cv2.putText(display,"liyanrui 3140102743",(150,300),cv2.FONT_HERSHEY_PLAIN,1.3,(0,0,255),2) 
            cv2.imshow("play", display) #显示
            cv2.waitKey(int(1000/int(fps))) #延迟
            
            success, frame = videoCapture.read() #获取下一帧
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
            
            


        
def main(argv):
    input=""
    opts,args = getopt.getopt(argv,"")
    finder=FileFilt()
    finder.FindFile(dirr=args[0],fileformat=Const_Image_Format)
    imglist=finder.fileList
    
    imgprocess(imglist)
    finder1=FileFilt()
    
    finder1.FindFile(dirr=args[0],fileformat=Const_Video_Format)
    vidlist=finder1.fileList
    
    vidprocess(vidlist)

if __name__ == "__main__":
    main(sys.argv[1:])#将读取的地址参数传入main
    
