#해당 코드는 Node-red와 연결, 버튼을 클릭시 사진이 촬영(Node-red로 구현) 
#Yolo모델로 촬영된 사진에서 차량을 예측한 후에 사진이 저장된다.

import cv2
import json
import os

BASE_DIR = "/home/oyj1234/py_rip"

image_path = os.path.join(BASE_DIR, "dashboard_photo.jpg")
cfg_path = os.path.join(BASE_DIR, "yolov3-tiny.cfg")
weights_path = os.path.join(BASE_DIR, "yolov3-tiny.weights")
names_path = os.path.join(BASE_DIR, "coco.names")
output_path = os.path.join(BASE_DIR, "vehicle_result.jpg")

vehicle_classes = ["car", "motorbike", "bus", "truck"]

with open(names_path, "r") as f:
    classes = [line.strip() for line in f.readlines()]

image = cv2.imread(image_path)

if image is None:
    print(json.dumps({
        "status": "error",
        "message": "Image not found",
        "image_path": image_path
    }))
    exit()

height, width = image.shape[:2]

net = cv2.dnn.readNetFromDarknet(cfg_path, weights_path)
output_layers = net.getUnconnectedOutLayersNames()

blob = cv2.dnn.blobFromImage(
    image,
    scalefactor=1 / 255.0,
    size=(416, 416),
    swapRB=True,
    crop=False
)

net.setInput(blob)
outputs = net.forward(output_layers)

boxes = []
confidences = []
class_ids = []

for output in outputs:
    for detection in output:
        scores = detection[5:]
        class_id = scores.argmax()
        confidence = scores[class_id]

        class_name = classes[class_id]

        if class_name in vehicle_classes and confidence > 0.3:
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.3, 0.4)

detected = []

if len(indexes) > 0:
    for i in indexes.flatten():
        x, y, w, h = boxes[i]
        label = classes[class_ids[i]]
        conf = confidences[i]

        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(
            image,
            f"{label} {conf:.2f}",
            (x, max(y - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

        detected.append({
            "class": label,
            "confidence": round(conf, 2)
        })

cv2.imwrite(output_path, image)

print(json.dumps({
    "status": "success",
    "vehicle_count": len(detected),
    "detected": detected,
    "result_image": output_path
}))
