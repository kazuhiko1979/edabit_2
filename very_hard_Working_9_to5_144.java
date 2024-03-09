import java.text.DecimalFormat;

public class very_hard_Working_9_to5_144 {
    public static String overTime(double[] lst){
        double start = lst[0];
        double end = lst[1];
        double rate = lst[2];
        double overtimeRate = lst[3];

        double regularHours = Math.max(0, Math.min(end, 17) - start);
        double overtimeHours = Math.max(0, end -17);

        double totalPay;
        if (start < 17){
            totalPay = regularHours * rate + overtimeHours * rate * overtimeRate + 0.001;
        } else {
            totalPay = (end -start) * rate * overtimeRate;
        }

        DecimalFormat df = new DecimalFormat("#, ###.00");
        return "$" + df.format(totalPay);

    }
    public static void main(String[] args) {
    System.out.println(overTime(new double[]{9, 17, 30, 1.5}));       // 出力: $240.00
    System.out.println(overTime(new double[]{16, 18, 30, 1.8}));      // 出力: $54.00
    System.out.println(overTime(new double[]{13.25, 18, 30, 1.5}));   // 出力: $209.63
    }
}