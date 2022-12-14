#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2019 RT Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from turtle import pos, position
import rospy
import moveit_commander
import actionlib
import math
import random
from geometry_msgs.msg import Point, Pose, Pose2D
from gazebo_msgs.msg import ModelStates
from control_msgs.msg import GripperCommandAction, GripperCommandGoal
from tf.transformations import quaternion_from_euler, euler_from_quaternion

gazebo_model_states = ModelStates()

class Subscribe_publishers():
    def __init__(self):
        # Subscriberを作成
        self.subscriber = rospy.Subscriber('blue', Pose2D, self.callback_A)
        # messageの型を作成
        self.message = Pose2D()
        # publsishu

    def callback_A(self, message):
        print("callbacl!!!!!!!!!!!")
        global sub_blue
        sub_blue = message
        print("sub_blue_x: "+str(sub_blue.x) + "sub_blue_y: "+ str(sub_blue.y))
        # callback時の処理
        #self.pub.make_msg(message)
        # publish
        #self.pub.send_msg()

def callback(msg):
    global gazebo_model_states
    gazebo_model_states = msg


def yaw_of(object_orientation):
    # クォータニオンをオイラー角に変換しyaw角度を返す
    euler = euler_from_quaternion(
        (object_orientation.x, object_orientation.y,
        object_orientation.z, object_orientation.w))

    return euler[2]


