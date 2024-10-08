import java.time.LocalTime;

public class NewTime {
    public static void main(String[] args) {
        LocalTime now = LocalTime.now();
        System.out.println(now);
        LocalTime customTime = LocalTime.of(4, 55, 22);
        System.out.println(customTime);

        String timeInString = "15:30:45";
        System.out.println(LocalTime.parse(timeInString));

        LocalTime oneHrLater = now.plusHours(1);
        System.out.println(oneHrLater);

        LocalTime oneHrBefore = now.minusHours(1);
        System.out.println(oneHrBefore);
    }
}
