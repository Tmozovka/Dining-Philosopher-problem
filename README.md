# Dining Philosopher problem

This repository represents a solution with a monitor pattern to the Dining Philosopher Problem.
The Dining Philosopher Problem states that K philosophers seated around a circular table with one chopstick between each pair of philosophers. There is one chopstick between each philosopher. A philosopher may eat if he can pick up the two chopsticks adjacent to him. One chopstick may be picked up by anyone of its adjacent followers but not both.

## Monitor based solution

### Structure description

#### Philosopher 

There are four states of philosopher: THINKING, HUNGRY, EATING and END.
States THINKING, HUNGRY and EATING change one after another until the philosopher gets enough. If the philosopher is full, then he goes into the END state. 
A philosopher needs to eat n times to become full. 

#### Waiter (Monitor)

The waiter is responsible for dinner. He opens a restaurant and waits for philosophers to register for dinner. When all the philosophers are ready, the waiter allows them to start dinner. To start eating, philosophers ask permission from the waiter.

### Solution

1) A philosopher wants to eat and he asks for permission from the monitor(waiter)
2) Waiter checks if both neighbors of the philosopher are not eating
  1. yes -> allow to eat. His neighbors must wait if they want to eat
  2. no -> wait

The solution is created with the help of condition variables and locks, that are implicit in the waiter-monitor

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

