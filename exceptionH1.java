public class exceptionH1 {
    public static void main(String[] args) {

        // Will read from cmd line
        try{
            int dividend = Integer.parseInt(args[0]);
            int divisor = Integer.parseInt(args[1]);

            int res = dividend/ divisor;
            System.out.println(res);
        }
        // Handles Arithmetic Exception
        catch (ArithmeticException e){
            System.out.println("The divisor cannot be zero.");
            e.getStackTrace();
        }

        // Handles NumberFormatException
        catch (NumberFormatException e){
            System.out.println("Enter Integers only");
            System.out.println(e);
        }

        // Handles ArrayIndexOutOfBounds Exception
        catch (ArrayIndexOutOfBoundsException e){
            System.out.println("Enter 2 values as dividend and divisor");
            System.out.println(e.getMessage());
        }

    }
}
