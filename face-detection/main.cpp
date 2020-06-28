#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main() {
	double scale = 3.0;
	CascadeClassifier faceCascade;
	faceCascade.load("C:\\Users\\Vansh Jain\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml");

	VideoCapture capture(0);
	if (!capture.isOpened()) {
		return 1;
	}

	while (1) {
		Mat frame;
		capture >> frame;

		Mat grayscale;
		cvtColor(frame, grayscale, COLOR_BGR2GRAY);
		resize(grayscale, grayscale, Size(grayscale.size().width / scale, grayscale.size().height / scale));

		vector<Rect> faces;
		faceCascade.detectMultiScale(grayscale, faces, 1.1, 3, 0, Size(30, 30));

		for (Rect area : faces) {
			Scalar colour = Scalar(0, 255, 0);
			int thickness = 3;
			rectangle(frame, Point(cvRound(area.x * scale), cvRound(area.y * scale)),
				Point(cvRound((area.x + area.width - 1) * scale), cvRound(area.y + area.height - 1) * scale),
				colour, thickness);
		}

		imshow("Webcam", frame);

		if (waitKey(30) >= 0) {
			exit(0);
		}
	}
}