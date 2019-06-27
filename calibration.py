import argparse

import cv2
import numpy as np

PAT_ROW = 7			# number of rows
PAT_COL = 11		# number of columns
CHESS_SIZE = 30.0	# [mm]

path_to_log = "./log/"
path_to_data = "./data/"

parser = argparse.ArgumentParser()
parser.add_argument("-p", help="The path to the preset data. ")
args = parser.parse_args()

use_preset =  args.p is not None

cap = cv2.VideoCapture(0) if not use_preset else cv2.VideoCapture(args.p)

