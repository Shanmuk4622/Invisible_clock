import cv2
import numpy as np

def nothing(x):
    pass

# Open the webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Unable to access the webcam.")
    exit()

# Create a window for the trackbars
cv2.namedWindow("HSV Calibration")

# Create trackbars for HSV ranges
cv2.createTrackbar("Lower Hue", "HSV Calibration", 0, 180, nothing)
cv2.createTrackbar("Lower Saturation", "HSV Calibration", 0, 255, nothing)
cv2.createTrackbar("Lower Value", "HSV Calibration", 0, 255, nothing)
cv2.createTrackbar("Upper Hue", "HSV Calibration", 0, 180, nothing)
cv2.createTrackbar("Upper Saturation", "HSV Calibration", 0, 255, nothing)
cv2.createTrackbar("Upper Value", "HSV Calibration", 0, 255, nothing)

# Set initial values for the upper trackbars
cv2.setTrackbarPos("Upper Hue", "HSV Calibration", 180)
cv2.setTrackbarPos("Upper Saturation", "HSV Calibration", 255)
cv2.setTrackbarPos("Upper Value", "HSV Calibration", 255)

print("Adjust the sliders to find the correct HSV range for your cloak. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to read from webcam.")
        break

    # Flip the frame
    frame = cv2.flip(frame, 1)

    # Convert the frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get the current positions of the trackbars
    l_h = cv2.getTrackbarPos("Lower Hue", "HSV Calibration")
    l_s = cv2.getTrackbarPos("Lower Saturation", "HSV Calibration")
    l_v = cv2.getTrackbarPos("Lower Value", "HSV Calibration")
    u_h = cv2.getTrackbarPos("Upper Hue", "HSV Calibration")
    u_s = cv2.getTrackbarPos("Upper Saturation", "HSV Calibration")
    u_v = cv2.getTrackbarPos("Upper Value", "HSV Calibration")

    # Define the HSV range
    lower_hsv = np.array([l_h, l_s, l_v])
    upper_hsv = np.array([u_h, u_s, u_v])

    # Create a mask for the selected HSV range
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)

    # Display the mask and the original frame
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Mask", mask)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Lower HSV:", lower_hsv)
        print("Upper HSV:", upper_hsv)
        break

cap.release()
cv2.destroyAllWindows()
