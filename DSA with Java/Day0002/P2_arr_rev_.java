import java.util.Scanner;

class InputArray {

    
    InputArray(int[] arr, Scanner sc) {
        System.out.println("Enter " + arr.length + " elements:");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }

       
        reverseArray(arr);

        
        System.out.println("Reversed Array:");
        for (int val : arr) {
            System.out.print(val + " ");
        }
    }

    
    void reverseArray(int[] arr) {
        int start = 0;
        int end = arr.length - 1;
        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }
}

public class P2_arr_rev_ {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size of the array: ");
        int n = sc.nextInt();
        int[] arr = new int[n];

        
        new InputArray(arr, sc);

        sc.close();
    }
}
