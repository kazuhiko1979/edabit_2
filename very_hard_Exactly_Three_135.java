public class very_hard_Exactly_Three_135{
    public static boolean isExactlyThree(long n){
        int count = 0;
        for (long i = 1; i <= Math.sqrt(n); i++){
            if (n % i == 0){
                count++;
                long complement = n / i;
                if (complement != i){
                    count++;
                }
            }
        if (count > 3){
            return false;
        }
    }
    return count == 3;
}


    public static void main(String[] args){
        System.out.println(isExactlyThree(4));   // false
        System.out.println(isExactlyThree(12));  // true
        System.out.println(isExactlyThree(25));  // false
        System.out.println(isExactlyThree(44398433));  // true
        System.out.println(isExactlyThree(27550356289L));  // true
    }
}