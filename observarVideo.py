import cv2

def video_readeR(classifier,video="placas.mp4",skip=8):
    capture = cv2.VideoCapture("./video/"+str(video))

    frm = capture.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = capture.get(cv2.CAP_PROP_FPS)
    contador = 0
    skipped = int(skip * fps)
    while(contador < frm):
        _,frame = capture.read()
        if(skipped <= 0):
            contador += 1
            frame = cv2.resize(frame,(800,500))
            img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            img_gray = cv2.GaussianBlur(img_gray,(3,3),3)
            _,img_thresh = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
            contours,_ = cv2.findContours(img_thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

            for index,cont in enumerate(contours):
                epsilon = 0.1*cv2.arcLength(cont,True)
                approx = cv2.approxPolyDP(cont,epsilon,True)
                shape = int(len(approx))
                area = cv2.contourArea(approx)
                if(shape == 4 & int(area) < int(350000) & int(area) > int(100)):
                    frame = cv2.drawContours(frame,[approx],0,(0,255,0),cv2.LINE_AA)
                    print("Area del contour: "+str(area))

            cv2.imshow("Video",img_thresh)
            cv2.imshow("Video_real",frame)
            cv2.imshow("img_gray",img_gray)
            key = (cv2.waitKey(int(1000/fps)) & 0xFF)
            if(key == ord("q")):
                break
        else:
            skipped -= 1
        
            
video_readeR(None)