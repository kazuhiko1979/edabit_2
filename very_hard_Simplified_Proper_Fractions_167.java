//Simplified Proper Fractions
//Create a function that takes a number max_den and returns the total number of fully simplified proper fractions that exist with denominator less than or equal to max_den.
//
//You only need to return the number of fractions; NOT the fractions themselves. In the examples below, I list the fractions simply for your reference.
//
//Examples
//sim_prop_frac(10) ➞ 31
//        # 1/2, 1/3, 2/3, 1/4, 3/4, 1/5, 2/5, 3/5, 4/5, 1/6, 5/6, 1/7, 2/7, 3/7, 4/7, 5/7, 6/7, 1/8, 3/8, 5/8, 7/8, 1/9, 2/9, 4/9, 5/9, 7/9, 8/9, 1/10, 3/10, 7/10, 9/10
//
//sim_prop_frac(7) ➞ 17
//        # 1/2, 1/3, 2/3, 1/4, 3/4, 1/5, 2/5, 3/5, 4/5, 1/6, 5/6, 1/7, 2/7, 3/7, 4/7, 5/7, 6/7
//Notes
//A fully simplified proper fraction is a fraction where both the numerator and denominator share no common factors besides 1 and the fraction is less than 1.
import java.util.HashSet;
import java.util.Set;


public class very_hard_Simplified_Proper_Fractions_167 {
    static class Fraction implements Comparable<Fraction> {

        final int numerator;
        final int denominator;

        Fraction(int numerator, int denominator) {
            int gcd = gcd(Math.abs(numerator), Math.abs(denominator));
            this.numerator = numerator / gcd;
            this.denominator = denominator / gcd;
        }

        private int gcd(int a, int b) {
            while (b != 0) {
                int temp = b;
                b = a % b;
                a = temp;
            }
            return a;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Fraction fraction = (Fraction) o;
            return numerator == fraction.numerator && denominator == fraction.denominator;
        }

        @Override
        public int hashCode() {
            return 31 * numerator + denominator;
        }

        @Override
        public int compareTo(Fraction other) {
            return Integer.compare(this.numerator * other.denominator, other.numerator * this.denominator);
        }
        }

    public static int simPropFrac(int maxDen) {
        Set<Fraction> uniqueFractions = new HashSet<>();

        for (int denominator = 2; denominator <= maxDen; denominator++) {
            for (int numerator = 1; numerator < denominator; numerator++) {
                Fraction fraction = new Fraction(numerator, denominator);
                if (fraction.compareTo(new Fraction(1, 1)) < 0) {
                    uniqueFractions.add(fraction);
                }
            }
        }

        return uniqueFractions.size();
    }

    public static void main(String[] args) {
        System.out.println(simPropFrac(10));  // 31
        System.out.println(simPropFrac(2));   // 1
        System.out.println(simPropFrac(30));  // 277
        System.out.println(simPropFrac(100)); // 3043
        System.out.println(simPropFrac(56));  // 963
    }
}
