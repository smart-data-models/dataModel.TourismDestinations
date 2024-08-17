from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class AgeRange(BaseModel):
    range: Optional[str] = Field(
        None,
        description='Value of ageRange. It uses the ranges defined by sortingOrder',
    )
    sortingOrder: Optional[List[str]] = Field(
        None,
        description="Ordered set of different age groups for ageRange. OrderedSet: '0-1, 2-5, 6-11, 12-17, 18-24, 25-29, 30-34, 35-39, 40-44, 45-49, 50-54, 55-59, 60-64, 65+'",
    )


class AvgDailyAccommodationAndBoardExpenditure(BaseModel):
    range: Optional[str] = Field(
        None,
        description='Value of avgDailyAccommodationAndBoardExpenditure. It uses the ranges defined by sortingOrder',
    )
    sortingOrder: Optional[List[str]] = Field(
        None,
        description="Ordered set of range of money amounts for avgDailyAccommodationAndBoardExpenditure. OrderedSet: '0 to 24 €, 25 to 49 €, 50 to 74 €, 75 to 99 €, 100 to 149 €, 150 to 199 €, 200 to 249 €, 250 to 299 €, 300 to 399 €, 400 to 499 €, 500 to 599 €, 600+ €'",
    )


class AvgDailyExpenditure(BaseModel):
    range: Optional[str] = Field(
        None,
        description='Value of avgDailyExpenditure. It uses the ranges defined by sortingOrder',
    )
    sortingOrder: Optional[List[str]] = Field(
        None,
        description="Ordered set of range of money amounts for avgDailyExpenditure. OrderedSet: '0 to 24 €, 25 to 49 €, 50 to 74 €, 75 to 99 €, 100 to 149 €, 150 to 199 €, 200 to 249 €, 250 to 299 €, 300 to 399 €, 400 to 499 €, 500 to 599 €, 600+ €'",
    )


class AvgDailyExtraExpenditure(BaseModel):
    range: Optional[str] = Field(
        None,
        description='Value of avgDailyExtraExpenditure. It uses the ranges defined by sortingOrder',
    )
    sortingOrder: Optional[List[str]] = Field(
        None,
        description="Ordered set of range of money amounts for avgDailyExtraExpenditure. OrderedSet: '0 to 24 €, 25 to 49 €, 50 to 74 €, 75 to 99 €, 100 to 149 €, 150 to 199 €, 200 to 249 €, 250 to 299 €, 300 to 399 €, 400 to 499 €, 500 to 599 €, 600+ €'",
    )


class Board(Enum):
    RO = 'RO'
    BB = 'BB'
    HB = 'HB'
    FB = 'FB'
    AI = 'AI'


class Gender(Enum):
    Female = 'Female'
    Male = 'Male'


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class LodgingCategory(Enum):
    field_1 = 1
    field_1_Superior = '1 Superior'
    field_2 = 2
    field_2_Superior = '2 Superior'
    field_3 = 3
    field_3_Superior = '3 Superior'
    field_4 = 4
    field_4_Superior = '4 Superior'
    field_5 = 5
    field_5_Superior = '5 Superior'


class LodgingSize(BaseModel):
    range: Optional[str] = Field(
        None,
        description='Value of lodgingSize. It uses the ranges defined by sortingOrder',
    )
    sortingOrder: Optional[List[str]] = Field(
        None,
        description="Ordered set of intervals of the quantity of rooms for lodgingSize. OrderedSet: '0 - 24 very small, 25 - 100 small, 101 - 300 medium, 301 - 700 large, 701 - 1200 very large, 1201+ massive'",
    )


class LodgingType(Enum):
    Hotel = 'Hotel'
    Resort = 'Resort'
    Hostel = 'Hostel'
    Motel = 'Motel'
    B_B = 'B&B'
    Aparthotel = 'Aparthotel'
    Lodge = 'Lodge'


class ReservationLeadTime(BaseModel):
    range: Optional[str] = Field(
        None,
        description='Value of reservationLeadTime. It uses the ranges defined by sortingOrder',
    )
    sortingOrder: Optional[List[str]] = Field(
        None,
        description="Ordered set of range of days for reservationLeadTime. OrderedSet: '1 to 7 days, 8 to 14 days, 15 to 30 days, 31 to 60 days, 61 to 90 days, 91 to 120 days, 121 to 240 days, 241 to 365 days, 366+ days'",
    )


class RoomOfStayType(Enum):
    Apartment = 'Apartment'
    Bungalow = 'Bungalow'
    Studio = 'Studio'
    Single = 'Single'
    Double = 'Double'
    Family = 'Family'
    Junior_Suite = 'Junior Suite'
    Senior_Executive_Suite = 'Senior/Executive Suite'
    Royal_Presidential_Suite = 'Royal/Presidential Suite'


class StayLength(BaseModel):
    range: Optional[str] = Field(
        None,
        description='Value of stayLength. It uses the ranges defined by sortingOrder',
    )
    sortingOrder: Optional[List[str]] = Field(
        None,
        description="Ordered set of range of nights for stayLength. OrderedSet: '1 night, 2 to 4 nights, 5 to 7 nights, 8 to 14 nights, 15 to 21 nights, 22+ nights'",
    )


