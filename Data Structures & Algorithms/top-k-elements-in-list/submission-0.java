class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> hm=new HashMap<>();
        for (int i:nums){
            hm.put(i,hm.getOrDefault(i,0)+1);
        }
        PriorityQueue<int []> pq=new PriorityQueue<>((a,b)->{
            return (a[1]-b[1]);
        });
        for (int i:hm.keySet()){
            pq.offer(new int[] {i,hm.get(i)});
            while (pq.size()>k){
                pq.poll();
            }
        }
        int[] ans=new int[pq.size()];
        int index=0;
        while (!pq.isEmpty()){
            ans[index++]=pq.poll()[0];
        }
        return ans;
    }
}
