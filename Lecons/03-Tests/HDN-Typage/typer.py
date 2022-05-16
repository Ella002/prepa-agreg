import re
import sys
from typing import List

EXPRESSION_REGEX = "(?:\".*\")|(?:\d+)|(?:\D\S*)"

def extract_function_types(program: List[str])->dict:
    result = dict()
    for line_number, line in enumerate(program):
        match = re.match("def\s+(\D\S*)\(((\D\S*(\s*:\s*\D+)?\s*,?\s*)*)\)(\s*->\s*(\D+))?:", line)
        if match:
            function_name = match[1]
            arguments = match[2]
            type_annotation = match[6]
            # We process argument list
            if arguments !="":
                argument_list = arguments.split(",")
            else:
                argument_list = []
            argument_types = []
            for argument in argument_list:
                m = re.match("\s*(\S+)\s*:\s*(\S+)\s*", argument)
                if m:
                    if m[2] in ("int","str"):
                        argument_types.append((m[1], m[2]))
                    else:
                        argument_types.append((m[1], "UKN"))
                else:
                    argument_types.append((remove_space(argument),"?"))
            # We process possible output type
            if type_annotation:
                if type_annotation in ("int", "str"):
                    type_out = type_annotation
                else:
                    type_out = "UKN"
            else:
                type_out = "?"
            result[function_name] = (line_number, argument_types, type_out)
    return result

def remove_space(expression : str) -> str:
    match = re.match("\s*(\S+)\s*", expression)
    if match:
        expression = match[1]
    return expression


def type_expression_with_context(local_type_context: dict, expression : str) -> str:
    # We first remove any space before and after our expression
    expression = remove_space(expression)
    if re.match("\".*\"$", expression):
        return "str"
    if re.match("\d+$", expression):
        return "int"
    match = re.match("(\D\S*)$", expression)
    if match:
        if match[0] in local_type_context:
            return local_type_context[match[0]]
        else:
            return "?"
    assert False, "{} isn't an expression.".format(expression)

def unify_in_context(local_type_context: dict, key : str, target_type : str, line_number : int) -> int:
    if (key in local_type_context) and (local_type_context[key]!="?") and (target_type !="?") and (local_type_context[key]!=target_type):
        print("We met an error line {}. {} should have type {} and not {}.".format(line_number, key, local_type_context[key], target_type))
        return 1
    if target_type != "?":
        local_type_context[key] = target_type
    return 0


def check_type_function(program: List[str], function_types, function_name: str, start_line: int, argument_types, type_out) -> int:
    local_type_context = dict()
    arg_type: str
    arg_name: str

    for arg_name, arg_type in argument_types:
        local_type_context[arg_name] = arg_type

    for relative_line, line in enumerate(program[start_line+1:]):
        line_number = relative_line + start_line + 2
        if re.match("\S.*", line):
            # We arrive at the end of the function, we return
            return 0

        if re.match("\s*#.*", line):
            # It’s a comment, we can skip the line
            continue
        if re.match("\s*$", line):
            # It's only space
            continue

        # Type annotation information
        m = re.match("\s*(\D\S*)\s*:\s*(\S*)\s*$", line)
        if m:
            target_type: str
            if m[2] in ("str","int"):
                target_type = m[2]
            else:
                target_type = "UKN"
            if unify_in_context(local_type_context, m[1], target_type, line_number):
                return 1
            continue

        # Variable affectation with a simple expression
        m = re.match("\s*(\D\S*)\s*=\s*({})\s*$".format(EXPRESSION_REGEX), line)
        if m:
            # print("Line recognized as simple variable affectation.")
            target_type = type_expression_with_context(local_type_context, m[2])
            if unify_in_context(local_type_context, m[1], target_type, line_number):
                return 1
            target_type = type_expression_with_context(local_type_context, m[1])
            if re.match("\s*\D\S*\s*", m[2]) and target_type!="?":
                if unify_in_context(local_type_context, m[2], target_type, line_number):
                    return 1
            continue

        # Variable affectation with evaluation of a function
        m = re.match("\s*(\D\S*)\s*=\s*(\D\S*)\s*\(((\s*{}\s*,?\s*)*)\)\s*$".format(EXPRESSION_REGEX), line)
        if m:
            if m[2] in function_types:
                argument_list = m[3].split(",")
                # We check number and type of arguments
                if len(argument_list)!=len(function_types[m[2]][1]):
                    print("Wrong number of arguments at line {}. Expected {} but got {}.".format(line_number, len(function_types[m[2]][1]), len(argument_list)))
                    return 1
                for given_argument, (_,expected_type) in zip(argument_list, function_types[m[2]][1]):
                    arg_type = type_expression_with_context(local_type_context, given_argument)
                    if arg_type!="?" and expected_type !="?" and expected_type != arg_type:
                        print("Wrong type for {}. Expected {} but was given {}.".format(given_argument, expected_type, arg_type))
                        return 1
                    if expected_type!="?" and re.match("\s*\D\S*\s*", given_argument):
                        if unify_in_context(local_type_context, given_argument, expected_type, line_number):
                            return 1


                # We now use what we know about the type of the function
                target_type = function_types[m[2]][2]
                if target_type!="?":
                    if unify_in_context(local_type_context, m[1], target_type, line_number):
                        return 1
            continue

        # Return statement
        m = re.match("\s*return\s+({})\s*$".format(EXPRESSION_REGEX), line)
        if m:
            arg_type = type_expression_with_context(local_type_context, m[1])
            if arg_type != "?" and type_out!= "?" and type_out!=arg_type:
                print("Wrong type in return at line {}. Expected type {}, but got type {}.".format(line_number, type_out, arg_type))
                return 1
            if re.match("\s*\D\S*\s*", m[1]):
                if unify_in_context(local_type_context, m[1], type_out, line_number):
                    return 1
            continue

    return 0


if __name__ == "__main__":
    if len(sys.argv)<=1:
        print("We need a target.")
        sys.exit(1)
    with open(sys.argv[1], "r") as file:
        program = file.read().split("\n")
    function_types = extract_function_types(program)
    print("Found {} function(s): {}".format(len(function_types), list(function_types)))
    for function_name, (line_number, argument_types, type_out) in function_types.items():
        if check_type_function(program, function_types, function_name, line_number, argument_types, type_out):
            print("Error while type checking {}.".format(function_name))
        else:
            print("Success while type checking {}.".format(function_name))
    sys.exit(0)
