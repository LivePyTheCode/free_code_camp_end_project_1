def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    # storing problem into different variables
    arranged_problems = ""
    problem_space = "    "
    first_line = ""
    second_line = ""
    dashes = ""
    for problem in problems:
        # splitting problem list and assigning it to different variables
        num1, operator, num2 = problem.split()

        #   errors
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # max width of numbers
        max_width = max(len(num1), len(num2))

        first_line += num1.rjust(max_width + 2) + problem_space
        second_line += operator + ' ' + num2.rjust(max_width) + problem_space
        dashes += "-" * (max_width + 2) + problem_space

    arranged_problems += first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + dashes.rstrip()

    # if show answers is True
    if show_answers:
        solution_line = ""
        for problem in problems:
            num1, operator, num2 = problem.split()
            max_width = max(len(num1), len(num2))
            if operator == '+':
                solution = int(num1) + int(num2)
            elif operator == '-':
                solution = int(num1) - int(num2)
            solution_line += str(solution).rjust(max_width + 2) + problem_space
        arranged_problems += '\n' + solution_line.rstrip()

    return arranged_problems


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')
print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"], True)}')
print(f'\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"], True)}')