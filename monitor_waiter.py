import threading

class Waiter():
    def __init__(self):
        self.conditions = list()
    
    def register_philosophers(self, philosophers):
        self.philosophers = philosophers 
        self.num_philosophers = len(philosophers)
        for _ in range(self.num_philosophers):
            self.conditions.append(threading.Condition())

    def start_dinner(self):
        for i in range(self.num_philosophers):
            self.philosophers[i].start()

    def start_eat(self, id):
        with self.conditions[id]:
            allow_to_eat = self.__allow_to_eat(id)
            if not allow_to_eat:
                self.conditions[id].wait()

    def __allow_to_eat(self, id):
        return self.philosophers[id].state == "HUNGRY" \
                and self.get_left_heighbour(id).state != "EATING" \
                    and self.get_right_heighbour(id).state != "EATING"
    
    def end_eat(self, id):
        left_heighbour_id = self.get_left_heighbour_id(id)
        with self.conditions[left_heighbour_id]:
            self.conditions[left_heighbour_id].notify()
        right_heighbour_id = self.get_right_heighbour_id(id)
        with self.conditions[right_heighbour_id]:
            self.conditions[right_heighbour_id].notify()

    def get_left_heighbour(self, id):
        return self.philosophers[self.get_left_heighbour_id(id)]
    
    def get_right_heighbour(self, id):
        return self.philosophers[self.get_right_heighbour_id(id)]

    def get_left_heighbour_id(self, id):
        return (id + self.num_philosophers - 1) % self.num_philosophers
    
    def get_right_heighbour_id(self, id):
        return (id + 1) % self.num_philosophers
