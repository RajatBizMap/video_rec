import frappe
import json
from frappe.model.document import Document
import cv2
import os, ffmpeg
import keyboard
import subprocess
import requests
import time




@frappe.whitelist()
def camera_recoder(doc):
    video = cv2.VideoCapture(0)
    if (video.isOpened() == False):
        print("Error reading video file")
    frame_width = int(video.get(3))
    frame_height = int(video.get(4))
    size = (frame_width, frame_height)
    result = cv2.VideoWriter("filename.mp4",cv2.VideoWriter_fourcc(*'MJPG'),10, size)
    while(True):
        ret, frame = video.read()
        if ret == True:
           result.write(frame)
           cv2.imshow('Frame', frame)
           if cv2.waitKey(1) & 0xFF==ord('s'):
              break
        else:
           break
    video.release()
    result.release()
    cv2.destroyAllWindows()




@frappe.whitelist()    
def compress_video():
    rootmediadir='/home/rajat/demo_frappe_bench/sites/'
    for subdirs,dirs,files in os.walk(rootmediadir):
        for file in files:
            extension = os.path.splitext(file)[-1].lower()
            if extension==".mp4":
               if not os.path.exists(subdirs + "/compressed"):
                  os.makedirs(subdirs + "/compressed")
               media_in = subdirs + "/" + file
               print("++++-----------",media_in)
               media_out = subdirs + "/compressed/" + file
               print("++++-----------+++++++++",media_out)
               subprocess.run("ffmpeg -i " + media_in.replace(" ","\\ ") + " -vcodec libx264 -crf 22 " +
               media_out.replace(" ","// "),shell=True)
               
            elif extension ==".avi":
                 media_in =subdirs + "/" + file
                 media_out = subdirs + "/compressed/" + file
                 subprocess.run("ffmpeg -i " + media_in.replace(" ","\\ ") + " -vcodec libx264 -crf 22 " +
                 media_out.replace(" ","\\ "),shell=True)

