# %%
names = {"firstname" : "Andy", "lastname": "Smith"}
print("Welcome {firstname} {lastname} to our shop!".format(**names))

# %%

def foo(s):
    if len(s)<3:
        return s
    elif s[-3:]=='ing':
        return s+'ly'
    else:
        return s+'ing'

def removedup(arr):
    l=0
    res=[]
    for r in range(len(arr)):
        res.append(arr[r])
        if arr[r]==arr[l] and r-l>2:
            res.pop()
            l+=1
    return len(res)

def twosum(arr,target):

    l=0
    r=len(arr)-1
    while l<=r:
        if arr[l]+arr[r]>target:
            r-=1
        elif arr[l]+arr[r]<target:
            l+=1
        else:
            return (l,r)

    return 

# three sum
    
def threesum(arr,target):
    if not arr or not target:
        return None
    
    result=[]

    arr.sort()

    for i in range(len(arr)):

        if i>0 and arr[i]==arr[i-1]:
            continue

        l=i+1
        r=len(arr)-1

        while l<r:

            if arr[i]+arr[l]+arr[r]<target:
                l+=1
            elif arr[i]+arr[l]+arr[r]>target:
                r-=1
            else:
                result.append([result[i],result[l],result[r]])
                l+=1
                r-=1
                while arr[l]==arr[l-1] and l<r:
                    l+=1

# Valid Palindrome

def ispalindrome(s):

    if not s:
        return True
    
    l=0
    r=len(s)-1

    while l<r:

        while not s[l].isalnum:
            l+=1
        
        while not s[r].isalnum:
            r-=1

        if s[l].lower()!=s[r].lower():
            return False
        
        l+=1
        r-=1
    
    return True

# Container with most water

def maxwater(height:list):
    if not height:
        return None
    
    maxwater=0

    l=0
    r=len(height)-1

    while l<r:

        w=r-l
        h=min(height[r],height[l])
        area=w*h

        maxwater=max(maxwater,area)

        if height[l]<height[r]:
            l+=1
        else:
            r-=1

    return maxwater
        
# Best time to buy and sell stock

def maxprofit(prices:list):

    if not prices:
        return None
    
    l=0
    lowest=prices[0]
    maxprofit=0

    for i in prices:
        if i<lowest:
            lowest=i
        maxprofit=max(maxprofit,i-lowest)

    return maxprofit
        
# Longest substring without repeating character:

def longestsubstr(s:str):
    if not s:
        return None
    
    maxlen=1
    
    l=0

    visited=[s[0]]

    for r in range(1,len(s)):

        if s[r] in visited:
            visited.remove(s[l])
            l+=1

        visited.append(s[r])
        maxlen=max(maxlen,r-l+1)
        
    return maxlen

# Longest repeating character replacement

def replacestr(s:str,k:int):
    if not s or not k:
        return None
    
    strcount={}

    l=0

    longstr=1

    for r in range(len(s)):

        strcount[s[i]]=1+strcount.get(s[i],0)
        max=max(strcount.values())

        if r-l+1>k:
            strcount[s[l]]-=1
            l+=1

        longstr=max(longstr,r-l+1)

    return longstr

# Minimum string
            
def minwindow(s,t):
    if not s or not t:
        return None
    if len(s)<len(t):
        return ""
    
    countT={}
    countS={}

    for i in t:
        countT[t]=1+countT.get(t,0)

    match_need=len(countT)

    minwindow=0

    l=0
    for r in range(len(s)):

        if s[r] in countT:
            countS[s[r]]=1+countS.get(s[r],0)
            if countS[s[r]]>=countT[s[r]]:
                match+=1
        else:
            continue


# Valid Parentheses

def validparent(s:str):

    if not s:
        return None
    
    map={')':'(','}':'{',']':'['}

    result=[]

    for i in s:
        if i not in map:
            result.append(i)
            continue

        if not result or map[i]!=result.pop():
            return False
        
        result.pop()
        
    return not result

class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)==1 or len(s)==0:
            return False

        map={'(':')','{':'}','[':']'}

        result=[]

        for i in range(len(s)):
            if s[i] in map:
                result.append(s[i])
            elif i==0 and s[i] not in map:
                return False
            elif i!=0 and not result and s[i] not in map:
                return False
            elif i!=0 and len(result)!=0 and map[result[-1]]!=s[i]:
                return False            
            elif i!=0 and len(result)!=0 and map[result[-1]]==s[i]:
                result.pop()   

        return not result
    
