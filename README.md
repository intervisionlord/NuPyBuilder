![GitHub](https://img.shields.io/github/license/intervisionlord/NuPyBuilder)
[![Code Intelligence Status](https://scrutinizer-ci.com/g/intervisionlord/NuPyBuilder/badges/code-intelligence.svg?b=main)](https://scrutinizer-ci.com/code-intelligence)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/intervisionlord/NuPyBuilder/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/intervisionlord/NuPyBuilder/?branch=main)
[![Build Status](https://scrutinizer-ci.com/g/intervisionlord/NuPyBuilder/badges/build.png?b=main)](https://scrutinizer-ci.com/g/intervisionlord/NuPyBuilder/build-status/main)
[![wakatime](https://wakatime.com/badge/github/intervisionlord/NuPyBuilder.svg)](https://wakatime.com/badge/github/intervisionlord/NuPyBuilder)


# NuPyBuilder

- [Описание](#описание)
- [Принцип работы](#принцип-работы)
- [Зависимости](#зависимости)
- [GUI](#gui)
- [Настройки](#настройки)
  - [Настройки сборщика](#настройки-сборщика)
  - [Настройки проектов](#настройки-проектов)
    - [Пример конфига](#пример-конфига)


## Описание
Надстройка для Nuitka, позволяющая запускать сборку нескольких проектов с использованием индивидуальных конфигураций под каждый.
## Принцип работы
Для каждого из проектов заполняется файл конфигурации, в котором указываются все необходимые для сборки данные, а также, дополнительные параметры, позволяющие расширить возможности дистрибуции собранного проекта.

После запуска сборщика с указанием целевого конфига вызывается Nuitka, с подставленными из конфига параметрами и происходит сборка.

После сборки происходит копирование указанных в конфиге дополнительных файлов и директорий, а также, если это указано, происходит упаковка всех файлов в архив.
## Зависимости
* Nuitka
## GUI
В разработке
## Настройки
### Настройки сборщика
### Настройки проектов
#### Пример конфига