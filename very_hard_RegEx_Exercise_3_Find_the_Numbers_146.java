import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class very_hard_RegEx_Exercise_3_Find_the_Numbers_146{
    public static void main(String[] args) {

        String integers = "(?<![.\\d+-])(?:[+-]?\\d+)(?![.\\d])";
        String floats = "(?<![.\\d+-])(?:[+-]?(?:\\d+\\.\\d+|\\d*\\.\\d+))(?![.\\d])";
        String positive = "(?<![.\\d+-])(?:\\+?\\d*\\.?\\d+)(?![.\\d])";
        String negative = "(?<![.\\d+-])(?:-\\d*\\.?\\d+)(?![.\\d])";
        String numbers = "(?<![.\\d+-])(?:[+-]?\\d*\\.?\\d+)(?![.\\d])";

        String txt = " 123.456 2 +7 -88 -.25 9.10.11 -4. +-34 -0.6 --5 ";

        Pattern patternIntgers = Pattern.compile(integers);
        Pattern patternFloats = Pattern.compile(floats);
        Pattern patternPositive = Pattern.compile(positive);
        Pattern patternNegative = Pattern.compile(negative);
        Pattern patternNumbers = Pattern.compile(numbers);
        
        Matcher matcherIntegers = patternIntgers.matcher(txt);
        Matcher matcherFloats = patternFloats.matcher(txt);
        Matcher matcherPositive = patternPositive.matcher(txt);
        Matcher matcherNegative = patternNegative.matcher(txt);
        Matcher matcherNumbers = patternNumbers.matcher(txt);
        
        List<String> integerList = new ArrayList<>();
        List<String> floatList = new ArrayList<>();
        List<String> positiveList = new ArrayList<>();
        List<String> negativeList = new ArrayList<>();
        List<String> numberList = new ArrayList<>();

        while (matcherIntegers.find()) {
            integerList.add(matcherIntegers.group());
        }
        System.out.println(integerList);

        while (matcherFloats.find()) {
            floatList.add(matcherFloats.group());
        }
        System.out.println(floatList);
        
        while (matcherPositive.find()) {
            positiveList.add(matcherPositive.group());
        }
        System.out.println(positiveList);

        while (matcherNegative.find()) {
            negativeList.add(matcherNegative.group());
        }
        System.out.println(negativeList);

        while (matcherNumbers.find()) {
            numberList.add(matcherNumbers.group());
        }
        System.out.println(numberList);
    }    
}