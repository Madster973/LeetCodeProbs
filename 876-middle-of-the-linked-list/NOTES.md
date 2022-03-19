Naive Approach:
1. Get the count of the linked_list
2. Check if the count is even or odd:
1. If even -> mid = count/2+1
2. If Odd -> mid = (count+1)/2
3. Loop the Linked List from 1 to mid and do head.next() operation
​
2 pointer approach.
You would be having 2 pointers:
1. Slow pointer
2. Fast Pointer
For every 1 step increment in slow pointer fast pointer moves by 2 increments. So by the time the fast pointer reaches the end of linked list, the slow pointer is in middle element