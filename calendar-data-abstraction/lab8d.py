# Write your code for lab 8d here.
from cal_abstraction import *  #  Previous: CalendarDay, Time
from settings import CHECK_AGAINST_FACIT
from cal_ui import *

if CHECK_AGAINST_FACIT:
    try:
        from facit_la8_uppg import TimeSpanSeq
    except:
        print("*" * 100)
        print("*" * 100)
        print("Kan inte hitta facit; ändra CHECK_AGAINST_FACIT i test_driver.py till False")
        print("*" * 100)
        print("*" * 100)
        raise
else:
    from lab8b import *


def free_spans(cal_day: CalendarDay, start: Time, end: Time) -> TimeSpanSeq:
    """
    Check what timespans are free during a given interval in a calendar day.

    The function works by first adding the timespan between the start of the
    day and the start of the defined interval and the time between the end of
    the interval and the end of the day and then add them to the TimeSpanSeq
    that contains the bookings, booked_tss.

    Later the function iterates through all the bookings, including the timespans
    at the start and end of the day and "inverts" the timespans and adds them into
    another TimeSpanSeq called unbooked_tss. Basically the loop at the end of the
    function iterates through the timespans and assigns the new unbooked timespans
    with the same start time as the previous booked timespan's end time and the 
    unbooked timespan's end time as the next booked timespan's start time and
    continues like this for all bookings.

    This gives us some edge cases, for example when the start times and/or end times
    is the same as the start times and/or end times for the day. How these are
    handled is documented below.
    """

    # Define the start and end of a day
    day_start = new_time_from_string("00:00")
    day_end = new_time_from_string("23:59")

    booked_tss = new_time_span_seq()
    unbooked_tss = new_time_span_seq()
    booked_end = None

    # Add the parts of the day that is outside the interval to the bookings
    if not time_equals(day_start, start):
        outside_interval_start = new_time_span(day_start, start)
        booked_tss = tss_plus_span(booked_tss, outside_interval_start)

    if not time_equals(day_end, end):
        outside_interval_end = new_time_span(end, day_end)
        booked_tss = tss_plus_span(booked_tss, outside_interval_end)

    # Add the timespans in the calendar day to the bookings
    for app in cd_iter_appointments(cal_day):
        app_ts = app_span(app)
        booked_tss = tss_plus_span(booked_tss, app_ts)
    
    # EDGE CASE: This if statement is run if and only if the interval
    # encompasses the entire day and there is no booked appointments
    # during the interval:
    if tss_is_empty(booked_tss):
        free_day = new_time_span(day_start, day_end)
        unbooked_tss = tss_plus_span(unbooked_tss, free_day)

    # Iterate through the booked spans and "reverse" the timespan sequence
    # so it gives back all times which are not included.
    for ts in tss_iter_spans(booked_tss):
        
        # On the first iteration do nothing, booked_end
        # will be defined during the second iteration.
        if booked_end:
            unbooked_start = booked_end
            unbooked_end = ts_start(ts)

            # If there are overlapping booking times,
            # no need to add anything unbooked.
            if time_precedes(unbooked_start, unbooked_end):
                unbooked_ts = new_time_span(unbooked_start, unbooked_end)
                unbooked_tss = tss_plus_span(unbooked_tss, unbooked_ts)

        # EDGE CASE: This statement is run if and only if the start time
        # of the day is the same as the start of the interval because
        # the loop doesn't do what it should otherwise because no booking
        # is added to booked_tss in the beginning that makes it iterate
        # correctly. So this is just an "extra iteration" at the start of 
        # the loop which covers this specific case.
        elif time_equals(day_start, start):
            unbooked_start = day_start
            unbooked_end = ts_start(ts)

            if time_precedes(unbooked_start, unbooked_end):
                unbooked_ts = new_time_span(unbooked_start, unbooked_end)
                unbooked_tss = tss_plus_span(unbooked_tss, unbooked_ts)

        # Save the end of the timespan for the next iteration.
        booked_end = ts_end(ts)

    if not tss_is_empty(booked_tss):
        # EDGE CASE: This statement is run if and only if the end time
        # of the day is the same as the end of the interval because
        # the loop doesn't do what it should otherwise because no booking
        # is added to booked_tss in the end that makes it iterate
        # correctly. So this is just an "extra iteration" at the end of 
        # the loop which covers this specific case.
        if time_equals(day_end, end):
            unbooked_start = booked_end
            unbooked_end = day_end

            if time_precedes(unbooked_start, unbooked_end):
                unbooked_ts = new_time_span(unbooked_start, unbooked_end)
                unbooked_tss = tss_plus_span(unbooked_tss, unbooked_ts)

    return unbooked_tss


def show_free(cal_name: str, day: int, month: str, start: str, end: str) -> str:
    """
    Shows all free timeslot in a specified day.
    """

    # Get correct cal year:
    correct_cal_year = get_calendar(cal_name)

    # Get correct cal month:
    regular_input_month = new_month(month)
    correct_cal_month = cy_get_month(regular_input_month, correct_cal_year)

    # Get correct cal day:
    regular_input_day = new_day(day)
    correct_cal_day = cm_get_day(correct_cal_month, regular_input_day)

    # Get correct start and end time:
    correct_start = new_time_from_string(start)
    correct_end = new_time_from_string(end)

    # Get all free spans in the correct cal day:
    free_tss = free_spans(correct_cal_day, correct_start, correct_end)

    # Print all available time spans.
    show_time_spans(free_tss)

create("JJ")
book("JJ", 20, "sep", "12:00", "14:00", "Rob train")
book("JJ", 20, "sep", "15:00", "16:00", "Escape with loot")
show_free("JJ", 20, "sep", "08:00", "19:00")