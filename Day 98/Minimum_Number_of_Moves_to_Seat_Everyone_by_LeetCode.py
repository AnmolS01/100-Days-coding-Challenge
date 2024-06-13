class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        n = len(seats)
        seats.sort() #[1,3,5]
        students.sort() # [2,4,7]

        count = 0
        for i in range(n):
            count += abs(seats[i]-students[i])
        return count
