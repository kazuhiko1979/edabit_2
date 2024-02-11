public class very_hard_Pilish_Strings_136 {

    public static String pilishString(String txt){
        String piDigits = "314159265358979";
        StringBuilder sb = new StringBuilder();
        int piIndex = 0;

        while (!txt.isEmpty() && piIndex < piDigits.length()){
            int wordLength = Character.getNumericValue(piDigits.charAt(piIndex));
            if(txt.length() >= wordLength){
                sb.append(txt.substring(0, wordLength)).append(" ");
                txt = txt.substring(wordLength);
            } else {
                sb.append(txt).append(String.valueOf(txt.charAt(txt.length() - 1)).repeat(Math.max(0, wordLength - txt.length()))).append(" ");
                txt = "";
            }
            piIndex++;
        }
        return sb.toString().trim();
    }

    public static void main(String[] args) {
        System.out.println(pilishString("FORALOOP"));
        System.out.println(pilishString("CANIMAKEAGUESS"));
        System.out.println(pilishString("CANIMAKEAGUESSNOW"));
        System.out.println(pilishString("X"));
        System.out.println(pilishString("ARANDOMSEQUENCEOFLETTERS"));
        System.out.println(pilishString(""));
        System.out.println(pilishString("33314444155555999999999226666665555533355555888888889999999997777777999999999"));
        System.out.println(pilishString("###*@"));
        System.out.println(pilishString(".........."));
        System.out.println(pilishString("NowIfallAtiredsuburbianInliquidunderthetreesDriftingalongsideforestssimm"));
        System.out.println(pilishString("HOWINEEDADRINKALCOHOLICINNATUREAFTERTHEHEAVYLECTURESINVOLVINGQUANTUMMECHANICSANDALLTHESECRETSOFTHEUNIVERSE"));
        System.out.println(pilishString("HOWINEEDADRINKALCOHOLICINNATUREAFTERTHEHEAVYCODING"));
    }
}