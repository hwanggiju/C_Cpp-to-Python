#ifdef _MSC_VER                      // VC++
#define EXPORT __declspec(dllexport) // 윈도우용 dll export 지정자
#else
#define EXPORT                       // 리눅스의 경우 별다른 지정자가 필요치 않다
#endif

#include <vector>
#include <numeric>

#include "opencv2/opencv.hpp"

using namespace cv;
using namespace std;

extern "C"
{

	VideoCapture cap(0);

	EXPORT void stream()
	{
		Mat frame;
		cap >> frame;
		if (frame.empty())
			return;

		return frame;
	}
}