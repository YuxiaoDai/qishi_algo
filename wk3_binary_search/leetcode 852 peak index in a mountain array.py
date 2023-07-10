class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (r - l)//2 + l
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid-1] > arr[mid] and arr[mid] > arr[mid + 1]:
                r = mid - 1
            else:
                l = mid + 1