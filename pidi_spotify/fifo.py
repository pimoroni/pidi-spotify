import os
import select


class FIFO:
    def __init__(self, fifo_name):
        self.fifo_name = fifo_name
        try:
            os.unlink(fifo_name)
        except (IOError, OSError):
            pass

        os.mkfifo(fifo_name)
        os.chmod(fifo_name, 0o777)
        self._f = None
        self._buf = ""

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._f is not None:
            os.close(self._f)
            self._f = None

    def read(self):
        if self._f is None:
            self._f = os.open(self.fifo_name, os.O_RDONLY | os.O_NONBLOCK)

        # Check for inbound command
        r, w, e = select.select([self._f], [], [], 0)
        if self._f in r:
            while True:
                char = os.read(self._f, 1).decode("UTF-8")
                if len(char) == 0:
                    return None
                if char == "\n":
                    buf = self._buf
                    self._buf = ""
                    return buf
                self._buf += char
        else:
            return None
