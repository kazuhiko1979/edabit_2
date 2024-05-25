import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class very_hard_Rectangle_or_Not_157 {

    public static boolean isRectangle(List<String> coordinates) {
        List<int[]> points = new ArrayList<>();

        for (String point : coordinates) {
            point = point.replaceAll("[()]", "");
            String[] xy = point.split(",");
            int x = Integer.parseInt(xy[0].trim());
            int y = Integer.parseInt(xy[1].trim());
            points.add(new int[]{x, y});
        }

        if (points.size() != 4) {
            return false;
        }

        for (List<int[]> perm : permutations(points)) {
            int[] A = perm.get(0);
            int[] B = perm.get(1);
            int[] C = perm.get(2);
            int[] D = perm.get(3);

            if (isParallelSides(A, B, C, D) && isParallelSides(A, D, B, C) &&
                    distance(A, B) == distance(C, D) && distance(A, D) == distance(B, C)) {
                return true;
            }
        }

        return false;
    }

    private static boolean isParallelSides(int[] p1, int[] p2, int[] p3, int[] p4) {
        return (p2[0] - p1[0]) * (p4[1] - p3[1]) == (p2[1] - p1[1]) * (p4[0] - p3[0]);
    }

    private static int distance(int[] p1, int[] p2) {
        return (p2[0] - p1[0]) * (p2[0] - p1[0]) + (p2[1] - p1[1]) * (p2[1] - p1[1]);
    }

    private static List<List<int[]>> permutations(List<int[]> original) {
        if (original.size() == 0) {
            List<List<int[]>> result = new ArrayList<>();
            result.add(new ArrayList<>());
            return result;
        }

        int[] firstElement = original.remove(0);
        List<List<int[]>> returnValue = new ArrayList<>();
        List<List<int[]>> permutations = permutations(original);
        for (List<int[]> smallerPermutated : permutations) {
            for (int index = 0; index <= smallerPermutated.size(); index++) {
                List<int[]> temp = new ArrayList<>(smallerPermutated);
                temp.add(index, firstElement);
                returnValue.add(temp);
            }
        }
        original.add(0, firstElement);
        return returnValue;
    }

    public static void main(String[] args) {
        System.out.println(isRectangle(Arrays.asList("(-4, 3)", "(4, 3)", "(4, -3)", "(-4, -3)"))); // true
        System.out.println(isRectangle(Arrays.asList("(0, 0)", "(0, 1)"))); // false
        System.out.println(isRectangle(Arrays.asList("(0, 0)", "(0, 1)", "(1, 0)"))); // false
        System.out.println(isRectangle(Arrays.asList("(0, 0)", "(9, 0)", "(7, 5)", "(16, 5)"))); // true
        System.out.println(isRectangle(Arrays.asList("(0, 0)", "(1, 0)", "(0, 1)", "(0, 0)"))); // false
        System.out.println(isRectangle(Arrays.asList("(1, 0)", "(1, 2)", "(2, 1)", "(2, 3)", "(3, 3)"))); // false
        System.out.println(isRectangle(Arrays.asList("(-2, 2)", "(-2, -1)", "(5, -1)", "(5, 2)"))); // true
    }
}