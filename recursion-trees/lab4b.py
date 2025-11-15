
def interpret(expression, true_or_false):
    """Find out if the expression is true or false."""

    # If the expression is a lone string (leaf),
    # check the bool for that specific expression
    if expression == "true" or expression == "false":
        return expression
    
    elif isinstance(expression, str):
        return true_or_false[expression]

    elif isinstance(expression, list):
        operator = expression[-2]

    # If the one sub-expression is true, return it
    # as false and vice versa.
    if operator == "NOT":
        if interpret(expression[1], true_or_false) == "true":
            return "false"
        elif interpret(expression[1], true_or_false) == "false":
            return "true"

    # If both sub-expressions are true, the entire
    # expression is interpreted as true.
    if operator == "AND":
        if interpret(expression[0], true_or_false) == "true" and interpret(expression[2], true_or_false) == "true":
            return "true"
        else:
            return "false"

    # If one of the two sub-expressions is true, the entire
    # expression is interpreted as true. 
    if operator == "OR":
        if interpret(expression[0], true_or_false) == "true" or interpret(expression[2], true_or_false) == "true":
            return "true"
        else:
            return "false"
    




print(interpret(["door_open", "AND", "cat_gone"], 
               {"door_open" : "false", "cat_gone" : "true", "cat_asleep" : "true"} ))
