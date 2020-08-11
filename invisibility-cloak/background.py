import cv2

def main():
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, back = cap.read()

        if ret:
            cv2.imshow("image", back)
            k = cv2.waitKey(10)
            # Escape to quit
            if k == 27:
                cv2.imwrite('image.jpg', back)
                break

    cap.release()

if __name__ == "__main__":
    main()