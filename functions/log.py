"""Модуль записи раздельных логов по каждой сборке."""
from datetime import datetime

class Log:
    """Создание файла лога для каждой задачи с записью.
    """
    # Тут неплохо добавить проверку, существует ли файл или нет
    def __init__(self, logfile) -> None:
        with open(f'log/{logfile}', 'w', encoding = 'utf8') as opened_logfile:
            self.logfile = opened_logfile
        self.now = datetime.now()
        self.separator = '=' * 10

    def write(self, row) -> None:
        """Запись передаваемых данных в лог.

        Args:
            row (str): передаваемая строка для записи в лог
        """
        self.logfile.write(f'{row}\n')
        self.logfile.close()

    def start(self) -> None:
        """Начало очередной сборки.
        """
        self.logfile.write(
            f'\n{self.separator}\n',
            self.now(),
            f'Сборка {self.logfile} начата',
            f'\n{self.separator}\n'
            )

    def stop(self) -> None:
        """Завершение сборки.
        """
        self.logfile.write(
            f'\n{self.separator}\n',
            self.now(),
            'Сборка завершена',
            f'\n{self.separator}\n'
            )
