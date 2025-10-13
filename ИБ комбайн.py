import random
import tkinter as tk
from tkinter import ttk


class SecurityToolkit:
    SYMBOLS = {
           "lowerletters": "abcdefghijklmnopqrstuvwxyz",
           "upperletters": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
           "digits": "123456789",
           "symbols": "!@#$%^&*()_+-=[]{}|;:,.<>?"
        }
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("ИБ-комбайн v1.0")
        self.window.geometry("600x400")

        self.tab_control = ttk.Notebook(self.window) #Создание вкладок

        self.tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text='🔐 Генератор паролей')

        self.tab_control.pack(expand=1, fill="both")

        self.setup_password_generator_tab()

    def setup_password_generator_tab(self):
        output_frame = tk.Frame(self.tab1)
        output_frame.pack(pady=20)

        # Label - метка "Сгенерированный пароль"
        result_label = tk.Label(output_frame, text="Сгенерированный пароль:",
                                font=("Arial", 12, "bold"))
        result_label.pack()

        # Entry - поле для вывода пароля (можно выделить и скопировать)
        self.password_entry = tk.Entry(output_frame, font=("Arial", 14),
                                       width=30, justify='center', state='readonly')
        self.password_entry.pack(pady=10)

        # === ПОЛЗУНОК ДЛИНЫ ПАРОЛЯ ===
        length_frame = tk.Frame(self.tab1)
        length_frame.pack(pady=15)

        # метка для ползунка
        length_label = tk.Label(length_frame, text="Длина пароля:", font=("Arial", 11))
        length_label.pack()

        # Scale - ползунок (минимальное, максимальное значение)
        self.length_scale = tk.Scale(length_frame, from_=8, to=32,
                                     orient="horizontal", length=300,
                                     font=("Arial", 10))
        self.length_scale.set(12) # значение по умолчанию
        self.length_scale.pack(pady=5)

        # Галочки выбора символов
        checks_frame = tk.Frame(self.tab1)
        checks_frame.pack(pady=15)

        # Checkbutton - флажки (галочки)
        self.use_lower = tk.IntVar(value=1)
        self.use_upper = tk.IntVar(value=1)
        self.use_digits = tk.IntVar(value=1)
        self.use_symbols = tk.IntVar(value=1)

        # Флажки
        lower_check = tk.Checkbutton(checks_frame, text="Нижний регистр (abc)",
                                     variable=self.use_lower, font=("Arial", 10))
        lower_check.grid(row=0, column=0, sticky='w', padx=10)
        upper_check = tk.Checkbutton(checks_frame, text="Верхний регистр (ABC)",
                                     variable=self.use_upper, font=("Arial", 10))
        upper_check.grid(row=0, column=1, sticky='w', padx=10)
        digits_check = tk.Checkbutton(checks_frame, text="Цифры (123)",
                                     variable=self.use_digits, font=("Arial", 10))
        digits_check.grid(row=1, column=0, sticky='w', padx=10, pady=5)
        symbols_check = tk.Checkbutton(checks_frame, text="Спецсимволы (!@#)",
                                     variable=self.use_symbols, font=("Arial", 10))
        symbols_check.grid(row=1, column=1, sticky='w', padx=10, pady=5)

        # КНОПКА ГЕНЕРАЦИИ
        generate_btn = tk.Button(self.tab1, text="Сгененерировать пароль",
                                 command=self.generate_password,
                                 font=("Arial", 12, "bold"),
                                 bg="#2196F3", fg='white',
                                 width=20, height=2)
        generate_btn.pack(pady=20)

    def generate_password(self):
        """Функция генерации пароля"""
        try:
            # Получаем значения из интерфейса
            length = self.length_scale.get()

            # Получаем состояние галочек
            use_lower = self.use_lower.get()
            use_upper = self.use_upper.get()
            use_digits = self.use_digits.get()
            use_symbols = self.use_symbols.get()

            # Создаем фильтрованный словарь
            filtered_dict = {}
            if use_lower:
                filtered_dict["lowerletters"] = self.SYMBOLS["lowerletters"]
            if use_upper:
                filtered_dict["upperletters"] = self.SYMBOLS["upperletters"]
            if use_digits:
                filtered_dict["digits"] = self.SYMBOLS["digits"]
            if use_symbols:
                filtered_dict["symbols"] = self.SYMBOLS["symbols"]

            # Проверяем что выбрана хотя бы одна категория
            if not filtered_dict:
                settings = "Ошибка: выберите хотя бы одну категорию!"
            else:
                # Генерируем настоящий пароль
                settings = self.pass_generate(length, filtered_dict)
           

            # Включаем поле для записи, записываем, снова делаем readonly
            self.password_entry.config(state='normal')
            self.password_entry.delete(0, tk.END) # Очищаем поле
            self.password_entry.insert(0, settings) # Вставляем текст
            self.password_entry.config(state='readonly')
        except Exception as e:
            # Обработка других ошибок
            self.password_entry.config(state='normal')
            self.password_entry.delete(0, tk.END) # Очищаем поле
            self.password_entry.insert(0, settings) # Вставляем текст
            self.password_entry.config(state='readonly')

    def pass_generate(self, length, char_dict):
        password = []
        for category in char_dict:
            password.append(random.choice(char_dict[category]))

        while len(password) < length:
            category = random.choice(list(char_dict.keys()))
            password.append(random.choice(char_dict[category]))

        random.shuffle(password)

        return ''.join(password)

    def run(self):
        self.window.mainloop()

# Запуск
if __name__ == "__main__":
    app = SecurityToolkit()
    app.run()

        