#!/usr/bin/pthon
# encoding: utf8
'''
Weekend Programming Challenge week 46
http://olimex.wordpress.com/2014/03/14/weekend-programming-challenge-week-46-clock-arrows/
Matthias Schmitz <matthias@sigxcpu.org>

The hour hand needs 12h to travel 360° (30°/h , 0.5°/min, 0,008333333°/sec ).

The minute hand needs one hour for the full 360° (6°/min, 0.1°/sec).

We can calculate the angle for the both clock hands for every second and
compare them. When the angles are (nearly) equal the clock hands meet each
other.

'''

# constants how many degree per second the hour hand move
HOUR_DEG_PER_SEC = 360.0 / 12 / 60 / 60  # 0.008333...°


def minute_to_degree(minute, second=0):
    ''' (int, int) -> float
    Calculate the angle of the minute clock hand from a given minute.
    If no second is provided 0 is assumed.

    >>> minute_to_degree(0)
    0.0
    >>> minute_to_degree(12)
    72.0
    >>> minute_to_degree(35, 45)
    214.5
    '''
    return (minute * 6.0 + second * 0.1)


def hour_to_degree(hour, minute=0, second=0):
    ''' (int, int, int) -> float
    Calculate the angle of the hour clock hand for a given hour,
    minute and second.
    >>> hour_to_degree(0, 0)
    0.0
    >>> hour_to_degree(11, 59)
    359.5
    '''
    return ((hour * 30.0) + (minute * 0.5) + (second * HOUR_DEG_PER_SEC))


def time_to_degrees(hour, minute, second):
    ''' (int, int, int) -> tuple
    Calculate the angles of hour hand, minute hand and second hand for
    a given time.

    Returns a tuple containing the angles for hour, minute and second hand:
    >>> time_to_degrees(0, 0, 0)
    (0.0, 0.0, 0.0)
    >>> time_to_degrees(6, 6, 6)
    (183.05, 36.6, 36.0)
    >>> time_to_degrees(11, 59, 59)
    (359.9916666666667, 359.9, 354.0)

    '''

    return ((hour_to_degree(hour, minute, second),
            minute_to_degree(minute, second),
            second * 6.0))


def main():
    meet_times = []
    for hour in range(0, 12):
        for minute in range(0, 60):
            for second in range(0, 60):
                angle_hour, angle_minute, c = time_to_degrees(hour,
                                                              minute,
                                                              second)

                # if the angles are nearly equal
                if int(angle_hour * 10) == int(angle_minute * 10):
                    meet_times.append((hour, minute, second))

    print "The clock hands meet each other %i times per 12 hours." % len(meet_times)
    for time in meet_times:
        print "%02i:%02i:%02i" % time


if __name__ == '__main__':
    main()
