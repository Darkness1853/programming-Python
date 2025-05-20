import unittest
from calculator import Calculator

"Запуск с помощью команды в терминале: python -m unittest test_Calculator.py
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_digit(self):
        "Добавление цифр"
        self.assertEqual(self.calc.add_digit(1), "1")
        self.assertEqual(self.calc.add_digit(2), "12")
        self.assertEqual(self.calc.add_digit(3), "123")

    def test_clear(self):
        "Очистка калькулятора"
        self.calc.add_digit(5)
        self.calc.set_operation("addition")
        self.assertEqual(self.calc.clear(), "")
        self.assertEqual(self.calc.first_number, 0)
        self.assertEqual(self.calc.operation, "")

    def test_addition(self):
        "Операция сложения"
        self.calc.add_digit(1)
        self.calc.add_digit(0)
        self.calc.set_operation("addition")
        self.calc.add_digit(2)
        self.calc.add_digit(0)
        self.assertEqual(self.calc.calculate(), "30")

    def test_subtraction(self):
        "Операция вычитания"
        self.calc.add_digit(5)
        self.calc.add_digit(0)
        self.calc.set_operation("subtraction")
        self.calc.add_digit(2)
        self.calc.add_digit(5)
        self.assertEqual(self.calc.calculate(), "25")

    def test_multiplication(self):
        "Операция умножения"
        self.calc.add_digit(5)
        self.calc.set_operation("multiplication")
        self.calc.add_digit(4)
        self.assertEqual(self.calc.calculate(), "20")

    def test_division(self):
        "Операция деления"
        self.calc.add_digit(1)
        self.calc.add_digit(0)
        self.calc.set_operation("division")
        self.calc.add_digit(2)
        self.assertEqual(self.calc.calculate(), "5.0")

    def test_sequence_operations(self):
        "Последовательность операций"
        self.calc.add_digit(1)
        self.calc.add_digit(0)
        self.calc.set_operation("addition")
        self.calc.add_digit(2)
        self.calc.add_digit(0)
        self.calc.calculate()
        self.calc.set_operation("multiplication")
        self.calc.add_digit(3)
        self.assertEqual(self.calc.calculate(), "90")

    def test_clear_operations(self):
        "Очистка между операциями"
        self.calc.add_digit(5)
        self.calc.set_operation("multiplication")
        self.calc.clear()
        self.calc.add_digit(3)
        self.assertEqual(self.calc.calculate(), "3")


if __name__ == '__main__':
    unittest.main(verbosity=2)
