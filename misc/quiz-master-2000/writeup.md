QUIZ MASTER 2000

This challenges is a network based challenge that requires students to perform a brute force guessing game.

To run this challenge use the command:
    python3 QuizMaster2000.py

The challengers must connect to the game over a socket.
They can do this by using the command:
    nc {IP} 4446

The game will ask them to guess a series of 4 numbers between 0 and 100
If they guess wrong the connection will close.
For students to solve this task they must code a brute force script that tries all numbers between 0 and 100 and remembers correct guesses.

The QuizMaster2000.py is a socket server and can handle many different connections at the same time.

SOLUTION

The solution is contained within the QuizMaster2000_Solve.py file. Simply run this in a different terminal to perform the brute force attack. 

FLAG
CBACTF{brut4l_f0rce}



