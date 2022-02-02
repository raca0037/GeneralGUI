#!/usr/bin/env python3
import rospy
from std_srvs.srv import Trigger, TriggerResponse
def button_service(): #our main function
    rospy.init_node("button_service_node") #init node, creating the node to communicate with other nodes.
    s = rospy.Service("ButtonService",Trigger,callback) #service node on top of our ros node. name of service, type of service, and service callback

    rospy.spin()
def callback(req):
    #print(1)
    res = TriggerResponse() #callback is creating response, res = response, req = request from service.
    res.success = True
    res.message = "button pressed"

    return res #has to return the data type it's desiring in callback.
    #if its more complicated than you'll return those values/data in here.






if __name__ == '__main__':
    try:
        button_service()
    except rospy.ROSInterruptException: #stops it from being run if we have not launched the launch file or ctrl c is being pushed.
        pass