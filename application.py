import cv2

# Function for create frames from a video, its easier to proccess later
def CreateFrames(video):

    vidcap = cv2.VideoCapture(video)
    success,image = vidcap.read()
    count = 0

    while success:
        cv2.imwrite("frames/frame%d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1

cap = cv2.VideoCapture("media/Video.mp4")
scale = 30

CreateFrames("media/Video.mp4")

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret :
#         break
#     width = int(frame.shape[1] * scale/100)
#     height = int(frame.shape[0] * scale/100)
#     frame = cv2.resize(frame,(width,height))

#     # Phase of Denoising
#     frame = cv2.fastNlMeansDenoisingColored(frame,None,10,10,7,21)

#     cv2.imshow("frame",frame)

#     if cv2.waitKey(0) == ord('w'):
#         continue
#     if cv2.waitKey(0) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
