Given an array arr of n integers, for each index i, find the length of the longest odd length subsequence of the array such that arr[i] is the median of the array and the number of distinct elements in the subsequence less than arr[i] is equal to the number of distinct elements in the subsequence greater than arr[i]. \
Note: A subsequence of an array is defined as an array obtained after deleting zero or more elements of the given array. Also, the median of an array with an odd number of elements is defined as the middle element obtained when the array is sorted. \
\
Example \
Suppose n = 8 and arr = [3, 4, 1, 5, 1, 2, 2, 2].
* For 3, the optimal subsequence is [3, 4, 1, 5, 2] which has a median of 3.
* For 4, the optimal subsequence is [3, 4, 5] which has a median of 5.
* For 1, the optimal subsequence is [1]. Note that [1, 1] can not be chosen as the subsequence must be of odd length.
* For 5, the optimal subsequence is [5].
* For 2, the optimal subsequence is [3, 1, 1, 2, 2]. \
  \
Thus the answer is [5, 3, 1, 1, 1, 5, 5, 5].

Constraints
* 1≤n≤105
* 1≤arr[i]≤109 \
\
### Sample Case 
Input: arr[] = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6]  \
Output:  
1
5
5
7
11
11
11
7
3
3
3
3  

### Explanation
For 1 the optimal subsequence is [1]. For 2, the optimal subsequence is [1, 2, 2, 3, 4]. For 3, the optimal subsequence is [1, 2, 2, 3, 4, 5, 6]. Note that [1, 2, 2, 3, 4, 4, 4] is not a valid subsequence as the distinct number of elements less than 3 i.e. 2 is not equal to that greater than 3 i.e.1.
For 4 the optimal subsequence is [1, 2, 2, 4, 4, 4, 5, 6, 6, 6, 6]. Note that the entire array is not a valid subsequence for 4 as the number of distinct elements less than 4 is 3 but that greater than 4 is only 2. For 5 the optimal subsequence is [4, 5, 6]. For 6 the optimal subsequence is [6, 6, 6].