# Valid Palindrome

def valid(s:str):

    l=0
    r=len(s)-1

    while l<r:

        while not s[l].isalnum:
            l+=1
        while not s[r].isalnum:
            r-=1
        
        if s[l].lower()!=s[r].lower():
            return False
        
        l+=1
        r-=1
        
    return True

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        rows=len(image)
        cols=len(image[0])

        def dfs(r,c):

            if (
            r>=rows 
            or c>=cols 
            or r<0 
            or c<0
            or image[r][c]!=image[sr][sc] 
            or image[r][c]==color
            ):
                return

            image[r][c]=color

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        dfs(sr,sc)

        return image
    
# Three sum

def threesum(nums:list):
    if not nums:
        return []
    
    nums.sort()

    result=[]

    for i in range(len(nums)):

        if nums[0]>0:
            break

        if i>0 and nums[i]==nums[i-1]:
            continue

        l=i+1
        r=len(nums)-1
        
        while l<r:

            if nums[i]+nums[l]+nums[r]>0:
                r-=1
            elif nums[i]+nums[l]+nums[r]<0:
                l+=1
            else:
                result.append([nums[i],nums[l],nums[r]])
                l+=1
                r-=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1

    return result
                
# Container with Most Water

def mostwater(height:list):

    if not height:
        return None
    
    l=0
    r=len(height)-1

    maxarea=0

    while l<r:

        w=r-l+1
        h=min(height[l],height[r])
        currentarea=w*h

        maxarea=max(maxarea,currentarea)

        if height[l]<height[r]:
            l+=1
        else:
            r-=1

    return maxarea

#Best time to buy stock
def maxprofit(prices:list):

    low=prices[0]

    maxprofit=0

    for p in prices:
        if p<low:
            low=p
        maxprofit=max(maxprofit,p-low)

    return maxprofit

# Longest substring without repeating characters

def longeststr(s:str):

    if not s:
        return None
    
    if len(s)==1:
        return s
    
    maxlen=1
    l=0
    substr=set()
    
    for r in range(0,len(s)):

        while s[r] in substr:
            substr.remove(s[l])
            l+=1

        strlen=r-l+1
        maxlen=max(maxlen,strlen)
        substr.add(s[r])

    return maxlen

# Longest repeating character replacement

def charreplace(s:str,k=2):

    if not s:
        return None
    
    if len(s)==1:
        return 1
    
    countS={}

    l=0

    maxlen=1

    for r in range(0,len(s)):

        countS[s[r]]=1+countS.get(s[r],0)
        maxcount=max(countS.values())

        if r-l+1-maxcount>k:
            countS[s[l]]-=1
            l+=1

        maxlen=max(maxlen,r-l+1)

    return maxlen
        
# Valid Parentheses

def valid(s:str):

    map={")":"(","}":"{","]":"["}

    stack=[]

    for i in s:
        if s not in map:
            stack.append(s)
            continue

        if not stack or stack[-1]!=map[i]:
            return False
        
        stack.pop()

    return True

# findmin in a rotated array

def findmin(nums:list):

    l=0
    r=len(nums)-1
    currmin=float('inf')

    while l<=r:
        m=(l+r)//2
        currmin=min(currmin,nums[m])

    if nums[m]>nums[r]:
        l=m+1
    else:
        r=m-1

    return min(currmin,nums[l])
        
# Sort a list after a formula

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def quadratic(x):
            return a*x**2 + b*x + c 
        n = len(nums)
        index = 0 if a < 0 else n-1
        l, r, ans = 0, n-1, [0] * n
        while l <= r:
            l_val, r_val = quadratic(nums[l]), quadratic(nums[r])
            if a >= 0:
                if l_val > r_val:
                    ans[index] = l_val 
                    l += 1
                else:    
                    ans[index] = r_val 
                    r -= 1
                index -= 1
            else:
                if l_val > r_val:
                    ans[index] = r_val 
                    r -= 1
                else:    
                    ans[index] = l_val 
                    l += 1
                index += 1
        return ans
        
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        M = 1440
        times = [False] * M
        for time in timePoints:
            minute = self.minute(time)
            if times[minute]:
                return 0
            times[minute] = True
        
        minutes = [i for i in range(M) if times[i]]
        return min((minutes[i] - minutes[i-1]) % M for i in range(len(minutes)))
        
    def minute(self, time: str) -> int:
        h, m = map(int, time.split(':'))
        return 60*h + m
    
