'''Finds solutions for numble.wtf website daily puzzle'''

OPERATORS = ["+", "-", "*", "/"]

def find_solution(num_string, goal_num):
    solution = 0
    solutions = []
    p_op = []
    for num in range(len(num_string)):
        for key in range(len(OPERATORS)):
            for num2 in range(len(num_string)):
                if num != num2:
                    p_op.append(f"({num_string[num]} {OPERATORS[key]} {num_string[num2]})")
                    expression = num_string[num] + OPERATORS[key] + num_string[num2]
                    solution = eval(expression)
                    if solution == goal_num:
                        solutions.append(f"{num_string[num]} {OPERATORS[key]} {num_string[num2]} = {solution}")
                    for op_num in range(len(p_op)):
                        for key_a in range(len(OPERATORS)):
                            if num != num2 and num_string[num] not in p_op[op_num] and num_string[num2] not in p_op[op_num]:
                                p_ex = p_op[op_num] + OPERATORS[key_a] + num_string[num] + OPERATORS[key] + num_string[num2]
                                solution = eval(p_ex)
                                if solution == goal_num:
                                    solutions.append(f"{p_op[op_num]} {OPERATORS[key]} {num_string[num]} {OPERATORS[key]} {num_string[num2]} = {solution}")
                    for op_num in range(len(p_op)):
                        for key_a in range(len(OPERATORS)):
                            if num != num2 and num_string[num] not in p_op[op_num] and num_string[num2] not in p_op[op_num]:
                                p_ex2 = num_string[num] + OPERATORS[key] + num_string[num2] + OPERATORS[key_a] + p_op[op_num]
                                solution = eval(p_ex2)
                                if solution == goal_num:
                                    solutions.append(f"{num_string[num]} {OPERATORS[key]} {num_string[num2]} {OPERATORS[key_a]} {p_op[op_num]}= {solution}")
                    for op_num in range(len(p_op)):
                        for key_a in range(len(OPERATORS)):
                            if num != num2 and num_string[num] not in p_op[op_num] and num_string[num2] not in p_op[op_num]:
                                p_ex3 = num_string[num] + OPERATORS[key] + p_op[op_num] + OPERATORS[key_a] +  num_string[num2]
                                solution = eval(p_ex3)
                                if solution == goal_num:
                                    solutions.append(f"{num_string[num]} {OPERATORS[key]} {p_op[op_num]} {OPERATORS[key_a]} {num_string[num2]} = {solution}")
                    for key2 in range(len(OPERATORS)):
                        for num3 in range(len(num_string)):
                            if num != num2 and num != num3 and num2 != num3:
                                expression = num_string[num] + OPERATORS[key] + num_string[num2] + OPERATORS[key2] + num_string[num3]
                                solution = eval(expression)
                                if solution == goal_num:
                                    solutions.append(f"{num_string[num]} {OPERATORS[key]} {num_string[num2]} {OPERATORS[key2]} {num_string[num3]} = {solution}")
                                for op_num in range(len(p_op)):
                                    for key_a in range(len(OPERATORS)):
                                        if num != num2 and num != num3 and num2 != num3 and num_string[num] not in p_op[op_num] and num_string[num2] not in p_op[op_num] and num_string[num3] not in p_op[op_num]:
                                            p_ex = p_op[op_num] + OPERATORS[key_a] + num_string[num] + OPERATORS[key] + num_string[num2] + OPERATORS[key2] + num_string[num3]
                                            solution = eval(p_ex)
                                            if solution == goal_num:
                                                solutions.append(f"{p_op[op_num]} {OPERATORS[key_a]} {num_string[num]} {OPERATORS[key]} {num_string[num2]} {OPERATORS[key2]} {num_string[num3]} = {solution}")
                                for op_num in range(len(p_op)):
                                    for key_a in range(len(OPERATORS)):
                                        if num != num2 and num != num3 and num2 != num3 and num_string[num] not in p_op[op_num] and num_string[num2] not in p_op[op_num] and num_string[num3] not in p_op[op_num]:
                                            p_ex2 = num_string[num] + OPERATORS[key] + p_op[op_num] + OPERATORS[key_a] + num_string[num2] + OPERATORS[key2] + num_string[num3]
                                            solution = eval(p_ex2)
                                            if solution == goal_num:
                                                solutions.append(f"{num_string[num]} {OPERATORS[key]} {p_op[op_num]} {OPERATORS[key_a]} {num_string[num2]} {OPERATORS[key2]} {num_string[num3]} = {solution}")
                                for op_num in range(len(p_op)):
                                    for key_a in range(len(OPERATORS)):
                                        if num != num2 and num != num3 and num2 != num3 and num_string[num] not in p_op[op_num] and num_string[num2] not in p_op[op_num] and num_string[num3] not in p_op[op_num]:
                                            p_ex3 = num_string[num] + OPERATORS[key] + num_string[num2] + OPERATORS[key2] + p_op[op_num] + OPERATORS[key_a] + num_string[num3]
                                            solution = eval(p_ex3)
                                            if solution == goal_num:
                                                solutions.append(f"{num_string[num]} {OPERATORS[key]} {num_string[num2]} {OPERATORS[key2]} {p_op[op_num]} {OPERATORS[key_a]} {num_string[num3]} = {solution}")
                                for op_num in range(len(p_op)):
                                    for key_a in range(len(OPERATORS)):
                                        if num != num2 and num != num3 and num2 != num3 and num_string[num] not in p_op[op_num] and num_string[num2] not in p_op[op_num] and num_string[num3] not in p_op[op_num]:
                                            p_ex4 = num_string[num] + OPERATORS[key] + num_string[num2] + OPERATORS[key2] + num_string[num3] + OPERATORS[key_a] + p_op[op_num]
                                            solution = eval(p_ex4)
                                            if solution == goal_num:
                                                solutions.append(f"{num_string[num]} {OPERATORS[key]} {num_string[num2]} {OPERATORS[key2]} {num_string[num3]} {OPERATORS[key_a]} {p_op[op_num]} = {solution}")
                                for key3 in range(len(OPERATORS)):
                                    for num4 in range(len(num_string)):
                                        if num != num2 and num != num3 and num2 != num3 and num != num4 and num2 != num4 and num3 != num4:
                                            expression = num_string[num] + OPERATORS[key] + num_string[num2] + OPERATORS[key2] + num_string[num3] + OPERATORS[key3] + num_string[num4]
                                            solution = eval(expression)
                                            if solution == goal_num:
                                                solutions.append(f"{num_string[num]} {OPERATORS[key]} {num_string[num2]} {OPERATORS[key2]} {num_string[num3]} {OPERATORS[key3]} {num_string[num4]} = {solution}")
                                            for op_num in range(len(p_op)):
                                                for key_a in range(len(OPERATORS)):
                                                    if num != num2 and num != num3 and num2 != num3 and num != num4 and num2 != num4 and num3 != num4 and num_string[num] not in p_op[op_num] and num_string[num2] not in p_op[op_num] and num_string[num3] not in p_op[op_num] and num_string[num4] not in p_op[op_num]:
                                                        p_ex = p_op[op_num] + OPERATORS[key_a] + num_string[num] + OPERATORS[key] + num_string[num2] + OPERATORS[key2] + num_string[num3] + OPERATORS[key3] + num_string[num4]
                                                        solution = eval(p_ex)
                                                        if solution == goal_num:
                                                            solutions.append(f"{p_op[op_num]} {OPERATORS[key_a]} {num_string[num]} {OPERATORS[key]} {num_string[num2]} {OPERATORS[key2]} {num_string[num3]} {OPERATORS[key3]} {num_string[num4]} = {solution}")
                                            for op_num in range(len(p_op)):
                                                for key_a in range(len(OPERATORS)):
                                                    if num != num2 and num != num3 and num2 != num3 and num != num4 and num2 != num4 and num3 != num4 and num_string[num] not in p_op[op_num] and num_string[num2] not in p_op[op_num] and num_string[num3] not in p_op[op_num] and num_string[num4] not in p_op[op_num]:
                                                        p_ex2 = num_string[num] + OPERATORS[key] + p_op[op_num] + OPERATORS[key_a] + num_string[num2] + OPERATORS[key2] + num_string[num3] + OPERATORS[key3] + num_string[num4]
                                                        solution = eval(p_ex2)
                                                        if solution == goal_num:
                                                            solutions.append(f"{num_string[num]} {OPERATORS[key]} {p_op[op_num]} {OPERATORS[key_a]} {num_string[num2]} {OPERATORS[key2]} {num_string[num3]} {OPERATORS[key3]} {num_string[num4]} = {solution}")
                                            for op_num in range(len(p_op)):
                                                for key_a in range(len(OPERATORS)):
                                                    if num != num2 and num != num3 and num2 != num3 and num != num4 and num2 != num4 and num3 != num4 and num_string[num] not in p_op[op_num] and num_string[num2] not in p_op[op_num] and num_string[num3] not in p_op[op_num] and num_string[num4] not in p_op[op_num]:
                                                        p_ex3 = num_string[num] + OPERATORS[key] + num_string[num2] + OPERATORS[key2] + p_op[op_num] + OPERATORS[key_a] + num_string[num3] + OPERATORS[key3] + num_string[num4]
                                                        solution = eval(p_ex3)
                                                        if solution == goal_num:
                                                            solutions.append(f"{num_string[num]} {OPERATORS[key]} {num_string[num2]} {OPERATORS[key2]} {p_op[op_num]} {OPERATORS[key_a]} {num_string[num3]} {OPERATORS[key3]} {num_string[num4]} = {solution}")
                                            for op_num in range(len(p_op)):
                                                for key_a in range(len(OPERATORS)):
                                                    if num != num2 and num != num3 and num2 != num3 and num != num4 and num2 != num4 and num3 != num4 and num_string[num] not in p_op[op_num] and num_string[num2] not in p_op[op_num] and num_string[num3] not in p_op[op_num] and num_string[num4] not in p_op[op_num]:
                                                        p_ex4 = num_string[num] + OPERATORS[key] + num_string[num2] + OPERATORS[key2] + num_string[num3] + OPERATORS[key3] + p_op[op_num] + OPERATORS[key_a] + num_string[num4]
                                                        solution = eval(p_ex4)
                                                        if solution == goal_num:
                                                            solutions.append(f"{num_string[num]} {OPERATORS[key]} {num_string[num2]} {OPERATORS[key2]} {num_string[num3]} {OPERATORS[key3]} {p_op[op_num]} {OPERATORS[key_a]} {num_string[num4]} = {solution}")
                                            for op_num in range(len(p_op)):
                                                for key_a in range(len(OPERATORS)):
                                                    if num != num2 and num != num3 and num2 != num3 and num != num4 and num2 != num4 and num3 != num4 and num_string[num] not in p_op[op_num] and num_string[num2] not in p_op[op_num] and num_string[num3] not in p_op[op_num] and num_string[num4] not in p_op[op_num]:
                                                        p_ex5 = num_string[num] + OPERATORS[key] + num_string[num2] + OPERATORS[key2] + num_string[num3] + OPERATORS[key3] + num_string[num4] + OPERATORS[key_a] + p_op[op_num]
                                                        solution = eval(p_ex5)
                                                        if solution == goal_num:
                                                            solutions.append(f"{num_string[num]} {OPERATORS[key]} {num_string[num2]} {OPERATORS[key2]} {num_string[num3]} {OPERATORS[key3]} {num_string[num4]} {OPERATORS[key_a]} {p_op[op_num]} = {solution}")
                                            for key4 in range(len(OPERATORS)):
                                                for num5 in range(len(num_string)):
                                                    if num != num2 and num != num3 and num2 != num3 and num != num4 and num2 != num4 and num3 != num4 and num != num5 and num2 != num5 and num3 != num5 and num4 != num5:
                                                        expression = num_string[num] + OPERATORS[key] + num_string[num2] + OPERATORS[key2] + num_string[num3] + OPERATORS[key3] + num_string[num4] + OPERATORS[key4] + num_string[num5]
                                                        solution = eval(expression)
                                                        if solution == goal_num:
                                                            solutions.append(f"{num_string[num]} {OPERATORS[key]} {num_string[num2]} {OPERATORS[key2]} {num_string[num3]} {OPERATORS[key3]} {num_string[num4]} {OPERATORS[key4]} {num_string[num5]} = {solution}")
                                                        for key5 in range(len(OPERATORS)):
                                                            for num6 in range(len(num_string)):
                                                                if num != num2 and num != num3 and num2 != num3 and num != num4 and num2 != num4 and num3 != num4 and num != num5 and num2 != num5 and num3 != num5 and num4 != num5 and num != num6 and num2 != num6 and num3 != num6 and num4 != num6 and num5 != num6:
                                                                    expression = num_string[num] + OPERATORS[key] + num_string[num2] + OPERATORS[key2] + num_string[num3] + OPERATORS[key3] + num_string[num4] + OPERATORS[key4] + num_string[num5] + OPERATORS[key5] + num_string[num6]
                                                                    solution = eval(expression)
                                                                    if solution == goal_num:
                                                                        solutions.append(f"{num_string[num]} {OPERATORS[key]} {num_string[num2]} {OPERATORS[key2]} {num_string[num3]} {OPERATORS[key3]} {num_string[num4]} {OPERATORS[key4]} {num_string[num5]} {OPERATORS[key5]} {num_string[num6]} = {solution}")
    return solutions

goal_num = 326
num_string = ["1", "5", "6", "7", "10", "75"]

solutions = find_solution(num_string, goal_num)

print(min(solutions))


