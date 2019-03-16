class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dicti={}
        array=[]
        if len(nums)== 1:
            return nums
        for i,v in enumerate(nums):
            if v not in dicti:
                dicti[v]=1
            else:
                dicti[v]+=1
            if dicti[v] >= (len(nums)//3+1) :
                if v not in array:
                    array.append(v)
        return array

def stringToIntegerList(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            
            ret = Solution().majorityElement(nums)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()