#!/usr/bin/python
import rospy
from geometry_msgs.msg import Twist,Pose,PoseStamped
from gazebo_msgs.msg import ModelStates,ModelState
import time
import numpy as np
import threading
x=[]
y=[]
angle=[]
t=60*18
with open('/home/microlab/microlab/files/0501/x.txt','r') as path_data:
    for line in path_data:
        x.append(line.split())
with open('/home/microlab/microlab/files/0501/y.txt','r') as path_data:
    for line in path_data:
        y.append(line.split())
with open('/home/microlab/microlab/files/0501/angle.txt','r') as path_data:
    for line in path_data:
        angle.append(line.split())
def thread_job():
    rospy.spin() 
class Publish0:
    def __init__(self):
        self.pub0 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(0)
               pose_msg.pose.position.x=eval(x[0][j])
               print(eval(x[0][j]))
               self.pub0.publish(pose_msg)
               time.sleep(0.1)
class Publish1:
    def __init__(self):
        self.pub1 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(1)
               pose_msg.pose.position.x=eval(x[1][j])
               print(eval(x[1][j]))
               self.pub1.publish(pose_msg)
               time.sleep(0.1)
class Publish2:
    def __init__(self):
        self.pub2 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(2)
               pose_msg.pose.position.x=eval(x[2][j])
               print(eval(x[2][j]))
               self.pub2.publish(pose_msg)
               time.sleep(0.1)
class Publish3:
    def __init__(self):
        self.pub3 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(3)
               pose_msg.pose.position.x=eval(x[3][j])
               print(eval(x[3][j]))
               self.pub3.publish(pose_msg)
               time.sleep(0.1)
class Publish4:
    def __init__(self):
        self.pub4 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(4)
               pose_msg.pose.position.x=eval(x[4][j])
               print(eval(x[4][j]))
               self.pub4.publish(pose_msg)
               time.sleep(0.1)
class Publish5:
    def __init__(self):
        self.pub5 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(5)
               pose_msg.pose.position.x=eval(x[5][j])
               print(eval(x[5][j]))
               self.pub5.publish(pose_msg)
               time.sleep(0.1)
class Publish6:
    def __init__(self):
        self.pub6 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(6)
               pose_msg.pose.position.x=eval(x[6][j])
               print(eval(x[6][j]))
               self.pub6.publish(pose_msg)
               time.sleep(0.1)
class Publish7:
    def __init__(self):
        self.pub7 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(7)
               pose_msg.pose.position.x=eval(x[7][j])
               print(eval(x[7][j]))
               self.pub7.publish(pose_msg)
               time.sleep(0.1)
class Publish8:
    def __init__(self):
        self.pub8 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(8)
               pose_msg.pose.position.x=eval(x[8][j])
               print(eval(x[8][j]))
               self.pub8.publish(pose_msg)
               time.sleep(0.1)
class Publish9:
    def __init__(self):
        self.pub9 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(9)
               pose_msg.pose.position.x=eval(x[9][j])
               print(eval(x[9][j]))
               self.pub9.publish(pose_msg)
               time.sleep(0.1)
class Publish10:
    def __init__(self):
        self.pub10 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(10)
               pose_msg.pose.position.x=eval(x[10][j])
               print(eval(x[10][j]))
               self.pub10.publish(pose_msg)
               time.sleep(0.1)
class Publish11:
    def __init__(self):
        self.pub11 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(11)
               pose_msg.pose.position.x=eval(x[11][j])
               print(eval(x[11][j]))
               self.pub11.publish(pose_msg)
               time.sleep(0.1)
class Publish12:
    def __init__(self):
        self.pub12 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(12)
               pose_msg.pose.position.x=eval(x[12][j])
               print(eval(x[12][j]))
               self.pub12.publish(pose_msg)
               time.sleep(0.1)
class Publish13:
    def __init__(self):
        self.pub13 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(13)
               pose_msg.pose.position.x=eval(x[13][j])
               print(eval(x[13][j]))
               self.pub13.publish(pose_msg)
               time.sleep(0.1)
