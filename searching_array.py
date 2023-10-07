# Searching an element in a sorted array is present or not
import math

class Solution:
    def searchInSorted(self,arr, N, K):
        for i in range(N):
            if(arr[i] == K):
                return 1
        return -1

if __name__=='__main__':
  t= int(input())
  for _ in range(t):
    NK = input().strip().split()
    N = int(NK[0])
    K = int(NK[1])
    A = [ int(x) for x in input().strip().split() ]
    ob = Solution()
    print(ob.searchInSorted(A,N,K))
