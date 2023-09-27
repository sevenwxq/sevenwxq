import unittest
import random

from 软工作业3.main import calculate_answer, generate_answers, generate_operand, OPERATORS


class MyTestCase(unittest.TestCase):
    def test_calculate_answer(self):
        excise='1+2+3'
        result=calculate_answer(excise)
        self.assertEqual(result, '6')  # add assertion here

    def test_generate_answers(self):
        answers = []
        excise=['1','2','3']
        excises='123'
        answers=generate_answers(excises)
        self.assertEqual(answers,excise )

    def test_generate_expression(self, max_value=9):

        # 运算符个数不超过3个
        operator_count= 1
        # 是否加括号
        roll = 0
        # 不加括号
        if roll == 0:
            expression = '2'

            for _ in range(operator_count):
                operator = '+'
                # 生成一个随机的操作数（operand）
                operand = '2'
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

        self.assertEqual(expression, '2 + 2')






if __name__ == '__main__':
    unittest.main()
