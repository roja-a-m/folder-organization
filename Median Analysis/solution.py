import heapq
def getMaxSubsequenceLen (arr):
    n, freq, K = len(arr), {}, {}
    for i in arr:
        freq[i] = 1 if i not in freq else freq[i] + 1
    sorted_arr = sorted(set(arr))
    for idx, x in enumerate(sorted_arr):
        num_smaller_than_x = idx
        num_greater_than_x = len(sorted_arr) - idx - 1
        K[x] = min(num_smaller_than_x, num_greater_than_x)
    sum_of_elements_smaller_than_x, min_heap, total_sum = {}, [], 0
    for x in sorted_arr:
        # Case when number of elements less than x is more than the number of elements greater than x
        if len(min_heap) <= K[x]:
            sum_of_elements_smaller_than_x[x] = total_sum
        # Case when number of elements less than x is less than the number of elements greater than x
        else:
            while len(min_heap) != K[x]:
                total_sum -= abs(heapq.heappop(min_heap))
            sum_of_elements_smaller_than_x[x] = total_sum
        heapq.heappush(min_heap, freq[x])
        total_sum += freq[x]
    # Pre computing the sum of K largest frequencies of numbers smaller than x
    sum_of_elements_greater_than_x, min_heap, total_sum = {}, [], 0
    for x in reversed(sorted_arr):
        # Case when number of elements less than x is more than the number of elements greater than x
        if len(min_heap) <= K[x]:
            sum_of_elements_greater_than_x[x] = total_sum
        # Case when number of elements less than x is less than the number of elements greater than x
        else:
            while len(min_heap) != K[x]:
                total_sum -= abs(heapq.heappop(min_heap))
            sum_of_elements_greater_than_x[x] = total_sum
        heapq.heappush(min_heap, freq[x])
        total_sum += freq[x]
    ans = {}
    for x in set(arr):
        lower, greater, equal = sum_of_elements_smaller_than_x[x], sum_of_elements_greater_than_x[x], freq[x]
        # Number of elements greater than x in optimal subsequence
        ans[x] = 2 * min(lower, greater) + equal + min(abs(lower - greater), equal)
    return [ans[i] if ans[i] % 2 else ans[i] - 1 for i in arr]