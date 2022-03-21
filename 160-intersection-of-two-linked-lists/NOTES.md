https://www.youtube.com/watch?v=D0X0BONOQhI
Naive Approach:
1. Traverse a Linked list and store each node in a dictionary
2. Next traverse the second linked list and check if the node is present in dictoinary of first linked list
3. Return the node if it is present else None
​
Algorithm:
1. Traverse Both Linked List to find the length
2. subract both length
3. now increment the bigger linked list by the difference
4. now increment both the linked list and check if they are same
5. if they are same return the node or else none
​
Optimised Algorithm:
1. Instead of finding the length, iterate the whole linked list, if it reaches the end then jump to head of other linked list
2. DO the same for other linked list