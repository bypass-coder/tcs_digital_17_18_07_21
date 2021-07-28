package hacker_rank;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'divisibleSumPairs' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. INTEGER k
     *  3. INTEGER_ARRAY ar
     */

    public static int divisibleSumPairs(int n, int k, int[] ar) {
    // Write your code here
        int count = 0;
       for (int i = 0 ; i < ar.length; i++){
           
           for (int j = i+1; j < ar.length; j++ ){
               
               if ((ar[i] + ar[j])%k == 0){
                   
                   count++;
                   
               }
               
           }
           
       } 
       
       return count;
    }
    
}

public class code_1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int n = scanner.nextInt();
        
        int k = scanner.nextInt();
        
        int[] ar = new int[n];
        
        for (int i = 0; i < n; i++){
            
            ar[i] = scanner.nextInt();
            
        }
        
        System.out.println(Result.divisibleSumPairs(n, k, ar));
        
    }
}
