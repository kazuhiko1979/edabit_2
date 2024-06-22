//The Susquehanna Hat Company
//        This fabled hat company has 5 production lines running simultaneously. The speed of each production line varies depending on the style and quality of the hat being produced. You will be given the number of hats required and a list of production line speeds.
//
//        Your job is to devise a function that will find the number of minutes elapsed for exactly n hats to be finished. If exactly n hats cannot be made in any time frame, return None. The speeds given are the number of minutes required to make one hat.
//
//        Examples
//        hats([5, [1, 1, 1, 1, 1]]) ➞ "1 minute"
//        # If each line makes a hat in 1 min, it takes 1 min to make 5 hats.
//
//        hats([3, [23, 11, 19, 9, 36]]) ➞ "18 minutes"
//
//        hats([650, [23, 11, 19, 9, 36]]) ➞ "2001 minutes"
//
//        hats([9, [23, 11, 19, 9, 36]]) ➞ None


import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class very_hard_The_Susquehanna_Hat_Company_165 {
    public static String hats(List<Object> lst) {
        int n = (int) lst.get(0);
        List<Integer> speeds = (List<Integer>) lst.get(1);
        int minTime = Collections.min(speeds);

        int low = 1;
        int high = minTime * n;

        while (low <= high) {
            int mid = (low + high) / 2;
            if (calculateTime(mid, speeds) >= n) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        if (calculateTime(low, speeds) == n) {
            return low + " minutes";
        } else {
            return null;
            }
        }

    public static int calculateTime(int time, List<Integer> speeds) {
        int count = 0;
        for (int speed : speeds) {
            count += time / speed;
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(hats(List.of(35, List.of(1, 1, 1, 1, 1)))); // "7 minutes"
        System.out.println(hats(List.of(11, List.of(4, 18, 11, 29, 10)))); // "24 minutes"
        System.out.println(hats(List.of(1, List.of(11, 21, 1, 18, 2)))); // "1 minute"
        System.out.println(hats(List.of(1, List.of(4, 18, 11, 29, 10)))); // "4 minutes"
        System.out.println(hats(List.of(100, List.of(6, 3, 18, 7, 87)))); // null
        System.out.println(hats(List.of(2001, List.of(1, 2, 3, 4, 5)))); // "877 minutes"
        System.out.println(hats(List.of(200, List.of(30, 45, 27, 78, 29)))); // "1440 minutes"
        System.out.println(hats(List.of(999999999, List.of(30, 45, 27, 78, 29)))); // "7148174160 minutes"
        System.out.println(hats(List.of(47, List.of(12, 19, 12, 28, 17)))); // null
    }
}