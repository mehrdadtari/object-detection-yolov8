import cv2
from ultralytics import YOLO
from draw_bbox import bbox_drawer

cap = cv2.VideoCapture("traffic.mp4")

# yolov8m is the medium version. 
# We also have smaller and bigger models. Bigger models are more accurate but slower.
model = YOLO("yolov8m.pt")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # results is a list with one entry of type:
    # ultralytics.yolo.engine.results.Results object
    results = model(frame, device="mps")
    # result is ultralytics.yolo.engine.results.Results object from
    # results list.
    result = results[0]

    processed_frame = bbox_drawer(result, frame, model)

    cv2.imshow("YOLOv8 Object Detection", processed_frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()