#!/usr/bin/env python
'''
trot demo
'''

#created on: July 9,2019
#author    : buenos
#e-mail    : buenos@buaa.edu.cn

import time
import rospy
from std_msgs.msg import Float64
from legController import LegController
#leg_control.
#sys.path.append("/home/muxiangru/catkin_ws2/src/cheetah_simu-master/cheetah_sim/ros_package/cheetah_core/script/legController.py")
        
class Cheetah:
    def __init__(self):
        self.leg_names = ["LF","LB","RF","RB"]
        self.controllers = {name:LegController(name) for name in self.leg_names}

    def stand(self):
        pos = {"LF":(72.20   ,0.0   ,-300.0),
               "LB":(72.20   ,-30.0   ,-310.0),
               "RF":(72.20   ,0.0   ,-300.0),
               "RB":(72.20   ,-30.0   ,-310.0),}
        for leg in self.controllers:
            self.controllers[leg].writeEndPos(pos[leg])

    def run(self):
        while not rospy.is_shutdown():
            self.stand()
            time.sleep(0.1)


if __name__=="__main__":
    node = rospy.init_node("control_node",anonymous=True)
    cheetah = Cheetah()
    cheetah.run()
