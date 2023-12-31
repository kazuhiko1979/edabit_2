import java.util.Arrays;

public class very_hard_Interquartile_Range_IQR_126 {

    public static double median(double[] lst) {
        int length = lst.length;
        Arrays.sort(lst);

        if (length % 2 == 0) {
            return (lst[length / 2 - 1] + lst[length / 2]) / 2.0;
        } else {
            return lst[length / 2];
        }
    }

    public static double iqr(double[] lst) {
        double[] sortedList = Arrays.copyOf(lst, lst.length);
        Arrays.sort(sortedList);

        int length = sortedList.length;
        double q1, q3;

        if (length % 2 == 0) {
            q1 = median(Arrays.copyOfRange(sortedList, 0, length / 2));
            q3 = median(Arrays.copyOfRange(sortedList, length / 2, length));
        } else {
            q1 = median(Arrays.copyOfRange(sortedList, 0, length / 2));
            q3 = median(Arrays.copyOfRange(sortedList, length / 2 + 1, length));
        }

        return q3 - q1;
    }

    public static void main(String[] args) {
        System.out.println(iqr(new double[]{1, 1, 3, 4, 4, 5, 5, 5, 6, 7, 9})); // 3.0
        System.out.println(iqr(new double[]{6, 4, 4, 4, 3, 3, 2, 1})); // 1.5
        System.out.println(iqr(new double[]{6, 5, 2.6, 8, 4.9, 5, 7.9})); // 3.0
        System.out.println(iqr(new double[]{14, 28, 0, 15, 12, 15, 15, 15})); // 2.0
        System.out.println(iqr(new double[]{-3.1, -3.8, -14, 23, 0})); // 20.4
        System.out.println(iqr(new double[]{-12, 0, 0, 0, 3})); // 7.5
        System.out.println(iqr(new double[]{-3, 0, 0, 0, 0, 4.7})); // 0.0
        System.out.println(iqr(new double[]{0, 0, 0, 0, 0, 0})); // 0.0
        System.out.println(iqr(new double[]{0, 0, 0, 0, 0, 0, 0})); // 0.0
    }
}