def longestStrChain(self, words: List[str]) -> int:
    
    words.sort(key=len)
    dic = {}
    
    for i in words:
        dic[ i ] = 1
        
        for j in range(len(i)):
            
            # creating words by deleting a letter
            successor = i[:j] + i[j+1:]
            if successor in dic:
                dic[ i ] = max (dic[i], 1 + dic[successor])
    
    res = max(dic.values())
    return res

### Backtracking ###

def subsets(nums:list):

    if not nums:
        return None
    
    res=[]

    subset=[]

    def backtrack(i):

        if i>=len(nums):
            res.append(subset.copy())
            return res
        
        subset.append(nums[i])
        backtrack(i+1)

        subset.pop()
        backtrack(i+1)

    backtrack(0)

    return res

# combination sum

def combsum(candidates:list,target:int):

    if not candidates or not target:
        return None
    
    res=[]

    subset=[]

    def backtrack(i,total):

        if total==target:
            res.append(subset.copy())
            return
        
        if i>=len(candidates) or total>target:
            return
        
        subset.append(candidates[i])
        backtrack(i,total+candidates[i])

        subset.pop()
        backtrack(i+1,total)

    backtrack(0,0)

    return res

# Permutations

def perm(nums:list):

    res=[]

    if len(nums)==1:
        return [nums.copy()]

    for i in range(len(nums)):
        n=nums.pop(0)
        perms=self.perm(nums)

        for perm in perms:
            perm.append(n)
            res.append(perm)

        nums.append(n)

    return res

## Subset with duplicates

def subset2(nums:list):

    res=[]
    nums.sort()

    subset=[]

    def backtrack(i):

        if i>=len(nums):
            res.append(subset[::])
            return
        
        subset.append(nums[i])
        backtrack(i+1)
        subset.pop()

        while i+1<len(nums) and nums[i]==nums[i+1]:
            i+=1

        backtrack(0)

    return res

## Combination Sum II

def combsum2(nums:list, target:int):

    if not nums or not target:
        return None
    
    res=[]
    subset=[]

    nums.sort()

    def backtrack(pos,total):
        if total==target:
            res.append(subset.copy())
            return

        if i>=len(nums) or total>target:
            return
        
        #prev=-1
        for i in range(pos,len(nums)):
            if i>0 and nums[i]==prev:
                continue
            subset.append(nums[i])
            backtrack(i+1,total+nums[i])
            subset.pop()

            prev=nums[i]

    backtrack(0,0)
    return res

## Palindrome partition

def partition(s:str):

    if not s:
        return None
    
    res=[]
    subset=[]

    def backtrack(i):
        
        if pos>=len(s):
            res.append(subset.copy)
            return
        
        for j in range(i,len(s)):
            if self.palidrom(s,i,j):
                subset.append(s[i,j+1])
                backtrack(j+1)
                subset.pop()

    backtrack(0)

    return res

def palidrom(s,l,r):
    
    while l<r:
        if s[l]!=s[r]:
            return False
        l+=1
        r-=1
    return True

## letter combinations

def lettercomb(digits:str):

    if not digits:
        return None
    
    digitToChar = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "qprs",
        "8": "tuv",
        "9": "wxyz",
    }
    
    res=[]
    subset=[]
    
    def backtrack(i,curstr):

        if len(curstr)==len(digits):
            res.append(curstr[::])
            return
        
        for c in digitToChar[digits[i]]:
            backtrack(i+1,curstr+c)
        
    backtrack(0,'')

    return res

def shortestWay(self, source: str, target: str) -> int:
    for t in target:
        if not t in source:
            return -1
    
    result = 1
    i, j = 0, 0
    
    while i < len(target):
        if j >= len(source):
            j = 0
            result += 1
        if target[i] == source[j]:
            i += 1
        j += 1
        
    return result

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        i, minimum = 0, 1
        
        for c in target:
            
			# Get leftmost char after previously matched index
            i = source.find(c, i)

			# If not found
            if i == -1:
                
				# Get leftmost char from begining of string and increase number of concatenated string
                i = source.find(c)
                minimum += 1
                
				# if not found, then target can't be formed. Return -1
                if i == -1:
                    return i
                
            i += 1
                
        return minimum

