M_IN_KM: int = 1000


class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float
                 ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def __str__(self) -> str:
        return self.get_message()

    def get_message(self) -> str:
        """Получить информационное сообщение о тренировке."""

        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}.')


class Training:
    """Базовый класс тренировки."""

    LEN_STEP: float = 0.65

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""

        distanse: float = 0.0
        distanse = self.action * self.LEN_STEP / M_IN_KM
        return distanse

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        mean_speed: float = 0.0
        mean_speed = self.get_distance() / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""

        distance = self.get_distance()
        speed = self.get_mean_speed()
        calories = self.get_spend_calories()

        message_obj: InfoMessage = InfoMessage(
            training_type, self.duration, distance, speed, calories
        )
        return message_obj


class Running(Training):
    """Тренировка: бег."""

    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79
    CALORIES_DURATION_MULTIPIER = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float) -> None:
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        mean_speed = super().get_mean_speed()
        spend_calories = ((self.CALORIES_MEAN_SPEED_MULTIPLIER * mean_speed
                           + self.CALORIES_MEAN_SPEED_SHIFT) * super().weight
                          / (M_IN_KM * super().duration
                             * self.CALORIES_DURATION_MULTIPIER))
        return spend_calories

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""

        distance = self.get_distance()
        speed = self.get_mean_speed()
        calories = self.get_spend_calories()

        message_obj: InfoMessage = InfoMessage(
            training_type, self.duration, distance, speed, calories
        )
        return message_obj


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    CALORIES_WEIGHT_MULTIPLIER_1 = 0.035
    CALORIES_WEIGHT_MULTIPLIER_2 = 0.029
    CALORIES_MEAN_SPEAD_DIVIDER = 3.6
    CALORIES_DURATION_MULTIPLIER = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        mean_speed = super().get_mean_speed()
        spend_calories = ((self.CALORIES_WEIGHT_MULTIPLIER_1 * super().weight
                           + ((mean_speed
                               / self.CALORIES_MEAN_SPEAD_DIVIDER)**2
                               / self.height)
                           * (self.CALORIES_WEIGHT_MULTIPLIER_2
                           * super().weight) * super().duration
                           * self.CALORIES_DURATION_MULTIPLIER))
        return spend_calories

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""

        distance = self.get_distance()
        speed = self.get_mean_speed()
        calories = self.get_spend_calories()

        message_obj: InfoMessage = InfoMessage(
            training_type, self.duration, distance, speed, calories
        )
        return message_obj


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP: float = 1.38

    def __init__(self, action: int, duration: float, weight: float) -> None:
        super().__init__(action, duration, weight)
        super().get_distance()
    
    def get_distance(self) -> float:
        """Получить дистанцию в км."""

        distanse: float = 0.0
        distanse = self.action * LEN_STEP / M_IN_KM
        return distanse

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        mean_speed: float = 0.0
        mean_speed = self.get_distance() / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""

        distance = self.get_distance()
        speed = self.get_mean_speed()
        calories = self.get_spend_calories()

        message_obj: InfoMessage = InfoMessage(
            training_type, self.duration, distance, speed, calories
        )
        return message_obj


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
