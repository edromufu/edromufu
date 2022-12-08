#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import possibleMovementsList

class StatsManipulator():
    
    def __init__(self):
        self.movList = possibleMovementsList.PossibleMovementsList()

    def isMovementListed(self, movement_to_be_checked):
        if movement_to_be_checked in self.movList.dict_movements_listed_and_their_status.keys():
            return True
        else:
            return False

    def changeMovementStatus(self, _new_movement, _status):
        
        if _new_movement not in self.movList.other_movements_listed:
            for movement in self.movList.other_movements_listed:
                if(self.movList.dict_movements_listed_and_their_status[movement]):
                    print(f"Impossivel alterar status. Movimento {movement} esta ligado")
                    return False

        for movement in self.movList.dict_movements_listed_and_their_status.keys():
            if (movement == _new_movement):
                self.movList.dict_movements_listed_and_their_status[movement] = _status
                print(f"O status de {movement} alterado para: {self.movList.dict_movements_listed_and_their_status[movement]}")
            else:
                self.movList.dict_movements_listed_and_their_status[movement] = False
                
        return True
        
    def showAllStatus(self):

        for key in self.movList.dict_movements_listed_and_their_status.keys():
            print("O movimento", key, "tem status:", self.movList.dict_movements_listed_and_their_status[key])
