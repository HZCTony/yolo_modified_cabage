# keras-yolo3
This project is modified from https://github.com/qqwweee/keras-yolo3.git 

You can just do three steps to train your own model.(The premise is that you should build your own development environment first)

# 1. prepare your own data
You should make your image paths corresponding to the points was written to a .txt file. 

every line should be:

/mypath/1.jpg xmin,ymin,xmax,ymax,classNum

The "xmin,ymin,xmax,ymax" means a labelling box of an object with its own left-up and right-down points.

The .txt file path should be added to "annotation_path" in YOLOv3_train.py

# 2. train your own data 

check path about your source data. like below:

    annotation_path = './cabage_renew.txt'
    log_dir = '/keras-yolo3/logs/001/'
    classes_path = './cabage_renew/cabage_name.txt'
    anchors_path = './cabage_renew/cabage_anchors.txt'

If you already checked, run:

```
python3 YOLOv3_train.py
```

# 3. infer your own data

check path in YOLOv3_infer.py:
    
    IN_DIR = './cabage_renew/jpg/'
    OUT_DIR = './cabage_renew/infer/'

check the params in yolomod.py:

          _defaults = {
              "model_path": '/keras-yolo3/logs/001/trained_model_final_anchors-3.h5',
              "anchors_path": '/keras-yolo3/cabage/cabage_anchors.txt',
              "classes_path": '/keras-yolo3/cabage/cabage_name.txt',
              "score" : a float num that you want as a threshold value,
              "iou" : a float num that you wantas a threshold value,
              "model_image_size" : (416, 416),
              "gpu_num" : 1,
          }

If you already checked, run:

```
python3 YOLOv3_infer.py
```
