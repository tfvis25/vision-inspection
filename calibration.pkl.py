import cv2 as cv
import numpy as np
import pickle

# Define dummy calibration parameters
cameraMatrix = np.array([[800, 0, 320], [0, 800, 240], [0, 0, 1]], dtype=np.float32)
dist = np.zeros((5,))  # Assume no lens distortion

# Save them to a file
with open("calibration.pkl", "wb") as f:
    pickle.dump((cameraMatrix, dist), f)

print("Calibration file created successfully.")
