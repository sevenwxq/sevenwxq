import argparse
import random
from fractions import Fraction
from time import * #引入时间库


OPERATORS = ['+', '-', '×', '÷']


def generate_expression(max_value):
    """
    生成一个随机的算术表达式
    :param max_value: 数值的范围，不包括该值
    :return: 算术表达式
    """
    if max_value <= 0:
        raise ValueError("max_value must be greater than 0")
    # 运算符个数不超过3个
    operator_count = random.randint(1, 3)
    # 是否加括号
    roll = random.randint(0, 1)
    # 不加括号
    if roll == 0:
        expression = generate_operand(max_value)

        for _ in range(operator_count):
            operator = random.choice(OPERATORS)
            # 生成一个随机的操作数（operand）
            operand = generate_operand(max_value)
            # 将'÷'替换成'/'
            expression += f" {operator} {operand.replace('÷', '/')}"
    # 加括号
    else:
        # 只有一个运算符。有没有括号都一样
        if operator_count == 1:
            expression = generate_operand(max_value)

            for _ in range(operator_count):
                operator = random.choice(OPERATORS)
                # 生成一个随机的操作数（operand）
                operand = generate_operand(max_value)
                # 将'÷'替换成'/'
                expression += f" {operator} {operand.replace('÷', '/')}"
        # 两个运算符 括号最多一对
        if operator_count == 2:
            kuohao_place = random.randint(1, 2)
            # （a+b)+c
            if kuohao_place == 1:
                operand = generate_operand(max_value)
                expression = f"{'('} {operand} "
                operator = random.choice(OPERATORS)
                operand = generate_operand(max_value)
                expression += f" {operator} {operand.replace('÷', '/')}"
                operator = random.choice(OPERATORS)
                operand = generate_operand(max_value)
                expression += f"{')'} {operator} {operand.replace('÷', '/')}"
            # a+(b+c)
            else:
                expression = generate_operand(max_value)
                operator = random.choice(OPERATORS)
                operand = generate_operand(max_value)
                expression += f" {operator}{'('}{operand.replace('÷', '/')}"
                operator = random.choice(OPERATORS)
                operand = generate_operand(max_value)
                expression += f"{operator} {operand.replace('÷', '/')}{')'} "
        # 三个运算符，括号最多两对
        if operator_count == 3:
            kuohao = random.randint(1, 2)
            # 只有一对括号
            if kuohao == 1:
                kuohao_place = random.randint(1, 3)
                # （a+b)+c+d
                if kuohao_place == 1:
                    operand = generate_operand(max_value)
                    expression = f"{'('} {operand} "
                    operator = random.choice(OPERATORS)
                    operand = generate_operand(max_value)
                    expression += f" {operator} {operand.replace('÷', '/')}{')'}"
                    operator = random.choice(OPERATORS)
                    operand = generate_operand(max_value)
                    expression += f" {operator} {operand.replace('÷', '/')}"
                    operator = random.choice(OPERATORS)
                    operand = generate_operand(max_value)
                    expression += f" {operator} {operand.replace('÷', '/')}"
                # a+(b+c)+d
                if kuohao_place == 2:
                    expression = generate_operand(max_value)
                    operator = random.choice(OPERATORS)
                    operand = generate_operand(max_value)
                    expression += f" {operator}{'('}{operand.replace('÷', '/')}"
                    operator = random.choice(OPERATORS)
                    operand = generate_operand(max_value)
                    expression += f"{operator} {operand.replace('÷', '/')}{')'} "
                    operator = random.choice(OPERATORS)
                    operand = generate_operand(max_value)
                    expression += f" {operator} {operand.replace('÷', '/')}"
                # a+b+(c+d)
                if kuohao_place == 3:
                    expression = generate_operand(max_value)
                    operator = random.choice(OPERATORS)
                    operand = generate_operand(max_value)
                    expression += f" {operator} {operand.replace('÷', '/')}"
                    operator = random.choice(OPERATORS)
                    operand = generate_operand(max_value)
                    expression += f" {operator}{'('} {operand.replace('÷', '/')}"
                    operator = random.choice(OPERATORS)
                    operand = generate_operand(max_value)
                    expression += f" {operator}{operand.replace('÷', '/')}{')'}"
            # 两对括号-----（a+b)+(c+d)
            if kuohao == 2:
                operand = generate_operand(max_value)
                expression = f"{'('} {operand} "
                operator = random.choice(OPERATORS)
                operand = generate_operand(max_value)
                expression += f" {operator} {operand.replace('÷', '/')}{')'}"
                operator = random.choice(OPERATORS)
                operand = generate_operand(max_value)
                expression += f" {operator}{'('} {operand.replace('÷', '/')}"
                operator = random.choice(OPERATORS)
                operand = generate_operand(max_value)
                expression += f" {operator} {operand.replace('÷', '/')}{')'}"
    return expression


