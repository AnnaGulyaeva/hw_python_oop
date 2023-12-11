from abc import ABCMeta, abstractmethod


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

    __metaclass__ = ABCMeta

    M_IN_KM: int = 1000
    H_IN_M: int = 60
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
        distanse = self.action * self.LEN_STEP / self.M_IN_KM
        return distanse

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        mean_speed: float = 0.0
        distance = self.get_distance()
        mean_speed = distance / self.duration
        return mean_speed

    @abstractmethod
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""

        distance: float = self.get_distance()
        speed: float = self.get_mean_speed()
        calories: float = self.get_spent_calories()
        training_type: str = self.__class__.__name__

        message_obj: InfoMessage = InfoMessage(
            training_type, self.duration, distance, speed, calories
        )
        return message_obj


class Running(Training):
    """Тренировка: бег."""

    CALORIES_MEAN_SPEED_MULTIPLIER: int = 18
    CALORIES_MEAN_SPEED_SHIFT: float = 1.79

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float) -> None:
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        mean_speed: float = super().get_mean_speed()
        spend_calories: float = 0.0
        spend_calories = ((self.CALORIES_MEAN_SPEED_MULTIPLIER * mean_speed
                           + self.CALORIES_MEAN_SPEED_SHIFT) * self.weight
                          / self.M_IN_KM * self.duration * self.H_IN_M)
        return spend_calories

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""

        distance: float = super().get_distance()
        speed: float = super().get_mean_speed()
        calories: float = self.get_spent_calories()
        training_type: str = self.__class__.__name__

        message_obj: InfoMessage = InfoMessage(
            training_type, self.duration, distance, speed, calories
        )
        return message_obj


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    CALORIES_WEIGHT_MULTIPLIER_1: float = 0.035
    CALORIES_WEIGHT_MULTIPLIER_2: float = 0.029
    KM_IN_H_TO_M_IN_S: float = 0.278
    SM_TO_M = 100

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        mean_speed: float = super().get_mean_speed() * self.KM_IN_H_TO_M_IN_S
        spend_calories: float = 0.0
        spend_calories = ((self.CALORIES_WEIGHT_MULTIPLIER_1 * self.weight
                           + (mean_speed ** 2 / self.height * self.SM_TO_M)
                           * self.CALORIES_WEIGHT_MULTIPLIER_2 * self.weight)
                          * self.duration * self.H_IN_M)
        return spend_calories

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""

        distance: float = super().get_distance()
        speed: float = super().get_mean_speed()
        calories: float = self.get_spent_calories()
        training_type: str = self.__class__.__name__

        message_obj: InfoMessage = InfoMessage(
            training_type, self.duration, distance, speed, calories
        )
        return message_obj


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP: float = 1.38
    CALORIES_MEAN_SPEED_SHIFT: float = 1.1
    CALORIES_WEIGHT_MULTIPLIER: float = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        mean_speed: float = 0.0
        mean_speed = (self.length_pool * self.count_pool
                      / self.M_IN_KM / self.duration)
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        mean_speed: float = self.get_mean_speed()
        spend_calories: float = 0.0
        spend_calories = ((mean_speed + self.CALORIES_MEAN_SPEED_SHIFT)
                          * self.CALORIES_WEIGHT_MULTIPLIER
                          * self.weight * self.duration)
        return spend_calories

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""

        distance: float = super().get_distance()
        speed: float = self.get_mean_speed()
        calories: float = self.get_spent_calories()
        training_type: str = self.__class__.__name__

        message_obj: InfoMessage = InfoMessage(
            training_type, self.duration, distance, speed, calories
        )
        return message_obj


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""

    workout_types: dict = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    return workout_types[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""

    info: InfoMessage = training.show_training_info()
    print(info)


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
