class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0
        
        if height[0] == 0:
            while height[0] == 0 :
                height.pop(0)
        w_stack = [height[0]]
        max_height = height[0]
        volume = 0
        
        for seq in range(1, len(height)):
            i = len(w_stack) - 1
            if w_stack[i] >= height[seq]:
                w_stack.append(height[seq])
                i+=1
            elif w_stack[i] <= height[seq] and max_height > height[seq]:
                while i>0 and (w_stack[i] < height[seq]):
                    volume = volume + (height[seq] - w_stack[i])
                    w_stack[i] = height[seq]
                    i-=1
                w_stack.append(height[seq])
                i+=1
            else :
                while i>0:
                    volume = volume + max_height - w_stack.pop()
                    i-=1
                w_stack[i] = height[seq]
                max_height = height[seq]
                    
        return volume 

# 투 포인터 풀이

class Solution:
    def trap_2(self, height: List[int]) -> int:
        if not height:
            return 0
        
        volume = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)

            if left_max <= right_max :
                volume += left_max - height[left]
                left+=1
            else:
                volume += right_max - height[right]
                right-=1
            return volume



