/*
Copyright (c) 2020, Souya Watanabe and Ryoko Shiojima
All rights reserved.
*/
#include <ros/ros.h>
#include <sensor_msgs/Image.h>
#include <cv_bridge/cv_bridge.h>
#include <opencv2/opencv.hpp>
#include <geometry_msgs/Pose2D.h>
#include <vector>

#define WIDTH 320
#define HEIGHT 240

using namespace::cv;
using namespace sensor_msgs;
void callback(const ImageConstPtr& rgb_msg, const ImageConstPtr& depth_msg)
{
  // Solve all of perception here...
}
geometry_msgs::Pose2D pose;
//std::string msg; 
class depth_estimater{
public:          //変数をpublicで宣言
    depth_estimater();
    ~depth_estimater();
    void rgbImageCallback(const sensor_msgs::ImageConstPtr& msg);
    void depthImageCallback(const sensor_msgs::ImageConstPtr& msg);
private:
    ros::NodeHandle nh;
    ros::Subscriber sub_rgb, sub_depth;
    ros::Publisher pub_blue = nh.advertise<geometry_msgs::Pose2D>("blue",1);//トピック名blue
    ros::Publisher pub_red = nh.advertise<geometry_msgs::Pose2D>("red",1);//トピック名red
};

depth_estimater::depth_estimater(){
  sub_rgb = nh.subscribe<sensor_msgs::Image>("/camera/color/image_raw", 1, &depth_estimater::rgbImageCallback, this);
  sub_depth = nh.subscribe<sensor_msgs::Image>("/camera/depth/image_rect_raw/", 1, &depth_estimater::depthImageCallback, this);
}

depth_estimater::~depth_estimater(){
}

