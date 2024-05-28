#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        print("Student.__init__ called.")
        self.knowledge = []

    def learn(self, new_knowledge):
        print("Student.learn called.")
        self.knowledge.append(new_knowledge)
            
        