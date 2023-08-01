# %%
#Exercise 1:
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l1new=[l1[i] for i in range(len(l1)) if i%2==1]
l2new=[l2[i] for i in range(len(l2)) if i%2==0]
l1new+l2new
# %%
# Exercise 2:
list1 = [54, 44, 27, 79, 91, 41]
a=list1.pop(4)
list1.insert(2,a)
list1.append(a)
list1
# %%
# Exercise 3: slice a list into 3 equal size and reverse
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
chunksize=int(len(sample_list)/3)
start=0
end=chunksize
for i in range(3):
    list=sample_list[start:end]
    reverselist=list[::-1]
    print(reverselist)
    start=end
    end+=end
# %%
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
d={}
for i in sample_list:
    if i not in d:
        d[i]=1
    d[i]+=1
print(d)
# %%
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
result=zip(first_list,second_list)
set(result)
# %%
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
intersect=[]

for i in first_set:
    if i in second_set:
        intersect.append(i)

for i in intersect:
    first_set.remove(i)

print(intersect,first_set)
# %%
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
result=[]
for v in speed.values():
    if v not in result:
        result.append(v)
print(result)
# %%
result=[]
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
for i in sample_list:
    if i not in result:
        result.append(i)
print(tuple(result))
minnum=result[0]
maxnum=result[0]
for i in result:
    minnum=min(minnum,i)
    maxnum=max(maxnum,i)
print(minnum,maxnum)
# %%
def productExceptSelf(nums):

    result=[1]*len(nums)

    prefix=1
    for i in range(len(nums)):
        result[i]=prefix
        prefix*=nums[i]

    postfix=1
    for i in range(len(nums)-1,-1,-1):
        result[i]*=postfix
        postfix*=nums[i]

    return result

# %%
# Valid Anagram
class Solution():

    def __init__(self) -> None:
        pass

    def valid_anagram(self,s1:str,s2:str):

        if len(s1)!=len(s2):
            return False
        
        count1={}
        count2={}

        for i in range(len(s1)):
            count1[s1[i]]=count1.get(s1[i],0)+1
            count2[s2[i]]=count2.get(s2[i],0)+1

        return count1==count2
    
solution=Solution()
solution.valid_anagram("anagram","nagaram")

# %%
# Replace Elements with Greatest element on right side

def rightgreatest(arr:list):

    maxe=-1
    result=[None]*len(arr)

    for i in range(len(arr)-1,-1,-1):
        result[i]=maxe
        maxe=max(maxe,arr[i])

    return result

rightgreatest([17,18,5,4,6,1])
# %%
# Is subsequence

def issubseq(s1:str,s2:str):

    i=0
    l=0
    res=0

    while l<len(s2):

        if s1[i]==s2[l]:
            i+=1
            res+=1

        if i>len(s1):
            i=0

        l+=1

    return res==len(s1)

issubseq('axc',"ahbgdc")
# %%
# Length of last word

def len_lastw(s:str):

    count=0

    for c in s[::-1]:

        if c==' ':
            if count!=0:
                return count
        else:
            count+=1

    return count

len_lastw("   fly me   to   the moon  ")
# %%
#two sum
def twosum(nums:list,t:int):

    d={}

    for i,v in enumerate(nums):
        need=t-v
        if need in d:
            return [i,d[need]]
        d[v]=i
    
twosum([2,7,11,15],9)
# %%
# Longest common prefix
def prefixcount(strs:list):

    strcomb=list(zip(*strs))

    s=''

    for i in range(len(strcomb)):
        if len(set(strcomb[i]))==1:
            s+=strcomb[i][0]
        else:
            break

    return s
prefixcount(["flower","flow","flight"])

# %%
# group anagrams

def grp_anagrams(strs:list):

    d={}

    for str in strs:

        count=[0]*26

        for s in str:

            count[ord(s)-ord('a')]+=1

        keys=tuple(count)

        if keys not in d:
            d[keys]=[str]
        else:
            d[keys].append(str)

    return list(d.values())

grp_anagrams(["eat","tea","tan","ate","nat","bat"])


# %%
# top K frequent elements

def topk(nums:list, k:int):

    count={}
    for n in nums:
        count[n]=count.get(n,0)+1

    count_sort=sorted(count.items(),key=lambda x:x[1],reverse=True)
    print(count_sort)

    result=[]
    for i,v in count_sort:
        result.append(i)
        if len(result)==k:
            return result
    
topk([1,1,1,2,2,3],2)

# %%
# product of array except self

def arrprod(arr:list):

    prefix=1

    result=[None]*len(arr)

    for i in range(len(arr)):
        result[i]=prefix
        prefix*=arr[i]

    postfix=1
    for i in range(len(arr)-1,-1,-1):
        result[i]*=postfix
        postfix*=arr[i]

    return result

arrprod([1,2,3,4])
# %%
# valid sudoku

def valid_sudoku(board:list[list[str]]):

    rowd=collections.defaultdict(set)
    cold=collections.defaultdict(set)
    squared=collections.defaultdict(set)

    row=len(board)
    col=len(board[0])

    for r in range(row):
        for c in range(col):

            if board[r][c]=='.':
                continue

            if board[r][c] in rowd or board[r][c] in cold or board[r][c] in squared[(r//3,c//3)]:
                return False
            
            rowd[r].add(board[r][c])
            cold[c].add(board[r][c])
            squared[(r//3,c//3)].add(board[r][c])

    return True

# %%
# Encode and Decode strings

# Encode strings:

def encode(strs:list):

    s=''

    for c in strs:
        l=len(c)
        s+=str(l)+'#'+c

    return s

encode(["Hello","World"])

# %%
# Decode strings

def decode(s:str):

    res=[]
    i=0

    while i<len(s):

        j=i

        while s[j]!='#':
            j+=1

        l=int(s[i:j])
        res.append(s[j+1:j+1+l])
        i=j+1+l

    return res

decode('5#Hello5#World')

# %%
## Longest Consecutive Sequence

def longseq(nums:list):

    maxlen=1

    for n in nums:

        length=1

        if n-1 not in nums:
            while n+length in nums:
                length+=1

        maxlen=max(maxlen,length)

    return maxlen

longseq([100,4,200,1,3,2])
# %%
# Valid palindrome

def valid_palindrom(s:str):

    l=0
    r=len(s)-1

    while l<r:

        while not s[l].isalnum():
            l+=1

        while not s[r].isalnum():
            r-=1

        if s[l].lower()!=s[r].lower():
            return False
        
        l+=1
        r-=1
    
    return True

valid_palindrom("A man, a plan, a canal: Panama")
# %%
# two sum of sorted array

def twosum_twopointer(arr:list,t:int):

    l=0
    r=len(arr)-1

    while l<r:

        if arr[l]+arr[r]>t:
            r-=1
        elif arr[l]+arr[r]<t:
            l+=1
        else:
            return [l+1,r+1]
        
twosum_twopointer([2,7,11,15],9)
# %%
# 3Sum
def threesum(arr:list):

    arr.sort()


def table_outputs(df):

    df = df.drop_duplicates()

    subdf=df[df['date']>'2019-09-01']

    #subdf['min_likes']=subdf.groupby(by=["account_name"]).agg('nb_likes':['min'])

    #subdf['total_number_tweets']=subdf.groupby(by=["account_name"]).agg({'text'}:['sum'])

    subdf=subdf[['account_name','min_likes','total_number_tweets']]

    return subdf



    

    