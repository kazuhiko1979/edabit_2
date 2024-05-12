"""
Clock Hands
Create a function whose argument is the time in 12 hour format (hh:mm:ss). The function returns the smaller angle between the hour and minute hands in degrees, rounded to three decimal points.

Examples
clock("12:00:00") ➞ 0.0

clock("12:15:00") ➞ 82.5

clock("12:32:44") ➞ 179.967

clock("03:33:33") ➞ 94.525
"""
def clock(time):

    h, m, s = [int(i) for i in time.split(':')]
    h_hand = (h + m / 60 + s/ 3600)*30
    m_hand = (m + s / 60) * 6
    angle = abs(h_hand - m_hand)

    if angle > 180:
        angle = 360 - angle
    return round(angle, 3)

print(clock("12:00:00"))
print(clock("12:15:00"))
print(clock("12:32:44"))
print(clock("03:33:33"))
print(clock("01:59:59"))



