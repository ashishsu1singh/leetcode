class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s=""
        listt=[]
        for i in range(len(digits)):
            s+=str(digits[i])
        x=int(s)+1
        while x!=0:
            digit=x%10
            listt.append(digit)
            x=x//10
        return listt[::-1]   