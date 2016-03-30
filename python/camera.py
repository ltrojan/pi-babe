from babe_cam import cam_io
import io
import picamera


if __name__ == "__main__":
    cam = picamera.PiCamera()
    img = cam_io.get_img(cam)
    print img.shape
    cam.close()