void depth_estimater::rgbImageCallback(const sensor_msgs::ImageConstPtr& msg){
  cv_bridge::CvImagePtr cv_ptr;//ros形式からopencv形式に変換したやつを格納する,cv_ptr->imageが cv::Mat
/*--rosからopencvに変換-----------------------------------*/
  try{
    cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::BGR8);
  }catch (cv_bridge::Exception& ex) {
    ROS_ERROR("error");
    exit(-1);
  }

  cv::Mat hsv_image_g, hsv_image_b, hsv_image_r;
  cv::Mat bin_image_g, bin_image_b, bin_image_r;
  cv::Mat output_image_g, output_image_b, output_image_r;

  cv::Mat rgb_image = cv_ptr->image, output_image;

  cvtColor(rgb_image, hsv_image_g, CV_BGR2HSV, 3);//rgbからhsvに変換
  cvtColor(rgb_image, hsv_image_b, CV_BGR2HSV, 3);
  cvtColor(rgb_image, hsv_image_r, CV_BGR2HSV, 3);

  //cvtColor(rgb_image, hsv_image, CV_BGR2HSV, 3);
  //cvtColor(cv_ptr->image, hsv_image, hsv_image, CV_BGR2HSV, 3);//rgbからhsvに変換

  Scalar low_g = Scalar(20, 100, 100);//hsvで表した緑あたり/(40. 50, 50)
  Scalar high_g = Scalar(100, 255, 255);
  Scalar low_b = Scalar(80, 150, 100);
  Scalar high_b = Scalar(160, 255, 255);
  Scalar low_r = Scalar(150, 100, 0);
  Scalar high_r = Scalar(190, 255, 255);

  cv::inRange(hsv_image_g, low_g, high_g, bin_image_g);//2値化
  cv::inRange(hsv_image_b, low_b, high_b, bin_image_b);
  cv::inRange(hsv_image_r, low_r, high_r, bin_image_r);
  
  //rgb_image.copyTo(output_image, bin_image_g);//マスク
  rgb_image.copyTo(output_image, bin_image_b);
  rgb_image.copyTo(output_image, bin_image_r);
  //cv_ptr->image.copyTo(output_image, bin_image);//マスク

  std::vector< std::vector< cv::Point > > contours_g, contours_b, contours_r;

  cv::findContours(bin_image_g, contours_g, CV_RETR_EXTERNAL, CV_CHAIN_APPROX_NONE);
  cv::findContours(bin_image_b, contours_b, CV_RETR_EXTERNAL, CV_CHAIN_APPROX_NONE);
  cv::findContours(bin_image_r, contours_r, CV_RETR_EXTERNAL, CV_CHAIN_APPROX_NONE);
  
  double area_b=0;
  int max_area_contour_b=-1;
  double max_area_b = 0;
  for(int j=0;j<contours_b.size();j++){
    area_b=contourArea(contours_b.at(j));
    if(max_area_b<area_b){
        max_area_b=area_b;
        max_area_contour_b=j;
    }
  }
  if(max_area_contour_b != -1){
    int count_b=contours_b.at(max_area_contour_b).size();
    double x_b=0;
    double y_b=0;
    for(int k=0;k<count_b;k++){
      x_b+=contours_b.at(max_area_contour_b).at(k).x;
      y_b+=contours_b.at(max_area_contour_b).at(k).y;
    }
    x_b/=count_b;
    y_b/=count_b;

    if(max_area_b > 1000){
      pose.theta = 1;
    }else{
      pose.theta = 0;
    }

    //画像の中心を(0,0)とした
   // pose.x = 320 - x_b;//→が正
    pose.x = x_b - 320;//←が正
    //pose.y = y_b - 240;//↓が正
    pose.y = 240 - y_b;//↑が正
    //printf("x = %lf, y = %lf theta = %lf\n", pose.x, pose.y, pose.theta);
    circle(rgb_image, Point(x_b,y_b),100, Scalar(128,0,128),3,4);

    pub_blue.publish(pose);
  }else{
    pub_blue.publish(pose);
    //printf("x = %lf, y = %lf theta = %lf\n", pose.x, pose.y, pose.theta);
  }

  for(int x = 0; x < 640; x += 50){
    line(rgb_image, Point(x, 0), Point(x, 480), Scalar(0, 200, 200), 1, 0);
  }
  for(int y = 0; y < 480; y +=50){
    line(rgb_image, Point(0, y), Point(640, y), Scalar(0, 200, 200), 1, 0);
  }

  double area_r=0;
  int max_area_contour_r=-1;
  double max_area_r = 0;
  for(int j=0;j<contours_r.size();j++){
    area_r=contourArea(contours_r.at(j));
    if(max_area_r<area_r){
        max_area_r=area_r;
        max_area_contour_r=j;
    }
  }
  if(max_area_contour_r != -1){
    int count_r=contours_r.at(max_area_contour_r).size();
    double x_r=0;
    double y_r=0;
    for(int k=0;k<count_r;k++){
      x_r+=contours_r.at(max_area_contour_r).at(k).x;
      y_r+=contours_r.at(max_area_contour_r).at(k).y;
    }
    x_r/=count_r;
    y_r/=count_r;
   
    if(max_area_r > 1000){
      pose.theta = 1;
    }else{
      pose.theta = 0;
    }
   
    //画像の中心を(0,0)とした
    //pose.x = 320 - x;//→が正
    pose.x = x_r - 320;//←が正
    //pose.y = y - 240;//↓が正
    pose.y = 240 - y_r;//↑が正
    //printf("x = %lf, y = %lf theta = %lf\n", pose.x, pose.y, pose.theta);
    circle(rgb_image, Point(x_r,y_r),100, Scalar(128,128,0),3,4);
   
    pub_red.publish(pose);
  }else{
    pub_red.publish(pose);
    printf("x = %lf, y = %lf theta = %lf\n", pose.x, pose.y, pose.theta);
  }
   
  for(int x = 0; x < 640; x += 50){
    line(rgb_image, Point(x, 0), Point(x, 480), Scalar(0, 200, 200), 1, 0);
  }
  for(int y = 0; y < 480; y +=50){
    line(rgb_image, Point(0, y), Point(640, y), Scalar(0, 200, 200), 1, 0);
  }
