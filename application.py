import cv2

# Function for create frames from a video, its easier to proccess later
def CreateFrames(video):

    vidcap = cv2.VideoCapture(video)
    success,image = vidcap.read()
    count = 0

    while success:
        cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1

cap = cv2.VideoCapture("media/Video.mp4")
scale = 30

# alpha = 50
# title_window = "Trackbar"

# def on_trackbar(frame):
#     hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#     cv2.add(hsv[::2], alpha, hsv[::2])
#     frame = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
#     cv2.imshow("frame",frame)

# cv2.namedWindow(title_window)
# trackbar_name = 'Alpha x %d' % alpha
# cv2.createTrackbar(trackbar_name,title_window,0,alpha,on_trackbar)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret :
        break
    width = int(frame.shape[1] * scale/100)
    height = int(frame.shape[0] * scale/100)
    frame = cv2.resize(frame,(width,height))

    # Phase of Denoising
    frame = cv2.fastNlMeansDenoisingColored(frame,None,10,10,7,21)

    cv2.imshow("frame",frame)

    if cv2.waitKey(0) == ord('w'):
        continue
    if cv2.waitKey(0) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
