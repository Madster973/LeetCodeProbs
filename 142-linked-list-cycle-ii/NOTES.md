First use the fast and slow pointer approach to detect the loop.
By using that approach,if the node ends at n then we will always converge at n-1 so we need to move our pointer to next
along with that move the head to head.next too
repeat it till head != fast/slow
they both converge at starting of the loop