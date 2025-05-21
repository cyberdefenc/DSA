//P3. Compress the string -Character can not come after different character

public class P3_no_repeat_compress_string_ {
    public static void main(String[] args) {
        String s = "aaaabbbcc";
        String compressed = ""; 

        int count = 1;
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == s.charAt(i - 1)) {
                count++;
            } else {
                compressed = compressed + s.charAt(i - 1) + count;
                count = 1; 
            }
        }

        
       compressed = compressed + s.charAt(s.length() - 1) + count;

        System.out.println("Compressed string: " + compressed);
    }
}
