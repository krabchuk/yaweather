# YaWeather | Yandex Weather API

[![Python](https://img.shields.io/badge/Python-3.6%20%7C%203.7%20%7C%203.8-blue.svg?longCache=true)]()
[![PyPI](https://img.shields.io/pypi/v/yaweather.svg)](https://pypi.python.org/pypi/yaweather)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/uburuntu/yaweather/blob/master/LICENSE)

[![Build Status](https://travis-ci.org/uburuntu/yaweather.svg?branch=master)](https://travis-ci.org/uburuntu/yaweather)

☀️🌤🌧🌩❄️ Yandex Weather API wrapper with typings and asyncio support.

Docs: https://tech.yandex.com/weather/doc/dg/concepts/forecast-test-docpage ([RU](https://yandex.ru/dev/weather/doc/dg/concepts/forecast-test-docpage/))

Get API Key: https://developer.tech.yandex.ru/services/18

![](https://i.imgur.com/pMf2tpT.png)

## 📝 Table of Contents

- [🎒 Installation](#-installation)
- [🛠 Examples](#-examples)
  - [Simple](#simple)
  - [Simple Async](#simple-async)
  - [Forecasts](#forecasts)
  - [Forecasts Async](#forecasts-async)
- [📜 Manual](#-manual)
  - [Methods](#methods)
  - [Types](#types)
  - [In case of unsupported types](#in-case-of-unsupported-types)
- [👨🏻‍💻 Author](#-author)
- [💬 Contributing](#-contributing)
- [📝 License](#-license)


---

## 🎒 Installation
Just
```
pip install yaweather
```

## 🛠 Examples

### Simple

```python3
from yaweather import UnitedKingdom, YaWeather

y = YaWeather(api_key='secret')
res = y.forecast(UnitedKingdom.London)

print(f'Now: {res.fact.temp} °C, feels like {res.fact.feels_like} °C')
print(f'Condition: {res.fact.condition}')

```
Output:
```text
Now: 18.0 °C, feels like 15.0 °C
Condition: cloudy
```

### Simple Async

```python3
import asyncio

from yaweather import Russia, YaWeatherAsync


async def main():
    async with YaWeatherAsync(api_key='secret') as y:
        res = await y.forecast(Russia.Moscow)

        print(f'Now: {res.fact.temp} °C, feels like {res.fact.feels_like} °C')
        print(f'Condition: {res.fact.condition}')


asyncio.run(main())

```
Output:
```text
Now: 16.0 °C, feels like 16.0 °C
Condition: clear
```

### Forecasts

```python3
from yaweather import UnitedStates, YaWeather

y = YaWeather(api_key='secret')

res = y.forecast(UnitedStates.NewYork)

for f in res.forecasts:
    day = f.parts.day_short
    print(f'{f.date} | {day.temp} °C, {day.condition}')

```
Output:
```text
2020-07-30 | 32.0 °C, cloudy
2020-07-31 | 26.0 °C, light-rain
2020-08-01 | 28.0 °C, cloudy
2020-08-02 | 28.0 °C, rain
2020-08-03 | 28.0 °C, light-rain
2020-08-04 | 27.0 °C, rain
2020-08-05 | 29.0 °C, light-rain
```

### Forecasts Async

```python3
import asyncio

from yaweather import China, YaWeatherAsync


async def main():
    async with YaWeatherAsync(api_key='secret') as y:
        res = await y.forecast(China.Beijing)

        for f in res.forecasts:
            day = f.parts.day_short
            print(f'{f.date} | {day.temp} °C, {day.condition}')


asyncio.run(main())

```
Output:
```text
2020-07-31 | 34.0 °C, light-rain
2020-08-01 | 34.0 °C, cloudy
2020-08-02 | 30.0 °C, heavy-rain
2020-08-03 | 33.0 °C, cloudy
2020-08-04 | 35.0 °C, cloudy
2020-08-05 | 34.0 °C, light-rain
2020-08-06 | 31.0 °C, heavy-rain
```

## 📜 Manual

### Methods
API have one method:
* `forecast` — request for the forecast, return type: `ResponseForecast`

### Types
This library uses [pydantic](https://github.com/samuelcolvin/pydantic/) for parsing API responses.
You can see data models in [yaweather/models](yaweather/models).

### In case of unsupported types
API results can change and the library may not parse the new result. So you can request «raw» dicts: 
```python3
raw_dict = y.forecast_raw(UnitedKingdom.London)
```

## 👨🏻‍💻 Author

**Ramzan Bekbulatov**:
- Telegram: [@rm_bk](https://t.me/rm_bk)
- Github: [@uburuntu](https://github.com/uburuntu)

## 💬 Contributing

Contributions, issues and feature requests are welcome! 

## 📝 License

This project is [MIT](https://github.com/uburuntu/yaweather/blob/master/LICENSE) licensed.
