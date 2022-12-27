# Robotdesign3_2022
**ロボット設計製作論実習3**  
こちらはCRANE-X7を用いて、自作の積み木を積み上げるためのROSパッケージになります。  
本パッケージはオリジナルである[rt-net/crane_x7_ros](https://github.com/rt-net/crane_x7_ros)を元に  
千葉工業大学先進工学部未来ロボティクス学科の学生が講義内でグループ2022-RobotDesign-team1(レッドリボン軍)が作成したものです。
## 実装内容
[CRANE-X7](https://rt-net.jp/products/crane-x7/)を用いて、積み木を積み上げるサンプルコードとなります。  
CRANE-X7とintelRealSenseD435を使用しています。  
## 動作内容
- Ubuntu 20.04.5 LTS
- ROS Noetic
  - Gazebo
  - Rviz
  - MoveIt
  - RealSense SDK
- OpenCV 4.5,1
---
## 環境構築
1. ROSのインストール
```
$
```
2. 動作環境
```
$
```
`Ctrl+C`でプログラムを終了
3. ワークスペースを作成し、`~/.bashrc`を編集
```
$
```
4. CRANE-X7のROSパッケージインストール
```
$
```
5. RVIZの動作確認
```
$
```
6. GAZEBOの動作確認
```
$
```
7. 本パッケージのインストール
```
$
```
8. RealSenseのセットアップ
```
$
```
9. OpenCVのインストール
```
$
```
## 知的財産について
CRANE-X7は、アールティが開発した研究用アームロボットです。 このリポジトリのデータ等に関するライセンスについては、[LICENSE](https://github.com/2021-RobotDesign3-team2/crane_x7_ros_test/blob/main/LICENSE)ファイルをご参照ください。 企業による使用については、自社内において研究開発をする目的に限り、本データの使用を許諾します。 本データを使って自作されたい方は、義務ではありませんが弊社ロボットショップで部品をお買い求めいただければ、励みになります。 商業目的をもって本データを使用する場合は、商業用使用許諾の条件等について弊社までお問合せください。

サーボモータのXM540やXM430に関するCADモデルの使用については、ROBOTIS社より使用許諾を受けています。 CRANE-X7に使用されているROBOTIS社の部品類にかかる著作権、商標権、その他の知的財産権は、ROBOTIS社に帰属します。
## Proprietary Rights
CRANE-X7 is an arm robot developed by RT Corporation for research purposes. Please read [the license information](https://github.com/2021-RobotDesign3-team2/crane_x7_ros_test/blob/main/LICENSE) contained in this repository to find out more about licensing. Companies are permitted to use CRANE-X7 and the materials made available here for internal, research and development purposes only. If you are interested in building your own robot for your personal use by utilizing the information made available here, take your time to visit our website and purchase relevant components and parts – that will certainly help us keep going! Otherwise, if you are interested in manufacturing and commercializing products based on the information herein, please contact us to arrange a license and collaboration agreement with us.

We have obtained permission from ROBOTIS Co., Ltd. to use CAD models relating to servo motors XM540 and XM430. The proprietary rights relating to any components or parts manufactured by ROBOTIS and used in this product, including but not limited to copyrights, trademarks, and other intellectual property rights, shall remain vested in ROBOTIS.
