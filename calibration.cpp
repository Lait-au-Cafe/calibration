#include <iostream>
#include <cmath>
#include <vector>
#include <opencv2/opencv.hpp>

#define PAT_ROW 7			// number of rows
#define PAT_COL 11			// number of columns
#define CHESS_SIZE 30.0		// [mm]

using uint = unsigned int;

int main() {
	// prepare video capture
	cv::VideoCapture cap(0);
	if (!cap.isOpened()) {
		std::cerr << "Cannot open webcam device. " << std::endl;
		return EXIT_FAILURE;
	}

	// prepare window
	cv::String windowName = "Calibration";	
	cv::namedWindow(windowName, CV_WINDOW_AUTOSIZE);

	std::cout << "Press space to capture frame. " << std::endl;
	std::cout << "Press 'q' to quit capturing and begin processing. " << std::endl;

	// collect corners
	cv::Size patt_size(PAT_COL, PAT_ROW);
	std::vector<cv::Point2f> corners;
	std::vector<std::vector<cv::Point2f>> img_points;
	int key = -1;
	cv::Mat frame, gray;
	while ((key = cv::waitKey(10)) != 'q') {
		cap >> frame;
		cv::imshow(windowName, frame);
		
		if (key != ' ') {
			continue;
		}

		// find chessboard corners
		auto found = cv::findChessboardCorners(
			frame, patt_size, corners);

		if (found) {
			std::cout << "Chessboard is found. "
				<< "  Count : " << img_points.size() + 1
				<< std::endl;
		}
		else {
			std::cerr << "Not found. " << std::endl;
			continue;
		}

		// convert to subpixel resolution
		cv::cvtColor(frame, gray, CV_BGR2GRAY);
		cv::find4QuadCornerSubpix(
			gray, corners, cv::Size(3, 3));
		img_points.push_back(corners);
	}

	if (img_points.size() < 1) {
		std::cerr 
			<< "The number of captured points is not enough. " 
			<< std::endl;
		return EXIT_FAILURE;
	}

	// initialize coordinate
	std::vector<cv::Point3f> object;
	for (int row = 0; row < PAT_ROW; row++) {
		for (int col = 0; col < PAT_COL; col++) {
			cv::Point3d p(
				row * CHESS_SIZE,
				col * CHESS_SIZE,
				0.0);
			object.push_back(p);
		}
	}
	std::vector<std::vector<cv::Point3f>> obj_points;
	for (uint n = 0; n < img_points.size(); n++) {
		obj_points.push_back(object);
	}
	
	// calibrate
	cv::Mat cam_mat, dist_coefs;
	std::vector<cv::Mat> rvecs, tvecs;
	cv::calibrateCamera(
		obj_points,
		img_points,
		frame.size(),
		cam_mat,		// camera inner parameter matrix
		dist_coefs,		// camera distortion coefficients
		rvecs,			// rotations of camera at each frame
		tvecs			// translations of camera at each frame
	);

	std::cout << "Camera parameter matrix" << std::endl;
	std::cout << cam_mat << std::endl;
	std::cout << "Camera distortion coefficients" << std::endl;
	std::cout << dist_coefs << std::endl;

	return 0;
}