class Publish14:
    def __init__(self):
        self.pub14 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(14)
               pose_msg.pose.position.x=eval(x[14][j])
               print(eval(x[14][j]))
               self.pub14.publish(pose_msg)
               time.sleep(0.1)
class Publish15:
    def __init__(self):
        self.pub15 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(15)
               pose_msg.pose.position.x=eval(x[15][j])
               print(eval(x[15][j]))
               self.pub15.publish(pose_msg)
               time.sleep(0.1)
class Publish16:
    def __init__(self):
        self.pub16 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(16)
               pose_msg.pose.position.x=eval(x[16][j])
               print(eval(x[16][j]))
               self.pub16.publish(pose_msg)
               time.sleep(0.1)
class Publish17:
    def __init__(self):
        self.pub17 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(17)
               pose_msg.pose.position.x=eval(x[17][j])
               print(eval(x[17][j]))
               self.pub17.publish(pose_msg)
               time.sleep(0.1)
class Publish18:
    def __init__(self):
        self.pub18 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(18)
               pose_msg.pose.position.x=eval(x[18][j])
               print(eval(x[18][j]))
               self.pub18.publish(pose_msg)
               time.sleep(0.1)
class Publish19:
    def __init__(self):
        self.pub19 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(19)
               pose_msg.pose.position.x=eval(x[19][j])
               print(eval(x[19][j]))
               self.pub19.publish(pose_msg)
               time.sleep(0.1)
class Publish20:
    def __init__(self):
        self.pub20 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(20)
               pose_msg.pose.position.x=eval(x[20][j])
               print(eval(x[20][j]))
               self.pub20.publish(pose_msg)
               time.sleep(0.1)
class Publish21:
    def __init__(self):
        self.pub21 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(21)
               pose_msg.pose.position.x=eval(x[21][j])
               print(eval(x[21][j]))
               self.pub21.publish(pose_msg)
               time.sleep(0.1)
class Publish22:
    def __init__(self):
        self.pub22 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(22)
               pose_msg.pose.position.x=eval(x[22][j])
               print(eval(x[22][j]))
               self.pub22.publish(pose_msg)
               time.sleep(0.1)
class Publish23:
    def __init__(self):
        self.pub23 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(23)
               pose_msg.pose.position.x=eval(x[23][j])
               print(eval(x[23][j]))
               self.pub23.publish(pose_msg)
               time.sleep(0.1)
class Publish24:
    def __init__(self):
        self.pub24 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(24)
               pose_msg.pose.position.x=eval(x[24][j])
               print(eval(x[24][j]))
               self.pub24.publish(pose_msg)
               time.sleep(0.1)
class Publish25:
    def __init__(self):
        self.pub25 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(25)
               pose_msg.pose.position.x=eval(x[25][j])
               print(eval(x[25][j]))
               self.pub25.publish(pose_msg)
               time.sleep(0.1)
class Publish26:
    def __init__(self):
        self.pub26 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(26)
               pose_msg.pose.position.x=eval(x[26][j])
               print(eval(x[26][j]))
               self.pub26.publish(pose_msg)
               time.sleep(0.1)
class Publish27:
    def __init__(self):
        self.pub27 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(27)
               pose_msg.pose.position.x=eval(x[27][j])
               print(eval(x[27][j]))
               self.pub27.publish(pose_msg)
               time.sleep(0.1)
class Publish28:
    def __init__(self):
        self.pub28 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(28)
               pose_msg.pose.position.x=eval(x[28][j])
               print(eval(x[28][j]))
               self.pub28.publish(pose_msg)
               time.sleep(0.1)
class Publish29:
    def __init__(self):
        self.pub29 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(29)
               pose_msg.pose.position.x=eval(x[29][j])
               print(eval(x[29][j]))
               self.pub29.publish(pose_msg)
               time.sleep(0.1)
class Publish30:
    def __init__(self):
        self.pub30 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(30)
               pose_msg.pose.position.x=eval(x[30][j])
               print(eval(x[30][j]))
               self.pub30.publish(pose_msg)
               time.sleep(0.1)
