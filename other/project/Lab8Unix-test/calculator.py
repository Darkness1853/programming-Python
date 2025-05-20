class Calculator:
    def __init__(self):
        self.first_number = 0
        self.operation = ""
        self.current_value = ""
        self.reset_state = False

    def add_digit(self, digit):
        """Добавляет цифру к текущему значению"""
        if self.reset_state:
            self.current_value = ""
            self.reset_state = False
        self.current_value += str(digit)
        return self.current_value

    def clear(self):
        """Полностью очищает калькулятор"""
        self.first_number = 0
        self.operation = ""
        self.current_value = ""
        self.reset_state = False
        return self.current_value

    def set_operation(self, operation):
        """Устанавливает операцию для вычисления"""
        if self.current_value:
            self.first_number = int(self.current_value)
            self.operation = operation
            self.current_value = ""
            self.reset_state = True

    def calculate(self):
        """Выполняет вычисление"""
        if not self.operation or not self.current_value:
            return self.current_value

        second_number = int(self.current_value)
        result = 0

        if self.operation == "addition":
            result = self.first_number + second_number
        elif self.operation == "subtraction":
            result = self.first_number - second_number
        elif self.operation == "multiplication":
            result = self.first_number * second_number
        elif self.operation == "division":
            result = self.first_number / second_number

        self.current_value = str(result)
        self.operation = ""
        self.reset_state = True
        return self.current_value
