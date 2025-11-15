
# Global constants which contain the allowed letter for each part of the message.
ALLOWED_CHARACTERS_1 = "abcdefghijklmnopqrstopqrstuvwxyzåäö_."
ALLOWED_CHARACTERS_2 = "ABCDEFGHIJKLMNOPQRSTOPQRSTUVWXYZÅÄÖ |"

def split_it(message):
    """
    Iterative function which splits a message in two parts
    based on what characters it contains.
    """

    first_message = ""
    second_message = ""

    # Iterate through the message and separate
    # into two based on the characters:
    for character in message:
        if character in ALLOWED_CHARACTERS_1:
            first_message += character
        if character in ALLOWED_CHARACTERS_2:
            second_message += character
    
    return first_message, second_message


def split_rec(message):
    """
    Recursive function which splits a message in two parts
    based on what characters it contains.
    """

    # Recursion stop condition:
    if not message:
        return ["", ""]
    
    # Split the message:
    else:
        character = message[0]
        message_tuple = split_rec(message[1:])
        if character in ALLOWED_CHARACTERS_1:
            message_tuple = (character + message_tuple[0], message_tuple[1])
        if character in ALLOWED_CHARACTERS_2:
            message_tuple = (message_tuple[0], character + message_tuple[1])
        return message_tuple

print(split_rec("'lMiED)teD5E,_hLAe;Nm,0@Dli&Eg ,#4aI?rN@T§&wetwbj  etgowjebgobSDF AJe7#4E #<(S0A?<)NT8<0'"))
print(split_it("'lMiED)teD5E,_hLAe;Nm,0@Dli&Eg ,#4aI?rN@T§&e7#4E #<(S0A?<)NT8<0'"))




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
