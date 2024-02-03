import java.util.Arrays;

public class very_hard_Intersecting_Rows_and_Columns_133 {

    public static int[][] transformMatrix(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;

        int[][] result = new int[rows][cols];

        for (int i=0; i<rows; i++){
            for (int j = 0; j < cols; j++){
                int rowSum = Arrays.stream(matrix[i]).sum() - matrix[i][j];

                int colSum = 0;
                for (int[] row : matrix){
                    colSum += row[j];
                }
                colSum -= matrix[i][j];
                result[i][j] = rowSum + colSum;
            }
        }
        return result;
    }

    public static void printMatrix(int[][] matrix){
        for (int[] row : matrix){
            System.out.println(Arrays.toString(row));
        }
        System.out.println();
    }


    // テストケース
    public static void main(String[] args) {
        int[][] matrix1 = {
            {1, 0, 0, 0, 1},
            {0, 1, 0, 0, 0},
            {0, 0, 0, 1, 0},
            {0, 1, 0, 1, 0},
            {0, 1, 0, 0, 0}
        };

        int[][] matrix2 = {
            {1, 0, 0},
            {0, 1, 0},
            {0, 0, 1}
        };

        int[][] matrix3 = {
            {1, 1, 1},
            {0, 0, 1},
            {0, 0, 1}
        };

        int[][] matrix4 = {
            {1, 1, 1},
            {0, 1, 1},
            {0, 0, 1}
        };

        int[][] result1 = transformMatrix(matrix1);
        int[][] result2 = transformMatrix(matrix2);
        int[][] result3 = transformMatrix(matrix3);
        int[][] result4 = transformMatrix(matrix4);

        printMatrix(result1);
        printMatrix(result2);
        printMatrix(result3);
        printMatrix(result4);
    }
}

