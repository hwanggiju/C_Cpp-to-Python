#include "opencv2/opencv.hpp"

using namespace cv;
using namespace std;

void main() {
	VideoCapture cap(0);

	if (!cap.isOpened()) {
		cerr << "camera open failed" << endl;
		return;
	}

	Mat frame, inversed;
	while (true) {
		cap >> frame;
		if (frame.empty())
			break;
		else {
			// inversed = ~frame;
			imshow("camera", frame);

			if (waitKey(10) == 27)
				break;
		}
	}
	destroyAllWindows();
}