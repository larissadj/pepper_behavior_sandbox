#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from pepper_flexbe_states.wait_for_naoqi_speech import WaitForNaoQiSpeechState
from pepper_flexbe_states.set_navgoal_state import MoveBaseState
from pepper_flexbe_states.generate_navgoal import GenerateNavgoalState
from pepper_flexbe_states.talk_state import TalkState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Jan 17 2018
@author: ffriese
'''
class LeadToAppartmentDemoSM(Behavior):
    '''
    Simple Demo where Pepper leads Guests to the Appartment
    '''


    def __init__(self):
        super(LeadToAppartmentDemoSM, self).__init__()
        self.name = 'LeadToAppartmentDemo'

        # parameters of this behavior

        # references to used behaviors

        # Additional initialization code can be added inside the following tags
        # [MANUAL_INIT]
        
        # [/MANUAL_INIT]

        # Behavior comments:



    def create(self):
        # x:135 y:584, x:382 y:306
        _state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

        # Additional creation code can be added inside the following tags
        # [MANUAL_CREATE]
        
        # [/MANUAL_CREATE]


        with _state_machine:
            # x:78 y:28
            OperatableStateMachine.add('WaitForGuideCommand',
                                        WaitForNaoQiSpeechState(strings_to_rec=['Hallo Pepper bitte bring unseren Gast zum Appartment'], outcomes=['appartment'], topic='/pepper_robot/speechrec/context'),
                                        transitions={'appartment': 'AcknowlegdeCommand'},
                                        autonomy={'appartment': Autonomy.Off})

            # x:329 y:147
            OperatableStateMachine.add('GuideToAppartment',
                                        MoveBaseState(),
                                        transitions={'arrived': 'AnnounceArrival', 'failed': 'AnnounceFailure'},
                                        autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off},
                                        remapping={'waypoint': 'outside_appartment'})

            # x:641 y:25
            OperatableStateMachine.add('SetNavgoalAtAppartment',
                                        GenerateNavgoalState(x=5, y=5, theta=0.0, frame_id='map'),
                                        transitions={'done': 'GuideToAppartment'},
                                        autonomy={'done': Autonomy.Off},
                                        remapping={'navgoal': 'outside_appartment'})

            # x:106 y:157
            OperatableStateMachine.add('AnnounceArrival',
                                        TalkState(message='Here We Are. I hope you enjoy your stay.', blocking=True),
                                        transitions={'done': 'SetNavgoalInside', 'failed': 'failed'},
                                        autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off})

            # x:546 y:232
            OperatableStateMachine.add('AnnounceFailure',
                                        TalkState(message='Unfortunately I could not guide you to the appartment. I am deeply sorry', blocking=True),
                                        transitions={'done': 'failed', 'failed': 'failed'},
                                        autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off})

            # x:103 y:319
            OperatableStateMachine.add('SetNavgoalInside',
                                        GenerateNavgoalState(x=6, y=7, theta=0.0, frame_id='map'),
                                        transitions={'done': 'DriveInside'},
                                        autonomy={'done': Autonomy.Off},
                                        remapping={'navgoal': 'inside_appartment'})

            # x:106 y:412
            OperatableStateMachine.add('DriveInside',
                                        MoveBaseState(),
                                        transitions={'arrived': 'finished', 'failed': 'failed'},
                                        autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off},
                                        remapping={'waypoint': 'inside_appartment'})

            # x:342 y:26
            OperatableStateMachine.add('AcknowlegdeCommand',
                                        TalkState(message='With Pleasure. Follow my lead.', blocking=True),
                                        transitions={'done': 'SetNavgoalAtAppartment', 'failed': 'SetNavgoalAtAppartment'},
                                        autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off})


        return _state_machine


    # Private functions can be added inside the following tags
    # [MANUAL_FUNC]
    
    # [/MANUAL_FUNC]
