import java.util.ArrayList;
import java.util.List;

public class very_hard_Block_Duke_127 {

    static boolean canClimb(int current, int next) {
        int diff = Math.abs(current - next);
        return current == next || diff == 1;
    }

    static boolean canTraverse(int[][] matrix) {
        List<List<Integer>> transposed = new ArrayList<>();
        for (int i = 0; i < matrix[0].length; i++) {
            List<Integer> col = new ArrayList<>();
            for (int[] row : matrix) {
                col.add(row[i]);
            }
            transposed.add(col);
        }

        int step = 0;
        int currentBlock = transposed.get(step).stream().mapToInt(x -> x).sum();

        for (int i = 1; i < transposed.size(); i++) {
            int countNextCol = transposed.get(i).stream().mapToInt(x -> x).sum();
            if (!canClimb(currentBlock, countNextCol)) {
                return false;
            }
            step++;
            currentBlock = countNextCol;
        }

        return step == matrix[0].length - 1;
    }

    public static void main(String[] args) {
        int[][] testMatrix1 = {
                {0, 0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 1, 0, 0, 0, 0, 0},
                {0, 0, 1, 1, 1, 0, 1, 0, 0},
                {0, 1, 1, 1, 1, 1, 1, 1, 0}
        };

        int[][] testMatrix2 = {
                {0, 0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 1, 0, 0, 0, 0, 0},
                {0, 0, 1, 1, 0, 0, 1, 0, 0},
                {0, 1, 1, 1, 1, 1, 1, 1, 0}
        };

        System.out.println(canTraverse(testMatrix1)); // Should return true
        System.out.println(canTraverse(testMatrix2)); // Should return false
    }
}