class TotalAccommodationAndBoardExpenditure(BaseModel):
    range: Optional[str] = Field(
        None,
        description='Value of totalAccommodationAndBoardExpenditure. It uses the ranges defined by sortingOrder',
    )
    sortingOrder: Optional[List[str]] = Field(
        None,
        description="Ordered set of range of money amounts for totalAccommodationAndBoardExpenditure. OrderedSet: '0 to 249 €, 250 to 499 €, 500 to 749 €, 750 to 999 €, 1000 to 1499 €, 1500 to 1999 €, 2000 to 2999 €, 3000 to 3999 €, 4000 to 4999 €, 5000+ €'",
    )


class TotalExpenditure(BaseModel):
    range: Optional[str] = Field(
        None,
        description='Value of totalExpenditure. It uses the ranges defined by sortingOrder',
    )
    sortingOrder: Optional[List[str]] = Field(
        None,
        description="Ordered set of range of money amounts for totalExpenditure. OrderedSet: '0 to 249 €, 250 to 499 €, 500 to 749 €, 750 to 999 €, 1000 to 1499 €, 1500 to 1999 €, 2000 to 2999 €, 3000 to 3999 €, 4000 to 4999 €, 5000+ €'",
    )


class TotalExtraExpenditure(BaseModel):
    range: Optional[str] = Field(
        None,
        description='Value of totalExtraExpenditure. It uses the ranges defined by sortingOrder',
    )
    sortingOrder: Optional[List[str]] = Field(
        None,
        description="Ordered set of range of money amounts for totalExtraExpenditure. OrderedSet: '0 to 249 €, 250 to 499 €, 500 to 749 €, 750 to 999 €, 1000 to 1499 €, 1500 to 1999 €, 2000 to 2999 €, 3000 to 3999 €, 4000 to 4999 €, 5000+ €'",
    )


class TravelPartyComposition(Enum):
    Single = 'Single'
    Single_parent = 'Single parent'
    Family = 'Family'
    Couple = 'Couple'
    Friends_Relatives = 'Friends/Relatives'


class Type6(Enum):
    TouristProfile = 'TouristProfile'


class TouristProfile(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    ageRange: Optional[AgeRange] = Field(
        None, description='Age range of the person profiled'
    )
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    avgDailyAccommodationAndBoardExpenditure: Optional[
        AvgDailyAccommodationAndBoardExpenditure
    ] = Field(
        None,
        description='Range of avg daily amount of money invoiced by the lodging establishment in accommodation and board concepts',
    )
    avgDailyExpenditure: Optional[AvgDailyExpenditure] = Field(
        None,
        description='Range of avg daily amount of money invoiced by the lodging establishment',
    )
    avgDailyExtraExpenditure: Optional[AvgDailyExtraExpenditure] = Field(
        None,
        description='Range of avg daily amount of money invoiced by the lodging establishment in extra concepts',
    )
    board: Optional[Board] = Field(
        None, description="Usual type of board type reserved. Enum:'RO, BB, HB, FB, AI'"
    )
    bookingChannel: Optional[str] = Field(
        None, description='Channel used by the tourist for the reservation'
    )
    country: Optional[str] = Field(
        None,
        description='Country of nationality - https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2',
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    gender: Optional[Gender] = Field(
        None, description="Gender of the person profiled. Enum:'Female, Male'"
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    lodgingCategory: Optional[LodgingCategory] = Field(
        None,
        description="Usual category of the lodging. Enum:'1, 1 Superior, 2, 2 Superior, 3, 3 Superior, 4, 4 Superior, 5, 5 Superior'",
    )
    lodgingSize: Optional[LodgingSize] = Field(
        None, description='Range size in number of rooms of the lodging'
    )
    lodgingType: Optional[LodgingType] = Field(
        None,
        description="Usual type of lodging for the stay. Could reference UNE178506 in the future. Enum:'Hotel, Resort, Hostel, Motel, B&B, Aparthotel, Lodge'",
    )
    name: Optional[str] = Field(None, description='The name of this item')
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    reservationLeadTime: Optional[ReservationLeadTime] = Field(
        None, description='Range of days between booking and check-in'
    )
    roomOfStayType: Optional[RoomOfStayType] = Field(
        None,
        description="Usual type of the accommodation room reserved. Enum:'Apartment, Bungalow, Studio, Single, Double, Family, Junior Suite, Senior/Executive Suite, Royal/Presidential Suite'",
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    stayLength: Optional[StayLength] = Field(
        None, description='Range of number of staying nights'
    )
    totalAccommodationAndBoardExpenditure: Optional[
        TotalAccommodationAndBoardExpenditure
    ] = Field(
        None,
        description='Range of total amount of money invoiced by the lodging establishment in accommodation and board concepts',
    )
    totalExpenditure: Optional[TotalExpenditure] = Field(
        None,
        description='Range of total amount of money invoiced by the lodging establishment',
    )
    totalExtraExpenditure: Optional[TotalExtraExpenditure] = Field(
        None,
        description='Range of total amount of money invoiced by the lodging establishment in extra concepts',
    )
    travelPartyComposition: Optional[TravelPartyComposition] = Field(
        None,
        description="Composition of the travelling party based on the number of adults and children. Enum:'Single, Single parent, Family, Couple, Friends/Relatives'",
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be TouristProfile'
    )