class Publish31:
    def __init__(self):
        self.pub31 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(31)
               pose_msg.pose.position.x=eval(x[31][j])
               print(eval(x[31][j]))
               self.pub31.publish(pose_msg)
               time.sleep(0.1)
class Publish32:
    def __init__(self):
        self.pub32 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(32)
               pose_msg.pose.position.x=eval(x[32][j])
               print(eval(x[32][j]))
               self.pub32.publish(pose_msg)
               time.sleep(0.1)
class Publish33:
    def __init__(self):
        self.pub33 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(33)
               pose_msg.pose.position.x=eval(x[33][j])
               print(eval(x[33][j]))
               self.pub33.publish(pose_msg)
               time.sleep(0.1)
class Publish34:
    def __init__(self):
        self.pub34 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(34)
               pose_msg.pose.position.x=eval(x[34][j])
               print(eval(x[34][j]))
               self.pub34.publish(pose_msg)
               time.sleep(0.1)
class Publish35:
    def __init__(self):
        self.pub35 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(35)
               pose_msg.pose.position.x=eval(x[35][j])
               print(eval(x[35][j]))
               self.pub35.publish(pose_msg)
               time.sleep(0.1)
class Publish36:
    def __init__(self):
        self.pub36 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(36)
               pose_msg.pose.position.x=eval(x[36][j])
               print(eval(x[36][j]))
               self.pub36.publish(pose_msg)
               time.sleep(0.1)
class Publish37:
    def __init__(self):
        self.pub37 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(37)
               pose_msg.pose.position.x=eval(x[37][j])
               print(eval(x[37][j]))
               self.pub37.publish(pose_msg)
               time.sleep(0.1)
class Publish38:
    def __init__(self):
        self.pub38 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(38)
               pose_msg.pose.position.x=eval(x[38][j])
               print(eval(x[38][j]))
               self.pub38.publish(pose_msg)
               time.sleep(0.1)
class Publish39:
    def __init__(self):
        self.pub39 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(39)
               pose_msg.pose.position.x=eval(x[39][j])
               print(eval(x[39][j]))
               self.pub39.publish(pose_msg)
               time.sleep(0.1)
class Publish40:
    def __init__(self):
        self.pub40 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(40)
               pose_msg.pose.position.x=eval(x[40][j])
               print(eval(x[40][j]))
               self.pub40.publish(pose_msg)
               time.sleep(0.1)
class Publish41:
    def __init__(self):
        self.pub41 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(41)
               pose_msg.pose.position.x=eval(x[41][j])
               print(eval(x[41][j]))
               self.pub41.publish(pose_msg)
               time.sleep(0.1)
class Publish42:
    def __init__(self):
        self.pub42 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(42)
               pose_msg.pose.position.x=eval(x[42][j])
               print(eval(x[42][j]))
               self.pub42.publish(pose_msg)
               time.sleep(0.1)
class Publish43:
    def __init__(self):
        self.pub43 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(43)
               pose_msg.pose.position.x=eval(x[43][j])
               print(eval(x[43][j]))
               self.pub43.publish(pose_msg)
               time.sleep(0.1)
class Publish44:
    def __init__(self):
        self.pub44 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(44)
               pose_msg.pose.position.x=eval(x[44][j])
               print(eval(x[44][j]))
               self.pub44.publish(pose_msg)
               time.sleep(0.1)
class Publish45:
    def __init__(self):
        self.pub45 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(45)
               pose_msg.pose.position.x=eval(x[45][j])
               print(eval(x[45][j]))
               self.pub45.publish(pose_msg)
               time.sleep(0.1)
class Publish46:
    def __init__(self):
        self.pub46 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(46)
               pose_msg.pose.position.x=eval(x[46][j])
               print(eval(x[46][j]))
               self.pub46.publish(pose_msg)
               time.sleep(0.1)
