import java.util.ArrayList;
import java.util.List;

public class very_hard_Combinator_148 {
    public static List<String> combinator(String[][] lst) {
        List<List<String>> temp = new ArrayList<>();
        for (String[] item : lst) {
            List<String> innerList = new ArrayList<>();
            for (String str : item) {
                if (!str.equals(" ")) {
                    innerList.add(str);
                }
            }
            temp.add(innerList);
        }
        List<List<String>> combinations = cartesian(temp);
        List<String> result = new ArrayList<>();
        for (List<String> pair : combinations) {
            if (pair.stream().allMatch(item -> item.length() <= 2)) {
                result.add(String.join("", pair));
            } else {
                result.add(String.join("", pair));
            }
        }
        return result;
    }

    public static List<List<String>> cartesian(List<List<String>> lists) {
        List<List<String>> result = new ArrayList<>();
        if (lists.isEmpty()) {
            result.add(new ArrayList<>());
            return result;
        } else {
            List<String> firstList = lists.get(0);
            List<List<String>> remainingLists = cartesian(lists.subList(1, lists.size()));
            for (String item : firstList) {
                for (List<String> remainingList : remainingLists) {
                    List<String> tempList = new ArrayList<>(remainingList);
                    tempList.add(0, item);
                    result.add(tempList);
                }
            }
            return result;
        }
    }

    public static void main(String[] args) {
        System.out.println(combinator(new String[][]{{"a"}}));
        System.out.println(combinator(new String[][]{{"ab"}, {"ba"}}));
        System.out.println(combinator(new String[][]{{"a", "b"}}));
        System.out.println(combinator(new String[][]{{"a", "b"}, {"c", "d"}}));
        System.out.println(combinator(new String[][]{{"a"}, {"a", "b"}, {"a", "b", "c"}}));
        System.out.println(combinator(new String[][]{{"foo", "bar"}, {"baz", "bamboo"}}));
        System.out.println(combinator(new String[][]{{"abcd"}, {"efgh"}, {"ijkl"}}));
        System.out.println(combinator(new String[][]{{}}));
        System.out.println(combinator(new String[][]{{"a", "b"}, {}, {"e", "f"}}));
        System.out.println(combinator(new String[][]{{}, {"e", "f"}}));
    }
}
