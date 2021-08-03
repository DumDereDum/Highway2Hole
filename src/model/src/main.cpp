#include <iostream>
#include "../include/detector.hpp"

#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <fstream>

#define str "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
#define pd 60

static const char* keys =
"{ m  models_path          | <none>	    | path to models                                                                    }"
"{ v  video_path           | <none>	    | path to video                                                                    }"
"{ o  outpath              | <none>     | path to save clips                                                                }"
"{ mode                    | 1          | mode to show result   mode=1 save result in out.avi    mode=2 show on screen      }"
"{ help h usage ?          |            | print help message                                                                }";

void progressBar(double progress) {
	int val = (int)(progress * 100);
	int left = (int)(progress * pd);
	int rigth = pd - left;
	printf("\r%3d%% [%.*s%*s]", val, left, str, rigth, "");
	fflush(stdout);
}

cv::Mat draw_bbox(cv::Mat& frame, std::vector<DetectionObject>& objects)
{
	for (int i = 0; i < objects.size(); i++)
	{
		if (objects[i].confidence > 0.5)
			cv::rectangle(frame, cv::Rect(cv::Point(objects[i].xmin, objects[i].ymin), cv::Point(objects[i].xmax, objects[i].ymax)), cv::Scalar(225, 0, 0));
	}
	return frame;
}

int main(int argc, char** argv) {

	cv::CommandLineParser parser(argc, argv, keys);

	if (parser.has("help"))
	{
		parser.printMessage();
		return 0;
	}

	cv::String FLAGS_m                 = parser.get<cv::String>("m") + "/yolov3-tiny.xml";
	cv::String FLAGS_c                 = parser.get<cv::String>("m") + "/yolov3-tiny.bin";
	cv::String FLAGS_v                 = parser.get<cv::String>("v");
	cv::String out_path                = parser.get<cv::String>("o") + "/out.avi";
	cv::String mode                    = parser.get<cv::String>("mode");

	if (!parser.check())
	{
		parser.printErrors();
		throw "Parse error";
		return 0;
	}

	InferenceEngine::Core ie;

	Detector detector(FLAGS_m, FLAGS_c, ie);

	int frame_counter = 1;
	cv::Mat frame;
	cv::Mat result;
	cv::VideoCapture capture(FLAGS_v);

	double frame_width = capture.get(cv::CAP_PROP_FRAME_WIDTH);
	double frame_height = capture.get(cv::CAP_PROP_FRAME_HEIGHT);
	std::vector<DetectionObject> detections;

	cv::VideoWriter out(out_path,
		cv::VideoWriter::fourcc('M', 'J', 'P', 'G'), 10, cv::Size(frame_width, frame_height), true);

	std::cout << "Progress bar..." << std::endl;

    double fps = capture.get(cv::CAP_PROP_FPS);

	std::ofstream log;
	log.open(parser.get<cv::String>("o") + "/log.txt");


	while (frame_counter < capture.get(cv::CAP_PROP_FRAME_COUNT))
	{
		progressBar((frame_counter + 1) / capture.get(cv::CAP_PROP_FRAME_COUNT));
		capture >> frame;
		if (frame.empty())
		{
			frame_counter++;
			continue;
		}

		detections = detector.getDetections(frame);
		if (detections.size())
			log << "Damage detected on frame = " << frame_counter << std::endl;
		frame = draw_bbox(frame, detections);
		
		if (mode == "1")
		{
			out.write(frame);
		}
		if (mode == "2") {
			cv::imshow("Roads", frame);
			if (cv::waitKey(5) >= 0)
				break;
		}
		frame_counter++;
	}

	std::cout << std::endl;
	std::cout << "Frames per second using video.get(CAP_PROP_FPS) : " << fps << std::endl;
	std::cout << std::endl;
	std::cout << "Completed";
	return 0;
}