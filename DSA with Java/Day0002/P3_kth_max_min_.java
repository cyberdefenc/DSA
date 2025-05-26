import java.util.Scanner;

class InputArray {

    
    InputArray(int[] arr, Scanner sc) {
        System.out.println("Enter " + arr.length + " elements:");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }


    }

    

}


class KthMax {


}

class KthMin {


}

public class P3_kth_max_min_ {

        public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size of the array: ");
        int n = sc.nextInt();
        int[] arr = new int[n];

        
        new InputArray(arr, sc);

        sc.close();
    }
    
}
