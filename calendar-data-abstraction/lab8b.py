from cal_abstraction import *
from cal_output import *

# =========================================================================
# Type definition
# =========================================================================

# Define the type somehow...  The initial "" is simply here as a placeholder.

TimeSpanSeq = NamedTuple("TimeSpanSeq", [("time_span_list", List[TimeSpan])])

# =========================================================================
#  Function implementations
# =========================================================================

# Implement these functions!  Also determine if you need *additional* functions.

def new_time_span_seq(timespans: List[TimeSpan] = None) -> TimeSpanSeq:
    """
    Create and return a new TimeSpanSeq, 
    with the given list of TimeSpans.
    """
    if timespans is None:
        # If we use [] as a default value above, then every call to this function will
        # use the *same* list as a default value.  Instead we must use None as
        # a value, and if something empty is provided, the line below correctly
        # creates a *new* list each time.
        timespans = []
    else:
        ensure_type(timespans, List[TimeSpan])
    return TimeSpanSeq(timespans or [])


def tss_is_empty(tss: TimeSpanSeq) -> bool:
    """Return true iff the given TimeSpanSeq has no TimeSpan."""   
    ensure_type(tss, TimeSpanSeq)
    return not tss.time_span_list


def tss_plus_span(tss: TimeSpanSeq, ts: TimeSpan) -> TimeSpanSeq:
    """
    Returns a copy of the given TimeSpanSeq, where the given TimeSpan
    has been added in its proper position.
    """

    ensure_type(tss, TimeSpanSeq)
    ensure_type(ts, TimeSpan)
    new_tss = new_time_span_seq()

    def add_to(timespans: List[TimeSpan], timespan_to_add: TimeSpan) -> List[TimeSpan]:
        if not timespans:
            return [timespan_to_add]
        
        next_timespan = timespans[0]
        next_timespan_value = hour_number(time_hour(ts_start(next_timespan))) * 60 + minute_number(time_minute(ts_start(next_timespan)))
        inserted_timespan_value = hour_number(time_hour(ts_start(ts))) * 60 + minute_number(time_minute(ts_start(ts)))
    
        if inserted_timespan_value <= next_timespan_value:
            # Add the new TimeSpan at the current position
            return [timespan_to_add] + timespans
        else:
            # Need to move further
            return [next_timespan] + add_to(timespans[1:], timespan_to_add)

    return TimeSpanSeq(add_to(tss.time_span_list, ts))


def tss_iter_spans(tss: TimeSpanSeq):
    """
    To be used as `for ts in tss_iter_spans(tss)`.  
    Iterates over all TimeSpans in the TimeSpanSeq.
    """
    ensure_type(tss, TimeSpanSeq)
    for ts in tss.time_span_list:
        yield ts


def show_time_spans(tss: TimeSpanSeq):
    """
    Iterate through all the timespans and print them.
    """
    ensure_type(tss, TimeSpanSeq)
    for ts in tss_iter_spans(tss):
        show_ts(ts)
        print("")


# Keep only time spans that satisfy pred.
# You do not need to modify this function.
def tss_keep_spans(tss, pred):
    result = new_time_span_seq()

    for span in tss_iter_spans(tss):
        if pred(span):
            result = tss_plus_span(result, span)

    return result
