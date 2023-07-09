We are solving the below problem:

We are taking n steps, each step in the direction of either east, south, west, or north, chosen randomly. 
It is given that if we are more than 4 blocks away from our starting point, we would need to take a transport in the end.

What is the longest random walk you can take so that on average you will end up 4 blocks or fewer from home.


It is shown that even numbers of walks would get you closer to the starting point in the end. 
Explanation as follows:

Since the direction of the steps is evenly distributed, in the even case, we can expect the number of steps going up to be the same to those going down. 
But in the odd case, we can expect the number of steps in one direction to be one larger than the other, leading us further away from the origin. 
The same is true for the left/right dimension. This phenomenon should be less and less noticeable, as we increase the number of steps.
