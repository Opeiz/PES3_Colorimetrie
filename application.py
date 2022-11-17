import cv2

# Function for create frames from a video, its easier to proccess later
def CreateFrames(video):

    vidcap = cv2.VideoCapture(video)
    success,image = vidcap.read()
    count = 0

    while success:
        cv2.imwrite("colors/frame%d.jpg" % count, image)     # save frame as JPG file      
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1

CreateFrames("media/Color.mp4")

# cap = cv2.VideoCapture("media/Color.mp4")


# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret :
#         break
    # width = int(frame.shape[1] * scale/100)
    # height = int(frame.shape[0] * scale/100)
    # frame = cv2.resize(frame,(width,height))

#     # Phase of Denoising
#     frame = cv2.fastNlMeansDenoisingColored(frame,None,10,10,7,21)

#     cv2.imshow("frame",frame)

#     if cv2.waitKey(0) == ord('w'):
#         continue
#     if cv2.waitKey(0) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
