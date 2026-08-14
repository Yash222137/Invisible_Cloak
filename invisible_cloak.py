import cv2
import numpy as np
import time

def main():
    print("Starting webcam...")
    cap = cv2.VideoCapture(0)

    # Allow camera to warm up
    time.sleep(2)
    background = 0

    # Capture background
    print("Capturing background... Please move out of frame.")
    for i in range(30):
        ret, background = cap.read()

    if not ret:
        print("Error: Could not capture background. Is the webcam connected?")
        cap.release()
        return

    # Flip the background horizontally
    background = np.flip(background, axis=1)

    print("Background captured. You can now enter the frame with the cloak.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip frame horizontally for a natural mirror view
        frame = np.flip(frame, axis=1)

        # Convert the frame to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define ranges for the red color
        # Red color has two ranges in HSV
        lower_red1 = np.array([0, 120, 70])
        upper_red1 = np.array([10, 255, 255])

        lower_red2 = np.array([170, 120, 70])
        upper_red2 = np.array([180, 255, 255])

        # Create masks for red color
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask = mask1 + mask2

        # Morphological operations to remove noise and smoothen the mask
        # Opening removes noise, dilation expands the mask slightly to cover edges
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)

        # Create an inverted mask to get everything EXCEPT the cloak
        mask_inv = cv2.bitwise_not(mask)

        # Segment out the cloak region from the background
        res1 = cv2.bitwise_and(background, background, mask=mask)

        # Segment out the non-cloak region from the current frame
        res2 = cv2.bitwise_and(frame, frame, mask=mask_inv)

        # Combine the two images
        final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

        # Display the result
        cv2.imshow("Invisible Cloak", final_output)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
