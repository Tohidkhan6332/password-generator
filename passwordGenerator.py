import threading
import random
import string


class PasswordGenerator:
    def __init__(self, possible_combination: int, combination_type: int, count_threads: int):
        self.possible_combination = possible_combination
        self.combination_type = combination_type
        self.special_character = string.punctuation
        self.numeric = string.digits
        self.alphabet = string.ascii_letters  # Используем встроенные константы
        self.get_character = ""
        self.count_threads = count_threads
        self.passwords = []

    def generate_get_character(self):
        if self.combination_type == 1:
            self.get_character = self.numeric + self.alphabet
        elif self.combination_type == 2:
            self.get_character = self.numeric
        elif self.combination_type == 3:
            self.get_character = self.alphabet
        elif self.combination_type == 4:
            self.get_character = self.special_character
        elif self.combination_type == 5:
            self.get_character = self.special_character + self.numeric
        elif self.combination_type == 6:
            self.get_character = self.special_character + self.numeric + self.alphabet
        else:
            raise ValueError("Invalid combination_type")

    def generate_password(self):
        for _ in range(self.possible_combination):
            password = ''.join(random.choice(self.get_character) for _ in range(self.possible_combination))
            self.passwords.append(password)

    def generate_password_thread(self):
        self.generate_password()

    def generate_passwords(self):
        self.generate_get_character()
        threads = []

        for _ in range(self.count_threads):
            thread = threading.Thread(target=self.generate_password_thread)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        self.write_to_file()

    def write_to_file(self):
        with open("password_list.txt", "w") as file:
            for password in self.passwords:
                file.write(password + "\n")

if __name__ == "__main__":
    possible_combination = int(input("How many password combinations do you want to create?: "))
    combination_type = int(input("Enter combination type (1-6): "))
    count_threads = int(input("How many threads to use? "))

    generator = PasswordGenerator(possible_combination, combination_type, count_threads)
    generator.generate_passwords()
