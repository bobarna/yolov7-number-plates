# Transfer Learning to Number Plate Recognition
## Main repository of the project
[https://github.com/bobarna/bme-image-processing](https://github.com/bobarna/bme-image-processing)

## Run inference (detect licence plates)
```
python detect.py --weights runs/train/number-plates7/weights/last.pt --img-size 448 --source number-plates-hun/test/ --save-txt --name test-number-plates
```
`--save-txt` also saves the labels as `*.txt` files. 
(`detect.py` could also take in single images instead of a whole directory.)

## Hungarian License Plate Recgnition Dataset
Images of cars with license plates (without labels) is available here:
https://barnabasborcsok.com/number-plates-hun-1342.zip

Backup:
https://drive.google.com/file/d/1Hgds3pXZP2sX2EB0GeYWaFLiA96h4JlW/view?usp=share_link

# Official YOLOv7
For more details, see the [original
implementation](https://github.com/WongKinYiu/yolov7) of the paper 
[YOLOv7:Trainable bag-of-freebies sets new state-of-the-art for real-time object
detectors](https://arxiv.org/abs/2207.02696).

