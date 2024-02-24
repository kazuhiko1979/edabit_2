import java.util.Arrays;

public class very_hard_Matrix_Multiplication_Part_2_141 {
    public static int[][] matrix_multiply(int[][] a, int[][] b) {
        if (a[0].length != b.length){
            System.out.println("Invalid");
            return null;
        }

        // Initialize the result matrix with zeros
        int[][] result = new int[a.length][b[0].length];

        // Perform matrix multiplication
        for(int i = 0; i < a.length; i++){
            for (int j = 0; j < b[0].length; j++){
                for (int k = 0; k < b.length; k++){
                    result[i][j] += a[i][k] * b[k][j];
                }
            }
        }
        return result;
    }

    // Helper function void print matrix
    public static void printMatrix(int[][] matrix){
        if(matrix == null){
            return;
        }
        for (int i = 0; i < matrix.length; i++){
            for (int j = 0; j < matrix[0].length; j++){
                System.out.println(matrix[i][j] + " ");
            }
        }
    }

    // Test cases
    public static void main(String[] args) {
        int[][] matrix1 = {{1, 2}};
        int[][] matrix2 = {{3}, {4}};
        printMatrix(matrix_multiply(matrix1, matrix2)); // ➞ [[11]]

        int[][] matrix3 = {{0, 0}, {0, 1}};
        int[][] matrix4 = {{1, 2}, {3, 4}, {5, 6}};
        printMatrix(matrix_multiply(matrix3, matrix4)); // ➞ "invalid"

        int[][] matrix5 = {{4, 2}, {3, 1}};
        int[][] matrix6 = {{5, 6}, {3, 8}};
        System.out.println(Arrays.deepToString(matrix_multiply(matrix5, matrix6)));
     


    }

}