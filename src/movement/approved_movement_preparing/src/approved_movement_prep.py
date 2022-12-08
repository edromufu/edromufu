#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import json
import os

from movement_msgs.msg import HeadParamsMsg, ApprovedMovementMsg, WalkCreatorRequestMsg
from std_msgs.msg import String

str_walking_movs_class = 'walking_movements'
str_head_movs_class = 'head_movements'
str_body_align_movs_class = 'body_alignment_movs'
str_page_movs_class = 'pages_list'

str_mov_class_func = 'function_to_call'
str_mov_params_field = 'params_all_kinds'

class MovementPreparation():

    def __init__(self):
        rospy.Subscriber('/movement/approved_movement', ApprovedMovementMsg, self.prepareMovement)

        self.walking_params_publisher = rospy.Publisher('/approved_movement_prep/IKWalk', WalkCreatorRequestMsg, queue_size=10)
        self.head_params_publisher = rospy.Publisher('/approved_movement_prep/XYHead', HeadParamsMsg, queue_size=10)
        self.page_params_publisher = rospy.Publisher('/approved_movement_prep/run_pages', String, queue_size=10)
        
        self.params_data = self.load_json_params()

    def load_json_params(self):
        user_name = os.environ.get("HOME")
        json_file = open(user_name + "/edrom/src/movement/approved_movement_preparing/include/movements_params.json") 
        data = json.load(json_file)
        json_file.close()

        self.walking_movements_func = data[str_walking_movs_class][str_mov_class_func]
        self.head_movements_func = data[str_head_movs_class][str_mov_class_func]
        self.body_alignment_func = data[str_body_align_movs_class][str_mov_class_func]
        self.page_run_func = data[str_page_movs_class][str_mov_class_func]

        return data

    def prepareMovement(self, request):
        print("\nMovimento aprovado a ser preparado: " + str(request.approved_movement))
        
        for mov_class in self.params_data:
            if request.approved_movement in self.params_data[mov_class][str_mov_params_field]:
                print("Movimento requisitado em " + mov_class + ", iniciando protocolo de preparação da classe.")

                func_to_call = self.params_data[mov_class][str_mov_class_func]

                if func_to_call == self.walking_movements_func:
                    self.walkingParamsRequest(self.params_data[mov_class][str_mov_params_field][request.approved_movement])
                    
                elif func_to_call == self.head_movements_func:
                    self.headParamsPublish(self.params_data[mov_class][str_mov_params_field][request.approved_movement])

                elif func_to_call == self.body_alignment_func:
                    self.bodyAlignmentPublish(self.params_data[mov_class][str_mov_params_field][request.approved_movement])  
                
                elif func_to_call == self.page_run_func:
                    self.pageRunPublish(self.params_data[mov_class][str_mov_params_field][request.approved_movement])
    
    def walkingParamsRequest(self, params):
        params2publish = WalkCreatorRequestMsg()
        params2publish.enabledGain = params['enabledGain']
        params2publish.stepGain = params['stepGain']
        params2publish.lateralGain = params['lateralGain']
        params2publish.turnGain = params['turnGain']

        self.walking_params_publisher.publish(params2publish)
    
    def headParamsPublish(self, params):
        params2publish = HeadParamsMsg()
        params2publish.direction = params['direction']
        params2publish.pattern = params['pattern']

        self.head_params_publisher.publish(params2publish)
    
    def bodyAlignmentPublish(self, params):
        walking_params_from_json = self.params_data[str_walking_movs_class][str_mov_params_field][params[str_walking_movs_class]]
        head_params_from_json = self.params_data[str_head_movs_class][str_mov_params_field][params[str_head_movs_class]]

        self.walkingParamsRequest(walking_params_from_json)
        self.headParamsPublish(head_params_from_json)
    
    def pageRunPublish(self, params):
        params2publish = String()
        params2publish.data = params['page_name']

        self.page_params_publisher.publish(params2publish)

if __name__ == "__main__":
    rospy.init_node('Approved_movement_prep_node', anonymous=False)

    preparing = MovementPreparation()

    rospy.spin()