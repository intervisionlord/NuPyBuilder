"""Модуль записи раздельных логов по каждой сборке."""
from datetime import datetime

class Log:
    """Создание файла лога для каждой задачи с записью.
    """
    # Тут неплохо добавить проверку, существует ли файл или нет
    # pylint: disable=consider-using-with
    # Тут придется именно так.
    def __init__(self, logfile) -> None:
        self.build_name = logfile
        self.logfile = open(f'logs/{logfile}.log', 'a', encoding = 'utf8')
        self.separator = '=' * 10

    def write(self, row) -> None:
        """Запись передаваемых данных в лог.

        Args:
            row (str): передаваемая строка для записи в лог
        """
        self.logfile.write(f'{datetime.now()} -- {row}\n')

    def start(self) -> None:
        """Начало очередной сборки.
        """
        self.logfile.write(
            f'{datetime.now()}\n \
            Сборка {self.build_name} начата\n'
            )

    def stop(self) -> None:
        """Завершение сборки.
        """
        self.logfile.write(
            f'\n{self.separator}\n',
            datetime.now(),
            'Сборка завершена',
            f'\n{self.separator}\n'
            )
        self.logfile.close()
