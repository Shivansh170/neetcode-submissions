class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder temp=new StringBuilder("");
        for (char c:s.toCharArray()){
            if (Character.isLetter(c) || Character.isDigit(c)){
                temp.append(Character.toLowerCase(c));
            }
        }
        int i=0;
        int j=temp.length()-1;
        while (i<=j){
            if (temp.charAt(i)!=temp.charAt(j))return false;
            i++;
            j--;
        }
        System.out.println(temp.toString());
        return true;
    }
}
