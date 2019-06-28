import argparse
import datetime.datetime

import cv2
import numpy as np

PAT_ROW = 7			# number of rows
PAT_COL = 11		# number of columns
CHESS_SIZE = 30.0	# [mm]

path_to_log = "./log/"
path_to_data = "./data/"
date_format = "%Y%m%d-%H%M%S"
filename_format = "%d.png"

parser = argparse.ArgumentParser()
parser.add_argument("-d", help="The path to the preset data (optional). ")
args = parser.parse_args()

use_preset =  args.d is not None

cap = cv2.VideoCapture(0) if not use_preset else cv2.VideoCapture(f"{args.d}{filename_format}")
if not cap.isOpened():
    exit("Cannot open a web camera or pre-captured images. ")

window_name = "Calibration"
cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

print("Press space to capture frame. ")
print("Press 'q' to quit capturing and begin processing. ")

now = datetime.now().strftime(date_format)
data_dirname = f"{path_to_data}{now}"
os.makedirs(data_dirname)

# The 3D coordinates of each corner of chessboard
obj_p = np.zeros((PAT_COL * PAT_ROW, 3), np.float32)
obj_p[:,:2] = np.mgrid[0:PAT_COL, 0:PAT_ROW].T.reshape(-1, 2)

img_pts = [] # 2D coordinates of chessboard corners
obj_pts = [] # 3D coordinates of chessboard corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
key = -1
while key != 27:
    ret, frame = cap.read()
    if not ret: break

    cv2.imshow(window_name, frame)

    if not use_preset and key != ord(' '): continue

    # Find chessboard and its corners
    found, corners = cv2.findChessboardCorners(frame, (PAT_COL, PAT_ROW))
    if found:
        print(f"Chessboard is found. Count: {len(img_pts) + 1}")
    else:
        print("Chessboard is not found. ")
        continue

    # append 3D coordinates
    obj_pts.append(obj_p)

    # Refine corners and append their 2D coordinates
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
    img_pts.append(corners)

    # save if it is captured now
    if not use_preset:
        cv2.imwrite(f"{data_dirname}/frame{len(img_pts)}.png", frame)

# Check if acquired points are enough
if len(img_pts) < 1:
    exit("The number of captured points is not enough. ")

# Calibrate camera
ret, k_mat, dist_coef, rvecs, tvecs = \
        cv2.calibrateCamera(obj_pts, img_pts, gray.shape[::-1], None, None)

print(k_mat)
print(type(k_mat))
