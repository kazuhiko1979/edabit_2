import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class very_hard_Sort_a_String_with_the_Given_Template_143 {
    public static String customSort(String t, String s){
        Map<Character, Integer> priority = new HashMap<>();
        for (int i = 0; i < t.length(); i++){
            priority.put(t.charAt(i), i);
        }

    List<Character> order = new ArrayList<>();
    List<Character> origin = new ArrayList<>();

    for (char c : s.toCharArray()) {
        if(t.indexOf(c) >= 0){
            order.add(c);
        } else {
            origin.add(c);
        }
    }

    Collections.sort(order, (a,b) -> {
        return Integer.compare(priority.getOrDefault(a, -1), priority.getOrDefault(b, -1));
    });

    Collections.sort(origin);

    StringBuilder result = new StringBuilder();
    for(char c : order){
        result.append(c);
    }
    for (char c : origin){
        result.append(c);
    }

    return result.toString();

}

public static void main(String[] args){
    System.out.println(customSort("edc", "abcdefzyx"));
        System.out.println(customSort("fby", "abcdefzyx"));
        System.out.println(customSort("", "abcdefzyx"));
        System.out.println(customSort("cteqh", "xnjanztmhg"));
        System.out.println(customSort("jv", "cxkafinfiuhnnaracsztbrcwaifwattzavwohoqskauififucq"));
    }
}