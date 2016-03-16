# hello

import StringIO
import time
import picamera


if __name__ == "__main__":
    cam = picamera.PiCamera()
    buf = StringIO.StringIO()
    cam.capture(buf, 'png')
    cam.close()
