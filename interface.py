import tkinter as tk
from tkinter import messagebox
from parser import *
from P.Polynomial import Polynomial
from TRANS.TRANS_Q_P import TRANS_Q_P
'''
class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Калькулятор")
        self.window.geometry("350x450")
        self.window.resizable(False, False)

        self.expression = ""

        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self.window, font=('Arial', 16), justify='right')
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky='ew')

        info_label = tk.Label(self.window, text="Введите выражение", font=('Arial', 10))
        info_label.grid(row=1, column=0, columnspan=5, pady=(0, 10))

        buttons = [
            '7', '8', '9', '/', 'x²',
            '4', '5', '6', '*', 'x³',
            '1', '2', '3', '-', 'xⁿ',
            '0', 'x', '=', '+', 'C',
            '(', ')','<—', ' ', ' '
        ]

        row = 2
        col = 0

        for button in buttons:
            if button == '=':
                cmd = self.show_result
            elif button == 'C':
                cmd = self.clear
            elif button == '<—':
                cmd = self.backspace
            elif button in ['x²', 'x³', 'xⁿ']:
                cmd = lambda x=button: self.add_power(x)
            elif button == ' ':
                col += 1
                if col > 4:
                    col = 0
                    row += 1
                continue
            else:
                cmd = lambda x=button: self.add_to_expression(x)

            tk.Button(
                self.window,
                text=button,
                font=('Arial', 12),
                command=cmd,
                height=2,
                width=6
            ).grid(row=row, column=col, padx=2, pady=2, sticky='ew')

            col += 1
            if col > 4:
                col = 0
                row += 1

        tk.Button(
            self.window,
            text="Ответ",
            font=('Arial', 12),
            command=self.show_result,
            height=2,
            bg='lightblue'
        ).grid(row=row, column=0, columnspan=5, padx=2, pady=10, sticky='ew')

    def add_to_expression(self, value):
        """Добавляет символ к выражению"""
        self.expression += str(value)
        self.update_display()

    def add_power(self, power_type):
        """Добавляет степень переменной"""
        if power_type == 'x²':
            self.expression += '^2'
        elif power_type == 'x³':
            self.expression += '^3'
        elif power_type == 'xⁿ':
            self.expression += '^'
        self.update_display()

    def clear(self):
        """Очищает выражение"""
        self.expression = ""
        self.update_display()

    def backspace(self):
        """Очищает последний символ выражения"""
        self.expression = self.expression[:-1]
        self.update_display()

    def show_result(self):
        """Получаем результат"""
        if self.expression:
            try:
                # Вычисляем результат
                result = self.process_expression(self.expression)
                # Выводим результат в то же поле
                self.clear()
                self.expression = str(result)  # Обновляем выражение
                self.update_display()
            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка вычисления: {e}")
        else:
            messagebox.showwarning("Предупреждение", "Введите выражение")

    def update_display(self):
        """Обновляет отображение выражения"""
        self.display.config(state='normal')
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)
        self.display.config(state='readonly')

    def process_expression(self, expr):
        """Обрабатывает выражение"""
        print(expr)
        print(to_rpn(expr))
        ans = eval_rpn(to_rpn(expr))
        if type(ans) != Polynomial:
            ans = TRANS_Q_P(ans)
        return ans.show()

    def run(self):
        """Запускает приложение"""
        self.window.mainloop()


s = Calculator().run()

'''


class CalculatorSelector:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Выбор калькулятора")
        self.window.geometry("350x450")
        self.window.resizable(False, False)

        self.create_widgets()

    def run(self):
        """Запускает приложение"""
        self.window.mainloop()

    def create_widgets(self):
        title_label = tk.Label(self.window, text="Выберите тип калькулятора",
                               font=('Arial', 16, 'bold'))
        title_label.pack(pady=20)

        # Кнопки для выбора типа калькулятора
        button_style = {'font': ('Arial', 14), 'height': 2, 'width': 20}

        natural_btn = tk.Button(self.window, text="Натуральные числа",
                                command=self.open_natural_calculator, **button_style)
        natural_btn.pack(pady=5)

        integer_btn = tk.Button(self.window, text="Целые числа",
                                command=self.open_integer_calculator, **button_style)
        integer_btn.pack(pady=5)

        rational_btn = tk.Button(self.window, text="Рациональные числа",
                                 command=self.open_rational_calculator, **button_style)
        rational_btn.pack(pady=5)

        polynomial_btn = tk.Button(self.window, text="Полиномы",
                                   command=self.open_polynomial_calculator, **button_style)
        polynomial_btn.pack(pady=5)

    def open_natural_calculator(self):
        geometry = self.window.geometry()
        self.window.destroy()
        calculator = Calculator("natural")
        calculator.window.geometry(geometry)
        calculator.run()

    def open_integer_calculator(self):
        geometry = self.window.geometry()
        self.window.destroy()
        calculator = Calculator("integer")
        calculator.window.geometry(geometry)
        calculator.run()

    def open_rational_calculator(self):
        geometry = self.window.geometry()
        self.window.destroy()
        calculator = Calculator("rational")
        calculator.window.geometry(geometry)
        calculator.run()

    def open_polynomial_calculator(self):
        geometry = self.window.geometry()
        self.window.destroy()
        calculator = Calculator("polynomial")
        calculator.window.geometry(geometry)
        calculator.run()