class Publish47:
    def __init__(self):
        self.pub47 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(47)
               pose_msg.pose.position.x=eval(x[47][j])
               print(eval(x[47][j]))
               self.pub47.publish(pose_msg)
               time.sleep(0.1)
class Publish48:
    def __init__(self):
        self.pub48 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(48)
               pose_msg.pose.position.x=eval(x[48][j])
               print(eval(x[48][j]))
               self.pub48.publish(pose_msg)
               time.sleep(0.1)
class Publish49:
    def __init__(self):
        self.pub49 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(49)
               pose_msg.pose.position.x=eval(x[49][j])
               print(eval(x[49][j]))
               self.pub49.publish(pose_msg)
               time.sleep(0.1)
class Publish50:
    def __init__(self):
        self.pub50 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(50)
               pose_msg.pose.position.x=eval(x[50][j])
               print(eval(x[50][j]))
               self.pub50.publish(pose_msg)
               time.sleep(0.1)
class Publish51:
    def __init__(self):
        self.pub51 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(51)
               pose_msg.pose.position.x=eval(x[51][j])
               print(eval(x[51][j]))
               self.pub51.publish(pose_msg)
               time.sleep(0.1)
class Publish52:
    def __init__(self):
        self.pub52 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(52)
               pose_msg.pose.position.x=eval(x[52][j])
               print(eval(x[52][j]))
               self.pub52.publish(pose_msg)
               time.sleep(0.1)
class Publish53:
    def __init__(self):
        self.pub53 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(53)
               pose_msg.pose.position.x=eval(x[53][j])
               print(eval(x[53][j]))
               self.pub53.publish(pose_msg)
               time.sleep(0.1)
class Publish54:
    def __init__(self):
        self.pub54 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(54)
               pose_msg.pose.position.x=eval(x[54][j])
               print(eval(x[54][j]))
               self.pub54.publish(pose_msg)
               time.sleep(0.1)
class Publish55:
    def __init__(self):
        self.pub55 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(55)
               pose_msg.pose.position.x=eval(x[55][j])
               print(eval(x[55][j]))
               self.pub55.publish(pose_msg)
               time.sleep(0.1)
class Publish56:
    def __init__(self):
        self.pub56 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(56)
               pose_msg.pose.position.x=eval(x[56][j])
               print(eval(x[56][j]))
               self.pub56.publish(pose_msg)
               time.sleep(0.1)
class Publish57:
    def __init__(self):
        self.pub57 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(57)
               pose_msg.pose.position.x=eval(x[57][j])
               print(eval(x[57][j]))
               self.pub57.publish(pose_msg)
               time.sleep(0.1)
class Publish58:
    def __init__(self):
        self.pub58 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(58)
               pose_msg.pose.position.x=eval(x[58][j])
               print(eval(x[58][j]))
               self.pub58.publish(pose_msg)
               time.sleep(0.1)
class Publish59:
    def __init__(self):
        self.pub59 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(59)
               pose_msg.pose.position.x=eval(x[59][j])
               print(eval(x[59][j]))
               self.pub59.publish(pose_msg)
               time.sleep(0.1)
class Publish60:
    def __init__(self):
        self.pub60 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(60)
               pose_msg.pose.position.x=eval(x[60][j])
               print(eval(x[60][j]))
               self.pub60.publish(pose_msg)
               time.sleep(0.1)
class Publish61:
    def __init__(self):
        self.pub61 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(61)
               pose_msg.pose.position.x=eval(x[61][j])
               print(eval(x[61][j]))
               self.pub61.publish(pose_msg)
               time.sleep(0.1)
class Publish62:
    def __init__(self):
        self.pub62 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(62)
               pose_msg.pose.position.x=eval(x[62][j])
               print(eval(x[62][j]))
               self.pub62.publish(pose_msg)
               time.sleep(0.1)
class Publish63:
    def __init__(self):
        self.pub63 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(63)
               pose_msg.pose.position.x=eval(x[63][j])
               print(eval(x[63][j]))
               self.pub63.publish(pose_msg)
               time.sleep(0.1)
