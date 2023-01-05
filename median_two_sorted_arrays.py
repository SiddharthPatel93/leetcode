from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)==0:
            if len(nums2)%2==1:
                med_index = len(nums2)//2
                return nums2[med_index]
            else:
                med_index = len(nums2)/2
                num1=nums2[med_index-1]
                num2=nums2[med_index]
                return ((num1+num2)/2)
        if len(nums2)==0:
            if len(nums1)%2==1:
                med_index = len(nums1)//2
                return nums1[med_index]
            else:
                med_index = len(nums1)/2
                num1=nums1[med_index-1]
                num2=nums1[med_index]
                return ((num1+num2)/2)
        med=0;
        index1=0
        index2=0
        arr_1_length = len(nums1)
        arr_2_length = len(nums2)
        total = arr_1_length + arr_2_length
        if total%2==1:
            med_index = total//2
            index=0
            while index !=med_index+1:
                if nums1[index1]<nums2[index2]:
                    if index==med_index:
                        return nums1[index1]
                    else:
                        index1+=1
                    
                else:
                    if index==med_index:
                        return nums2[index2]
                    else:
                        index2+=1                    
                index+=1
        else:
            med_index = total/2
            val1 =0
            val2=0
            index=0
            while index !=med_index+1:
                if nums1[index1]<nums2[index2] and index1<len(nums1)-1:
                    if index==med_index-1:
                        val1= nums1[index1]
                    elif index==med_index:
                        val2=nums1[index1]
                        return (val1+val2)/2
                    if index1<len(nums1)-1:
                        index1+=1      
                else: 
                    if index==med_index-1:
                        val1= nums2[index2]
                    elif index==med_index:
                        val2 = nums2[index2]
                        return (val1+val2)/2
                    if index2<len(nums2)-1:
                        index2+=1                    
                index+=1

arr1= [1,2]
arr2=[3,4]
x=Solution()
print(x.findMedianSortedArrays(arr1,arr2))