class Calculator:
    def __init__(self, calc_type):
        self.calc_type = calc_type
        self.window = tk.Tk()

        # Устанавливаем заголовок в зависимости от типа калькулятора
        titles = {
            "natural": "Калькулятор натуральных чисел",
            "integer": "Калькулятор целых чисел",
            "rational": "Калькулятор рациональных чисел",
            "polynomial": "Калькулятор полиномов"
        }

        self.window.title(titles.get(calc_type, "Калькулятор"))
        self.window.geometry("350x450")
        self.window.resizable(False, False)

        self.expression = ""

        self.create_widgets()

    def create_widgets(self):
        # Добавляем информацию о типе калькулятора
        type_label = tk.Label(self.window,
                              text=f"Тип: {self.get_calc_type_name()}",
                              font=('Arial', 10, 'bold'),
                              fg='blue')
        type_label.grid(row=0, column=0, columnspan=5, pady=(10, 0))

        self.display = tk.Entry(self.window, font=('Arial', 16), justify='right')
        self.display.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky='ew')

        info_label = tk.Label(self.window, text="Введите выражение", font=('Arial', 10))
        info_label.grid(row=2, column=0, columnspan=5, pady=(0, 10))

        buttons = [
            '7', '8', '9', '/', 'x²',
            '4', '5', '6', '*', 'x³',
            '1', '2', '3', '-', 'xⁿ',
            '0', 'x', '=', '+', 'C',
            '(', ')', '%', '//', '<—'
        ]

        row = 3
        col = 0

        for button in buttons:
            if button == '=':
                cmd = self.show_result
            elif button == 'C':
                cmd = self.clear
            elif button == '<—':
                cmd = self.backspace
            elif button in ['x²', 'x³', 'xⁿ']:
                cmd = lambda x=button: self.add_power(x)
            elif button == ' ':
                col += 1
                if col > 4:
                    col = 0
                    row += 1
                continue
            else:
                cmd = lambda x=button: self.add_to_expression(x)

            tk.Button(
                self.window,
                text=button,
                font=('Arial', 12),
                command=cmd,
                height=2,
                width=6
            ).grid(row=row, column=col, padx=2, pady=2, sticky='ew')

            col += 1
            if col > 4:
                col = 0
                row += 1

        # Кнопка для возврата к выбору калькулятора
        tk.Button(
            self.window,
            text="Назад к выбору",
            font=('Arial', 12),
            command=self.back_to_selector,
            height=2,
            bg='lightgreen'
        ).grid(row=row, column=0, columnspan=2, padx=2, pady=10, sticky='ew')

        tk.Button(
            self.window,
            text="Вычислить",
            font=('Arial', 12),
            command=self.show_result,
            height=2,
            bg='lightblue'
        ).grid(row=row, column=2, columnspan=3, padx=2, pady=10, sticky='ew')

    def get_calc_type_name(self):
        """Возвращает читаемое название типа калькулятора"""
        names = {
            "natural": "Натуральные числа",
            "integer": "Целые числа",
            "rational": "Рациональные числа",
            "polynomial": "Полиномы"
        }
        return names.get(self.calc_type, "Неизвестный тип")

    def add_to_expression(self, value):
        """Добавляет символ к выражению"""
        if self.calc_type in ["natural", "integer", "rational"] and value[0] == 'x':
            messagebox.showwarning("Ошибка", "В натуральном калькуляторе нельзя использовать переменную 'x'")
            return
        self.expression += str(value)
        self.update_display()

    def add_power(self, power_type):
        """Добавляет степень переменной"""
        if self.calc_type in ["natural","integer", "rational"] :
            messagebox.showwarning("Ошибка", "В данном калькуляторе нельзя использовать переменную 'x'")
            return
        if power_type == 'x²':
            self.expression += 'x^2'
        elif power_type == 'x³':
            self.expression += 'x^3'
        elif power_type == 'xⁿ':
            self.expression += 'x^'
        self.update_display()

    def clear(self):
        """Очищает выражение"""
        self.expression = ""
        self.update_display()

    def backspace(self):
        """Очищает последний символ выражения"""
        self.expression = self.expression[:-1]
        self.update_display()

    def show_result(self):
        """Получаем результат"""
        if self.expression:
            try:
                # Вычисляем результат в зависимости от типа калькулятора
                result = self.process_expression(self.expression)
                # Выводим результат в то же поле
                self.clear()
                self.expression = str(result)
                self.update_display()
            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка вычисления: {e}")
        else:
            messagebox.showwarning("Предупреждение", "Введите выражение")

    def update_display(self):
        """Обновляет отображение выражения"""
        self.display.config(state='normal')
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)
        self.display.config(state='readonly')

    def process_expression(self, expr):
        """Обрабатывает выражение в зависимости от типа калькулятора"""
        # Здесь будет происходить передача строки с выражением
        # в соответствующий модуль обработки

        # Заглушка для демонстрации
        if self.calc_type == "natural":
            ans = eval_rpn_n(to_rpn(expr))
            return f"{ans.show()}"
        elif self.calc_type == "integer":
            print(to_rpn(expr))
            ans = eval_rpn_z(to_rpn(expr))
            return f"{ans.show()}"
        elif self.calc_type == "rational":
            ans = eval_rpn_q(to_rpn(expr))
            return f"{ans.show()}"
        elif self.calc_type == "polynomial":
            ans = eval_rpn_p(to_rpn(expr))
            if type(ans) != Polynomial:
                ans = TRANS_Q_P(ans)
            return f"{ans.show()}"

        # но так же можно оставить старую обработку просто вставив ее СЮДА
        return 'answer'

    def back_to_selector(self):
        """Возврат к окну выбора калькулятора"""
        geometry = self.window.geometry()
        self.window.destroy()
        selector = CalculatorSelector()
        selector.window.geometry(geometry)
        selector.window.mainloop()

    def run(self):
        """Запускает приложение"""
        self.window.mainloop()


# Запуск приложения начинается с выбора калькулятора
if __name__ == "__main__":
    selector = CalculatorSelector().run()