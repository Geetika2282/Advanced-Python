import java.io.IOException;
import java.util.*;

public class greaterNumExcept {
    public static void greater(int n){
        try{
            if (n > 60000){
                throw new IOException("Number is greater than 60000");
            }
        }
        catch (Exception e){
            System.out.println(e.getMessage());
        }

    }

    public static void main(String[] args) {
        System.out.println("Enter a number: ");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        greater(n);
        System.out.println("After except");

    }
}
