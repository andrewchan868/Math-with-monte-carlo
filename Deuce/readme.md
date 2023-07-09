# Deuce_match

Original Question: 
Two players are at deuce in a tennis match - player 1 has 60% of winning the point, player 2 has 40% chance. What are the odds of player 1 winning?

Mathematically, we could treat this question as an recursive problem:

Assuming p as the probability of player 1 winning
p = 0.60^2 + 2*0.60*0.40*p
p = 0.6923076923