def main(n):
    global gazebo_model_states
    if n == -1:
        print(n)
    else:
        n = 0

        OBJECT_NAME = "wood_cube_5cm"   # 掴むオブジェクトの名前
        OBJECT_NAME_1 = "wood_cube_5cm_1"   # 掴むオブジェクト_1の名前
        OBJECT_NAME_2 = "wood_cube_5cm_2"   # 掴むオブジェクト_1の名前
        GRIPPER_OPEN = 1.2              # 掴む時のハンド開閉角度
        #GRIPPER_CLOSE = 0.42            # 設置時のハンド開閉角度
        GRIPPER_CLOSE = 0.20            # 設置時のハンド開閉角度
        APPROACH_Z = 0.15               # 接近時のハンドの高さ
        LEAVE_Z = 0.20                  # 離れる時のハンドの高さ
        #PICK_Z = 0.12                   # 掴む時のハンドの高さ
        PICK_Z = 0.10                   # 掴む時のハンドの高さ
        OBJECT_NAME_POSITIONS = [
                #Point(0.2, 0.2, 0.13),
                Point(0.2, 0.0, 0.13),
                #Point(0.1, 0.2, 0.13),
                Point(0.2, -0.1, 0.13),
                Point(0.2, -0.2, 0.13),
                Point(0.1, -0.2, 0.13),
                
                ]
        PLACE_POSITIONS = [             # オブジェクトの設置位置 (ランダムに設置する)
                #Point(0.4, 0.0, 0.0),
                #Point(0.0, 0.3, 0.0),
                #Point(0.0, -0.3, 0.0),
                Point(0.2, 0.2, 0.0),#last
                Point(0.2-0.01, 0.23-0.05, 0.0),#last
                Point(0.2-0.01, 0.26-0.03, 0.0),#last
                Point(0.2, 0.215, 0.0),#last
                Point(0.2, 0.245+0.01, 0.0),#last
                Point(0.2, 0.23, 0.0),#last
                #Point(0.2, -0.2, 0.0),
                #Point(0.2, 0.0, 0.0)
                ]
        WAY_POINT = [
                #Point(0.2, 0.2, 0.2)
                Point(0.2, 0.23, 0.2),#last
                Point(0.2, 0.26, 0.2),#last
                Point(0.2, 0.215, 0.2),#last
                Point(0.2, 0.245+0.01, 0.2),#last
                Point(0.2, 0.23, 0.2),#last
                ]

        sub_model_states = rospy.Subscriber("gazebo/model_states", ModelStates, callback, queue_size=1)
        #sub_blue = rospy.Subscriber("blue", Pose2D, callback_blue, queue_size=1)

        

        arm = moveit_commander.MoveGroupCommander("arm")
        arm.set_max_velocity_scaling_factor(0.4)
        arm.set_max_acceleration_scaling_factor(1.0)
        gripper = actionlib.SimpleActionClient("crane_x7/gripper_controller/gripper_cmd", GripperCommandAction)
        gripper.wait_for_server()
        gripper_goal = GripperCommandGoal()
        gripper_goal.command.max_effort = 4.0
        
        a = 0

        rospy.sleep(1.0)

        while True:
            # 何かを掴んでいた時のためにハンドを開く
            gripper_goal.command.position = GRIPPER_OPEN
            gripper.send_goal(gripper_goal)
            gripper.wait_for_result(rospy.Duration(1.0))

            # SRDFに定義されている"home"の姿勢にする
            #arm.set_named_target("home")
            arm.set_named_target("game_ofset")
            arm.go()
            rospy.sleep(1.0)

            # 一定時間待機する
            # この間に、ユーザがgazebo上のオブジェクト姿勢を変更しても良い
            sleep_time = 1.5
            print("Wait " + str(sleep_time) + " secs.")
            rospy.sleep(sleep_time)
            print("Start")

            # オブジェクトがgazebo上に存在すれば、pick_and_placeを実行する
            #if OBJECT_NAME in gazebo_model_states.name:
            if a == 0:
                #object_index = gazebo_model_states.name.index(OBJECT_NAME)
                #print("object_index: " + str(object_index))
                # オブジェクトの姿勢を取得
                #object_position = gazebo_model_states.pose[object_index].position
                object_position = OBJECT_NAME_POSITIONS[n]
                print("object_position: " + str(object_position))
                #object_orientation = gazebo_model_states.pose[object_index].orientation
                #print("object_orientation: " + str(object_orientation))
                #object_yaw = yaw_of(object_orientation)

                # オブジェクトに接近する
                target_pose = Pose()
                target_pose.position.x = object_position.x
                target_pose.position.y = object_position.y
                #target_pose.position.z = APPROACH_Z
                target_pose.position.z = object_position.z
                print("target_x: "+str(target_pose.position.x)+"target_y: "+str(target_pose.position.y)+"target_z: "+str(target_pose.position.z))
                #q = quaternion_from_euler(-math.pi, 0.0, object_yaw)
                q = quaternion_from_euler(-math.pi, 0.0, 0.0)
                #print("first_q: "+str(q))
                target_pose.orientation.x = q[0]
                target_pose.orientation.y = q[1]
                target_pose.orientation.z = q[2]
                target_pose.orientation.w = q[3]
                arm.set_pose_target(target_pose)
                if arm.go() is False:
                    print("Failed to approach an object.")
                    #continue
                rospy.sleep(1.0)

                # 掴みに行く
                #target_pose.position.z = PICK_Z + n*0.05
                target_pose.position.z = PICK_Z
                arm.set_pose_target(target_pose)
                if arm.go() is False:
                    print("Failed to grip an object.")
                    continue
                rospy.sleep(1.0)
                gripper_goal.command.position = GRIPPER_CLOSE
                print("gripper_goal.command.position: "+str(gripper_goal.command.position))
                gripper.send_goal(gripper_goal)
                gripper.wait_for_result(rospy.Duration(1.0))

                # 持ち上げる
                place_position = WAY_POINT[0]
                target_pose.position.z = place_position.z + n*0.032
                """if n < 3:
                    target_pose.position.z = place_position.z + 1*0.03
                elif n < 5:
                    target_pose.position.z = place_position.z + 2*0.03
                else:
                    target_pose.position.z = place_position.z + 3*0.03"""
                print("target_pose: " + str(target_pose))
                #target_pose.position.z = LEAVE_Z
                arm.set_pose_target(target_pose)
                if arm.go() is False:
                    print("Failed to pick up an object.!!")
                    #continue
                rospy.sleep(1.0)
                
                # オブジェクトを回避しながら設置位置に移動する
                """
                place_position = WAY_POINT[n] # 設置位置をランダムに選択する
                #target_pose.position.x = place_position.x
                #target_pose.position.y = place_position.y
                target_pose.position.z = place_position.z
                print("target_z: "+str(target_pose.position.z))
                #q = quaternion_from_euler(-math.pi, 0.0, -math.pi/2.0)
                print("first_q: "+str(q))
                #target_pose.orientation.x = q[0]
                #target_pose.orientation.y = q[1]
                #target_pose.orientation.z = q[2]
                #target_pose.orientation.w = q[3]
                arm.set_pose_target(target_pose)
                if arm.go() is False:
                    print("1_Failed to approach target position.")
                    continue
                rospy.sleep(1.0)
                """

                # 設置位置に移動する
                #place_position = random.choice(PLACE_POSITIONS) # 設置位置をランダムに選択する
                place_position = PLACE_POSITIONS[n] # 設置位置をランダムに選択する
                target_pose.position.x = place_position.x
                target_pose.position.y = place_position.y
                print("target_x: "+str(target_pose.position.x)+"target_y: "+str(target_pose.position.y))
                #q = quaternion_from_euler(-math.pi, 0.0, -math.pi/2.0)
                q = quaternion_from_euler(-math.pi, 0.0, 0.0)
                print("first_q: "+str(q))
                target_pose.orientation.x = q[0]
                target_pose.orientation.y = q[1]
                target_pose.orientation.z = q[2]
                target_pose.orientation.w = q[3]
                arm.set_pose_target(target_pose)
                if arm.go() is False:
                    print("1Failed to approach target position.")
                    #continue
                rospy.sleep(1.0)

                # 設置する
                #target_pose.position.z = PICK_Z + (n+1)*0.05
                #target_pose.position.z = PICK_Z + (n+1)*0.03
                if n < 1:
                    target_pose.position.z = 0.07 + 1*0.03
                elif n < 2:
                    target_pose.position.z = 0.07 + 2*0.03
                elif n < 3:
                    target_pose.position.z = 0.07 + 3*0.03
                elif n < 5:
                    target_pose.position.z = 0.07 + 2*0.03
                else:
                    target_pose.position.z = 0.07 + 3*0.03
                #target_pose.position.z = place_position.z
                arm.set_pose_target(target_pose)
                if arm.go() is False:
                    print("2Failed to place an object.")
                    #continue
                rospy.sleep(1.0)
                gripper_goal.command.position = GRIPPER_OPEN
                gripper.send_goal(gripper_goal)
                gripper.wait_for_result(rospy.Duration(1.0))

                # ハンドを上げる
                #target_pose.position.z = LEAVE_Z + (n+1)*0.05
                target_pose.position.z = LEAVE_Z + (n+1)*0.03
                arm.set_pose_target(target_pose)
                if arm.go() is False:
                    print("3Failed to leave from an object.")
                    #continue
                rospy.sleep(1.0)

                # SRDFに定義されている"home"の姿勢にする
                #arm.set_named_target("home")
                arm.set_named_target("game_ofset")
                if arm.go() is False:
                    print("4Failed to go back to home pose.")
                    continue
                rospy.sleep(1.0)

                print("Done")
                n+=1
                print(n)

            else:
                print("No objects")


if __name__ == '__main__':
    n = 0
    rospy.init_node("pick_and_place_in_gazebo_example")
    sub = Subscribe_publishers()
    

    try:
        if not rospy.is_shutdown():
            main(n)
    except rospy.ROSInterruptException:
        pass
#nr_x: 0.09970760233918133nr_y: -0.1960167084377611nr_z: 0.2
#nr_x: 0.3016643967642684nr_y: -0.19725015791511302nr_z: 0.2