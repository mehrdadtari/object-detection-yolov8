import cv2
import numpy as np

# This function draws bounding boxes and their associated class names.
def bbox_drawer(res, frame, model):
    bboxes = np.array(res.boxes.xyxy.cpu(), dtype="int")
    classes = np.array(res.boxes.cls.cpu(), dtype="int")
    for cls, bbox in zip(classes, bboxes):
        (x, y, x2, y2) = bbox
        cv2.rectangle(frame, (x,y), (x2, y2), (70, 110, 225), 2)
        cv2.putText(frame, model.names[int(cls)], (x, y-6), cv2.FONT_HERSHEY_PLAIN, 2, (10, 30, 255), 2)
    return frame