def generate_operand(max_value):
    """
    生成一个随机的操作数（自然数或真分数）
    :param max_value: 数值的范围，不包括该值
    :return: 操作数
    """
    # 分子分母
    numerator = random.randint(1, max_value)
    denominator = random.randint(numerator, max_value)
    if numerator == denominator:
        operand = str(numerator)
    else:
        fraction = Fraction(numerator, denominator)
        if fraction.numerator > fraction.denominator:
            operand = f"{'('}{fraction.numerator // fraction.denominator}'{fraction.numerator % fraction.denominator}/{fraction.denominator}{')'}"
        else:
            operand= f"{'('}"
            operand1 = str(fraction)
            operand +=f"{operand1}{')'}"
    return operand


def generate_exercises(num_exercises, max_value):
    """
    生成指定数量的四则运算题目
    :param num_exercises: 题目数量
    :param max_value: 数值的范围，不包括该值
    :return: 题目列表
    """
    exercises = []
    while len(exercises) < num_exercises:
        expression = generate_expression(max_value)
        # 避免生成重复的题目
        if expression not in exercises:
            exercises.append(expression)
    return exercises


def calculate_answer(expression):
    expression = expression.replace(' ', '')  # 去除空格
    expression = expression.replace('×', '*').replace('÷', '/')


    try:
        result = eval(expression)
        if isinstance(result, int):
            return str(result) if result >= 0 else "Error"
        else:
            fraction = Fraction(result).limit_denominator()
            whole_part = fraction.numerator // fraction.denominator
            numerator = fraction.numerator % fraction.denominator
            if whole_part == 0:
                return f"{numerator}/{fraction.denominator}" if result >= 0 else "Error"
            elif numerator == 0:
                return str(whole_part) if result >= 0 else "Error"
            else:
                return f"{whole_part}'{numerator}/{fraction.denominator}" if result >= 0 else "Error"
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception:
        return "Error: Invalid expression"


def generate_answers(exercises):
    """
    生成题目对应的答案列表
    :param exercises: 题目列表
    :return: 答案列表
    """
    answers = []
    for exercise in exercises:
        answer = calculate_answer(exercise)
        answers.append(answer)
    return answers


def save_to_file(filename, data):
    """
    将数据保存到文件中
    :param filename: 文件名
    :param data: 数据列表
    """
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item}\n")


def load_from_file(filename):
    """
    从文件中读取数据
    :param filename: 文件名
    :return: 数据列表
    """
    with open(filename, 'r') as file:
        data = file.read().splitlines()
    return data


def check_answers(exercise_file, answer_file):
    """
    检查答案文件中的对错并进行数量统计
    :param exercise_file: 题目文件
    :param answer_file: 答案文件
    """
    exercises = load_from_file(exercise_file)
    answers = load_from_file(answer_file)

    correct_count = 0
    wrong_count = 0
    error_count=0
    wrong_exercises = []
    error_exercises = []

    for i in range(len(exercises)):
        exercise = exercises[i]
        expected_answer = answers[i]
        actual_answer = calculate_answer(exercise)

        if expected_answer != 'Error':
            if expected_answer == actual_answer:
                correct_count += 1

            else:
                wrong_count += 1
                wrong_exercises.append(i + 1)
        else:
            error_count += 1
            error_exercises.append(i + 1)
    #正确题目
    result = f"Correct: {correct_count} ({', '.join(map(str, range(1, correct_count + 1)))})\n"
    #错误题目
    result += f"Wrong: {wrong_count} ({', '.join(map(str, wrong_exercises))})\n"
    #结果为负数的题目
    result += f"Error: {error_count} ({', '.join(map(str, error_exercises))})\n"

    save_to_file("Grade.txt", [result])

#@profile
def main():
    parser = argparse.ArgumentParser(description="Generate elementary arithmetic exercises.")
    parser.add_argument("-n", type=int, help="number of exercises")
    parser.add_argument("-r", type=int, help="range of values")
    parser.add_argument("-e", help="exercise file")
    parser.add_argument("-a", help="answer file")
    args = parser.parse_args()

    if args.n and args.r:
        num_exercises = args.n
        max_value = args.r

        exercises = generate_exercises(num_exercises, max_value)
        answers = generate_answers(exercises)

        save_to_file("Exercises.txt", exercises)
        save_to_file("Answers.txt", answers)
    elif args.e and args.a:
        exercise_file = args.e
        answer_file = args.a

        check_answers(exercise_file, answer_file)
    else:
        parser.print_help()


if __name__ == "__main__":
    # 开始
    startT = time()
    main()
    #结束
    endT = time()
    print("花费时间time=%.2g 秒" % (endT - startT))
