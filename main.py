import threading
from philosopher import Philosopher 
from monitor_waiter import Waiter

waiter = Waiter()

p0 = Philosopher(id = 0, waiter = waiter, number_of_times_to_eat = 10, eat_time = 1, think_time = 1)
p1 = Philosopher(id = 1, waiter = waiter, number_of_times_to_eat = 2, eat_time = 2, think_time = 2)
p2 = Philosopher(id = 2, waiter = waiter, number_of_times_to_eat = 3, eat_time = 3, think_time = 5)
p3 = Philosopher(id = 3, waiter = waiter, number_of_times_to_eat = 1, eat_time = 1, think_time = 2)
p4 = Philosopher(id = 4, waiter = waiter, number_of_times_to_eat = 2, eat_time = 5, think_time = 2)

philosophers = [p0, p1, p2, p3, p4]
waiter.register_philosophers(philosophers)
waiter.start_dinner()