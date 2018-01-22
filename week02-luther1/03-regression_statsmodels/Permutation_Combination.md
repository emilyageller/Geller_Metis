## Permutation

#### With Repetition

How many ways can you fill this _ _ with numbers between 0 and 9 with repetition. It's just all numbers between 0 and 99, which is one hundred.

So how many ways for _ _ _ _ . It's 10000, correct?

So the number of ways we can get r values from N values with repetion is N^r.

#### Without Repetition

How many ways can you fill this _ _ with numbers between 0 and 9 with repetition. It's  all numbers between 0 and 99, except the repeating numbers (0,11,22, etc). That's 100-10=90. Another way to approach: for the first dash, we have 10 options. For the second one, we have only 9 options (since we can repeat). So that give is 10x9=90.

For _ _ _ _ , we have 10x9x8x7=5040.

So the number of ways we can get r values from N values with repetition is Nx(N-1)x(N-2).. and so on up to r values. Which can be written as N!/(N-r)!

nPr = N!/(N-r)!


## Combination

Combination is when the ordering of the results don't matter. We want to pick 4 numbers from 0 to 9 without repetition. So the same _ _ _ _ , but now 1234, 2134, 4213 are all the same.

In that case, we can uncount the various ordering. Order is nothing but permutations. So r choices can be ordered in r! ways. And we'll have to divide by that.

In this case 4! is 24. We have 5040 from above. So 5040/24=210

nCr = N!/((N-r)!r!)


## Challenge 1

There are 10 kids what to order ice cream. Each one can choose between chocolate, vanilla or strawberry. You'll collect their choices and make one order, something like: 5 chocolate, 3 vanilla and 2 strawberry. How many possible orders can you make, where every flavor is represented (8c, 1v, 1s is valid but 8c, 2v, 0s is not valid)?

Answer #1: If you write it out possibilities, chocolate can be between 8 to 1. If chocolate is 8, there is only option for vanilla, which is 1. If chocolate is 7, there are two options for vanilla (1 or 2), and so on. We can sum up those options, 1+2+3...+8, which is 8x9/2=36.

Answer #2: You want two dividers between 1 and 10 to split the orders. The first block will be chocolate, the second vanilla and third strawberry. There are 9 gaps (between 1 and 10). The order of the two choices doesn't matter. So it's 9C2, which is 9x8/2 = 36.


## Challenge 2

Revisit the problem from the application:

Six individuals are sitting in a circle. I have six cards, three red and three blue. If I randomly had each one a card, what is the probability that the colors would perfectly alternate, that is no two adjacent person has the same color?

Answer: What the first person (player 0) gets doesn't matter. The color he got, there are 2 more left and we have to choose 2 from the other 5 to get that color. That's 5C2 = 5x4/2 = 10. Of those ten, only one suits our need: player 2 and 4 getting that color. So the probability is 1/10 = 0.1.
