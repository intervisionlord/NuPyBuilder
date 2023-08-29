import zipfile
from yaml import full_load as loadyaml
from os import system as runCommand
from os import path
from sys import argv
from sys import exit as sysexit
from datetime import datetime
# from functions.man import manpage as man

class BuildConfig:
    """Класс динамической конфигурации
    """
    # pylint: disable=too-many-instance-attributes
    # Может быть будет оптимизировано. А может и нет.
    def __init__(self, build_config: str = 'configs/config.yaml') -> None:
        # Тут нужно точно сделать оптимальнее
        config_file = f'./configs/{build_config}.yaml'
        try:
            with open(config_file, 'r', encoding = 'utf8') as build_config_file:
                self.config_file = loadyaml(build_config_file)
        except FileNotFoundError:
            sysexit(f'[Err.:6] Файл не найден или не указан: {config_file}')
        # Cекция source конфига
        self.mainfile, self.outfile, self.workdir = [
            self.config_file['source']['mainfile'],
            self.config_file['source']['output'],
            self.config_file['source']['workdir']
        ]
        # Секция main конфига
        self.version, self.author, self.authorlink = [
            self.config_file['main']['version'],
            self.config_file['main']['author'],
            self.config_file['main']['authorlink']
            ]
        # Прочие детали конфига
        self.plugins = self.config_file['plugins']
        self.params: list = self.config_file['params']
        self.addition_files = self.config_file['files']
        self.product_name: str = self.config_file['main']['product_name']
    # Вывод параметров конфига, в случае необходимости
    def outprint(self) -> None:
        """Вывод параметров конфига
        """
        today = datetime.today().strftime('%d-%m-%Y  %H:%M:%S')
        print('-' * 10, f'\n{today}\n', '-' * 10)
        print('Config directives\n'
              # Секция предварительных настроек
              f'WorkDir: {self.workdir}\n'
              f'Main File: {self.mainfile}\n'
              f'Output File: {self.outfile}\n'
              # Секция продукта / сборки
              '\nProdut info\n'
              f'Version: {self.version}\n'
              f'Author: {self.author}\n'
              f'Authorlink: {self.authorlink}\n'
              f'Product Name: {self.product_name}\n'
              # Секция плагинов
              '\nBuild Plugins\n'
              f'Plugins: {self.plugins}'
              # Секция параметров
              '\nBuild parameters\n'
              f'Parameters: {self.params}\n'
              )
        print('-' * 10)
    # Упаковка сборки в архив
    def zip_output(self) -> None:
        """Упаковывает собранные файлы в архив
        """
        with zipfile.ZipFile(f'{self.product_name}.zip',
                             'w',
                             compression=zipfile.ZIP_DEFLATED,
                             compresslevel=9) as zip_arch:
            zip_arch.write(self.outfile)
            if len(self.addition_files) > 0: # Протестировать бы, но потом...
                for other_files in self.addition_files:
                    secondpth = f'{path.basename(path.dirname(path.abspath(other_files)))}/{path.basename(other_files)}'
                    zip_arch.write(path.abspath(other_files), secondpth)
        zip_arch.close() # Но это не точно...
# Получение основного конфига (не тестировалось)
def get_core_config() -> dict:
    """Читает конфиг сборщка

    Returns:
        dict: Словарь с параметрами конфигурации сборщика
    """
    try:
        with open('configs/core.yaml', 'r') as core_c:
            core_config = loadyaml(core_c)
    except FileNotFoundError:
        print('File not found')
        sysexit(6) # Потому что 42, вот почему!
    return core_config
# Получение конфига сборки (не тестировалось)
def get_build_config(conf_path: str) -> dict:
    """Читает конфиг сборки

    Args:
        conf_path (str): Путь до персонализированного конфига сборки

    Returns:
        dict: Словарь с параметрами конфигурации определенной сборки
    """
    if conf_path == '':
        print(
            'Не указан файл конфигурации сборки.\n'
            f'Необходимо запускать "{argv[0]} <путь до конфига>"')
    else:
        with open(conf_path, 'r', encoding = 'utf8') as build_conf_yaml:
            build_config = loadyaml(build_conf_yaml)
            return build_config
# Запуск алгоритма сборки
def build_start(config_input: str) -> None:
    """Запуск алгоритма сборки

    Args:
        config_input (str): Путь к файлу конфига сборки
    """
    config = BuildConfig(config_input)
    config.outprint()
# Запуск скрипта
if __name__ == '__main__':
    """Запуск скрипта
    """
    # man()
    set_build_config = input('Укажите файл сборки конфига:')
    if set_build_config is None or set_build_config == '':
        print('Конфиг сборки не указан')
    else:
        build_start(set_build_config)
### Старые наработки, они будут понемногу переноситься в основной код,
### Но в нормальном виде. После переноса и тестирования они должны быть удалены.
#
# def getconfig() -> dict:
#     """Загружает данные из конфига сборки.
#
#     Returns:
#         dict: Список переменных конфига
#     """
#     try:
#         with open('./config.yaml', 'r') as confFile:
#             conf: dict = loadyaml(confFile)
#     except FileNotFoundError:
#         print('File not found')
#     return conf
#
# def zipOutput():
#     """Упаковывает готовый файл в архив.
#     """
#     with zipfile.ZipFile('SimpleTester.zip', 'w',
#                          compression=zipfile.ZIP_DEFLATED,
#                          compresslevel=9) as zipArch:
#         zipArch.write('SimpleTester.exe')
#
# def makeParamStr(getconfig) -> str:
#     """Создает строку параметров сборки из данных конфига.
#
#     Args:
#         getconfig (function): Принимает на вход функцию парсинга конфига
#
#     Returns:
#         str: Строка с набором параметров сборки
#     """
#     paramList = []
#     for param in getconfig['params']:
#         if param == 'windows-product-version':
#             param = '{}="{}"'.format(param, getconfig['main']['version'])
#         paramList.append(param)
#     paramStr = '--' + ' --'.join(paramList)
#     return paramStr    
#
# if __name__ == '__main__':
#     """Запуск сборки бинарного файла и его упаковка в архив.
#     """
#     paramsStr = makeParamStr(getconfig())
#     plugins = getconfig()['plugins']
#     icon = getconfig()['main']['icon']
#     runCommand(f'nuitka {paramsStr} --plugin-enable={plugins} --windows-icon-from-ico={icon} --include-data-files=../ui/imgs/*.png=imgs/ ../SimpleTester.py')
#     zipOutput()