class Publish64:
    def __init__(self):
        self.pub64 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(64)
               pose_msg.pose.position.x=eval(x[64][j])
               print(eval(x[64][j]))
               self.pub64.publish(pose_msg)
               time.sleep(0.1)
class Publish65:
    def __init__(self):
        self.pub65 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(65)
               pose_msg.pose.position.x=eval(x[65][j])
               print(eval(x[65][j]))
               self.pub65.publish(pose_msg)
               time.sleep(0.1)
class Publish66:
    def __init__(self):
        self.pub66 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(66)
               pose_msg.pose.position.x=eval(x[66][j])
               print(eval(x[66][j]))
               self.pub66.publish(pose_msg)
               time.sleep(0.1)
class Publish67:
    def __init__(self):
        self.pub67 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(67)
               pose_msg.pose.position.x=eval(x[67][j])
               print(eval(x[67][j]))
               self.pub67.publish(pose_msg)
               time.sleep(0.1)
class Publish68:
    def __init__(self):
        self.pub68 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(68)
               pose_msg.pose.position.x=eval(x[68][j])
               print(eval(x[68][j]))
               self.pub68.publish(pose_msg)
               time.sleep(0.1)
class Publish69:
    def __init__(self):
        self.pub69 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(69)
               pose_msg.pose.position.x=eval(x[69][j])
               print(eval(x[69][j]))
               self.pub69.publish(pose_msg)
               time.sleep(0.1)
class Publish70:
    def __init__(self):
        self.pub70 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(70)
               pose_msg.pose.position.x=eval(x[70][j])
               print(eval(x[70][j]))
               self.pub70.publish(pose_msg)
               time.sleep(0.1)
class Publish71:
    def __init__(self):
        self.pub71 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(71)
               pose_msg.pose.position.x=eval(x[71][j])
               print(eval(x[71][j]))
               self.pub71.publish(pose_msg)
               time.sleep(0.1)
class Publish72:
    def __init__(self):
        self.pub72 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(72)
               pose_msg.pose.position.x=eval(x[72][j])
               print(eval(x[72][j]))
               self.pub72.publish(pose_msg)
               time.sleep(0.1)
class Publish73:
    def __init__(self):
        self.pub73 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(73)
               pose_msg.pose.position.x=eval(x[73][j])
               print(eval(x[73][j]))
               self.pub73.publish(pose_msg)
               time.sleep(0.1)
class Publish74:
    def __init__(self):
        self.pub74 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(74)
               pose_msg.pose.position.x=eval(x[74][j])
               print(eval(x[74][j]))
               self.pub74.publish(pose_msg)
               time.sleep(0.1)
class Publish75:
    def __init__(self):
        self.pub75 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(75)
               pose_msg.pose.position.x=eval(x[75][j])
               print(eval(x[75][j]))
               self.pub75.publish(pose_msg)
               time.sleep(0.1)
class Publish76:
    def __init__(self):
        self.pub76 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(76)
               pose_msg.pose.position.x=eval(x[76][j])
               print(eval(x[76][j]))
               self.pub76.publish(pose_msg)
               time.sleep(0.1)
class Publish77:
    def __init__(self):
        self.pub77 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(77)
               pose_msg.pose.position.x=eval(x[77][j])
               print(eval(x[77][j]))
               self.pub77.publish(pose_msg)
               time.sleep(0.1)
class Publish78:
    def __init__(self):
        self.pub78 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(78)
               pose_msg.pose.position.x=eval(x[78][j])
               print(eval(x[78][j]))
               self.pub78.publish(pose_msg)
               time.sleep(0.1)
class Publish79:
    def __init__(self):
        self.pub79 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(79)
               pose_msg.pose.position.x=eval(x[79][j])
               print(eval(x[79][j]))
               self.pub79.publish(pose_msg)
               time.sleep(0.1)
class Publish80:
    def __init__(self):
        self.pub80 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(80)
               pose_msg.pose.position.x=eval(x[80][j])
               print(eval(x[80][j]))
               self.pub80.publish(pose_msg)
               time.sleep(0.1)
