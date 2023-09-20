![GitHub](https://img.shields.io/github/license/intervisionlord/NuPyBuilder)
[![Code Intelligence Status](https://scrutinizer-ci.com/g/intervisionlord/NuPyBuilder/badges/code-intelligence.svg?b=main)](https://scrutinizer-ci.com/code-intelligence)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/intervisionlord/NuPyBuilder/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/intervisionlord/NuPyBuilder/?branch=main)
[![Build Status](https://scrutinizer-ci.com/g/intervisionlord/NuPyBuilder/badges/build.png?b=main)](https://scrutinizer-ci.com/g/intervisionlord/NuPyBuilder/build-status/main)
[![wakatime](https://wakatime.com/badge/github/intervisionlord/NuPyBuilder.svg)](https://wakatime.com/badge/github/intervisionlord/NuPyBuilder)


# NuPyBuilder

- [Описание](#описание)
  - [Версии](#версии)
  - [Roadmap](#roadmap)
- [Принцип работы](#принцип-работы)
- [Зависимости](#зависимости)
- [GUI](#gui)
- [Настройки](#настройки)
  - [Настройки сборщика](#настройки-сборщика)
  - [Настройки проектов](#настройки-проектов)
    - [main](#main)
    - [source](#source)
    - [plugins](#plugins)
    - [params](#params)
    - [files](#files)


## Описание
Надстройка для Nuitka, позволяющая запускать сборку нескольких проектов с использованием индивидуальных конфигураций под каждый проект.

### Версии
* pre-alpha version - релиз не опубликован

### Roadmap
Релиз стабильной версии -> GUI -> WIN-Версия

## Принцип работы
Для каждого из проектов заполняется файл конфигурации, в котором указываются все необходимые для сборки данные, а также, дополнительные параметры, позволяющие расширить возможности дистрибуции собранного проекта.

После запуска сборщика с указанием целевого конфига вызывается Nuitka, с подставленными из конфига параметрами и происходит сборка.

После сборки происходит копирование указанных в конфиге дополнительных файлов и директорий, а также, если это указано, происходит упаковка всех файлов в архив.

## Зависимости
* Nuitka

## GUI
В разработке

## Настройки
Все настройки выполнены в виде `yaml` файлов.

### Настройки сборщика
Базовые настройки:
*core.yaml*
```
main: # Основная секция конфига
  name: NuPyBuilder # название сборщика
  version: 0.0.4.1 # текущая версия сборщика
  author: intervision # разработчик
  authorlink: https://github.com/intervisionlord # ссылка на профиль в github

default_params: # Параметры по-умолчанию используются если не указаны в индивидуальном конфиге сборки
  - windows-disable-console
  - follow-imports
  - onefile
  - standalone
  - remove-output
  - windows-product-name="NuPyProject"
  - windows-company-name="CompanyName"
  - windows-product-version="0.0.0.0"
  - windows-file-description="Product description"
```

### Настройки проектов
Настройки сборок можно создать по примеру `example.yaml`, все параметры описаны и прокомментированы в файле-примере.

#### main
**product_name:**
Название программы. Используется для подстановки в свойства собранного исполняемого файла и в названии самого файла при сборке.

**version:**
Версия программы. Используется в свойствах собранного файла. Формат в виде 4х цифр, разделенных точками.

**author:**
Имя автора программы. Использутся в свойствах собранного файла.

**authorlink:**
Ссылка на ресурс автора. На данный момент **не используется!**

**icon:**
Путь к иконке для собранного исполняемого файла. Допускается использование `*.PNG` и `*.ICO`

#### source
**mainfile:**
Путь до основного файла скрипта `*.py`

**outputfile:**
Название скомпилированного файла

**workdir:**
Путь до директории, в которой располагаются сопутствующие файлы проекта. *(На данный момент не используется)*

#### plugins
**Примечание:** На данный момент реализовано только использование одного плагина (PyQT/Pyside2)

#### params
В большинстве случаев эту секцию можно не менять, за исколючением параметров, содержащих данные о названии прогрмаммы и разработчике.

Для изменения параметров и добавления новых необходимо ознакомиться с документацией по Nuitka.

#### files
Пути до дополнительный файлов, используемых программой, которые должны быть помещены в архив после завершения сборки.