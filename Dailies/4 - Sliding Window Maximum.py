# Day 4, Aug 16, https://leetcode.com/problems/sliding-window-maximum/

from collections import deque


def maxSlidingWindow(nums, k):
    q = deque()  # stores *indices*
    res = []
    for i, cur in enumerate(nums):
        while q and nums[q[-1]] <= cur:
            q.pop()
        q.append(i)
        # remove first element if it's outside the window
        if q[0] == i - k:
            q.popleft()
        # if window has k elements add to results (first k-1 windows have < k elements because we start from empty window and add 1 element each iteration)
        if i >= k - 1:
            res.append(nums[q[0]])
    return res