class Publish81:
    def __init__(self):
        self.pub81 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(81)
               pose_msg.pose.position.x=eval(x[81][j])
               print(eval(x[81][j]))
               self.pub81.publish(pose_msg)
               time.sleep(0.1)
class Publish82:
    def __init__(self):
        self.pub82 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(82)
               pose_msg.pose.position.x=eval(x[82][j])
               print(eval(x[82][j]))
               self.pub82.publish(pose_msg)
               time.sleep(0.1)
class Publish83:
    def __init__(self):
        self.pub83 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(83)
               pose_msg.pose.position.x=eval(x[83][j])
               print(eval(x[83][j]))
               self.pub83.publish(pose_msg)
               time.sleep(0.1)
class Publish84:
    def __init__(self):
        self.pub84 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(84)
               pose_msg.pose.position.x=eval(x[84][j])
               print(eval(x[84][j]))
               self.pub84.publish(pose_msg)
               time.sleep(0.1)
class Publish85:
    def __init__(self):
        self.pub85 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(85)
               pose_msg.pose.position.x=eval(x[85][j])
               print(eval(x[85][j]))
               self.pub85.publish(pose_msg)
               time.sleep(0.1)
class Publish86:
    def __init__(self):
        self.pub86 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(86)
               pose_msg.pose.position.x=eval(x[86][j])
               print(eval(x[86][j]))
               self.pub86.publish(pose_msg)
               time.sleep(0.1)
class Publish87:
    def __init__(self):
        self.pub87 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(87)
               pose_msg.pose.position.x=eval(x[87][j])
               print(eval(x[87][j]))
               self.pub87.publish(pose_msg)
               time.sleep(0.1)
class Publish88:
    def __init__(self):
        self.pub88 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(88)
               pose_msg.pose.position.x=eval(x[88][j])
               print(eval(x[88][j]))
               self.pub88.publish(pose_msg)
               time.sleep(0.1)
class Publish89:
    def __init__(self):
        self.pub89 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(89)
               pose_msg.pose.position.x=eval(x[89][j])
               print(eval(x[89][j]))
               self.pub89.publish(pose_msg)
               time.sleep(0.1)
class Publish90:
    def __init__(self):
        self.pub90 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(90)
               pose_msg.pose.position.x=eval(x[90][j])
               print(eval(x[90][j]))
               self.pub90.publish(pose_msg)
               time.sleep(0.1)
class Publish91:
    def __init__(self):
        self.pub91 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(91)
               pose_msg.pose.position.x=eval(x[91][j])
               print(eval(x[91][j]))
               self.pub91.publish(pose_msg)
               time.sleep(0.1)
class Publish92:
    def __init__(self):
        self.pub92 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(92)
               pose_msg.pose.position.x=eval(x[92][j])
               print(eval(x[92][j]))
               self.pub92.publish(pose_msg)
               time.sleep(0.1)
class Publish93:
    def __init__(self):
        self.pub93 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(93)
               pose_msg.pose.position.x=eval(x[93][j])
               print(eval(x[93][j]))
               self.pub93.publish(pose_msg)
               time.sleep(0.1)
class Publish94:
    def __init__(self):
        self.pub94 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(94)
               pose_msg.pose.position.x=eval(x[94][j])
               print(eval(x[94][j]))
               self.pub94.publish(pose_msg)
               time.sleep(0.1)
class Publish95:
    def __init__(self):
        self.pub95 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(95)
               pose_msg.pose.position.x=eval(x[95][j])
               print(eval(x[95][j]))
               self.pub95.publish(pose_msg)
               time.sleep(0.1)
class Publish96:
    def __init__(self):
        self.pub96 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(96)
               pose_msg.pose.position.x=eval(x[96][j])
               print(eval(x[96][j]))
               self.pub96.publish(pose_msg)
               time.sleep(0.1)
