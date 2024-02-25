public class very_hard_String_Compression_from_Characters_Array_142 {
    public static String compress(char[] chars){
        if (chars.length == 0){
            return "";
        }

        StringBuilder compressed = new StringBuilder();
        char currentChar = chars[0];
        int count = 1;

        for (int i = 1; i < chars.length; i++){
            if (chars[i] == currentChar){
                count++;
            } else {
                compressed.append(currentChar);
                if (count > 1){
                    compressed.append(count);
                }
                currentChar = chars[i];
                count = 1;
            }
        }
        compressed.append(currentChar);
        if (count > 1){
            compressed.append(count);
        }
        return compressed.toString();
    }
    public static void main(String[] args) {
        System.out.println(compress(new char[]{'a', 'a', 'b', 'b', 'c', 'c', 'c'})); // ➞ "a2b2c3"
        System.out.println(compress(new char[]{'a'})); // ➞ "a"
        System.out.println(compress(new char[]{'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'})); // ➞ "ab12"
        System.out.println(compress(new char[]{'a', 'a', 'a', 'b', 'b', 'a', 'a'})); // ➞ "a3b2a2"
    }


}