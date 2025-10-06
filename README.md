# simple-fps-counter

python fps module you can plug into a thread

```py
import cv2
from fps import FPSCounter
fps_counter = FPSCounter()
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    print(fps_counter.measure_fps())
cap.release()
```
