from .mixin import StringMixin
from .utils import date

class Forecast(StringMixin):
    def __init__(self, data):
        self.latitude  = data.get("latitude")
        self.longitude = data.get("longitude")
        self.timezone  = data.get("timezone")
        self.offset    = data.get("offset")
        self.currently = Currently(data.get("currently", {}))
        self.minutely  = Minutely(data.get("minutely", {}))
        self.hourly    = Hourly(data.get("hourly", {}))
        self.daily     = Daily(data.get("daily", {}))
        self.alerts    = map(Alert, data.get("alerts", []))
        self.flags     = Flags(data.get("flags", {}))
        self.apicalls  = data.get("apicalls")
        self.code      = data.get("code")

class Alert(StringMixin):
    def __init__(self, data):
        self.title       = data.get("title")
        self.description = data.get("description")
        self.time        = date(data.get("time"))
        self.expires     = data.get("expires")
        self.uri         = data.get("uri")

class Flags(StringMixin):
    def __init__(self, data):
        self.darkSkyUnavailable = data.get("darksky-unavailable")
        self.darkSkyStations    = data.get("darksky-stations", [])
        self.dataPointStations  = data.get("datapoint-stations", [])
        self.ISDStations        = data.get("isds-stations", [])
        self.LAMPStations       = data.get("lamp-stations", [])
        self.METARStations      = data.get("metars-stations", [])
        self.METNOLicense       = data.get("metnol-license")
        self.sources            = data.get("sources", [])
        self.units              = data.get("units")

class DataBlock(StringMixin):
    def __init__(self, data):
        self.summary = data.get('summary')
        self.icon    = data.get('icon')
        self.data    = map(DataPoint, data.get('data', []))

    def get(self, index=None):
        if index is None:
            return self.data
        elif index < self.count():
            return self.data[index]
        else:
            return None

    def count(self):
        return len(self.data)

class Minutely(DataBlock):
    def get_minute(self, minute):
        return self.get(minute)

    @property
    def minutes(self):
        return self.count()

class Hourly(DataBlock):
    def get_hour(self, hour):
        return self.get(hour)

    @property
    def hours(self):
        return self.count()

class Daily(DataBlock):
    def get_day(self, day):
        return self.get(day)

    @property
    def days(self):
        return self.count()

class DataPoint(StringMixin):
    def __init__(self, data):
        self.time                   = date(data.get("time"))
        self.summary                = data.get("summary")
        self.icon                   = data.get("icon")
        self.sunriseTime            = date(data.get("sunriseTime"))
        self.sunsetTime             = date(data.get("sunsetTime"))
        self.precipIntensity        = data.get("precipIntensity")
        self.precipIntensityMax     = data.get("precipIntensityMax")
        self.precipIntensityMaxTime = date(data.get("precipIntensityMaxTime"))
        self.precipProbability      = data.get("precipProbability")
        self.precipType             = data.get("precipType")
        self.precipAccumulation     = data.get("precipAccumulation")
        self.temperature            = data.get("temperature")
        self.temperatureMin         = data.get("temperatureMin")
        self.temperatureMinTime     = date(data.get("temperatureMinTime"))
        self.temperatureMax         = data.get("temperatureMax")
        self.temperatureMaxTime     = date(data.get("temperatureMaxTime"))
        self.apparentTemperature    = data.get("apparentTemperature")
        self.dewPoint               = data.get("dewPoint")
        self.windSpeed              = data.get("windSpeed")
        self.windBearing            = data.get("windBearing")
        self.cloudCover             = data.get("cloudCover")
        self.humidity               = data.get("humidity")
        self.pressure               = data.get("pressure")
        self.visibility             = data.get("visibility")
        self.ozone                  = data.get("ozone")
        self.moonPhase              = data.get("moonPhase")

class Currently(DataPoint):
    pass

class Units(StringMixin):
    AUTO = 'auto'
    CA   = 'ca'
    UK   = 'uk'
    US   = 'us'
    SI   = 'si'

class Language(StringMixin):
    ARABIC      = "ar"
    AZERBAIJANI = "az"
    BELARUSIAN  = "be"
    BOSNIAN     = "bs"
    CATALAN     = "ca"
    CHINESE     = "zh"
    CORNISH     = "kw"
    CROATIAN    = "hr"
    CZECH       = "cs"
    DUTCH       = "nl"
    ENGLISH     = "en"
    ESTONIAN    = "et"
    FRENCH      = "fr"
    GERMAN      = "de"
    GREEK       = "el"
    HUNGARIAN   = "hu"
    ICELANDIC   = "is"
    INDONESIA   = "nb"
    INDONESIAN  = "id"
    ITALIAN     = "it"
    PIGLATIN    = "x-pig-latin"
    POLISH      = "pl"
    PORTUGUESE  = "pt"
    RUSSIAN     = "ru"
    SERBIAN     = "sr"
    SLOVAK      = "sk"
    SLOVENIAN   = "sl"
    SPANISH     = "es"
    SWEDISH     = "sv"
    TETUM       = "te"
    TURKISH     = "tr"
    UKRAINIAN   = "uk"
