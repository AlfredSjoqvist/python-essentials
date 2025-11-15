
from tkinter import S
import calc


def exec_program(p, variable_table={}):
    """Execute a calc program."""

    #-- Check if p is a program.
    if calc.is_program(p):
        s = calc.program_statements(p)      # If p is a program, remove the initial calc string and keep all the statements.
        return exec_statements(s, variable_table)
    else:
        print("no program")                 # If p is no program, return None and raise error.
        return


def exec_statements(s, calc_variables):
    """Execute a chain of statements."""

    if calc.is_statements(s):
        calc_variables = exec_statement(calc.first_statement(s), calc_variables)
        return exec_statements(calc.rest_statements(s), calc_variables)
    else:
        return calc_variables


def exec_statement(s, calc_variables):
    """Detect statement type and execute it accordingly."""

    if calc.is_assignment(s):
        return exec_assignment(s, calc_variables)

    elif calc.is_repetition(s):
        return exec_repetition(s, calc_variables)

    elif calc.is_selection(s):
        return exec_selection(s, calc_variables)
        
    elif calc.is_input(s):
        return exec_input(s, calc_variables)

    elif calc.is_output(s):
        return exec_output(s, calc_variables)
    else:
        raise TypeError


def exec_assignment(s, calc_variables):
    """Assign a value to a variable."""

    modified_calc_variables = calc_variables.copy() 
    modified_calc_variables.update({calc.assignment_variable(s) : eval_expression(calc.assignment_expression(s), modified_calc_variables)}) 
    
    return modified_calc_variables


def exec_repetition(s, calc_variables):
    """Loop through statement(s)."""

    while eval_condition(calc.repetition_condition(s), calc_variables):
        calc_variables.update(exec_statements(calc.repetition_statements(s), calc_variables))

    return calc_variables


def exec_selection(s, calc_variables):
    """Execute a statement if a condition is fulfilled."""

    if eval_condition(calc.selection_condition(s), calc_variables):
        return exec_statement(calc.selection_true_branch(s), calc_variables)
    elif calc.selection_has_false_branch(s):
        return exec_statement(calc.selection_false_branch(s), calc_variables)
    else:
        return calc_variables


def exec_input(s, calc_variables):
    """Take an input value from the user and assign it to a variable."""

    inp = input("Enter value for " + calc.input_variable(s) + ": ")
    
    modified_calc_variables = calc_variables.copy() 
    modified_calc_variables.update({calc.input_variable(s) : int(inp)}) 
    
    return modified_calc_variables


def exec_output(s, calc_variables):
    """
    If the expression is a variable, print it and its assigned value. 
    If it is instead just a pure value, just print the value.
    """

    if calc.is_variable(calc.output_expression(s)):
        print(f"{calc.output_expression(s)} = {eval_expression(calc.output_expression(s), calc_variables)}")
    else:
        print(eval_expression(calc.output_expression(s), calc_variables))

    return calc_variables


def eval_expression(s, calc_variables):
    """Detect expression type and evaluate it accordingly."""
    
    if calc.is_binaryexpr(s):
        return eval_binaryexpr(s, calc_variables)

    elif calc.is_variable(s):
        return eval_variable(s, calc_variables)

    elif calc.is_constant(s):
        return eval_constant(s)
    
    else:
        raise TypeError


def eval_binaryexpr(s, calc_variables):
    """Detect binary expression type and evaluate it based on the operator."""

    if calc.binaryexpr_operator(s) == "+":
        return eval_expression(calc.condition_left(s), calc_variables) + eval_expression(calc.condition_right(s), calc_variables)
    elif calc.binaryexpr_operator(s) == "*":
        return eval_expression(calc.condition_left(s), calc_variables) * eval_expression(calc.condition_right(s), calc_variables)
    elif calc.binaryexpr_operator(s) == "-":
        return eval_expression(calc.condition_left(s), calc_variables) - eval_expression(calc.condition_right(s), calc_variables)
    elif calc.binaryexpr_operator(s) == "/":
        return eval_expression(calc.condition_left(s), calc_variables) / eval_expression(calc.condition_right(s), calc_variables)
    else:
        raise TypeError

def eval_condition(s, calc_variables):
    """Detect condition type and evaluate it based on the operator."""
    
    if calc.condition_operator(s) == ">":
        return eval_expression(calc.condition_left(s), calc_variables) > eval_expression(calc.condition_right(s), calc_variables)
    elif calc.condition_operator(s) == "<":
        return eval_expression(calc.condition_left(s), calc_variables) < eval_expression(calc.condition_right(s), calc_variables)
    elif calc.condition_operator(s) == "=":
        return eval_expression(calc.condition_left(s), calc_variables) == eval_expression(calc.condition_right(s), calc_variables)
    else:
        raise TypeError

def eval_variable(s, calc_variables):
    """Translate a variable to its assigned value."""

    try:                           # Try-except statement to handle if the variable is not assigned.
        return calc_variables[s]
    except KeyError:
        return


def eval_constant(s):
    """Return a constant."""

    return s


program1 = ['calc', ['if', [3, '=', 3], ['print', 2], ['print', 4]]]
program2 = ["calc", ["set", "counter", 1], ["while", ["counter", "<", 5], ["print", "counter"], ["set", "counter", ["counter", "+", 1]]]]
program3 = ["calc", ["set", "counter", 1], ["print", "counter"], ["set", "counter", ["counter", "+", 1]], ["print", "counter"]]
program4 = ["calc", ["set", "a", [[5, "+", 1], "+", 5]], ["print", "a"]]
program5 = ["calc", ["read", "p1"], ["print", "p1"]]
program6 = ["calc", ["set", "counter", 1], ["set", "counter", 5], ["print", "counter"]]
program7 = ["calc", ["print", ["a", "/", 8]], ["set", "b", 1], ["set", "a", 33]]

programs = [program1, program2, program3, program4, program5, program6]

# Test all the different statement types
for i in range(0, 6):
    print(f"Program: {str(i+1)}")
    program = programs[i]
    print(exec_program(program))
    print("")

# Test destructiveness
print(f"Program: 7")
my_table = {"a": 41212}
new_table = exec_program(program7, my_table)
print(my_table)
print(new_table)
