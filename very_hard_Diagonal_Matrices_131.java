import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class very_hard_Diagonal_Matrices_131 {

    public static List<List<Integer>> diagonalize(int n, String d) {
        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                row.add(i + j);
            }
            result.add(row);
        }
        
        if ("ul".equals(d)){
            return result;
        } else if ("lr".equals(d)){
            Collections.reverse(result);
            for (List<Integer> row : result) {
                Collections.reverse(row);
            }
            return result;
        } else if ("ur".equals(d)) {
            for (List<Integer> row : result) {
                Collections.reverse(row);
            }
            return result;
        } else if ("ll".equals(d)) {
            Collections.reverse(result);
            return result;
        }

        return result;
    }

    public static void main(String[] args) {
        // Examples
        System.out.println(diagonalize(3, "ul"));
        System.out.println(diagonalize(4, "ur"));
        System.out.println(diagonalize(3, "ll"));
        System.out.println(diagonalize(5, "lr"));
    }
}