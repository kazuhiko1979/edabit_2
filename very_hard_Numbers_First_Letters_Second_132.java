import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class very_hard_Numbers_First_Letters_Second_132 {

        public static List<List<Object>> num_then_char(List<List<Object>> lsts){
            List<Object> nums = new ArrayList<>();
            List<Object> letters = new ArrayList<>();

            // 数字と文字を分類
            for (List<Object> lst : lsts){
                for (Object a : lst){
                    if (a instanceof String){
                        letters.add(a);
                    } else{
                        nums.add(a);
                    }
                }
            }

            // ソート
            nums.sort(new Comparator<Object>() {
            @Override
            public int compare(Object o1, Object o2) {
                if (o1 instanceof Integer && o2 instanceof Integer) {
                    return ((Integer) o1).compareTo((Integer) o2);
                } else if (o1 instanceof Double && o2 instanceof Double) {
                    return ((Double) o1).compareTo((Double) o2);
                }
                return 0;
                }
            });

            Collections.sort(letters, new Comparator<Object>() {
                @Override
                public int compare(Object o1, Object o2) {
                    return o1.toString().compareTo(o2.toString());
                }
            });

            // Collections.sort(nums, (a, b) -> {
            //     if (a instanceof Integer && b instanceof Integer) {
            //         return (Integer) a - (Integer) b;
            //     } else if (a instanceof Double && b instanceof Double){
            //         return Double.compare((Double) a, (Double) b);
            //     }
            //     return 0;
            // });
            // Collections.sort(letters);


            List<Object> sortedList = new ArrayList<>();
            sortedList.addAll(nums);
            sortedList.addAll(letters);

            // リストを更新
            int index = 0;
            for (List<Object> lst : lsts){
                for (int j = 0; j <lst.size(); j++){
                    lst.set(j, sortedList.get(index));
                    index++;
                }
            }
            return lsts;
    }

    public static void main(String[] args) {

        List<List<Object>> lst1 = new ArrayList<>();
        lst1.add(new ArrayList<>(List.of(1, 2, 4, 3, "a", "b")));
        lst1.add(new ArrayList<>(List.of(6, "c", 5)));
        lst1.add(new ArrayList<>(List.of(7, "d")));
        lst1.add(new ArrayList<>(List.of("f", "e", 8)));

        List<List<Object>> lst2 = new ArrayList<>();
        lst2.add(new ArrayList<>(List.of(1, 2, 4.4, "f", "a", "b")));
        lst2.add(new ArrayList<>(List.of(0)));
        lst2.add(new ArrayList<>(List.of(0.5, "d", "X", 3, "s")));
        lst2.add(new ArrayList<>(List.of("f", "e", 8)));
        lst2.add(new ArrayList<>(List.of("p", "Y", "Z")));
        lst2.add(new ArrayList<>(List.of(12, 18)));

        List<List<Object>> lst3 = new ArrayList<>();
        lst3.add(new ArrayList<>(List.of(10, 2)));
        lst3.add(new ArrayList<>(List.of("a", 3)));
        lst3.add(new ArrayList<>(List.of(2.2, "d", "h", 6, "s", 14, 1)));
        lst3.add(new ArrayList<>(List.of("f", "e")));
        lst3.add(new ArrayList<>(List.of("p", "y", "z", "V")));
        lst3.add(new ArrayList<>(List.of(5)));

        List<List<Object>> lst4 = new ArrayList<>();
        lst4.add(new ArrayList<>(List.of(10, 2, 6, 6.5, 8.1, "q", "w", "a", "s")));
        lst4.add(new ArrayList<>(List.of("f", 4)));
        lst4.add(new ArrayList<>(List.of(2, 3, "h", 6, "x", 1, 0)));
        lst4.add(new ArrayList<>(List.of("g")));
        lst4.add(new ArrayList<>(List.of("p", 7, "j", "k", "l")));
        lst4.add(new ArrayList<>(List.of(5, "C", "A", "B")));
        lst4.add(new ArrayList<>(List.of("L", 9)));

        System.out.println(num_then_char(lst1));
        System.out.println(num_then_char(lst2));
        System.out.println(num_then_char(lst3));
        System.out.println(num_then_char(lst4));
    }
}