class Publish97:
    def __init__(self):
        self.pub97 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(97)
               pose_msg.pose.position.x=eval(x[97][j])
               print(eval(x[97][j]))
               self.pub97.publish(pose_msg)
               time.sleep(0.1)
class Publish98:
    def __init__(self):
        self.pub98 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(98)
               pose_msg.pose.position.x=eval(x[98][j])
               print(eval(x[98][j]))
               self.pub98.publish(pose_msg)
               time.sleep(0.1)
class Publish99:
    def __init__(self):
        self.pub99 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        pose_msg = ModelState()
        while(1):
           for j in range(t):
               pose_msg.model_name = 'turtlebot3_'+str(99)
               pose_msg.pose.position.x=eval(x[99][j])
               print(eval(x[99][j]))
               self.pub99.publish(pose_msg)
               time.sleep(0.1)
if __name__ == '__main__':
    rospy.init_node('multi_pub')
    rate = rospy.Rate(100)
    pub0 = Publish0()
    pub1 = Publish1()
    pub2 = Publish2()
    pub3 = Publish3()
    pub4 = Publish4()
    pub5 = Publish5()
    pub6 = Publish6()
    pub7 = Publish7()
    pub8 = Publish8()
    pub9 = Publish9()
    pub10 = Publish10()
    pub11 = Publish11()
    pub12 = Publish12()
    pub13 = Publish13()
    pub14 = Publish14()
    pub15 = Publish15()
    pub16 = Publish16()
    pub17 = Publish17()
    pub18 = Publish18()
    pub19 = Publish19()
    pub20 = Publish20()
    pub21 = Publish21()
    pub22 = Publish22()
    pub23 = Publish23()
    pub24 = Publish24()
    pub25 = Publish25()
    pub26 = Publish26()
    pub27 = Publish27()
    pub28 = Publish28()
    pub29 = Publish29()
    pub30 = Publish30()
    pub31 = Publish31()
    pub32 = Publish32()
    pub33 = Publish33()
    pub34 = Publish34()
    pub35 = Publish35()
    pub36 = Publish36()
    pub37 = Publish37()
    pub38 = Publish38()
    pub39 = Publish39()
    pub40 = Publish40()
    pub41 = Publish41()
    pub42 = Publish42()
    pub43 = Publish43()
    pub44 = Publish44()
    pub45 = Publish45()
    pub46 = Publish46()
    pub47 = Publish47()
    pub48 = Publish48()
    pub49 = Publish49()
    pub50 = Publish50()
    pub51 = Publish51()
    pub52 = Publish52()
    pub53 = Publish53()
    pub54 = Publish54()
    pub55 = Publish55()
    pub56 = Publish56()
    pub57 = Publish57()
    pub58 = Publish58()
    pub59 = Publish59()
    pub60 = Publish60()
    pub61 = Publish61()
    pub62 = Publish62()
    pub63 = Publish63()
    pub64 = Publish64()
    pub65 = Publish65()
    pub66 = Publish66()
    pub67 = Publish67()
    pub68 = Publish68()
    pub69 = Publish69()
    pub70 = Publish70()
    pub71 = Publish71()
    pub72 = Publish72()
    pub73 = Publish73()
    pub74 = Publish74()
    pub75 = Publish75()
    pub76 = Publish76()
    pub77 = Publish77()
    pub78 = Publish78()
    pub79 = Publish79()
    pub80 = Publish80()
    pub81 = Publish81()
    pub82 = Publish82()
    pub83 = Publish83()
    pub84 = Publish84()
    pub85 = Publish85()
    pub86 = Publish86()
    pub87 = Publish87()
    pub88 = Publish88()
    pub89 = Publish89()
    pub90 = Publish90()
    pub91 = Publish91()
    pub92 = Publish92()
    pub93 = Publish93()
    pub94 = Publish94()
    pub95 = Publish95()
    pub96 = Publish96()
    pub97 = Publish97()
    pub98 = Publish98()
    pub99 = Publish99()
    thread_rosspin = threading.Thread(target=thread_job)
    thread_rosspin.start()
