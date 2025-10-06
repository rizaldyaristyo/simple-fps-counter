import time
from collections import deque

class FPSCounter:
    def __init__(self, smoothing: int = 30, round: bool = True):
        self.last_time = None
        self.intervals = deque(maxlen=smoothing)

    def measure_fps(self) -> float:
        now = time.time()

        if self.last_time is None:
            self.last_time = now
            return 0.0
        elapsed = now - self.last_time
        self.last_time = now
        if elapsed > 0:
            self.intervals.append(elapsed)
        if not self.intervals:
            return 0.0
        avg_interval = sum(self.intervals) / len(self.intervals)
        return (round(1.0 / avg_interval, 2) if round else 1.0 / avg_interval) if avg_interval > 0 else 0

if __name__ == "__main__":
    import cv2
    fps_counter = FPSCounter()
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        print(fps_counter.measure_fps())

    cap.release()