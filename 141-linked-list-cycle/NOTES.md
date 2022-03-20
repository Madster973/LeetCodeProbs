https://leetcode.com/problems/linked-list-cycle/discuss/823960/two-approaches-in-Python-3%3A-dictionary-and-two-pointers
Naive Approach:
It is similar to that of detecting duplicate in an array by using hashmap(dictionary in python)
​
Floyd detection algorithm:
https://www.youtube.com/watch?v=jcZtMh_jov0
It is similar to tortoise and hare approach.
slow pointer moves by 1 step and fast pointer moves by 2 steps. If there is a loop then both slow and fast would meet.
To get the starting of the loop after detecting the loop assign a temp position to the pointer and assign another dummy position to the head of the linked list. Increment them by 1 by 1 they would meet at the starting of the loop