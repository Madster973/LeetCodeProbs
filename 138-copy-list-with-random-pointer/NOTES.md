https://www.youtube.com/watch?v=4apaOcK586U
Naive:
1. Make a dictionary which contains the copy of all the nodes
2. Loop through the link list and assign the next and random pointers in the copy
​
Here we are using O(n) extra space. Below algorithm uses optimised approach and does not occupy extra space
Optimised:
1.Traverse through the LinkedList and make a each duplicate node and assign the currents'next pointer to duplicate node's pointer and duplicate node's next pointer to currents' actual next pointer
2. After that traverse through the Linked List and assign the random pointers:
*       If current.random = null then current.next.random = null
*      If current.next.random = current.random.next
3. After that again traverse the Linked List and assign the next pointers:
*       current.next = current.next.next