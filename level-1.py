'''
Google FooBar Challenge

Level 1
Question 1 : Re-ID

There’s some unrest in the minion ranks: minions with ID numbers like “1”, “42”, and other “good” numbers have been lording it over the poor minions who are stuck with more boring IDs. 
To quell the unrest, Commander Lambda has tasked
you with reassigning everyone new random IDs based on a Completely Foolproof Scheme.
Commander Lambda has concatenated the prime numbers in a single long string: “2357111317192329…”. 
Now every minion must draw a number from a hat. That number is the starting index in that string of primes, and the minion’s new ID number will be the next five digits in the string. 
So if a minion draws “3”, their ID number will be “71113”.

Help the Commander assign these IDs by writing a function solution(n) which takes in the starting index n of Lambda’s string of all primes, and returns the next five digits in the string. 
Commander Lambda has a lot of minions, so the value of n will always be between 0 and 10000.

— Test cases —

Input:
Solution.solution(0)
Output:
23571

Input:
Solution.solution(3)
Output:
71113
'''


def solution(i):
    prime_str = '23'
    if i < 10: 
    	endNum = i+30
    else: 
    	endNum = i*3

    for isPrime in range(5, endNum, 2):
        tester = False
        for div in range(3, isPrime, 2):
            if isPrime%div == 0:
                tester = True
                break
        if tester == False:
            prime_str += str(isPrime)
        if len(prime_str) >= 10006:
            break
    return prime_str[i:i+5:]


#from timeit import default_timer as timer

#start = timer()
print(solution(5))
#end = timer()
#print((end - start)*1000, 'ms')
