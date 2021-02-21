class Solution:
    def intersect(self, nums1, nums2):
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        i, j = 0, 0
        RET = []
        while i <= len(nums1)-1 and j <= len(nums2)-1:
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                RET.append(nums1[i])
                i += 1
                j += 1
        return RET
n1, n2 = [1,3,4,2], [2,1]
s = Solution()
s.intersect(n1, n2)