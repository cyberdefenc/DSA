// P2. Compress the string-Character can  come after different character

public class P2_Compress_String_ {

    public static void main(String[] args) {
        
    
    String s="aaaabbbcc";
    
    

    for(int i=0;i<s.length();i++){
        int count=0;
        for(int j=i+1;j<s.length();j++){
            if(s.charAt(i)==s.charAt(j)){
                count++;
               
            }

        }
        if(count>0){
            System.out.print(s.charAt(i)+""+count);
        }
        else{
            System.out.print(s.charAt(i)+""+1);
        }

    }
}
    
}
