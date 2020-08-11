import cv2 # noqa
import numpy as np # noqa 

def main():
    capture_video = cv2.VideoCapture(0)
    background = cv2.imread("image.jpg")
    
    while (capture_video.isOpened()): 
        return_val, frame = capture_video.read() 
        if not return_val : 
            break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        red = np.uint8([[[64,30,254]]])

        hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)

        l_red = np.array([100, 40, 40]) # fix lower value
        u_red = np.array([180, 255, 255]) # fix upper value

        mask = cv2.inRange(hsv, l_red, u_red)

        part1 = cv2.bitwise_and(background, background, mask=mask)

        mask = cv2.bitwise_not(mask)

        part2 = cv2.bitwise_and(frame, frame, mask=mask)

        final_output = part1 + part2
        cv2.imshow("Invisibility Cloak", final_output) 

        k = cv2.waitKey(10)
        # Escape to quit
        if k == 27:
            break

    capture_video.release()

if __name__ == "__main__":
    main()