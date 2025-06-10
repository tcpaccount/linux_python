'''
A little girl counts from 1 to M using the fingers of her left hand as follows. She starts by calling her thumb 1, index finger 2, middle finger 3, ring finger 4, and little finger 5. Then she reverses direction, calling ring finger 6, middle finger 7, index finger 8, and her thumb 9, after which she calls her index finger 10, and so on. If she continues to count in this manner, on which finger will she stop?
Input
Line 1: The number M the girl counts up to.
Output
Line 1: The finger on which the little girl stops: thumb, index, middle, ring or little.
Constraints
0 < M < 10^9
Example
Input
1
Output
thumb
2
index

4
ring

7
middle

9
thumb

15
middle

'''
m = int(input())
# generate dictionary via merging two lists with help of zip function
my_dict = dict(zip(range(1,9), "thumb index middle ring little ring middle index".split()))
print(my_dict[m % 8])
