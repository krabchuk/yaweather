# YaWeather | Yandex Weather API

[![Python](https://img.shields.io/badge/Python-3.6%20%7C%203.7%20%7C%203.8-blue.svg?longCache=true)]()
[![PyPI](https://img.shields.io/pypi/v/yaweather.svg)](https://pypi.python.org/pypi/yaweather)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/uburuntu/yaweather/blob/master/LICENSE)

[![Build Status](https://travis-ci.org/uburuntu/yaweather.svg?branch=master)](https://travis-ci.org/uburuntu/yaweather)

☀️🌤🌧🌩❄️ Yandex Weather API wrapper with typings and asyncio support.

Docs: https://tech.yandex.com/weather/doc/dg/concepts/forecast-test-docpage ([RU](https://yandex.ru/dev/weather/doc/dg/concepts/forecast-test-docpage/))

Get API Key: https://developer.tech.yandex.ru/services/18

{toc}

---

## 🎒 Installation
Just
```
pip install yaweather
```

## 🛠 Examples

### Simple

```python3
{simple}
```
Output:
```text
Now: 18.0 °C, feels like 15.0 °C
Condition: cloudy
```

### Simple Async

```python3
{simple_async}
```
Output:
```text
Now: 16.0 °C, feels like 16.0 °C
Condition: clear
```

### Forecasts

```python3
{forecasts}
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
{forecasts_async}
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