/*
  double area_g=0;
  int max_area_contour_g=-1;
  double max_area_g = 0;
  for(int j=0;j<contours_g.size();j++){
    area_g=contourArea(contours_g.at(j));
    if(max_area_g<area_g){
        max_area_r=area_g;
        max_area_contour_g=j;
    }
  }
  if(max_area_contour_g != -1){
    int count_g=contours_g.at(max_area_contour_g).size();
    double x=0;
    double y=0;
    for(int k=0;k<count_g;k++){
      x+=contours_g.at(max_area_contour_g).at(k).x;
      y+=contours_g.at(max_area_contour_g).at(k).y;
    }
    x/=count_g;
    y/=count_g;

    if(max_area_g > 1000){
      pose.theta = 1;
    }else{
      pose.theta = 0;
    }

    //画像の中心を(0,0)とした
    //pose.x = 320 - x;//→が正
    pose.x = x - 320;//←が正
    //pose.y = y - 240;//↓が正
    pose.y = 240 - y;//↑が正
    //printf("x = %lf, y = %lf theta = %lf\n", pose.x, pose.y, pose.theta);
    circle(rgb_image, Point(x,y),100, Scalar(0,0,255),3,4);

    pub_pose.publish(pose);
  }else{
    pub_pose.publish(pose);
    //printf("x = %lf, y = %lf theta = %lf\n", pose.x, pose.y, pose.theta);
  }

  for(int x = 0; x < 640; x += 50){
    line(rgb_image, Point(x, 0), Point(x, 480), Scalar(0, 200, 200), 1, 0);
  }
  for(int y = 0; y < 480; y +=50){
    line(rgb_image, Point(0, y), Point(640, y), Scalar(0, 200, 200), 1, 0);
  }
  //circle(rgb_image, Point(x,y),100, Scalar(0,0,255),3,4);
*/
  circle(rgb_image, Point(320, 240),25, Scalar(0,255,255),3,4);
  cv::imshow("rgb", rgb_image);//RGB画像を表示
  cv::imshow("result", output_image);//2値化画像を表示
  cv::imshow("hsv", hsv_image_b);//HSV画像を表示
  cv::waitKey(10);

}

void depth_estimater::depthImageCallback(const sensor_msgs::ImageConstPtr& msg){
int x1, x2, y1, y2;
int i, j, k;
int width = WIDTH;
int height = HEIGHT;
double sum = 0.0;
double ave;
cv_bridge::CvImagePtr cv_ptr;

try{
cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::TYPE_32FC1);
}catch (cv_bridge::Exception& ex){
ROS_ERROR("error");
exit(-1);
}
cv::Mat depth(cv_ptr->image.rows, cv_ptr->image.cols, CV_32FC1);
cv::Mat img(cv_ptr->image.rows, cv_ptr->image.cols, CV_8UC1);
//cv::Mat depth = cv_ptr;

x1 = int(depth.cols / 2) - width;
x2 = int(depth.cols / 2) + width;
y1 = int(depth.rows / 2) - height;
y2 = int(depth.rows / 2) + height;

for(i = 0; i < cv_ptr->image.rows;i++){
float* Dimage = cv_ptr->image.ptr<float>(i);
float* Iimage = depth.ptr<float>(i);
char* Ivimage = img.ptr<char>(i);
for(j = 0 ; j < cv_ptr->image.cols; j++){
if(Dimage[j] > 0.0){
Iimage[j] = Dimage[j];
Ivimage[j] = (char)(255*(Dimage[j]/8.0));
}else{
}

if(i > y1 && i < y2){ if(j > x1 && j < x2){ if(Dimage[j] > 0.0){
sum += Dimage[j];
        }
      }
    }
  }
}
ave = sum / ((width * 2) * (height * 2));
//ROS_INFO("depth : %f [mm]", ave);
//cv::imshow("DEPTH image", depth);
cv::waitKey(10);
}

int main(int argc, char **argv){
  sleep(2.0);
  ros::init(argc, argv, "depth_estimater");
  depth_estimater depth_estimater;
  ros::spin();
  return 0;
}
