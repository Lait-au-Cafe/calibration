# Camera Calibration with OpenCV

## About

This project is a sample of C++ implementation of a camera calibration with OpenCV. 
This project can be used to calibrate a web camera. 

You can do following things. 

* You can start a calibration without preset datas. It means you can do data collection and calibration at the same time. 
* Collected datas are saved automatically to "./data/[current date and time]/data[sequence number].bmp". 
* Calibration parameters are also saved to "./log/[current date and time].dat". 
* You can also use preset datas for a calibration. 

## How to use

At the root directory of this project, execute following commands. 

```
$ make
$ ./calibration
```

If you want to use preset datas, 

1. Place preset datas in "./data/[directory_name]/".  
	File format must be ".bmp" (but you can easily change to other formats by editting a script a bit).  
	You can set a directory name as you like, but file names must be "data01.bmp", "data02.bmp", ..., "data20.bmp", for example. 
2. Execute following command to run the program.  
```
$ ./calibration [directory_name]
```

The chessboard image can be aquired from [here (opencv.jp)](http://opencv.jp/sample/pics/chesspattern_7x10.pdf). 
If you want to a use different chessboard image, please make sure that the defined parameters (PAT_ROW, PAT_SIZE, CHESS_SIZE) are set correctly. 

## Reference

I refered the pages below. 

* [Camera Model in OpenCV](http://opencv.jp/opencv-2.1/cpp/camera_calibration_and_3d_reconstruction.html)
* [Sample Code in C lang by opencv.jp](http://opencv.jp/sample/camera_calibration.html)
