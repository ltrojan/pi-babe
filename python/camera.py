import StringIO
import picamera
import cv2


if __name__ == "__main__":
    cam = picamera.PiCamera()
    buf = StringIO.StringIO()
    cam.capture(buf, 'png')
    cv2.imwrite('test.png', buf)
    cam.close()