### Compare Strings    
def compstrs(str1:str,str2:str):
    if not str1 or not str2:
        return None
    
    str2d={}
    str1d={}
    
    import collections
    
    for s in str2.split(' '):
        count=collections.Counter(s)
        str2d[s]=max(count.values())

    for s in str1.split(' '):
        count=collections.Counter(s)
        str1d[s]=max(count.values())

    res=[]
    countn=0
    for v2 in str2d.values():
        for v1 in str1d.values():
            if v2>v1:
                countn+=1
        res.append(countn)
        countn=0
    return res
        
## Largest Subarray

def subarray(arr,k):

    res=[]

    for n in arr:

        if n-1 in arr:
            continue
        else:
            res.append(n)
            length=1
            while n+1 in arr:
                length+=1
                res.append(n+1)
                if length==k:
                    return res

# Minimum number of decreasing subsequence partitions                
def min_decreasing_partitions(arr: List[int]) -> int:
    ends = []
    for x in arr:
        i = bisect_right(ends, x)
        print(i)
        print(ends)
        if i < len(ends):
            ends[i] = x
        else:
            ends.append(x)

    print(ends)
    return len(ends)

# Maximum Subarray

def maxsubarray(nums:list):

    if len(nums)==1:
        return nums[0]

    maxsum=nums[0]
    currsum=0

    for n in nums:
        if currsum<0:
            currsum=0
        currsum+=n
        maxsum=max(maxsum,currsum)

    return maxsum

# Longest Palindromic Substring

def longestpalindrom(s:str):

    res=''
    reslen=0

    for i in range(len(s)):
        

        ## Odd palidrom
        l=r=i
        while l>=0 and r<=len(s)-1 and s[l]==s[r]:
            if r-l+1>reslen:
                res=s[l:r+1]
                reslen=r-l+1
            l-=1
            r+=1

        ## Even palidrom
        l=i
        r=i+1
        while l>=0 and r<=len(s)-1 and s[l]==s[r]:
            if r-l+1>reslen:
                res=s[l:r+1]
                reslen=r-l+1

            l-=1
            r+=1

    return res
        
## return a list of Palindrom substrings
class Solution():
    def palindromstr(self,s:str):

        if not s:
            return None
        
        res=0
        
        for i in range(len(s)):

            # Odd palindrom

            res+=self.countPalindrom(s,i,i)

            # Even palindrom
            res+=self.countPalindrom(s,i,i+1)

    def countPlindrom(self,s,l,r):
        
        res=0
        while l>=0 and r<len(s) and s[l]==s[r]:
            res+=1
            l-=1
            r+=1

        return res
    
# Count majority element with o(n) and boyer moore algorithm

def majority(nums):

    res,count=0,0

    for n in nums:
        if count==0:
            res=n
        count+=(1 if n==res else -1)

    return res

# Next Greater Element using stack

def nextgeelement(nums1,nums2):

    nums1index={v:i for i,v in enumerate(nums1)}
    res=[-1]*len(nums1index)

    stack=[]

    for n in nums2:
        while stack and n>stack[-1]:
            val=stack.pop()
            res[nums1index[val]]=n
        if n in nums1:
            stack.append(n)

    return res

# find pivot index

def pivotindex(nums):

    totalsum=sum(nums)

    leftsum=0

    for i in range(len(nums)):

        rightsum=totalsum-nums[i]-leftsum

        if rightsum==leftsum:
            return i
        
        leftsum+=nums[i]

    return -1

# Replace elements with greatest element on right side

class solution:

    def rightmax(arr:list):

        if not arr:
            return None
        
        maxval=-1

        res=[0]*len(arr)

        for i in range(len(arr)-1,-1,-1):

            res[i]=maxval
            maxval=max(maxval,arr[i])

        return res
    
# Is subsequence
def subseq(s1,s2):

    i=0
    j=0

    while j<len(s2):

        if s1[i]==s2[j]:
            i+=1
            res+=1

        if i==len(s1):
            i=0

        j+=1

    return True if res==len(s1) else False