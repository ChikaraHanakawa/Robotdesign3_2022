#! /usr/bin/env python3
#

import rospy
import moveit_commander
import geometry_msgs.msg
from geometry_msgs.msg import Point, Pose, Pose2D
import rosnode
from tf.transformations import quaternion_from_euler
import sys
from PyQt5.QtWidgets import QFrame, QSlider, QMainWindow, QPushButton, QApplication, QDialog, QLabel, QHBoxLayout, QVBoxLayout, QCheckBox, QWidget, QStatusBar
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QObject
import math
import pick_and_place_in_gazebo_example

class Subscribe_publishers():
    def __init__(self):
        # Subscriberを作成
        self.subscriber_b = rospy.Subscriber('blue', Pose2D, self.callback_blue)
        self.subscriber_r = rospy.Subscriber('red', Pose2D, self.callback_red)
        self.subscriber_g = rospy.Subscriber('green', Pose2D, self.callback_green)
        # messageの型を作成
        self.message = Pose2D()
        # publsishu

    def callback_blue(self, message):
        #print("callback!!!!!!!!!!!")
        global sub_blue
        sub_blue = message
        print("sub_blue_x: "+str(sub_blue.x) + "sub_blue_y: "+ str(sub_blue.y))
        # callback時の処理
        #self.pub.make_msg(message)
        # publish
        #self.pub.send_msg()
    def callback_red(self, message):
        #print("callback!!!!!!!!!!!")
        global sub_red
        sub_red = message
        print("sub_red_x: "+str(sub_red.x) + "sub_red_y: "+ str(sub_red.y))
        # callback時の処理
        #self.pub.make_msg(message)
        # publish
        #self.pub.send_msg()
    def callback_green(self, message):
        #print("callback!!!!!!!!!!!")
        global sub_green
        sub_green = message
        print("sub_green_x: "+str(sub_green.x) + "sub_green_y: "+ str(sub_green.y))
        # callback時の処理
        #self.pub.make_msg(message)
        # publish
        #self.pub.send_msg()
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        #ex_q = Example.Example_Q()
        #ex_q.show()
        #self.qt_slider()
        #self.qt_slider1()

    def initUI(self):
        #ex_q = Example.Example_Q()
        label_1 = QLabel('<h1><font size="8" color="blue">BUILD BLOCKS<h1>', self)
        label_1.move(220, 20)
        label_2 = QLabel('<font size="5" color="black">[ MODE ]', self)
        #label_2.move(250, 100) 
        label_2.move(280, 100) 
        label_3 = QLabel('<i><p><font size="5" color="black">fuck you bitch !<i></font></p>', self)
        label_3.move(45, 220) 
                       
        self.resize(670, 350) 
        self.move(300, 300) 
                       
        btn1 = QPushButton("→ 緑", self)
        btn1.move(80, 150) 
                       
        btn2 = QPushButton("↑ 青", self)
        btn2.move(200, 150) 
                       
        btn3 = QPushButton("↓ 赤", self)
        btn3.move(340, 150) 
                       
        btn4 = QPushButton("GO!", self)
        btn4.move(480, 150)

        btn5 = QPushButton("app_G", self)
        btn5.move(620, 150)

        btn6 = QPushButton("catch", self)
        btn6.move(80, 200)

        btn7 = QPushButton("put", self)
        btn7.move(200, 200)

        btn8 = QPushButton("to_green", self)
        btn8.move(340, 200)

        btn9 = QPushButton("to_blue", self)
        btn9.move(480, 200)

        btn10 = QPushButton("ofset", self)
        btn10.move(620, 200)

        btn11 = QPushButton("x_game+", self)
        btn11.move(80, 250)

        btn12 = QPushButton("y_game+", self)
        btn12.move(200, 250)

        btn13 = QPushButton("z_game", self)
        btn13.move(340, 250)

        btn14 = QPushButton("x_game-", self)
        btn14.move(80, 300)

        btn15 = QPushButton("y_game-", self)
        btn15.move(200, 300)

        btn16 = QPushButton("z_game-", self)
        btn16.move(340, 300)
        """
        btn5 = QPushButton("Button", self)
        btn5.move(620, 150)

        btn5.setAutoRepeat(True)
        btn5.setAutoRepeatDelay(1000)  # 1秒
        btn5.setAutoRepeatInterval(300)  # 300ミリ秒"""

        
        
        btn1.clicked.connect(self.Push_Right)
        btn2.clicked.connect(self.Push_Up)
        btn3.clicked.connect(self.Push_Down)
        btn4.clicked.connect(self.Push_Go)
        btn5.clicked.connect(self.Push_A)
        btn6.clicked.connect(self.Push_B)
        btn7.clicked.connect(self.Push_C)
        btn8.clicked.connect(self.Push_D)
        btn9.clicked.connect(self.Push_E)
        btn10.clicked.connect(self.Push_F)
        btn11.clicked.connect(self.Push_G)
        btn12.clicked.connect(self.Push_H)
        btn13.clicked.connect(self.Push_I)
        btn14.clicked.connect(self.Push_J)
        btn15.clicked.connect(self.Push_K)
        btn16.clicked.connect(self.Push_L)


        #btn5.pressed.connect(self.updateStatusBar())
        
        #Example.Example_Q.statusBar()
        #QMainWindow.statusBar()
        #ex_q.statusBar()
        
        self.setWindowTitle('Crane_x7_build_blockers')

        ##slider
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('orange.png'))
        self.label.setGeometry(160, 40, 80, 30)
        #self.setGeometry(300, 300, 280, 170)
        #self.setWindowTitle('QSlider')
        self.show()
        

    def changeValue(self, value):
        if value == 0:
            # オレンジ色の画像
            self.label.setPixmap(QPixmap('orange.png'))
        elif value > 0 and value <= 30:
            # 黄色の画像
            self.label.setPixmap(QPixmap('yellow.png'))
        elif value > 30 and value < 80:
            # 緑色の画像
            self.label.setPixmap(QPixmap('green.png'))
        else:
            # 青色の画像
            self.label.setPixmap(QPixmap('blue.png'))

    def value_change(self):
        for i in range(1):
            self.angle_label[i].setText(str(self.angle_slider[i].value()))

    def Push_Right(self):
        print("1111111111111111111111")
        food_stock = Food_Stock()
        food_stock.main()

    def Push_Up(self):
        print("2222222222222222222222")
        food_stock = Food_Stock()
        food_stock.x_move()

    def Push_Down(self):
        print("3333333333333333333333")
        food_stock = Food_Stock()
        food_stock.y_move()

    def Push_Go(self):
        print("4444444444444444444444")
        food_stock = Food_Stock()
        food_stock.game_ofset()

    def Push_A(self):
        print("555555555555555555555")
        food_stock = Food_Stock()
        food_stock.third_block_ofset()
        
    def Push_B(self):
        print("666666666666666666666")
        food_stock = Food_Stock()
        food_stock.catch_block()

    def Push_C(self):
        print("7777777777777777777")
        food_stock = Food_Stock()
        food_stock.put_block()
    
    def Push_D(self):
        print("7777777777777777777")
        food_stock = Food_Stock()
        food_stock.choose_put_pos_G()

    def Push_E(self):
        print("7777777777777777777")
        food_stock = Food_Stock()
        food_stock.choose_put_pos_B()
    
    def Push_F(self):
        print("7777777777777777777")
        food_stock = Food_Stock()
        food_stock.ofset_b()

    def Push_G(self):
        print("7777777777777777777")
        food_stock = Food_Stock()
        food_stock.x_move_game()

    def Push_H(self):
        print("7777777777777777777")
        food_stock = Food_Stock()
        food_stock.y_move_game()

    def Push_I(self):
        print("7777777777777777777")
        food_stock = Food_Stock()
        food_stock.z_move_game()

    def Push_J(self):
        print("7777777777777777777")
        food_stock = Food_Stock()
        food_stock.x_move_game_min()

    def Push_K(self):
        print("7777777777777777777")
        food_stock = Food_Stock()
        food_stock.y_move_game_min()

    def Push_L(self):
        print("7777777777777777777")
        food_stock = Food_Stock()
        food_stock.z_move_game_min()

    def qt_slider(self):
        self.angle_label = [QLabel() for x in range(1)]
        for each_label in self.angle_label:
            each_label.setText(str(90))
        self.angle_slider = [QSlider(Qt.Orientation.Horizontal) for x in range(1)]
        for each_slider in self.angle_slider:
            each_slider.setMaximum(100)
            each_slider.setMinimum(80)
            each_slider.setValue(90)
            each_slider.valueChanged.connect(self.value_change)

        servo_frame = [QFrame() for x in range(1)]
        servo_layout = [QHBoxLayout() for x in range(1)]

        vbox = QVBoxLayout()

        for i in range(1):
            servo_layout[i].addWidget(self.angle_label[i])
            servo_layout[i].addWidget(self.angle_slider[i])

            servo_frame[i].setLayout(servo_layout[i])
            vbox.addWidget(servo_frame[i])  
            
        self.setLayout(vbox)
        #self.setGeometry(300, 300, 450, 300)
        self.show()

    def value_s(self, label_test):
        self.label_test.setText(str(self.slider.value()))

    def qt_slider1(self):
        #root = QWidget()

        #self.resize(300,300)
        #self.setWindowTitle('Hello, world')

        self.slider = QSlider(self)
        self.slider.setGeometry(50, 50, 200, 50)
        self.slider.setMinimum(0)
        self.slider.setMaximum(20)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(2)
        self.slider.valueChanged.connect(self.value_s)

        self.label_test = QLabel(self)
        self.label_test.move(100, 100)

        self.show()

    class Example_Q(QMainWindow):
        def __init__(self):
            super().__init__()
            #self.initUI()
            self.counter = 0

        def initUI(self):
            btn5 = QPushButton("Button", self)
            btn5.move(620, 150)
            btn5.setAutoRepeat(True)
            btn5.setAutoRepeatDelay(1000)  # 1秒
            btn5.setAutoRepeatInterval(300)  # 300ミリ秒

            btn5.pressed.connect(self.updateStatusBar)

            self.statusBar()
            self.setGeometry(300, 300, 200, 150)
            self.show()

        def updateStatusBar(self):
            self.counter += 1
            msg = self.sender().text() + ' was pressed... {}'.format(self.counter)
            self.statusBar().showMessage(msg)

