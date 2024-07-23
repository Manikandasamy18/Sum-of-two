class Soluction:
    def twoSum(self,nums,target):
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []

if __name__=="__main__":
    try:
        nums=input("Enter a list: ")
        target=int(input('Enter a target: '))
        nums=list(map(int,nums.split()))
        soluction=Soluction()
        result=soluction.twoSum(nums,target)
        print("Indices value: ",result)
    except ValueError:
        print("Enter vaild Number")


