class Solution {
    public int binary_search(int[] numbers,int start,int end,int target){
        while(start<=end){
            int mid=start+(end-start)/2;
            if (numbers[mid]==target)return mid;
            else if (numbers[mid]<target){
                start=mid+1;
            }else{
                end=mid-1;
            }
        }
        return -1;
    }
    public int[] twoSum(int[] numbers, int target) {
        int n=numbers.length;
        for(int i=0;i<n;i++){
            int rem=target-numbers[i];
            if (rem<numbers[i]){
                int second_index=binary_search(numbers,0,i-1,rem);
                if (second_index!=-1)return new int[] {second_index+1,i+1};
            }else{
                int second_index=binary_search(numbers,i+1,n-1,rem);
                if (second_index!=-1)return new int[] {i+1,second_index+1};
            }
        }
        return new int[] {-1,-1};
    }
}
