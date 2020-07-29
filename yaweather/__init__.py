"""Yandex Weather API with asyncio support and typings"""

from . import cities
from .cities import Afghanistan, Albania, Algeria, AmericanSamoa, Andorra, Angola, AntiguaAndBarbuda, Argentina, Armenia, Aruba, Australia, \
    Austria, Azerbaijan, Bahamas, Bahrain, Bangladesh, Barbados, Belarus, Belgium, Belize, Benin, Bhutan, Bolivia, BosniaAndHerzegovina, \
    Botswana, Brazil, Brunei, Bulgaria, BurkinaFaso, Burma, Burundi, CaboVerde, Cambodia, Cameroon, Canada, CentralAfricanRepublic, Chad, \
    Chile, China, Colombia, Comoros, CongoBrazzaville, CongoKinshasa, CostaRica, CoteDIvoire, Croatia, Cuba, Curacao, Cyprus, Czechia, \
    Denmark, Djibouti, Dominica, DominicanRepublic, Ecuador, Egypt, ElSalvador, EquatorialGuinea, Eritrea, Estonia, Ethiopia, Fiji, Finland, \
    France, Gabon, Gambia, Georgia, Germany, Ghana, Greece, Grenada, Guam, Guatemala, Guinea, GuineaBissau, Guyana, Haiti, Honduras, \
    HongKong, Hungary, Iceland, India, Indonesia, Iran, Iraq, Ireland, Israel, Italy, Jamaica, Japan, Jordan, Kazakhstan, Kenya, Kiribati, \
    KoreaNorth, KoreaSouth, Kosovo, Kuwait, Kyrgyzstan, Laos, Latvia, Lebanon, Lesotho, Liberia, Libya, Liechtenstein, Lithuania, \
    Luxembourg, Macau, Macedonia, Madagascar, Malawi, Malaysia, Maldives, Mali, Malta, MarshallIslands, Mauritania, Mauritius, Mexico, \
    Micronesia, Moldova, Monaco, Mongolia, Montenegro, Morocco, Mozambique, Namibia, Nepal, Netherlands, NewZealand, Nicaragua, Niger, \
    Nigeria, NorthernMarianaIslands, Norway, Oman, Pakistan, Palau, Panama, PapuaNewGuinea, Paraguay, Peru, Philippines, Poland, Portugal, \
    Qatar, Romania, Russia, Rwanda, SaintKittsAndNevis, SaintLucia, SaintVincentAndTheGrenadines, Samoa, SanMarino, SaoTomeAndPrincipe, \
    SaudiArabia, Senegal, Serbia, Seychelles, SierraLeone, Singapore, SintMaarten, Slovakia, Slovenia, SolomonIslands, Somalia, SouthAfrica, \
    SouthSudan, Spain, SriLanka, Sudan, Suriname, Swaziland, Sweden, Switzerland, Syria, Taiwan, Tajikistan, Tanzania, Thailand, TimorLeste, \
    Togo, Tonga, TrinidadAndTobago, Tunisia, Turkey, Turkmenistan, Tuvalu, Uganda, Ukraine, UnitedArabEmirates, UnitedKingdom, UnitedStates, \
    Uruguay, Uzbekistan, Vanuatu, Venezuela, Vietnam, WestBank, Yemen, Zambia, Zimbabwe
from .main import YaWeather, YaWeatherAPIError, YaWeatherAsync, YaWeatherBase
from .models.base import Base, Condition, DayTime, Lang, MoonCode, MoonText, PhenomCondition, PrecipitationType, Season, WindDir
from .models.fact import Fact
from .models.info import Info, TzInfo
from .models.request import Request, RequestForecast
from .models.response import Response, ResponseForecast

__author__ = 'uburuntu'
__email__ = 'github@rmbk.me'

__license__ = 'MIT'
__version__ = '1.1.0'

__all__ = (
    'Base',
    'Condition',
    'DayTime',
    'Fact',
    'Info',
    'Lang',
    'MoonCode',
    'MoonText',
    'PhenomCondition',
    'PrecipitationType',
    'Request',
    'RequestForecast',
    'Response',
    'ResponseForecast',
    'Season',
    'TzInfo',
    'WindDir',
    'YaWeather',
    'YaWeatherAsync',
    'YaWeatherBase',
    'YaWeatherAPIError',
    'cities',

    # Countries
    'Afghanistan',
    'Albania',
    'Algeria',
    'AmericanSamoa',
    'Andorra',
    'Angola',
    'AntiguaAndBarbuda',
    'Argentina',
    'Armenia',
    'Aruba',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'BosniaAndHerzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'BurkinaFaso',
    'Burma',
    'Burundi',
    'CaboVerde',
    'Cambodia',
    'Cameroon',
    'Canada',
    'CentralAfricanRepublic',
    'Chad',
    'Chile',
    'China',
    'Colombia',
    'Comoros',
    'CongoBrazzaville',
    'CongoKinshasa',
    'CostaRica',
    'CoteDIvoire',
    'Croatia',
    'Cuba',
    'Curacao',
    'Cyprus',
    'Czechia',
    'Denmark',
    'Djibouti',
    'Dominica',
    'DominicanRepublic',
    'Ecuador',
    'Egypt',
    'ElSalvador',
    'EquatorialGuinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guam',
    'Guatemala',
    'Guinea',
    'GuineaBissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'HongKong',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'KoreaNorth',
    'KoreaSouth',
    'Kosovo',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macau',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'MarshallIslands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Montenegro',
    'Morocco',
    'Mozambique',
    'Namibia',
    'Nepal',
    'Netherlands',
    'NewZealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'NorthernMarianaIslands',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'PapuaNewGuinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'SaintKittsAndNevis',
    'SaintLucia',
    'SaintVincentAndTheGrenadines',
    'Samoa',
    'SanMarino',
    'SaoTomeAndPrincipe',
    'SaudiArabia',
    'Senegal',
    'Serbia',
    'Seychelles',
    'SierraLeone',
    'Singapore',
    'SintMaarten',
    'Slovakia',
    'Slovenia',
    'SolomonIslands',
    'Somalia',
    'SouthAfrica',
    'SouthSudan',
    'Spain',
    'SriLanka',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'TimorLeste',
    'Togo',
    'Tonga',
    'TrinidadAndTobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'UnitedArabEmirates',
    'UnitedKingdom',
    'UnitedStates',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Venezuela',
    'Vietnam',
    'WestBank',
    'Yemen',
    'Zambia',
    'Zimbabwe',
)