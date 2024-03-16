public class very_hard_Bowling_Scorekeeping_145 {
    public static int calculateBowlingScore(int[] rolls){
        int totalScore = 0;
        int rollIndex = 0;
        int frame = 1;

        while (frame <= 10){ // 10フレームまで繰り返す
            if (rolls[rollIndex] == 10) { // ストライクの場合
                totalScore += 10;
                totalScore += rolls[rollIndex + 1] + rolls[rollIndex + 2];
                rollIndex += 1;
            } else if (rolls[rollIndex] + rolls[rollIndex + 1] == 10){ // スペア
                totalScore += 10;
                totalScore += rolls[rollIndex + 2];
                rollIndex += 2;
            } else {
                totalScore += rolls[rollIndex] + rolls[rollIndex + 1];
                rollIndex += 2;
            }
            frame++;
        }
    return totalScore;
}

public static void main(String[] args) {
    // テストケースの実行
    System.out.println(calculateBowlingScore(new int[]{10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10}));  // ➞ 300
    System.out.println(calculateBowlingScore(new int[]{4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4}));  // ➞ 80
    System.out.println(calculateBowlingScore(new int[]{5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5}));  // ➞ 150
    System.out.println(calculateBowlingScore(new int[]{10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10}));  // ➞ 200
    System.out.println(calculateBowlingScore(new int[]{10, 0, 10, 7, 2, 10, 10, 10, 8, 2, 9, 1, 7, 2, 10, 10, 5}));  // ➞ 194
    System.out.println(calculateBowlingScore(new int[]{8, 0, 8, 2, 10, 10, 7, 3, 9, 1, 7, 2, 10, 10, 9, 0}));  // ➞ 177
        
}
}