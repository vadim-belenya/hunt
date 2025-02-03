import random


class Tiger:
    def __init__(self):
        self.state = "Выследить добычу"  # Атаковать добычу,Бежать домой.
        self.x = 0
        self.y = 0
        self.successful_attack_prob = 0.5

    def update_state(self):
        if self.state == "Выследить добычу":
            print("Тигр выслеживает добычу")
            print("Тигр движется в случайно направлении")  # Позже здесь будет вызвана функция движения
            print("Проверяем наличиерядом зайца")  # Позже здесь будет вызвана функция проверки на наличие рядом зайца
            print("Если заяц рядом,то меняем состоянеие на Атаковать добычу")
        elif self.state == "Атаковать добычу":
            a = random.random()
            if a > self.successful_attack_prob:
                print("Тигр успешно cхватил зайца")
                # Здесь будет вызвана функция захвата зайца
                self.state = "Бежать домой"
            else:
                print("Заяц убежал.Атака не состоялась")
        elif self.state == "Бежать домой":
            print("Тигр возвращается домой с добычей")
            self.x = 0
            self.y = 0

