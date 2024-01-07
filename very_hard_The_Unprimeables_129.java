import java.util.*;

public class very_hard_The_Unprimeables_129 {
    public static Object isUnprimeable(int n) {
        if (isPrime(n)) return "Prime Input";

        Set<Integer> result = new HashSet<>();
        String numStr = String.valueOf(n);

        for (int i = 0; i < numStr.length(); i ++){
            for (int j = 0; j < 10; j++) {
                if (j != Character.getNumericValue(numStr.charAt(i))) {
                    int newNum = Integer.parseInt(numStr.substring(0, i) + j + numStr.substring(i + 1));
                    result.add(newNum);
                }
            }
        }
        
        if (result.isEmpty()) return "Unprimeable";

        List<Integer> primes = new ArrayList<>();
        int maxResult = Collections.max(result);
        for (int i = 0; i <= maxResult; i++) {
            if (isPrime(i)) primes.add(i);
        }

        if (primes.contains(n)) return "Prime Input";

        List<Integer> finalList = new ArrayList<>(result);
        finalList.removeIf(num -> !primes.contains(num));
        Collections.sort(finalList);

        return finalList.isEmpty() ? "Unprimeable" : finalList;
    }

    private static boolean isPrime(int num) {
        if (num < 2) return false;
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }
        return true;
    }


public static void main(String[] args) {
        System.out.println(isUnprimeable(200));
        System.out.println(isUnprimeable(14));
        System.out.println(isUnprimeable(2));
        System.out.println(isUnprimeable(839));
        System.out.println(isUnprimeable(4065));
        System.out.println(isUnprimeable(5042));
        System.out.println(isUnprimeable(1));
        System.out.println(isUnprimeable(5137));
        System.out.println(isUnprimeable(666));
        System.out.println(isUnprimeable(13490));
        System.out.println(isUnprimeable(294001));
    }
}