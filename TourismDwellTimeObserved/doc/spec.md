[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png)](https://smartdatamodels.org)
Entity: TourismDwellTimeObserved
================================
<!-- 10-Header -->

[Open License](https://github.com/smart-data-models/dataModel.TourismDestinations/blob/master/TourismDwellTimeObserved/LICENSE.md)
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)
Global description: **Hourly observation of visitor dwell time (permanence duration) at a specific location (municipality), segmented by nationality and dwell time range.**
version: 0.0.1

<!-- 15-License -->

<!-- 20-Description -->

<!-- 30-PropertiesList -->

## List of properties

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)
  - `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)
  - `addressLocality[string]`: The locality in which the street address is, and which is in the region  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)
  - `addressRegion[string]`: The region in which the locality is, and which is in the country  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)
  - `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government
  - `postOfficeBoxNumber[string]`: The post office box number for PO box addresses. For example, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)
  - `postalCode[string]`: The postal code. For example, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)
  - `streetAddress[string]`: The street address  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)
  - `streetNr[string]`: Number identifying a specific property on a public street
- `aggregationType[string]`: Type of aggregation used for this hourly observation  . Model: [https://schema.org/Text](https://schema.org/Text)
- `alternateName[string]`: An alternative name for this item
- `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)
- `dataProvider[string]`: Provider of the data  . Model: [https://schema.org/Text](https://schema.org/Text)
- `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform
- `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform
- `dateObserved[date-time]`: Date and time of the observation (ISO8601 UTC)  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)
- `description[string]`: A description of this item
- `dwellTimeRange[string]`: Dwell time range in minutes (e.g. 0-5, 5-15, 30-60, 120+)  . Model: [https://schema.org/Text](https://schema.org/Text)
- `hour[number]`: Hour of the day (0-23) for this observation  . Model: [https://schema.org/Number](https://schema.org/Number)
- `id[*]`: Unique identifier of the entity
- `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon
- `locationCode[string]`: Official code of the location/municipality (e.g. DICOFRE)  . Model: [https://schema.org/Text](https://schema.org/Text)
- `locationName[string]`: Name of the location/municipality  . Model: [https://schema.org/Text](https://schema.org/Text)
- `name[string]`: The name of this item
- `nationality[string]`: Nationality of visitors. ISO 3166-1 alpha-2 country code  . Model: [https://schema.org/Text](https://schema.org/Text)
- `nationalityName[string]`: Full name of the nationality country (optional)  . Model: [https://schema.org/Text](https://schema.org/Text)
- `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)
- `seeAlso[*]`: list of uri pointing to additional resources about the item
- `source[string]`: Original source of the data as a URL  . Model: [https://schema.org/Text](https://schema.org/Text)
- `totalVisitors[number]`: Total number of visitors across all dwell time ranges for this hour  . Model: [https://schema.org/Number](https://schema.org/Number)
- `type[string]`: NGSI entity type. It has to be TourismDwellTimeObserved
- `visitorCount[number]`: Number of visitors in this dwell time range  . Model: [https://schema.org/Number](https://schema.org/Number)

<!-- 35-RequiredProperties -->

## Required properties

- `id`
- `type`
- `dateObserved`
- `location`
- `locationCode`
- `nationality`
- `dwellTimeRange`
- `visitorCount`
- `hour`

<!-- 40-DataModel -->

## Data Model description of properties

```json
{
  "TourismDwellTimeObserved": {
    "description": "Hourly observation of visitor dwell time (permanence duration) at a specific location (municipality), segmented by nationality and dwell time range.",
    "x-version": "0.0.1",
    "properties": {
      "address": {
        "description": "The mailing address",
        "properties": {
          "addressCountry": {
            "description": "The country. For example, Spain",
            "type": "string",
            "x-ngsi": {
              "model": "https://schema.org/addressCountry",
              "type": "Property"
            }
          },
          "addressLocality": {
            "description": "The locality in which the street address is, and which is in the region",
            "type": "string",
            "x-ngsi": {
              "model": "https://schema.org/addressLocality",
              "type": "Property"
            }
          },
          "addressRegion": {
            "description": "The region in which the locality is, and which is in the country",
            "type": "string",
            "x-ngsi": {
              "model": "https://schema.org/addressRegion",
              "type": "Property"
            }
          },
          "district": {
            "description": "A district is a type of administrative division that, in some countries, is managed by the local government",
            "type": "string",
            "x-ngsi": {
              "type": "Property"
            }
          },
          "postOfficeBoxNumber": {
            "description": "The post office box number for PO box addresses. For example, 03578",
            "type": "string",
            "x-ngsi": {
              "model": "https://schema.org/postOfficeBoxNumber",
              "type": "Property"
            }
          },
          "postalCode": {
            "description": "The postal code. For example, 24004",
            "type": "string",
            "x-ngsi": {
              "model": "https://schema.org/https://schema.org/postalCode",
              "type": "Property"
            }
          },
          "streetAddress": {
            "description": "The street address",
            "type": "string",
            "x-ngsi": {
              "model": "https://schema.org/streetAddress",
              "type": "Property"
            }
          },
          "streetNr": {
            "description": "Number identifying a specific property on a public street",
            "type": "string",
            "x-ngsi": {
              "type": "Property"
            }
          }
        },
        "type": "object",
        "x-ngsi": {
          "model": "https://schema.org/address",
          "type": "Property"
        }
      },
      "aggregationType": {
        "description": "Type of aggregation used for this hourly observation",
        "enum": [
          "hourly_sum",
          "hourly_average",
          "hourly_snapshot",
          "hourly_estimate"
        ],
        "type": "string",
        "x-ngsi": {
          "model": "https://schema.org/Text",
          "type": "Property"
        }
      },
      "alternateName": {
        "description": "An alternative name for this item",
        "type": "string",
        "x-ngsi": {
          "type": "Property"
        }
      },
      "areaServed": {
        "description": "The geographic area where a service or offered item is provided",
        "type": "string",
        "x-ngsi": {
          "model": "https://schema.org/Text",
          "type": "Property"
        }
      },
      "dataProvider": {
        "description": "Provider of the data",
        "type": "string",
        "x-ngsi": {
          "model": "https://schema.org/Text",
          "type": "Property"
        }
      },
      "dateCreated": {
        "description": "Entity creation timestamp. This will usually be allocated by the storage platform",
        "format": "date-time",
        "type": "string",
        "x-ngsi": {
          "type": "Property"
        }
      },
      "dateModified": {
        "description": "Timestamp of the last modification of the entity. This will usually be allocated by the storage platform",
        "format": "date-time",
        "type": "string",
        "x-ngsi": {
          "type": "Property"
        }
      },
      "dateObserved": {
        "description": "Date and time of the observation (ISO8601 UTC)",
        "format": "date-time",
        "type": "string",
        "x-ngsi": {
          "model": "https://schema.org/DateTime",
          "type": "Property"
        }
      },
      "description": {
        "description": "A description of this item",
        "type": "string",
        "x-ngsi": {
          "type": "Property"
        }
      },
      "dwellTimeRange": {
        "description": "Dwell time range in minutes (e.g. 0-5, 5-15, 30-60, 120+)",
        "type": "string",
        "x-ngsi": {
          "model": "https://schema.org/Text",
          "type": "Property"
        }
      },
      "hour": {
        "description": "Hour of the day (0-23) for this observation",
        "maximum": 23,
        "minimum": 0,
        "type": "number",
        "x-ngsi": {
          "model": "https://schema.org/Number",
          "type": "Property"
        }
      },
      "id": {
        "anyOf": [
          {
            "description": "Identifier format of any NGSI entity",
            "maxLength": 256,
            "minLength": 1,
            "pattern": "^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$",
            "type": "string",
            "x-ngsi": {
              "type": "Property"
            }
          },
          {
            "description": "Identifier format of any NGSI entity",
            "format": "uri",
            "type": "string",
            "x-ngsi": {
              "type": "Property"
            }
          }
        ],
        "description": "Unique identifier of the entity",
        "x-ngsi": {
          "type": "Relationship"
        }
      },
      "location": {
        "description": "Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon",
        "oneOf": [
          {
            "description": "Geojson reference to the item. Point",
            "properties": {
              "bbox": {
                "description": "BBox of the  Point",
                "items": {
                  "type": "number"
                },
                "minItems": 4,
                "type": "array",
                "x-ngsi": {
                  "type": "Property"
                }
              },
              "coordinates": {
                "description": "Coordinates of the Point",
                "items": {
                  "type": "number"
                },
                "minItems": 2,
                "type": "array",
                "x-ngsi": {
                  "type": "Property"
                }
              },
              "type": {
                "enum": [
                  "Point"
                ],
                "type": "string"
              }
            },
            "required": [
              "type",
              "coordinates"
            ],
            "title": "GeoJSON Point",
            "type": "object",
            "x-ngsi": {
              "type": "GeoProperty"
            }
          },
          {
            "description": "Geojson reference to the item. LineString",
            "properties": {
              "bbox": {
                "description": "BBox coordinates of the LineString",
                "items": {
                  "type": "number"
                },
                "minItems": 4,
                "type": "array",
                "x-ngsi": {
                  "type": "Property"
                }
              },
              "coordinates": {
                "description": "Coordinates of the LineString",
                "items": {
                  "items": {
                    "type": "number"
                  },
                  "minItems": 2,
                  "type": "array"
                },
                "minItems": 2,
                "type": "array",
                "x-ngsi": {
                  "type": "Property"
                }
              },
              "type": {
                "enum": [
                  "LineString"
                ],
                "type": "string"
              }
            },
            "required": [
              "type",
              "coordinates"
            ],
            "title": "GeoJSON LineString",
            "type": "object",
            "x-ngsi": {
              "type": "GeoProperty"
            }
          },
          {
            "description": "Geojson reference to the item. Polygon",
            "properties": {
              "bbox": {
                "description": "BBox coordinates of the Polygon",
                "items": {
                  "type": "number"
                },
                "minItems": 4,
                "type": "array",
                "x-ngsi": {
                  "type": "Property"
                }
              },
              "coordinates": {
                "description": "Coordinates of the Polygon",
                "items": {
                  "items": {
                    "items": {
                      "type": "number"
                    },
                    "minItems": 2,
                    "type": "array"
                  },
                  "minItems": 4,
                  "type": "array"
                },
                "type": "array",
                "x-ngsi": {
                  "type": "Property"
                }
              },
              "type": {
                "enum": [
                  "Polygon"
                ],
                "type": "string"
              }
            },
            "required": [
              "type",
              "coordinates"
            ],
            "title": "GeoJSON Polygon",
            "type": "object",
            "x-ngsi": {
              "type": "GeoProperty"
            }
          },
          {
            "description": "Geojson reference to the item. MultiPoint",
            "properties": {
              "bbox": {
                "description": "BBox coordinates of the LineString",
                "items": {
                  "type": "number"
                },
                "minItems": 4,
                "type": "array",
                "x-ngsi": {
                  "type": "Property"
                }
              },
              "coordinates": {
                "description": "Coordinates of the MulitPoint",
                "items": {
                  "items": {
                    "type": "number"
                  },
                  "minItems": 2,
                  "type": "array"
                },
                "type": "array",
                "x-ngsi": {
                  "type": "Property"
                }
              },
              "type": {
                "enum": [
                  "MultiPoint"
                ],
                "type": "string"
              }
            },
            "required": [
              "type",
              "coordinates"
            ],
            "title": "GeoJSON MultiPoint",
            "type": "object",
            "x-ngsi": {
              "type": "GeoProperty"
            }
          },
          {
            "description": "Geojson reference to the item. MultiLineString",
            "properties": {
              "bbox": {
                "description": "BBox coordinates of the LineString",
                "items": {
                  "type": "number"
                },
                "minItems": 4,
                "type": "array",
                "x-ngsi": {
                  "type": "Property"
                }
              },
              "coordinates": {
                "description": "Coordinates of the MultiLineString",
                "items": {
                  "items": {
                    "items": {
                      "type": "number"
                    },
                    "minItems": 2,
                    "type": "array"
                  },
                  "minItems": 2,
                  "type": "array"
                },
                "type": "array",
                "x-ngsi": {
                  "type": "Property"
                }
              },
              "type": {
                "enum": [
                  "MultiLineString"
                ],
                "type": "string"
              }
            },
            "required": [
              "type",
              "coordinates"
            ],
            "title": "GeoJSON MultiLineString",
            "type": "object",
            "x-ngsi": {
              "type": "GeoProperty"
            }
          },
          {
            "description": "Geojson reference to the item. MultiLineString",
            "properties": {
              "bbox": {
                "items": {
                  "type": "number"
                },
                "minItems": 4,
                "type": "array"
              },
              "coordinates": {
                "description": "Coordinates of the MultiPolygon",
                "items": {
                  "items": {
                    "items": {
                      "items": {
                        "type": "number"
                      },
                      "minItems": 2,
                      "type": "array"
                    },
                    "minItems": 4,
                    "type": "array"
                  },
                  "type": "array"
                },
                "type": "array",
                "x-ngsi": {
                  "type": "Property"
                }
              },
              "type": {
                "enum": [
                  "MultiPolygon"
                ],
                "type": "string"
              }
            },
            "required": [
              "type",
              "coordinates"
            ],
            "title": "GeoJSON MultiPolygon",
            "type": "object",
            "x-ngsi": {
              "type": "GeoProperty"
            }
          }
        ],
        "x-ngsi": {
          "type": "GeoProperty"
        }
      },
      "locationCode": {
        "description": "Official code of the location/municipality (e.g. DICOFRE)",
        "type": "string",
        "x-ngsi": {
          "model": "https://schema.org/Text",
          "type": "Property"
        }
      },
      "locationName": {
        "description": "Name of the location/municipality",
        "type": "string",
        "x-ngsi": {
          "model": "https://schema.org/Text",
          "type": "Property"
        }
      },
      "name": {
        "description": "The name of this item",
        "type": "string",
        "x-ngsi": {
          "type": "Property"
        }
      },
      "nationality": {
        "description": "Nationality of visitors. ISO 3166-1 alpha-2 country code",
        "pattern": "^[A-Z]{2}$",
        "type": "string",
        "x-ngsi": {
          "model": "https://schema.org/Text",
          "type": "Property"
        }
      },
      "nationalityName": {
        "description": "Full name of the nationality country (optional)",
        "type": "string",
        "x-ngsi": {
          "model": "https://schema.org/Text",
          "type": "Property"
        }
      },
      "owner": {
        "description": "A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)",
        "items": {
          "anyOf": [
            {
              "description": "Identifier format of any NGSI entity",
              "maxLength": 256,
              "minLength": 1,
              "pattern": "^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$",
              "type": "string",
              "x-ngsi": {
                "type": "Property"
              }
            },
            {
              "description": "Identifier format of any NGSI entity",
              "format": "uri",
              "type": "string",
              "x-ngsi": {
                "type": "Property"
              }
            }
          ],
          "description": "Unique identifier of the entity",
          "x-ngsi": {
            "type": "Relationship"
          }
        },
        "type": "array",
        "x-ngsi": {
          "type": "Property"
        }
      },
      "seeAlso": {
        "description": "list of uri pointing to additional resources about the item",
        "oneOf": [
          {
            "items": {
              "format": "uri",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          {
            "format": "uri",
            "type": "string"
          }
        ],
        "x-ngsi": {
          "type": "Property"
        }
      },
      "source": {
        "description": "Original source of the data as a URL",
        "type": "string",
        "x-ngsi": {
          "model": "https://schema.org/Text",
          "type": "Property"
        }
      },
      "totalVisitors": {
        "description": "Total number of visitors across all dwell time ranges for this hour",
        "minimum": 0,
        "type": "number",
        "x-ngsi": {
          "model": "https://schema.org/Number",
          "type": "Property",
          "units": "persons"
        }
      },
      "type": {
        "description": "NGSI entity type. It has to be TourismDwellTimeObserved",
        "enum": [
          "TourismDwellTimeObserved"
        ],
        "type": "string",
        "x-ngsi": {
          "type": "Property"
        }
      },
      "visitorCount": {
        "description": "Number of visitors in this dwell time range",
        "minimum": 0,
        "type": "number",
        "x-ngsi": {
          "model": "https://schema.org/Number",
          "type": "Property",
          "units": "persons"
        }
      }
    },
    "required": [
      "id",
      "type",
      "dateObserved",
      "location",
      "locationCode",
      "nationality",
      "dwellTimeRange",
      "visitorCount",
      "hour"
    ]
  }
}
```

<!-- 50-Examples -->

## Examples

### JSON Example
```json
{}
```

### LD Example
```json
{}
```

<!-- 90-Footer -->

## See also

* [original specification](https://github.com/smart-data-models/dataModel.Transportation/blob/master/{data_model}/notes.yaml) (temporary link)