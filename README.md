# Camera Calibration with OpenCV

## About

This project is a sample of C++ implementation of a camera calibration with OpenCV. 
This project can be used to calibrate a web camera. 

You can do following things. 

1. You can start a calibration without preset datas. It means you can do data collection and calibration at the same time. 
2. Collected datas are saved automatically to "./data/[current date and time]/data[sequence number].bmp". 
3. Calibration parameters are also saved to "./log/[current date and time].dat". 

## How to use

At the root directory of this project, execute following commands. 

```
$ make
$ ./calibration
```

I refered the pages below. 

* [Camera Model in OpenCV](http://opencv.jp/opencv-2.1/cpp/camera_calibration_and_3d_reconstruction.html)
* [Sample Code in C lang by opencv.jp](http://opencv.jp/sample/camera_calibration.html)
