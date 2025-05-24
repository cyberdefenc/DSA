import java.util.Scanner;

class ArrayInput {

    void inputArray(int[] arr, Scanner sc) {
        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }
    }

    void printArray(int[] arr) {
        System.out.println("Array elements are:");
        for (int val : arr) {
            System.out.print(val + " ");
        }
        System.out.println();
    }

    void findMinMax(int[] arr) {
        int min = arr[0];
        int max = arr[0];
        for (int val : arr) {
            if (val < min) min = val;
            if (val > max) max = val;
        }
        System.out.println("Minimum = " + min);
        System.out.println("Maximum = " + max);
    }
}

public class P1_max_min_arr_ {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter the size of the array:");
        int n = sc.nextInt();
        
        int[] arr = new int[n];

        ArrayInput helper = new ArrayInput();
        helper.inputArray(arr, sc);
        helper.printArray(arr);
        helper.findMinMax(arr);
        
        sc.close();
    }
}
