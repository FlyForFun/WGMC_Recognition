# coding: utf-8

class Robot:
    population=0
    def __init__(self,name):
        self.name=name
        Robot.population+=1
        print(Robot.population)
print('mm2')      
Robot('mm2_1')