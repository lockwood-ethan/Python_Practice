def find_solution(number_string, goal_num):
    solution = 0
    solutions = []
    for num in range(len(number_string)):
        for key in range(len(operators)):
            for num2 in range(len(number_string)):
                if num != num2:
                    expression = number_string[num] + operators[key] + number_string[num2]
                    solution = eval(expression)
                    if solution == goal_num:
                        solutions.append(f"{number_string[num]} {operators[key]} {number_string[num2]} = {solution}")
                    for key2 in range(len(operators)):
                        for num3 in range(len(number_string)):
                            if num != num2 and num != num3 and num2 != num3:
                                expression = number_string[num] + operators[key] + number_string[num2] + operators[key2] + number_string[num3]
                                solution = eval(expression)
                                if solution == goal_num:
                                    solutions.append(f"{number_string[num]} {operators[key]} {number_string[num2]} {operators[key2]} {number_string[num3]} = {solution}")
                                for key3 in range(len(operators)):
                                    for num4 in range(len(number_string)):
                                        if num != num2 and num != num3 and num2 != num3 and num != num4 and num2 != num4 and num3 != num4:
                                            expression = number_string[num] + operators[key] + number_string[num2] + operators[key2] + number_string[num3] + operators[key3] + number_string[num4]
                                            solution = eval(expression)
                                            if solution == goal_num:
                                                solutions.append(f"{number_string[num]} {operators[key]} {number_string[num2]} {operators[key2]} {number_string[num3]} {operators[key3]} {number_string[num4]} = {solution}")
                                            for key4 in range(len(operators)):
                                                for num5 in range(len(number_string)):
                                                    if num != num2 and num != num3 and num2 != num3 and num != num4 and num2 != num4 and num3 != num4 and num != num5 and num2 != num5 and num3 != num5 and num4 != num5:
                                                        expression = number_string[num] + operators[key] + number_string[num2] + operators[key2] + number_string[num3] + operators[key3] + number_string[num4] + operators[key4] + number_string[num5]
                                                        solution = eval(expression)
                                                        if solution == goal_num:
                                                            solutions.append(f"{number_string[num]} {operators[key]} {number_string[num2]} {operators[key2]} {number_string[num3]} {operators[key3]} {number_string[num4]} {operators[key4]} {number_string[num5]} = {solution}")
                                                        for key5 in range(len(operators)):
                                                            for num6 in range(len(number_string)):
                                                                if num != num2 and num != num3 and num2 != num3 and num != num4 and num2 != num4 and num3 != num4 and num != num5 and num2 != num5 and num3 != num5 and num4 != num5 and num != num6 and num2 != num6 and num3 != num6 and num4 != num6 and num5 != num6:
                                                                    expression = number_string[num] + operators[key] + number_string[num2] + operators[key2] + number_string[num3] + operators[key3] + number_string[num4] + operators[key4] + number_string[num5] + operators[key5] + number_string[num6]
                                                                    solution = eval(expression)
                                                                    if solution == goal_num:
                                                                        solutions.append(f"{number_string[num]} {operators[key]} {number_string[num2]} {operators[key2]} {number_string[num3]} {operators[key3]} {number_string[num4]} {operators[key4]} {number_string[num5]} {operators[key5]} {number_string[num6]} = {solution}")
    return solutions

goal_num = 217
number_string = ["3", "5", "9", "10", "50", "75"]
operators = ["+", "-", "*", "/"]

solutions = find_solution(number_string, goal_num)

print(min(solutions))


