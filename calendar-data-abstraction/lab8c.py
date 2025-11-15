# Write your code for lab 8C (remove) here.

from cal_ui import *
from cal_abstraction import *


# Tester

def remove(input_cal_name: str, input_day: int, input_month: str, input_start_time: str):
    """
    Remove an appointment with the specified
    start time from the given calendar year.

    This function belongs in cal_ui.py
    """

    # Get correct year:
    correct_cal_year = get_calendar(input_cal_name)

    # Get correct month:
    regular_input_month = new_month(input_month)

    # Get correct day:
    regular_input_day = new_day(input_day)

    # Get correct start time:
    input_regular_start_time = new_time_from_string(input_start_time)

    # Create empty calendar data type instances:
    updated_cal_year = new_calendar_year()
    updated_cal_month = new_calendar_month(regular_input_month)
    updated_cal_day = new_calendar_day(regular_input_day)

    # Check if an appointment actually has been removed:
    appointment_removed = False


    def loop_elements(correct_element: CalendarYear or CalendarMonth or CalendarDay or Appointment) -> CalendarYear or CalendarMonth or CalendarDay or None:
        """
        Inner function that loops through the 
        specified calendar element type.
        """

        # Recursive stop condition
        if isinstance(correct_element, Appointment):
            nonlocal appointment_removed
            appointment_removed = True
            return None
    
        else:

            iterator, converter, adder, regular_input_value, updated_cal_object = get_loop_values(correct_element)

            # Loop through the calendar object
            for calendar_element in iterator(correct_element):

                regular_element = converter(calendar_element)

                # If the element that is to be removed is found, mark it
                if regular_input_value == regular_element:

                    new_correct_element = calendar_element
                    
                else:
                    updated_cal_object = adder(updated_cal_object, calendar_element)
                    continue
            
                # Loop the element that should be removed on one level lower
                lower_updated_cal_object = loop_elements(new_correct_element)

                # If the recursion has not reached the bottom, 
                # add the smaller calendar element to the larger calendar element
                if lower_updated_cal_object:
                    updated_cal_object = adder(updated_cal_object, lower_updated_cal_object)
            
            return updated_cal_object


    def get_loop_values(correct_element: CalendarYear or CalendarMonth or CalendarDay) -> tuple:
        """Get the specific values for the loop."""

        # return [iterator] [converter] [adder] [regular element] [calendar object to update]

        if isinstance(correct_element, CalendarYear):
            return cy_iter_months, cm_month, cy_plus_cm, regular_input_month, updated_cal_year
        elif isinstance(correct_element, CalendarMonth):
            return cm_iter_days, cd_day, cm_plus_cd, regular_input_day, updated_cal_month
        elif isinstance(correct_element, CalendarDay):
            return cd_iter_appointments, get_start_time, cd_plus_appointment, input_regular_start_time, updated_cal_day

    # Start the loops
    updated_cal_year = loop_elements(correct_cal_year)

    if appointment_removed:
        print("Appointment removed.")
    else:
        print("The appointment did not exist in the calendar.")

    insert_calendar(input_cal_name, updated_cal_year)


def get_start_time(ts: Appointment) -> Time:
    """
    Combines two helper functions from cal_abstraction.
    This function belongs in cal_abstraction.py
    """

    return ts_start(app_span(ts))



create("Jayne")
book("Jayne", 20, "sep", "12:00", "14:00", "Rob train")
book("Jayne", 20, "sep", "15:00", "16:00", "Escape with loot")
show("Jayne", 20, "sep")

remove("Jayne", 20, "sep", "15:00")

show("Jayne", 20, "sep")

create("Random Cal")
# Test remove same appointment twice
book("Random Cal", 15, "dec", "13:30", "17:00", "Finish lab")
book("Random Cal", 15, "dec", "17:00", "18:00", "Test")
show("Random Cal", 15, "dec")

remove("Random Cal", 15, "dec", "13:30")
remove("Random Cal", 15, "dec", "13:30")
show("Random Cal", 15, "dec")

# Test remove one appointment when there are two in different months
book("Random Cal", 15, "dec", "13:30", "17:00", "Finish lab")
book("Random Cal", 20, "jul", "15:00", "20:00", "Deadline")
show("Random Cal", 15, "dec")
show("Random Cal", 20, "jul")

remove("Random Cal", 20, "jul", "15:00")
show("Random Cal", 15, "dec")
show("Random Cal", 20, "jul")

# Test last day of month and start and short time span
book("Random Cal", 31, "jul", "21:00", "21:01", "Deadline")
show("Random Cal", 31, "jul")
remove("Random Cal", 31, "jul", "21:00")
show("Random Cal", 31, "jul")

# Test removing appointment thatg doesn't exist
remove("Random Cal", 19, "jan", "21:00")
show("Random Cal", 19, "jan")