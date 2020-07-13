# AlphaZeroTicTacToe
An AlphaZero approach to the tic tac toe game. The program allows the player to compete against the program.This program implements pure monte carlo tree search with a number of random playouts to create the best tile to play.


 Pure MCTS is a greedy algorithm, choosing the optimal solution at a given state. 

 Due to the random nature of random playouts, a 100% guranatee of winning is not possible without other game logic.
 The issue with pure MCTS on a tic tac toe game is the program cannot account for a state which is unwinnable.

 A state is unwinnable if the player has two options to win with one move. The robot can only block one option.
 When the robot encounters such state during its playouts, the robot will not determine or compensate for the unwinnalbe state.

 Due to the restrictions of our assignment (pure MCTS), there is 1 case where the player can win (given the player goes first).

 In my testings, I have the player go first because this gives a big disadvantage to the robot.
 

 Case 1) 
 1. The player places a x on any corner. The robot will place an o in the center.
 2. The player places an x in the opposite corner of the first x. 
 3. If the robot places the next o in any 2 corners, the robot has lost.
 4. The player will place an x in the last remaining corner to create an unwinnable state for the robot.
 
 This unwinnable state is preventable by having the robot place an o in a non-corner tile during its first turn by changing wieghts.
 But the change of weights have led to other unwinnable states

##WEIGHTS USED
 number of playouts = 1000
 playerWin = -2
 robotWin = +2
 Draw = +1
 x = player
 o = robot
 
I chose 1000 to be my number of playouts because the only case where it loses is the Case 1 shown below.
Playouts less than 1000 have also resulted in DIFFERENT unwinnable states.
More playouts creates a more even distribution to the possible playout states.

Player and Robot to having the same weight was a good heurisitic for my program. 
Draw was set to 2 because we want the program to at least draw (never lose).
