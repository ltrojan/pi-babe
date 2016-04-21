import time
import io
import threading
import picamera


class Camera(object):

    _cls_thread = None  # background thread that reads frames from camera
    _cls_frame = None  # current frame is stored here by background thread
    _time_access = 0  # time of last client access to the camera
    _time_limit = 10

    @property
    @classmethod
    def _time_update(cls):
        cls._time_access = time.time()
        return cls._time_access

    @property
    @classmethod
    def _time_elapsed(cls):
        return time.time() - cls._last_access

    @property
    @classmethod
    def _time_stop(cls):
        return cls._time_elapsed > cls._time_limit

    def _initialize(self):

        # initialize only if thread is dead
        if self._cls_thread is not None:
            return None

        # start background frame thread
        Camera.thread = threading.Thread(target=self._thread)
        Camera.thread.start()

        # wait until frames start to be available
        while self.frame is None:
            time.sleep(0)

    def get_frame(self):
        if Camera.thread is None:
            self.initialize()
        Camera.last_access = time.time()
        return self.frame

    @classmethod
    def _thread(cls):
        with picamera.PiCamera() as camera:
            # camera setup
            cls._time_update
            camera.resolution = (640, 480)
            camera.hflip = True
            camera.vflip = True

            # let camera warm up
            camera.start_preview()
            time.sleep(2)

            stream = io.BytesIO()
            for foo in camera.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
                # store frame
                stream.seek(0)
                cls.frame = stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()

                # if there hasn't been any clients asking for frames in
                # the last 10 seconds stop the thread
                if time.time() - cls.last_access > 10:
                    cls.frame = None
                    break
        cls.thread = None
