import numpy as np
import cv2
import pdb

# Open a sample video available in sample-videos
# pdb.set_trace()
vcap = cv2.VideoCapture('http://137.158.127.114:8082/testing')
# pdb.set_trace()
# vcap = cv2.VideoCapture('ColdFusionBookUpdates.mp4')
# pdb.set_trace()
if not vcap.isOpened():
    vcap.open('http://137.158.127.114:8082/testing')



while(True):
    # Capture frame-by-frame
    ret, frame = vcap.read()
    #print cap.isOpened(), ret
    # pdb.set_trace()
    if frame is not None:
        # Display the resulting frame
        # pdb.set_trace()
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
