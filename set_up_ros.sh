### 18.04の場合（20.04なら18を20に書き換え） ###
git clone https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_desktop.git
cd ros_setup_scripts_Ubuntu20.04_desktop/
sudo apt update
sudo apt upgrade
./locale.ja.bash
./step0.bash
./step1.bash
source ~/.bashrc
cd
mkdir -p catkin_ws/src
cd catkin_ws/src
catkin_init_workspace
cd ../
catkin_make
echo source ~/catkin_ws/devel/setup.bash >> ~/.bashrc
source ~/.bashrc
cd ~/catkin_ws/
catkin_make
### CRANE_X7のROSパッケージをインストール
cd ~/catkin_ws/src/
git clone https://github.com/rt-net/crane_x7_ros.git
git clone https://github.com/rt-net/crane_x7_description.git
git clone https://github.com/roboticsgroup/roboticsgroup_gazebo_plugins.git
rosdep install -r -y --from-paths --ignore-src crane_x7_ros
mkdir ~/.ignition
cd ~/.ignition
mkdir fuel
cd fuel
touch config.yaml
echo servers: > config.yaml
echo   - >> config.yaml
echo     name: osrf >> config.yaml
echo     url: https://api.ignitionrobotics.org >> config.yaml
