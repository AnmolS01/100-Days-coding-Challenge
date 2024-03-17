# problem Statement: 57. Insert Interval
# ______________________________________________________________CODE________________________________________________________________________
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        n=len(intervals) 
        result=[]
        i=0
      
        while (i<n and (intervals[i][1] < newInterval[0])):
            result.append(intervals[i])
            i+=1
        while (i<n and (newInterval[1] >= intervals[i][0])):
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i+=1
        result.append(newInterval)
        while (i<n):
            result.append(intervals[i])
            i+=1

        return result

# ___________________________________________________START OF EXPLAINATION______________________________________________________________

# ***************************************************  Lets understand:  ***************************************************************

# step 1:
# while (i<n and (intervals[i][1] < newInterval[0])):
#             result.append(intervals[i])
#             i+=1
# ==> here we check that, 'end' element of intervals is less than 'starting' element of newIntervals. if it satisy the condition
# then we can see that, there is no need changes in the intervals. so we keep that element as it is and add in empty list i.e result=[].
# and move to next intervals

# step 2:
# while (i<n and (newInterval[1] >= intervals[i][0])):
#             newInterval[0] = min(intervals[i][0], newInterval[0])
#             newInterval[1] = max(intervals[i][1], newInterval[1])
#             i+=1
# ==> here we check logic for overlapping
# let say: Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]. so as we can see that 4 is lies in [3,5] intervals
# and 8 is lies in [8,10] intervals. so we need to overlap the newIntervals, so we get [[1,2],[3,10],[12,16]]. it means our new 
# interval [3,10] start from 3 and end at 10. but the question is how??
# but firts understand, we have to find new interval such that it overlaps the interval itself and values which appeared in between 
# that interval[4,8] so we have to find exactly minimum of 4 and exactly max of 8 in old intervals. so we can see that,
# 3 is exactly min of 4 and 10 is exactly max of 8. so we have to find [3,10]

# lets find [3,10] : 
# Answer is: ==> : we compare 'end' of newInterval [4,8] that is 8. and 'start' of intervals [3,5] that is 3 and then compare. 8>=3 yes.
# next : we compare and find 'start' of intervals [3,5] that is 3 and and 'start' of intervals [4,8] that is 3 and compare. min(3,4) 
# we find 3. so we have created newInterval or you can say that existing newInterval, we set 'start' element as 3.
# next: we compare and find 'end' of intervals [3,5] that is 5 and and 'end' of intervals [4,8] that is 8 and compare. max(3,4)
# we find 8. so we set 'end' element as 8.

# so we have newInterval [3,8]. but we can see that end element is still '8' not '10' so we do not add this interval into list.
# and continue for next interval that is [6,7]. so now we caopare [6,7] and [3,8]

# We compare the end of the newInterval ([3,8]) with the start of the next interval ([6,7]). Since 8 is greater than or equal to 6, 
# there is an overlap.
# We compare the start of the next interval ([6,7]) with the start of the newInterval ([3,8]) and choose the minimum value,
# which is 3. So, the start of the newInterval remains unchanged.
# We compare the end of the next interval ([6,7]) with the end of the newInterval ([3,8]) and choose the maximum value,
# which is 8. So, the end of the newInterval remains unchanged.
# Now, the newInterval is still [3,8]. Since its end is still 8, which is not equal to 10, we continue to the next interval.

# The next interval is [8,10]. We compare it with the newInterval [3,8].
# There is an overlap between the end of the newInterval (8) and the start of the next interval (8).
# We update the end of the newInterval to the maximum of its current end (8) and the end of the next interval (10), which becomes 10.
# Now, the newInterval becomes [3,10], covering all the overlapping intervals.

# Since the end of the newInterval is now 10, it satisfies the condition, and we add this merged interval into the list.

# So, the output would be [[1,2], [3,10], [12,16]], as the newInterval [4,8] overlaps with intervals [3,5], [6,7], and [8,10].

# _____________________________________________________________Thank You____________________________________________________________________
