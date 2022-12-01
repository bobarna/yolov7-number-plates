# Transfer Learning to Number Plate Recognition
## Main repository of the project
[https://github.com/bobarna/bme-image-processing](https://github.com/bobarna/bme-image-processing)

## Run inference (detect licence plates)
```
python detect.py --weights weights-number-plates.pt --img-size 448 --source number-plates-hun/ --name test-number-plates --save-txt --save-conf
```

- `--weights`: pretrained weights (result of the transfer learning)
- `--img-size`: size used for the inference
- `--source`: folder containing the images
- `--name`: name for this inference
- `--save-txt`: also saves the labels as `*.txt` files 
- `--save-conf`: also saves the confidence in the `*.txt` files

(`detect.py` could also take in single images instead of a whole directory.)

Each line of a detection (`image_name.txt`) takes the following form:

```
object_id x_min x_max y_min y_max confidence
```

- `object_id`: describes which object is detected (in our case, this is always
0 for the number plate class)
- `x_min`, `x_max`, `y_min`, `y_max`: describe the dimension of the bounding box
- `confidence`: 0..1 value for the confidence of the given detection.

(We modified `detect.py` to output detections in image-space, instead of the
original relative dimensions.)

## Run transfer learning (for reproducibility)
```
python3 train.py --workers 8 --device 0 --batch-size 8 --data data/number-plates.yaml --img 420 --cfg cfg/training/yolov7-number-plates.yaml --weights yolov7_training.pt --name yolov7-custom --hyp data/hyp.scratch.custom.yaml
```

**Hungarian License Plate Recognition Dataset:** 
Images of cars with license plates (without labels) 
- https://barnabasborcsok.com/number-plates-hun-1342.zip
- backup: https://drive.google.com/file/d/1Hgds3pXZP2sX2EB0GeYWaFLiA96h4JlW/view?usp=share_link

# Forked from the official YOLOv7 implementation
For more details, see: 
- [original implementation](https://github.com/WongKinYiu/yolov7) 
- [paper](https://arxiv.org/abs/2207.02696)

