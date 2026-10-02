class Solution:
    def trap(self, height: List[int]) -> int:
        st=[]
        total_water=0
        for i in range(len(height)):
            if len(st)==0:
                st.append(i)
            elif height[st[-1]]>=height[i]:
                st.append(i)
            else:
                water=0
                while len(st)>0 and height[st[-1]]<height[i]:
                    bottom=st.pop()
                    if len(st)==0:
                        break
                    height_curr=min(height[i],height[st[-1]])-height[bottom]
                    width=i-st[-1]-1
                    water+=height_curr*width
                total_water+=water
                st.append(i)
        return total_water