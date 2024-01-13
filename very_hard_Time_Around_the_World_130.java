import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.Locale;

public class very_hard_Time_Around_the_World_130 {

    private static final HashMap<String, String> GMT = new HashMap<>();

    static {
        GMT.put("Los Angeles", "-08:00");
        GMT.put("New York", "-05:00");
        GMT.put("Caracas", "-04:30");
        GMT.put("Buenos Aires", "-3:00");
        GMT.put("London", "00:00");
        GMT.put("Rome", "+01:00");
        GMT.put("Moscow", "+03:00");
        GMT.put("Tehran", "+03:30");
        GMT.put("New Delhi", "+05:30");
        GMT.put("Beijing", "+08:00");
        GMT.put("Canberra", "+10:00");
    }

    public static String timeDifference(String cityA, String timestamp, String cityB) throws ParseException {
        SimpleDateFormat inputFormat = new SimpleDateFormat("MMMM d, yyyy HH:mm", Locale.ENGLISH);

        Date inputDateTime = inputFormat.parse(timestamp);

        int[] gmtCityA = getHourMinute(cityA);
        int[] gmtCityB = getHourMinute(cityB);

        int offsetA = GMT.get(cityA).charAt(0) == '-' ? 1 : -1;
        int offsetB = GMT.get(cityB).charAt(0) == '-' ? -1 : 1;

        Date outputDateTime = new Date(inputDateTime.getTime() + offsetA * (gmtCityA[0] * 60 + gmtCityA[1]) * 60 * 1000);
        outputDateTime.setTime(outputDateTime.getTime() + offsetB * (gmtCityB[0] * 60 + gmtCityB[1]) * 60 * 1000);

        SimpleDateFormat outputFormat = new SimpleDateFormat("yyyy-M-d HH:mm");
        return outputFormat.format(outputDateTime);
    }

    private static int[] getHourMinute(String city) {
        String[] parts = GMT.get(city).substring(1).split(":");
        int hours = Integer.parseInt(parts[0]);
        int minutes = Integer.parseInt(parts[1]);
        return new int[]{hours, minutes};
    }

    public static void main(String[] args) throws ParseException {
        System.out.println(timeDifference("Los Angeles", "April 1, 2011 23:23", "Canberra"));
        System.out.println(timeDifference("London", "July 31, 1983 23:01", "Rome"));
        System.out.println(timeDifference("New York", "December 31, 1970 13:40", "Beijing"));
        System.out.println(timeDifference("London", "August 20, 1985 12:23", "Buenos Aires"));
        System.out.println(timeDifference("Rome", "December 21, 1987 15:11", "New Delhi"));
        System.out.println(timeDifference("Canberra", "March 1, 2009 18:32", "Caracas"));
        System.out.println(timeDifference("Moscow", "September 14, 1953 19:54", "New York"));
        System.out.println(timeDifference("Beijing", "November 18, 1999 02:03", "New Delhi"));
    }
}
