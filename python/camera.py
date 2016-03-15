# hello

import StringIO
import time
import picamera


if __name__ == "__main__":
    cam = picamera.PiCamera()
    buf = cam.capture(self._buf, 'png')
    cam.close()
