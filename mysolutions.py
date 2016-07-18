# Algorithmic Complexity

## Big O Questions

Determine the "Big O" for the problems below:

1. double each number in an array of n numbers.
2. given a number between 0 to 6, return Sunday for 0, Monday for 1, Tuesday for 2, Wednesday for 3, Thursday for 4, Friday for 5, and Saturday for 6.
3. find the result of multiplying each number in an array of n numbers.
4. calculate the multiplication table for the numbers between 0 to n.
5. given an array of basketball players that are sorted by average points per game, find the player who scored exactly 10 points per game, if he exists.
6. find the player in an array whose first name is "LeBron".


# Big O-  Solutions

# 1. double each number
arr = [2,3, 5]
newarr = [4, 9, 25]
the num of times of processes will be according to the length of the array
O(n)

2. arr = [0,1,2,3,4,5,6]
    the process will evaluate once for 0
    the process will evaluate once for 1
    the process will evaluate once for 2 and so on..

the number of processes = no. of days provided to be evaluated
O(1)
# We don't write O(7),we treat it a s a constant,  it will be amongst the list
O(1)
O(log n)
O(n)
O(n log n)
O(n ^ 2)

3. multiplying each num with the array of numbers
arr1 = [2,3,4]
arr2 = [5, 6, 7]
result = n * n
result = [10, 12, 14, 15,18, 21, 20, 24, 28]

O(n^2)

if arr1 = [2,3,4]
arr2 = [5, 6, 7,7 , 8, 6]
result = n * m
O(n * m)

3. multiplying each num in an array of n numbers

[2, 3, 4, 5, 6, 7, 8]
 We keep going multiplying each number starting from the beginning
 if the lenght is 7 then the process will be executed 6 times
 O(n)

4. Multiplication table between 0 to n

1 table will process for n times = 1 * n
2 table will process for n times = 2 * n
n table will process for n times = n * n

O(n * n) = n^ 2

5. Average points:

arr = [
    {
        name: LeBron,
        avg points: 10
    },
    {
        name: Max,
        avg points: 20
    },
    {
        name: Lee,
        avg points: 30
    }
    ]
 The loop will run through all(n) the elements and check each object's average points is more than 10 .

 O(log n)- binary search

6.  First name:
The loop will run through all(n) the elements and check each object's first name = Lebron
not sorted: O(n)
sorted :O(log n) -binary search by sorting alphabetically
