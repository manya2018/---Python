if __name__ == "__main__":
    class Animal:
        def __init__(self, name: str, age: int):
            """
            Создание объекта Animal


            name (str): имя животного
            age (int): возраст животного

    				Примеры:
            >>> animal = Animal("Мурка", 5)  # инициализация экземпляра класса
            """
            self.name = name
            self.age = age

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта класса Animal
            """
            return f"Animal: {self.name}"

        def __repr__(self) -> str:
            """
            Возвращает представление объекта класса Animal, которое можно использовать для создания точной копии объекта
            """
            return f"Animal(name='{self.name}', age={self.age})"

        def bathe_the_animal(self) -> str:
            """
            Купание животного
            """
            return "Животное помыто"

        def eat(self, food: str) -> None:
            """
            Кушает указанную еду


            food (str): еда, которую животное кушает
            """
            pass


    class Dog(Animal):
        def __init__(self, name: str, age: int, breed: str):
            """
            Конструктор класса Dog


            name (str): имя собаки
            age (int): возраст собаки
            breed (str): порода собаки

    				Примеры:
            >>> dog = Dog("Мурка", 5,"Корги")  # инициализация экземпляра класса

            """
            super().__init__(name, age)
            self.breed = breed

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта класса Dog
            """
            return f"Dog: {self.name}"

        def __repr__(self) -> str:
            """
            Возвращает представление объекта класса Dog, которое можно использовать для создания точной копии объекта
            """
            return f"Dog(name='{self.name}', age={self.age}, breed='{self.breed}')"

        def bathe_the_animal(self) -> str:
            """
            Купание животного
            """
            return super().bathe_the_animal() + " и счастливо идет к себе на лежанку ."

        def eat(self, food: str) -> None:
            """
            Кушает указанную еду


            food (str): еда, которую собака кушает
            """
            if food == "кость":
                print(f"{self.name} радостно грызет кость")
            else:
                print(f"{self.name} отказывается есть {food}")


    class Cat(Animal):
        def __init__(self, name: str, age: int, color: str):
            """
            Конструктор класса Cat


            name (str): имя кошки
            age (int): возраст кошки
            color (str): цвет кошки
            """
            super().__init__(name, age)
            self.color = color

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта класса Cat
            """
            return f"Cat: {self.name}"

        def __repr__(self) -> str:
            """
            Возвращает представление объекта класса Cat, которое можно использовать для создания точной копии объекта
            """
            return f"Cat(name='{self.name}', age={self.age}, color='{self.color}')"

        def bathe_the_animal(self) -> str:
            """
            Купание животного
            """
            return super().bathe_the_animal() + ", а исцарапанный хозяин ищет в аптечке бинты ."

        def eat(self, food: str) -> None:
            """
            Кушает указанную еду


            food (str): еда, которую кошка кушает

    				В данном случае необходимо перегрузить метод, ткразные животные любят есть разную еду
            """
            if food == "рыба":
                print(f"{self.name} с удовольствием поедает рыбу")
            else:
                print(f"{self.name} осматривает еду и уходит без еды")
    pass
