### 18.04の場合（20.04なら18を20に書き換え） ###
cd
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
echo "servers:" > config.yaml
echo "  -" >> config.yaml
echo "    name: osrf" >> config.yaml
echo "    url: https://api.ignitionrobotics.org" >> config.yaml
### build_blocksのパッケージの設定方法
cd ~/catkin_ws/src/
git clone https://github.com/ChikaraHanakawa/Robotdesign3_2022.git
cd crane_x7_ros/crane_x7_moveit_config/config/
sed -i -e '31i \    <group_state name="game_ofset" group="arm">' crane_x7.srdf
sed -i -e '32i \        <joint name="crane_x7_lower_arm_fixed_part_joint" value="0" />' crane_x7.srdf
sed -i -e '33i \        <joint name="crane_x7_lower_arm_revolute_part_joint" value="-1.6" />' crane_x7.srdf
sed -i -e '34i \        <joint name="crane_x7_shoulder_fixed_part_pan_joint" value="0" />' crane_x7.srdf
sed -i -e '35i \        <joint name="crane_x7_shoulder_revolute_part_tilt_joint" value="0" />' crane_x7.srdf
sed -i -e '36i \        <joint name="crane_x7_upper_arm_revolute_part_rotate_joint" value="-1.4994" />' crane_x7.srdf
sed -i -e '37i \        <joint name="crane_x7_upper_arm_revolute_part_twist_joint" value="0" />' crane_x7.srdf
sed -i -e '38i \        <joint name="crane_x7_wrist_joint" value="0" />' crane_x7.srdf
sed -i -e '39i \    </group_state>' crane_x7.srdf
cd ~/catkin_ws/
catkin_make
### realsenseをgazeboで使用するためのパッケージをインストール
cd ~/catkin_ws/src/
git clone https://github.com/issaiass/realsense2_description.git
git clone https://github.com/issaiass/realsense_gazebo_plugin
cd ~/catkin_ws/
catkin_make
echo "export PS1='\[\033[01;32m\]\u@\h\[\033[01;34m\] \w\[\033[01;31m\]$(__git_ps1 "\""[%s]"\"")\[\033[00m\]\$\[\033[00m\] ' " >> ~/.bashrc
