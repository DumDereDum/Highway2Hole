cmake_minimum_required(VERSION 3.0.0)
project(OV_proj)
find_package(ngraph REQUIRED)
find_package(InferenceEngine REQUIRED)
find_package(OpenCV REQUIRED)
add_executable(${PROJECT_NAME} src/main.cpp src/detector.cpp
include/detector.hpp)
target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS} ${InferenceEngine_LIBRARIES} ${NGRAPH_LIBRARIES})