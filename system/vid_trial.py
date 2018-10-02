import numpy as np
import cv2
import pdb

# Open a sample video available in sample-videos
# pdb.set_trace()
# vcap = cv2.VideoCapture('http://137.158.126.51:8081/')
# pdb.set_trace()
vcap = cv2.VideoCapture('ColdFusionBookUpdates.mp4')
# pdb.set_trace()
if not vcap.isOpened():
    vcap.open('ColdFusionBookUpdates.mp4')



while(True):
    # Capture frame-by-frame
    ret, frame = vcap.read()
    #print cap.isOpened(), ret
    # pdb.set_trace()
    if frame is not None:
        # Display the resulting frame
        pdb.set_trace()
        cv2.imshow('frame',frame)
        # Press q to close the video windows before it ends if you want
        if cv2.waitKey(22) & 0xFF == ord('q'):
            break
    else:
        print "Frame is None"
        break

# When everything done, release the capture
vcap.release()
cv2.destroyAllWindows()
print "Video stop"






# import numpy as np
# import cv2
#
# img = cv2.imread('rose.jpeg',0)
# cv2.imshow('image',img)
# k = cv2.waitKey(0) & 0xFF
# if k == 27:         # wait for ESC key to exit
#     cv2.destroyAllWindows()
# elif k == ord('s'): # wait for 's' key to save and exit
#     cv2.imwrite('messigray.png',img)
#     cv2.destroyAllWindows()















#
# import urllib, cStringIO
#
# file = cStringIO.StringIO(urllib.urlopen('http://137.158.126.51:8081/').read())
# img = Image.open(file)









# import cv2
# import urllib
# import numpy as np
#
# stream=urllib.urlopen('http://137.158.126.51:8081/')
# bytes=''
# while True:
#     bytes+=stream.read(1024)
#     a = bytes.find('\xff\xd8')
#     b = bytes.find('\xff\xd9')
#     if a!=-1 and b!=-1:
#         jpg = bytes[a:b+2]
#         bytes= bytes[b+2:]
#         i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
#         cv2.imshow('i',i)
#         if cv2.waitKey(1) ==27:
#             exit(0)
