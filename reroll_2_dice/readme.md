# Two-dice-with-n-re-roll

In this simulation, we are solving the following question:
Roll two dice, and you have a chance to reroll 1 dice if you want. Sum up the numbers of the two dice, what is the probability of each situation, and what is the expected number under that situation?

The EV for one dice is 3.5.
Therefore, if one of the dice has a value of less than 3.5, which is 1-3, we would re-roll the dice.


<img width="321" alt="EV map" src="https://github.com/andrewchan868/Math-with-monte-carlo/assets/66477660/ab9db236-1352-4284-90d4-243bc38d0f67">

For 2 dice, 

if both of them are less than 4, we will reroll the lower one 

if one has a value higher than 3.5 and another has a value lower than 3.5, we will reroll the one with the value of lower than 3.5

if both of them are more than than 3.5, we will not reroll
