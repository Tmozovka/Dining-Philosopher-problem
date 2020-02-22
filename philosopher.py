import threading
from time import sleep

#states:  THINKING -> HUNGRY -> EATING 
class Philosopher(threading.Thread):
    def __init__(self, id, waiter, number_of_times_to_eat, eat_time, think_time,*args,**kwargs):
        threading.Thread.__init__(self)
        self.eat_time = eat_time
        self.think_time = think_time
        self.id = id  # int 0,1,2,3,4
        self.number_of_times_to_eat = number_of_times_to_eat
        self.waiter = waiter # monitor 
        self.state = None

    def run(self):
        number_of_times_to_eat = 0
        while number_of_times_to_eat != self.number_of_times_to_eat:
            self.think()
            self.be_hungry()
            self.eat()
            number_of_times_to_eat += 1
            print("Philosopher %i ate %i time"% (self.id,number_of_times_to_eat))
        self.state = "END"

    def think(self):
        self.state = "THINKING"
        print("Philosopher %i is thinking"%self.id)
        sleep(self.think_time)

    def be_hungry(self):
        print("Philosopher %i is hungry"%self.id)
        self.state = "HUNGRY"

    def eat(self):
        self.waiter.start_eat(self.id)
        self.state = "EATING"
        print("Philosopher %i is eating"%self.id)
        sleep(self.eat_time)
        self.waiter.end_eat(self.id)