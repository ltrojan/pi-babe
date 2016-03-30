import io
import cv2
import numpy as np


def decode(string, ext='png'):
    img = np.fromstring(string, dtype=np.uint8)
    img = cv2.imdecode(img, 1)
    return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)


def get_img(cam, ext='png'):
    with io.BytesIO() as buf:
        cam.capture(buf, ext)
        return decode(buf.getvalue(), ext=ext)


if __name__ == "__main__":

    import picamera
    cam = picamera.PiCamera()

    for num in range(10):
        print "grabbing n.", num
        buf = get_img(cam)
        cv2.imwrite('tmp_' + str(num) + '.png', buf)
