# Write your code for lab 8d here.

from test_driver import store_test_case, run_free_spans_tests


# Create additional test cases, and add to them to create_tests_for_free_span().

def create_tests_for_free_span() -> dict:
    """Create and return a number of test cases for the free_spans function"""
    test_cases = dict()


    ## 1 ##
    # - The first appointment overlaps with the interval start time.
    store_test_case(
        test_cases,
        1,
        start_str="08:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=["07:00-09:00", "13:00-18:00"],  # This day's appointments
        exp_result=["09:00-13:00", "18:00-21:00"],
    )  # Expected free time


    ## 2 ##
    # - The first appointment has the same start time as the interval.
    store_test_case(
        test_cases,
        2,
        start_str="07:00",  # Search interval starts
        end_str="23:00",  # Search interval ends
        booking_data=["07:00-09:00"],  # This day's appointments
        exp_result=["09:00-23:00"],
    )  # Expected free time


    ## 3 ##
    # - The last appointment has the same end time as the interval.
    store_test_case(
        test_cases,
        3,
        start_str="07:00",  # Search interval starts
        end_str="23:00",  # Search interval ends
        booking_data=["21:00-23:00"],  # This day's appointments
        exp_result=["07:00-21:00"],
    )  # Expected free time


    ## 4 ##
    # - The last appointment overlaps with the interval end time.
    store_test_case(
        test_cases,
        4,
        start_str="08:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=["08:30-09:00", "13:00-22:00"],  # This day's appointments
        exp_result=["08:00-08:30", "09:00-13:00"],
    )  # Expected free time

    ## 5 ##
    # - The only appointment encompasses the entire interval.
    store_test_case(
        test_cases,
        5,
        start_str="08:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=["07:00-22:00"],  # This day's appointments
        exp_result=[],
    )  # Expected free time


    ## 6 ##
    # - The only appointment encompasses the entire interval. 
    #   and has the same start and end time
    store_test_case(
        test_cases,
        6,
        start_str="08:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=["08:00-21:00"],  # This day's appointments
        exp_result=[],
    )  # Expected free time

    ## 7 ##
    # - The interval encompasses the entire day
    store_test_case(
        test_cases,
        7,
        start_str="00:00",  # Search interval starts
        end_str="23:59",  # Search interval ends
        booking_data=[],  # This day's appointments
        exp_result=["00:00-23:59"],
    )  # Expected free time

    ## 8 ##
    # - The interval start is the same as day start
    store_test_case(
        test_cases,
        8,
        start_str="00:00",  # Search interval starts
        end_str="23:00",  # Search interval ends
        booking_data=[],  # This day's appointments
        exp_result=["00:00-23:00"],
    )  # Expected free time

    ## 9 ##
    # - The interval end is the same as day end
    store_test_case(
        test_cases,
        9,
        start_str="01:00",  # Search interval starts
        end_str="23:59",  # Search interval ends
        booking_data=[],  # This day's appointments
        exp_result=["01:00-23:59"],
    )  # Expected free time

    ## 10 ##
    # - The interval encompasses the entire day 
    #   and there is one booking in the middle of the day
    store_test_case(
        test_cases,
        10,
        start_str="00:00",  # Search interval starts
        end_str="23:59",  # Search interval ends
        booking_data=["12:00-13:00"],  # This day's appointments
        exp_result=["00:00-12:00", "13:00-23:59"],
    )  # Expected free time

    ## 11 ##
    # - The interval encompasses the entire day 
    #   and there is one booking in the middle of the day
    #   which also encompasses the entire day
    store_test_case(
        test_cases,
        11,
        start_str="00:00",  # Search interval starts
        end_str="23:59",  # Search interval ends
        booking_data=["00:00-23:59"],  # This day's appointments
        exp_result=[],
    )  # Expected free time

    ## 12 ##
    # - The interval encompasses the entire day 
    #   and there is one booking in the middle of the day
    #   which has the same end time as the day
    store_test_case(
        test_cases,
        12,
        start_str="00:00",  # Search interval starts
        end_str="23:59",  # Search interval ends
        booking_data=["14:00-23:59"],  # This day's appointments
        exp_result=["00:00-14:00"],
    )  # Expected free time

    ## 13 ##
    # - The interval encompasses the entire day 
    #   and there is one booking in the middle of the day
    #   which has the same start time as the day
    store_test_case(
        test_cases,
        13,
        start_str="00:00",  # Search interval starts
        end_str="23:59",  # Search interval ends
        booking_data=["00:00-14:00"],  # This day's appointments
        exp_result=["14:00-23:59"],
    )  # Expected free time

    ## 14 ##
    # - The interval encompasses the entire day 
    #   and there is several bookings in the middle of the day
    store_test_case(
        test_cases,
        14,
        start_str="00:00",  # Search interval starts
        end_str="23:59",  # Search interval ends
        booking_data=["01:00-14:00", "15:00-16:00"],  # This day's appointments
        exp_result=["00:00-01:00", "14:00-15:00", "16:00-23:59"],
    )  # Expected free time

    ## 15 ##
    # - The interval encompasses the entire day 
    #   and there are several bookings in the middle of the day
    #   one of which has the same start time as the day
    store_test_case(
        test_cases,
        15,
        start_str="00:00",  # Search interval starts
        end_str="23:59",  # Search interval ends
        booking_data=["00:00-14:00", "15:00-16:00"],  # This day's appointments
        exp_result=["14:00-15:00", "16:00-23:59"],
    )  # Expected free time

    ## 16 ##
    # - The interval encompasses the entire day 
    #   and there are several bookings in the middle of the day
    #   one of which has the same end time as the day
    store_test_case(
        test_cases,
        16,
        start_str="00:00",  # Search interval starts
        end_str="23:59",  # Search interval ends
        booking_data=["01:00-14:00", "15:00-23:59"],  # This day's appointments
        exp_result=["00:00-01:00", "14:00-15:00"],
    )  # Expected free time

    ## 17 ##
    # - The interval encompasses the entire day 
    #   and there are two bookings in the middle of the day
    #   both which has start and end times which overlap with
    #   the day start and end times respectively
    store_test_case(
        test_cases,
        17,
        start_str="00:00",  # Search interval starts
        end_str="23:59",  # Search interval ends
        booking_data=["00:00-14:00", "15:00-23:59"],  # This day's appointments
        exp_result=["14:00-15:00"],
    )  # Expected free time

    




    print("Test cases generated.")

    return test_cases


if __name__ == '__main__':
    # Actually run the tests, using the test driver functions
    tests = create_tests_for_free_span()
    run_free_spans_tests(tests)
