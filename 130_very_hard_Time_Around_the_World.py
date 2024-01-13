"""
Time Around the World
In this challenge, the goal is to calculate what time it is in two different cities. You're given a string city_a and the related string timestamp (time in city_a) with the date formatted in full U.S. notation, as in this example:

"July 21, 1983 23:01"
You have to return a new timestamp with date and corresponding time in city_b, formatted as in this example:

"1983-7-22 23:01"
See the table below for a list of given cities and their GMT (Greenwich Mean Time) hours offsets.

GMT	City
- 08:00	Los Angeles
- 05:00	New York
- 04:30	Caracas
- 03:00	Buenos Aires
00:00	London
+ 01:00	Rome
+ 03:00	Moscow
+ 03:30	Tehran
+ 05:30	New Delhi
+ 08:00	Beijing
+ 10:00	Canberra
Examples
time_difference("Los Angeles", "April 1, 2011 23:23", "Canberra") ➞ "2011-4-2 17:23"
# Can be a new day.

time_difference("London", "July 31, 1983 23:01", "Rome") ➞ "1983-8-1 00:01"
# Can be a new month.

time_difference("New York", "December 31, 1970 13:40", "Beijing") ➞ "1971-1-1 02:40"
# Can be a new year.
Notes
Pay attention to hours and minutes, a leading 0 is needed in the returned timestamp when they're a single digit.
Pay attention to cities with half hours offsets.
"""

from datetime import datetime, timedelta

GMT = {
    "Los Angeles": "-08:00",
    "New York": "-05:00",
    "Caracas": "-04:30",
    "Buenos Aires": "-3:00",
    "London": "00:00",
    "Rome": "+01:00",
    "Moscow": "+03:00",
    "Tehran": "+03:30",
    "New Delhi": "+05:30",
    "Beijing": "+08:00",
    "Canberra": "+10:00",
}

def time_difference(city_a, timestamp, city_b):

    timestamp = datetime.strptime(timestamp, "%B %d, %Y %H:%M")
    gmt_city_a = get_hour_minute(city_a)
    gmt_city_b = get_hour_minute(city_b)

    offset_a = 1 if GMT[city_a][0] == '-' else -1
    offset_b = -1 if GMT[city_b][0] == '-' else 1

    output_datetime = timestamp + offset_a * timedelta(hours=gmt_city_a[0], minutes=gmt_city_a[1])
    output_datetime = output_datetime + offset_b * timedelta(hours=gmt_city_b[0], minutes=gmt_city_b[1])
    result = datetime.strptime(str(output_datetime), "%Y-%m-%d %H:%M:%S")
    result = "{}-{}-{} {:02d}:{:02d}".format(result.year, result.month, result.day, result.hour, result.minute)

    return result


def get_hour_minute(city):
    city_time_int = datetime.strptime(GMT[city][1:], "%H:%M")
    return city_time_int.hour, city_time_int.minute


print(time_difference("Los Angeles", "April 1, 2011 23:23", "Canberra"))
print(time_difference("London", "July 31, 1983 23:01", "Rome"))
print(time_difference("New York", "December 31, 1970 13:40", "Beijing"))
print(time_difference("London", "August 20, 1985 12:23", "Buenos Aires"))
print(time_difference("Rome", "December 21, 1987 15:11", "New Delhi"))
print(time_difference("Canberra", "March 1, 2009 18:32", "Caracas"))
print(time_difference("Moscow", "September 14, 1953 19:54", "New York"))
print(time_difference("Beijing", "November 18, 1999 02:03", "New Delhi"))
print(time_difference("Tehran", "June 3, 1977 11:18", "Moscow"))