class Food_Stock:
    def main(self):
        robot = moveit_commander.RobotCommander()
        arm = moveit_commander.MoveGroupCommander("arm")
        arm.set_max_velocity_scaling_factor(0.5)
        gripper = moveit_commander.MoveGroupCommander("gripper")

        # アーム初期ポーズを表示
        arm_initial_pose = arm.get_current_pose().pose
        print("Arm initial pose:")
        print(arm_initial_pose)

        def move_gripper(pou):
            gripper.set_joint_value_target([pou, pou])
            gripper.go()

        def move_arm(pos_x, pos_y, pos_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            q = quaternion_from_euler(-math.pi/2.0, 0.0, -math.pi/2.0)  
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            arm.go()  # 実行

        def rotate_hand(pos_x, pos_y, pos_z, euler_x, euler_y, euler_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            q = quaternion_from_euler(euler_x, euler_y, euler_z)  
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            arm.go()  # 実行

        # SRDFに定義されている"home"の姿勢にする
        arm.set_named_target("game_ofset")
        #arm.set_named_target("vertical")
        arm.go()
        #move_arm(0.2, 0.0, 0.13)
        nr.position.x, nr.position.y, nr.position.z = 0.2, -0.2, 0.2
        rotate_hand(nr.position.x, nr.position.y, 0.2, -math.pi, 0.0, 0.0)
        #rotate_hand(0.2-0.1, -0.2-0.00, 0.2, -math.pi, 0.0, 0.0)
        #ハンドを開く
        #move_gripper(1.3)
        #arm.set_max_velocity_scaling_factor(0.5)
        #rotate_hand(0.2, 0.0, 0.3, -math.pi, 0.0, 0.0)
        #move_arm(0.19656094687103462, 0.2018005936419827, 0.18980440929975606)
        #rotate_hand(0.2, 0.2, 0.2, -math.pi, 0.0, -math.pi/2.0)

        #rotate_hand(0.19656094687103462, 0.2018005936419827, 0.18980440929975606, 0.7073039496558831, -0.7066695134571028, 0.006372004050582716)
        #w: 0.017283492583064008

    def x_move(self):
        robot = moveit_commander.RobotCommander()
        arm = moveit_commander.MoveGroupCommander("arm")
        arm.set_max_velocity_scaling_factor(0.5)
        gripper = moveit_commander.MoveGroupCommander("gripper")

        # アーム初期ポーズを表示
        arm_initial_pose = arm.get_current_pose().pose
        print("Arm initial pose:")
        print(arm_initial_pose)

        def move_gripper(pou):
            gripper.set_joint_value_target([pou, pou])
            gripper.go()

        def move_arm(pos_x, pos_y, pos_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            #q = quaternion_from_euler(-math.pi/2.0, math.pi/2.0, 0.0)  
            q = quaternion_from_euler(-math.pi, 0.0, 0.0)
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            arm.go()  # 実行

        def rotate_hand(pos_x, pos_y, pos_z, euler_x, euler_y, euler_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            q = quaternion_from_euler(euler_x, euler_y, euler_z)  
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            print(target_pose)
            arm.go()  # 実行
        
        #rotate_hand(0.19, 0.05, 0.2, -math.pi, 0.0, 0.0)
        #nr.position.x, nr.position.y, nr.position.z = 0.2-(sub_blue.x)+0.06, 0.2-(sub_blue.y)-0.07,0.2
        nr.position.x, nr.position.y, nr.position.z = nr.position.x-(sub_blue.x)+0.06, nr.position.y-(sub_blue.y)-0.07,0.2
        rotate_hand(nr.position.x, nr.position.y, 0.2, -math.pi, 0.0, 0.0)

        #(-0.01, +0.05, 0)
        #move_arm(0.2, 0.01, 0.2)
        #rotate_hand(0.0, 0.0, 0.63, 0.0, 0.0, 0.0)
        """
        for i in range(1, 26):
            move_arm(0.2, 0.0125*i, 0.3)
            rospy.sleep(0.2)
            print(str(i))"""
        """move_arm(0.2, 0.05*2, 0.3)
        rospy.sleep(0.2)
        print("2")
        #rotate_hand(0.2, 0.15, 0.3, -math.pi, 0.0, 0.0)
        move_arm(0.2, 0.05*3, 0.3)
        rospy.sleep(0.2)
        print("3")
        move_arm(0.2, 0.05*4, 0.3)
        rospy.sleep(0.2)
        print("4")
        move_arm(0.2, 0.05*5, 0.3)
        rospy.sleep(0.2)
        print("5")
        move_arm(0.2, 0.05*6, 0.3)
        print("6")
        #move_arm(0.2, 0.05*7, 0.3)"""

    def y_move(self):
        robot = moveit_commander.RobotCommander()
        arm = moveit_commander.MoveGroupCommander("arm")
        arm.set_max_velocity_scaling_factor(0.5)
        gripper = moveit_commander.MoveGroupCommander("gripper")

        # アーム初期ポーズを表示
        arm_initial_pose = arm.get_current_pose().pose
        print("Arm initial pose:")
        print(arm_initial_pose)

        def move_gripper(pou):
            gripper.set_joint_value_target([pou, pou])
            gripper.go()

        def move_arm(pos_x, pos_y, pos_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            #q = quaternion_from_euler(-math.pi/2.0, math.pi/2.0, 0.0)  
            q = quaternion_from_euler(-math.pi, 0.0, 0.0)
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            arm.go()  # 実行

        def rotate_hand(pos_x, pos_y, pos_z, euler_x, euler_y, euler_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            q = quaternion_from_euler(euler_x, euler_y, euler_z)  
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            arm.go()  # 実行

        """"
        move_arm(0.0, 0.05*6, 0.3)
        move_arm(0.05, 0.05*6, 0.3)
        move_arm(0.05*2, 0.05*6, 0.3)
        move_arm(0.05*3, 0.05*6, 0.3)
        #move_arm(0.05*4, 0.05*6, 0.3)
        #move_arm(0.05*5, 0.05*6, 0.3)
        #move_arm(0.05*6, 0.05*6, 0.3)
        """
        #move_arm(0.2, 0.2, 0.3)
        arm.set_named_target("home")
        arm.go()
        #move_arm(0.2, 0.2, 0.3)
        nr.position.x, nr.position.y, nr.position.z = 0.2, 0.2, 0.2
        rotate_hand(nr.position.x, nr.position.y, 0.2, -math.pi, 0.0, 0.0)
        #rotate_hand(0.2, 0.2, 0.3, -math.pi, 0.0, 0.0)
        #rospy.sleep(0.3)
        #rotate_hand(0.2-(0.162934)+0.01, 0.2-(-0.0949304)-0.05,0.2)

    def game_ofset(self):
        robot = moveit_commander.RobotCommander()
        arm = moveit_commander.MoveGroupCommander("arm")
        arm.set_max_velocity_scaling_factor(0.5)
        gripper = moveit_commander.MoveGroupCommander("gripper")
        arm.set_named_target("home")
        arm.go()
        rospy.sleep(0.1)
        arm.set_named_target("game_ofset")
        arm.go()

    def third_block_ofset(self):
        robot = moveit_commander.RobotCommander()
        arm = moveit_commander.MoveGroupCommander("arm")
        arm.set_max_velocity_scaling_factor(0.5)
        gripper = moveit_commander.MoveGroupCommander("gripper")

        # アーム初期ポーズを表示
        arm_initial_pose = arm.get_current_pose().pose
        print("Arm initial pose:")
        print(arm_initial_pose)

        def move_gripper(pou):
            gripper.set_joint_value_target([pou, pou])
            gripper.go()

        def move_arm(pos_x, pos_y, pos_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            #q = quaternion_from_euler(-math.pi/2.0, math.pi/2.0, 0.0)  
            q = quaternion_from_euler(-math.pi, 0.0, 0.0)
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            arm.go()  # 実行

        def rotate_hand(pos_x, pos_y, pos_z, euler_x, euler_y, euler_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            q = quaternion_from_euler(euler_x, euler_y, euler_z)  
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            arm.go()  # 実行

        #move_arm(0.2, 0.21, 0.2)
        #pick_and_place_in_gazebo_example.main(n=0)
        #rotate_hand(0.2-(0.108762)+0.01, -0.2-(-0.0469294)-0.05, 0.2, -math.pi, 0.0, 0.0)
        #nr.position.x, nr.position.y, nr.position.z = 0.2-(sub_blue.x)+0.06, -0.2-(sub_blue.y)-0.07, 0.2
        nr.position.x, nr.position.y, nr.position.z = nr.position.x-(sub_blue.x)+0.06, nr.position.y-(sub_blue.y)-0.07, 0.2
        rotate_hand(nr.position.x, nr.position.y, 0.2, -math.pi, 0.0, 0.0)

    def catch_block(self):
        robot = moveit_commander.RobotCommander()
        arm = moveit_commander.MoveGroupCommander("arm")
        arm.set_max_velocity_scaling_factor(0.5)
        gripper = moveit_commander.MoveGroupCommander("gripper")

        _target_pose = Pose()
        

        # アーム初期ポーズを表示
        arm_initial_pose = arm.get_current_pose().pose
        print("Arm initial pose:")
        print(arm_initial_pose)

        def move_gripper(pou):
            gripper.set_joint_value_target([pou, pou])
            gripper.go()

        def move_arm(pos_x, pos_y, pos_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            #q = quaternion_from_euler(-math.pi/2.0, math.pi/2.0, 0.0)  
            q = quaternion_from_euler(-math.pi, 0.0, 0.0)
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            arm.go()  # 実行

        def rotate_hand(pos_x, pos_y, pos_z, euler_x, euler_y, euler_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            q = quaternion_from_euler(euler_x, euler_y, euler_z)  
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            arm.go()  # 実行

        move_gripper(1.2)
        #_target_pose.position.x, _target_pose.position.y = 0.2-(sub_blue.x)+0.06, -0.2-(sub_blue.y)-0.07
        _target_pose.position.z = 0.10
        #print(_target_pose.position.x)
        move_arm(nr.position.x, nr.position.y, _target_pose.position.z)
        rospy.sleep(1.0)
        move_gripper(0.24)

        _target_pose.position.z = 0.2
        move_arm(nr.position.x, nr.position.y, _target_pose.position.z)

    def put_block(self):
        robot = moveit_commander.RobotCommander()
        arm = moveit_commander.MoveGroupCommander("arm")
        arm.set_max_velocity_scaling_factor(0.5)
        gripper = moveit_commander.MoveGroupCommander("gripper")

        _target_pose = Pose()
        

        # アーム初期ポーズを表示
        arm_initial_pose = arm.get_current_pose().pose
        print("Arm initial pose:")
        print(arm_initial_pose)

        def move_gripper(pou):
            gripper.set_joint_value_target([pou, pou])
            gripper.go()

        def move_arm(pos_x, pos_y, pos_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            #q = quaternion_from_euler(-math.pi/2.0, math.pi/2.0, 0.0)  
            q = quaternion_from_euler(-math.pi, 0.0, 0.0)
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            arm.go()  # 実行
        
        _target_pose.position.z = 0.1 + 0.03*1
        move_arm(nr.position.x, nr.position.y, _target_pose.position.z)
        rospy.sleep(1.0)
        move_gripper(1.2)
        _target_pose.position.z = 0.20 + 0.03*1
        move_arm(nr.position.x, nr.position.y, _target_pose.position.z)
        move_gripper(0.24)

    def choose_put_pos_G(self):
        robot = moveit_commander.RobotCommander()
        arm = moveit_commander.MoveGroupCommander("arm")
        arm.set_max_velocity_scaling_factor(0.5)
        gripper = moveit_commander.MoveGroupCommander("gripper")

        _target_pose = Pose()
        

        # アーム初期ポーズを表示
        arm_initial_pose = arm.get_current_pose().pose
        print("Arm initial pose:")
        print(arm_initial_pose)

        def move_gripper(pou):
            gripper.set_joint_value_target([pou, pou])
            gripper.go()

        def move_arm(pos_x, pos_y, pos_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            #q = quaternion_from_euler(-math.pi/2.0, math.pi/2.0, 0.0)  
            q = quaternion_from_euler(-math.pi, 0.0, 0.0)
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            arm.go()  # 実行
        
        #nr.position.x, nr.position.y, nr.position.z = 0.2-(sub_green.x)+0.06, 0.2-(sub_green.y)-0.07,0.2
        print("nr_x: "+str(nr.position.x) + "nr_y: " +str(nr.position.y) + "nr_z: "+ str(nr.position.z))

        nr.position.x, nr.position.y, nr.position.z = nr.position.x-(sub_green.x)-0.06+0.04, nr.position.y-(sub_green.y)-0.07,0.2#TODO
        print("nr_x: "+str(nr.position.x) + "nr_y: " +str(nr.position.y) + "nr_z: "+ str(nr.position.z))
        move_arm(nr.position.x, nr.position.y, nr.position.z)

    def choose_put_pos_B(self):
        robot = moveit_commander.RobotCommander()
        arm = moveit_commander.MoveGroupCommander("arm")
        arm.set_max_velocity_scaling_factor(0.5)
        gripper = moveit_commander.MoveGroupCommander("gripper")

        _target_pose = Pose()
        

        # アーム初期ポーズを表示
        arm_initial_pose = arm.get_current_pose().pose
        print("Arm initial pose:")
        print(arm_initial_pose)

        def move_gripper(pou):
            gripper.set_joint_value_target([pou, pou])
            gripper.go()

        def move_arm(pos_x, pos_y, pos_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            #q = quaternion_from_euler(-math.pi/2.0, math.pi/2.0, 0.0)  
            q = quaternion_from_euler(-math.pi, 0.0, 0.0)
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            arm.go()  # 実行
        
        #nr.position.x, nr.position.y, nr.position.z = 0.2-(sub_green.x)+0.06, 0.2-(sub_green.y)-0.07,0.2
        nr.position.x, nr.position.y, nr.position.z = nr.position.x-(sub_blue.x)+0.06, nr.position.y-(sub_blue.y)-0.07,0.2
        move_arm(nr.position.x, nr.position.y, nr.position.z)

    def ofset_b(self):
        robot = moveit_commander.RobotCommander()
        arm = moveit_commander.MoveGroupCommander("arm")
        arm.set_max_velocity_scaling_factor(0.5)
        gripper = moveit_commander.MoveGroupCommander("gripper")

        _target_pose = Pose()
        

        # アーム初期ポーズを表示
        arm_initial_pose = arm.get_current_pose().pose
        print("Arm initial pose:")
        print(arm_initial_pose)

        def move_gripper(pou):
            gripper.set_joint_value_target([pou, pou])
            gripper.go()

        def move_arm(pos_x, pos_y, pos_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            #q = quaternion_from_euler(-math.pi/2.0, math.pi/2.0, 0.0)  
            q = quaternion_from_euler(-math.pi, 0.0, 0.0)
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            arm.go()  # 実行

        def rotate_hand(pos_x, pos_y, pos_z, euler_x, euler_y, euler_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            q = quaternion_from_euler(euler_x, euler_y, euler_z)  
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            arm.go()  # 実行

        nr.position.x, nr.position.y, nr.position.z = 0.19, 0.05, 0.2
        rotate_hand(nr.position.x, nr.position.y, 0.2, -math.pi, 0.0, 0.0)
        #rotate_hand(0.19, 0.05, 0.2, -math.pi, 0.0, 0.0)

    def x_move_game(self):
        robot = moveit_commander.RobotCommander()
        arm = moveit_commander.MoveGroupCommander("arm")
        arm.set_max_velocity_scaling_factor(0.5)
        gripper = moveit_commander.MoveGroupCommander("gripper")

        # アーム初期ポーズを表示
        arm_initial_pose = arm.get_current_pose().pose
        print("Arm initial pose:")
        print(arm_initial_pose)

        def move_gripper(pou):
            gripper.set_joint_value_target([pou, pou])
            gripper.go()

        def move_arm(pos_x, pos_y, pos_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            #q = quaternion_from_euler(-math.pi/2.0, math.pi/2.0, 0.0)  
            q = quaternion_from_euler(-math.pi, 0.0, 0.0)
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            arm.go()  # 実行

        def rotate_hand(pos_x, pos_y, pos_z, euler_x, euler_y, euler_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            q = quaternion_from_euler(euler_x, euler_y, euler_z)  
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            print(target_pose)
            arm.go()  # 実行
        
        #rotate_hand(0.19, 0.05, 0.2, -math.pi, 0.0, 0.0)
        n_x, n_y, n_z = nr.position.x + 0.0125, nr.position.y, nr.position.z
        #nr.position.x, nr.position.y, nr.position.z = 0.2-(sub_blue.x)+0.06, 0.2-(sub_blue.y)-0.07,0.2
        #nr.position.x, nr.position.y, nr.position.z = nr.position.x-(sub_blue.x)+0.06, nr.position.y-(sub_blue.y)-0.07,0.2
        rotate_hand(n_x, n_y, n_z, -math.pi, 0.0, 0.0)
        nr.position.x, nr.position.y, nr.position.z = n_x, n_y, n_z

    def y_move_game(self):
        robot = moveit_commander.RobotCommander()
        arm = moveit_commander.MoveGroupCommander("arm")
        arm.set_max_velocity_scaling_factor(0.5)
        gripper = moveit_commander.MoveGroupCommander("gripper")

        # アーム初期ポーズを表示
        arm_initial_pose = arm.get_current_pose().pose
        print("Arm initial pose:")
        print(arm_initial_pose)

        def move_gripper(pou):
            gripper.set_joint_value_target([pou, pou])
            gripper.go()

        def move_arm(pos_x, pos_y, pos_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            #q = quaternion_from_euler(-math.pi/2.0, math.pi/2.0, 0.0)  
            q = quaternion_from_euler(-math.pi, 0.0, 0.0)
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            arm.go()  # 実行

        def rotate_hand(pos_x, pos_y, pos_z, euler_x, euler_y, euler_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            q = quaternion_from_euler(euler_x, euler_y, euler_z)  
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            print(target_pose)
            arm.go()  # 実行
        
        #rotate_hand(0.19, 0.05, 0.2, -math.pi, 0.0, 0.0)
        n_x, n_y, n_z = nr.position.x, nr.position.y + 0.0125, nr.position.z
        #nr.position.x, nr.position.y, nr.position.z = 0.2-(sub_blue.x)+0.06, 0.2-(sub_blue.y)-0.07,0.2
        #nr.position.x, nr.position.y, nr.position.z = nr.position.x-(sub_blue.x)+0.06, nr.position.y-(sub_blue.y)-0.07,0.2
        rotate_hand(n_x, n_y, n_z, -math.pi, 0.0, 0.0)
        nr.position.x, nr.position.y, nr.position.z = n_x, n_y, n_z

    def z_move_game(self):
        robot = moveit_commander.RobotCommander()
        arm = moveit_commander.MoveGroupCommander("arm")
        arm.set_max_velocity_scaling_factor(0.5)
        gripper = moveit_commander.MoveGroupCommander("gripper")

        # アーム初期ポーズを表示
        arm_initial_pose = arm.get_current_pose().pose
        print("Arm initial pose:")
        print(arm_initial_pose)

        def move_gripper(pou):
            gripper.set_joint_value_target([pou, pou])
            gripper.go()

        def move_arm(pos_x, pos_y, pos_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            #q = quaternion_from_euler(-math.pi/2.0, math.pi/2.0, 0.0)  
            q = quaternion_from_euler(-math.pi, 0.0, 0.0)
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            arm.go()  # 実行

        def rotate_hand(pos_x, pos_y, pos_z, euler_x, euler_y, euler_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            q = quaternion_from_euler(euler_x, euler_y, euler_z)  
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            print(target_pose)
            arm.go()  # 実行
        
        #rotate_hand(0.19, 0.05, 0.2, -math.pi, 0.0, 0.0)
        n_x, n_y, n_z = nr.position.x, nr.position.y, nr.position.z-0.01
        #nr.position.x, nr.position.y, nr.position.z = 0.2-(sub_blue.x)+0.06, 0.2-(sub_blue.y)-0.07,0.2
        #nr.position.x, nr.position.y, nr.position.z = nr.position.x-(sub_blue.x)+0.06, nr.position.y-(sub_blue.y)-0.07,0.2
        rotate_hand(n_x, n_y, n_z, -math.pi, 0.0, 0.0)
        nr.position.x, nr.position.y, nr.position.z = n_x, n_y, n_z
    
    def x_move_game_min(self):
        robot = moveit_commander.RobotCommander()
        arm = moveit_commander.MoveGroupCommander("arm")
        arm.set_max_velocity_scaling_factor(0.5)
        gripper = moveit_commander.MoveGroupCommander("gripper")

        # アーム初期ポーズを表示
        arm_initial_pose = arm.get_current_pose().pose
        print("Arm initial pose:")
        print(arm_initial_pose)

        def move_gripper(pou):
            gripper.set_joint_value_target([pou, pou])
            gripper.go()

        def move_arm(pos_x, pos_y, pos_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            #q = quaternion_from_euler(-math.pi/2.0, math.pi/2.0, 0.0)  
            q = quaternion_from_euler(-math.pi, 0.0, 0.0)
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            arm.go()  # 実行

        def rotate_hand(pos_x, pos_y, pos_z, euler_x, euler_y, euler_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            q = quaternion_from_euler(euler_x, euler_y, euler_z)  
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            print(target_pose)
            arm.go()  # 実行
        
        #rotate_hand(0.19, 0.05, 0.2, -math.pi, 0.0, 0.0)
        n_x, n_y, n_z = nr.position.x - 0.0125, nr.position.y, nr.position.z
        #nr.position.x, nr.position.y, nr.position.z = 0.2-(sub_blue.x)+0.06, 0.2-(sub_blue.y)-0.07,0.2
        #nr.position.x, nr.position.y, nr.position.z = nr.position.x-(sub_blue.x)+0.06, nr.position.y-(sub_blue.y)-0.07,0.2
        rotate_hand(n_x, n_y, n_z, -math.pi, 0.0, 0.0)
        nr.position.x, nr.position.y, nr.position.z = n_x, n_y, n_z

    def y_move_game_min(self):
        robot = moveit_commander.RobotCommander()
        arm = moveit_commander.MoveGroupCommander("arm")
        arm.set_max_velocity_scaling_factor(0.5)
        gripper = moveit_commander.MoveGroupCommander("gripper")

        # アーム初期ポーズを表示
        arm_initial_pose = arm.get_current_pose().pose
        print("Arm initial pose:")
        print(arm_initial_pose)

        def move_gripper(pou):
            gripper.set_joint_value_target([pou, pou])
            gripper.go()x_game

        def move_arm(pos_x, pos_y, pos_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            #q = quaternion_from_euler(-math.pi/2.0, math.pi/2.0, 0.0)  
            q = quaternion_from_euler(-math.pi, 0.0, 0.0)
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            arm.go()  # 実行

        def rotate_hand(pos_x, pos_y, pos_z, euler_x, euler_y, euler_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            q = quaternion_from_euler(euler_x, euler_y, euler_z)  
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            print(target_pose)
            arm.go()  # 実行
        
        #rotate_hand(0.19, 0.05, 0.2, -math.pi, 0.0, 0.0)
        n_x, n_y, n_z = nr.position.x, nr.position.y - 0.0125, nr.position.z
        #nr.position.x, nr.position.y, nr.position.z = 0.2-(sub_blue.x)+0.06, 0.2-(sub_blue.y)-0.07,0.2
        #nr.position.x, nr.position.y, nr.position.z = nr.position.x-(sub_blue.x)+0.06, nr.position.y-(sub_blue.y)-0.07,0.2
        rotate_hand(n_x, n_y, n_z, -math.pi, 0.0, 0.0)
        nr.position.x, nr.position.y, nr.position.z = n_x, n_y, n_z

    def z_move_game_min(self):
        robot = moveit_commander.RobotCommander()
        arm = moveit_commander.MoveGroupCommander("arm")
        arm.set_max_velocity_scaling_factor(0.5)
        gripper = moveit_commander.MoveGroupCommander("gripper")

        # アーム初期ポーズを表示
        arm_initial_pose = arm.get_current_pose().pose
        print("Arm initial pose:")
        print(arm_initial_pose)

        def move_gripper(pou):
            gripper.set_joint_value_target([pou, pou])
            gripper.go()

        def move_arm(pos_x, pos_y, pos_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            #q = quaternion_from_euler(-math.pi/2.0, math.pi/2.0, 0.0)  
            q = quaternion_from_euler(-math.pi, 0.0, 0.0)
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            arm.go()  # 実行

        def rotate_hand(pos_x, pos_y, pos_z, euler_x, euler_y, euler_z):
            target_pose = geometry_msgs.msg.Pose()
            target_pose.position.x = pos_x
            target_pose.position.y = pos_y
            target_pose.position.z = pos_z
            q = quaternion_from_euler(euler_x, euler_y, euler_z)  
            target_pose.orientation.x = q[0]
            target_pose.orientation.y = q[1]
            target_pose.orientation.z = q[2]
            target_pose.orientation.w = q[3]
            arm.set_pose_target(target_pose)  # 目標ポーズ設定
            print(target_pose)
            arm.go()  # 実行
        
        #rotate_hand(0.19, 0.05, 0.2, -math.pi, 0.0, 0.0)
        n_x, n_y, n_z = nr.position.x, nr.position.y, nr.position.z+0.01
        #nr.position.x, nr.position.y, nr.position.z = 0.2-(sub_blue.x)+0.06, 0.2-(sub_blue.y)-0.07,0.2
        #nr.position.x, nr.position.y, nr.position.z = nr.position.x-(sub_blue.x)+0.06, nr.position.y-(sub_blue.y)-0.07,0.2
        rotate_hand(n_x, n_y, n_z, -math.pi, 0.0, 0.0)
        nr.position.x, nr.position.y, nr.position.z = n_x, n_y, n_z        
        


if __name__ == '__main__':
    counter = 0
    global nr 
    nr = Pose()
    try:
        if not rospy.is_shutdown():
            rospy.init_node("crane_x7_crane_game")
            sub = Subscribe_publishers()
            app = QApplication(sys.argv)
            ex = Example()
            ex.show()
            sys.exit(app.exec_())        

    except rospy.ROSInterruptException:
        pass

