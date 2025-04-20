import cv2
import time
import numpy as np

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

cap = cv2.VideoCapture(0)
time.sleep(3)

# Capture background
background = None
for i in range(60):
    ret, background = cap.read()
    if not ret:
        print("Failed to capture background. Exiting...")
        cap.release()
        exit(0)
background = np.flip(background, axis=1)

# Main loop
while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break

    img = np.flip(img, axis=1)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define the HSV range for black
    lower_black = np.array([ 0,0 ,0])
    upper_black = np.array([96,49,111])
    mask1 = cv2.inRange(hsv, lower_black, upper_black)

    # Morphological operations
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

    # Invert mask
    mask2 = cv2.bitwise_not(mask1)

    # Segment out the black color and replace with background
    res1 = cv2.bitwise_and(img, img, mask=mask2)
    res2 = cv2.bitwise_and(background, background, mask=mask1)

    # Combine results
    finalOutput = cv2.addWeighted(res1, 1, res2, 1, 0)
    # out.write(finalOutput)

    # Display output
    cv2.imshow("Magic", finalOutput)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
