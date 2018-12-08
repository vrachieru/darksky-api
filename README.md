<p align="center">
    <img src="https://user-images.githubusercontent.com/5860071/49687361-68206b80-fb0a-11e8-92bb-634a9ede62df.png" width="200px" />
    <br/>
    <a href="https://github.com/vrachieru/darksky-api/releases/latest">
        <img src="https://img.shields.io/badge/version-1.0.1-brightgreen.svg?style=flat-square" alt="Version">
    </a>
    <a href="https://travis-ci.org/vrachieru/darksky-api">
        <img src="https://img.shields.io/travis/vrachieru/darksky-api.svg?style=flat-square" alt="Version">
    </a>
    <br/>
    Dark Sky API wrapper
</p>

## Features

* Get complete (current/minutely/hourly/daily) forecast for location

## Install

```bash
$ pip3 install git+https://github.com/vrachieru/darksky-api.git
```
or
```bash
$ git clone https://github.com/vrachieru/darksky-api.git
$ pip3 install ./darksky-api
```

## Usage

All usage requires a Dark Sky API key, which you can obtain from the [Dark Sky developer site](https://darksky.net/dev/).  
To use the client, instantiate a [DarkSky](https://github.com/vrachieru/darksky-api/blob/master/darksky/api.py#L4) with your Dark Sky API key:

```python
from darksky import DarkSky

darksky = DarkSky('YOUR_API_KEY')
forecast = darksky.get(47.2, 27.6)

print('Summary: %s' % forecast.currently.summary)
print('Temperature: %s*C, feels like %s*C' % (forecast.currently.temperature, forecast.currently.apparentTemperature))
```

```bash
$ python3 example.py
Summary: Partly Cloudy
Temperature: 0*C, feels like -4*C
```

See the [Forecast](https://github.com/vrachieru/darksky-api/blob/master/darksky/model.py#L4), [DataBlock](https://github.com/vrachieru/darksky-api/blob/master/darksky/model.py#L39), and [DataPoint](https://github.com/vrachieru/darksky-api/blob/master/darksky/model.py#L80) structs to get a picture of the shape of the returned data.

You may also want to explore the [Dark Sky Response Format documentation](https://darksky.net/dev/docs/response), which explains when each property is expected to be populated (note that [DataPoint](https://github.com/vrachieru/darksky-api/blob/master/darksky/model.py#L80)) will be very sparse for certain kinds of output.

## License

MIT