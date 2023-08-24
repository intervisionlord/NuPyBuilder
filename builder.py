import zipfile
from yaml import full_load as loadyaml
from os import system as runCommand
from datetime import datetime
# from functions.man import manpage as man

class build_config:
    """Класс динамической конфигурации
    """
    def __init__(self, build_config: str = 'configs/config.yaml') -> None:
        config_file = f'./configs/{build_config}.yaml'
        try:
            with open(config_file, 'r') as build_config:
                self.config_file = loadyaml(build_config)
        except FileNotFoundError:
            exit(f'[Err.:6] Файл не найден или не указан: {config_file}')
        self.mainfile: str = self.config_file['source']['mainfile']
        self.outfile: str = self.config_file['source']['outputfile']
        self.workdir: str = self.config_file['source']['workdir']
        self.version, self.author, self.authorlink = [
            self.config_file['main']['version'],
            self.config_file['main']['author'],
            self.config_file['main']['authorlink']
            ]
        self.plugins = self.config_file['plugins']
        self.params: list = self.config_file['params']
        self.product_name: str = self.config_file['main']['product_name']
    
    def outprint(self) -> None:
        today = datetime.today().strftime('%d-%m-%Y  %H:%M:%S')
        print('-' * 10, f'\n{today}\n', '-' * 10)
        print('Config directives\n'
              f'WorkDir: {self.workdir}\n'
              f'Main File: {self.mainfile}\n'
              f'Output File: {self.outfile}\n'
              
              '\nProdut info\n'
              f'Version: {self.version}\n'
              f'Author: {self.author}\n'
              f'Authorlink: {self.authorlink}\n'
              f'Product Name: {self.product_name}\n'
              
              '\nBuild Plugins\n'
              f'Plugins: {self.plugins}'
              
              '\nBuild parameters\n'
              f'Parameters: {self.params}\n'
              )
        print('-' * 10)
    
    def zip_output(self) -> None:
        """Упаковывает собранные файлы в архив
        """
        with zipfile.ZipFile(f'{self.product_name}.zip',
                             'w',
                             compression=zipfile.ZIP_DEFLATED,
                             compresslevel=9) as zipArch:
            zipArch.write(f'{self.product_name}.exe')

def build_start(config_input):
    config = build_config(config_input)
    config.outprint()


if __name__ == '__main__':
    # man()
    config_input = input('Укажите файл сборки конфига:')
    if config_input is None or config_input == '':
        print('Конфиг не указан')
    else:
        build_start(config_input)

# exit

# def getconfig() -> dict:
#     """Загружает данные из конфига сборки.

#     Returns:
#         dict: Список переменных конфига
#     """
#     try:
#         with open('./config.yaml', 'r') as confFile:
#             conf: dict = loadyaml(confFile)
#     except FileNotFoundError:
#         print('File not found')
#     return conf

# def zipOutput():
#     """Упаковывает готовый файл в архив.
#     """
#     with zipfile.ZipFile('SimpleTester.zip', 'w',
#                          compression=zipfile.ZIP_DEFLATED,
#                          compresslevel=9) as zipArch:
#         zipArch.write('SimpleTester.exe')

# def makeParamStr(getconfig) -> str:
#     """Создает строку параметров сборки из данных конфига.

#     Args:
#         getconfig (function): Принимает на вход функцию парсинга конфига

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

# if __name__ == '__main__':
#     """Запуск сборки бинарного файла и его упаковка в архив.
#     """
#     paramsStr = makeParamStr(getconfig())
#     plugins = getconfig()['plugins']
#     icon = getconfig()['main']['icon']
#     runCommand(f'nuitka {paramsStr} --plugin-enable={plugins} --windows-icon-from-ico={icon} --include-data-files=../ui/imgs/*.png=imgs/ ../SimpleTester.py')
#     zipOutput()