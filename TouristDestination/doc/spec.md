Entity: TouristDestination  
==========================







- `id`  



<details><summary><strong>full yaml details</strong></summary>    

TouristDestination:    
  description: 'A tourist destination. In principle any Place can be a TouristDestination from a City, Region or Country to an AmusementPark or Hotel.'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/areaServed'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    id:    
      anyOf: &touristdestination_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      type: Property    
    includesAttraction:    
      description: ""    
      items:    
        properties:    
          name:    
            type: string    
          type:    
            items:    
              enum:    
                - AmusementPark    
                - Apartment    
                - Aquarium    
                - ArtGallery    
                - AutoRental    
                - BarOrPub    
                - Beach    
                - BedAndBreakfast    
                - BodyOfWater    
                - Brewery    
                - BusinessEvent    
                - BusStation    
                - BusStop    
                - CafeOrCoffeeShop    
                - Campground    
                - Casino    
                - Cemetery    
                - City    
                - CivilBuilding    
                - CivicStructure    
                - Distillery    
                - Embassy    
                - EmergencyService    
                - Event    
                - EventVenue    
                - ExhibitionEvent    
                - Festival    
                - FinancialService    
                - FoodEstablishment    
                - FoodEvent    
                - funerario    
                - GasStation    
                - GolfCourse    
                - HealthAndBeautyBusiness    
                - Hostel    
                - Hotel    
                - House    
                - IceCreamShop    
                - Landform    
                - LandmarksOrHistoricalBuildings    
                - Library    
                - LodgingBusiness    
                - Mountain    
                - MovieTheater    
                - Museum    
                - MusicEvent    
                - MusicVenue    
                - NightClub    
                - Offer    
                - Organization    
                - Park    
                - ParkingFacility    
                - Person    
                - Place    
                - PlaceOfWorship    
                - Restaurant    
                - RVPark    
                - ShoppingCenter    
                - SkiResort    
                - SportsActivityLocation    
                - SportsEvent    
                - Store    
                - SubwayStation    
                - TaxiStand    
                - TouristAttraction    
                - TouristDestination    
                - TouristInformationCenter    
                - TouristTrip    
                - TrainStation    
                - TravelAgency    
                - Volcano    
                - Waterfall    
                - WorldHeritageSite    
                - Winery    
                - Zoo    
              type: string    
            type: array    
          url:    
            format: uri    
            type: string    
        type: object    
      type: Property    
      x-ngsi:    
        model: ""    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      title: 'GeoJSON Geometry'    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *touristdestination_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'It has to be TouristDestination'    
      enum:    
        - TouristDestination    
      type: Property    
      x-ngsi:    
        model: https://schema.org/TouristDestination    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    





  "id": "ngsi:uri:TouristDestination:1",  
  "type": "TouristDestination",  
  "name": "Sitios Patrimonio de la Humanidad in Spain",  
  "description": "Ejemplo tecnico de Destino Turistico, incluyendo el uso del atributo includesAttraction. Lista de sitios abreviada>",  
  "includesAttraction": [  
    {  
      "type": [  
        "TouristAttraction",  
        "WorldHeritageSite",  
        "CivilBuilding"  
      ],  
      "name": "Alhambra, Generalife y Albaicin de Granada",  
      "url": "https://www.spain.info/es/que-quieres/arte/monumentos/granada/la_alhambra.html"  
    },  
    {  
      "type": [  
        "TouristAttraction",  
        "WorldHeritageSite",  
        "PlaceOfWorship"  
      ],  
      "name": "Catedral de Burgos",  
      "url": "https://www.spain.info/es/que-quieres/arte/monumentos/burgos/catedral_de_burgos.html"  
    }  
  ]  
}  
```  




  "id": {  
    "type": "string",  
    "value": "ngsi:uri:TouristDestination:1"  
  },  
  "type": {  
    "type": "string",  
    "value": "TouristDestination"  
  },  
  "name": {  
    "type": "string",  
    "value": "Sitios Patrimonio de la Humanidad os spain"  
  },  
  "description": {  
    "type": "string",  
    "value": "Ejemplo tecnico de Destino Turistico, incluyendo el uso del atributo includesAttraction. Lista de sitios abreviada>"  
  },  
  "includesAttraction": {  
    "type": "array",  
    "value": [  
      {  
        "type": [  
          "TouristAttraction",  
          "WorldHeritageSite",  
          "CivilBuilding"  
        ],  
        "name": "Alhambra, Generalife y Albaicin de Granada",  
        "url": "https://www.spain.info/es/que-quieres/arte/monumentos/granada/la_alhambra.html"  
      },  
      {  
        "type": [  
          "TouristAttraction",  
          "WorldHeritageSite",  
          "PlaceOfWorship"  
        ],  
        "name": "Catedral de Burgos",  
        "url": "https://www.spain.info/es/que-quieres/arte/monumentos/burgos/catedral_de_burgos.html"  
      }  
    ]  
  }  
}  
```  




  "id": "ngsi:uri:TouristDestination:1",  
  "type": "TouristDestination",  
  "name": "Sitios Patrimonio de la Humanidad in Spain",  
  "description": "Ejemplo tecnico de Destino Turistico, incluyendo el uso del atributo includesAttraction. Lista de sitios abreviada>",  
  "includesAttraction": [  
    {  
      "type": [  
        "TouristAttraction",  
        "WorldHeritageSite",  
        "CivilBuilding"  
      ],  
      "name": "Alhambra, Generalife y Albaicin de Granada",  
      "url": "https://www.spain.info/es/que-quieres/arte/monumentos/granada/la_alhambra.html"  
    },  
    {  
      "type": [  
        "TouristAttraction",  
        "WorldHeritageSite",  
        "PlaceOfWorship"  
      ],  
      "name": "Catedral de Burgos",  
      "url": "https://www.spain.info/es/que-quieres/arte/monumentos/burgos/catedral_de_burgos.html"  
    }  
  ],  
  "@context": [  
    "https://smart-data-models.github.io/data-models/context.jsonld"  
  ]  
}  
```  




  "id": {  
    "type": "string",  
    "value": "ngsi:uri:TouristDestination:1"  
  },  
  "type": {  
    "type": "string",  
    "value": "TouristDestination"  
  },  
  "name": {  
    "type": "string",  
    "value": "Sitios Patrimonio de la Humanidad os spain"  
  },  
  "description": {  
    "type": "string",  
    "value": "Ejemplo tecnico de Destino Turistico, incluyendo el uso del atributo includesAttraction. Lista de sitios abreviada>"  
  },  
  "includesAttraction": {  
    "type": "array",  
    "value": [  
      {  
        "type": [  
          "TouristAttraction",  
          "WorldHeritageSite",  
          "CivilBuilding"  
        ],  
        "name": "Alhambra, Generalife y Albaicin de Granada",  
        "url": "https://www.spain.info/es/que-quieres/arte/monumentos/granada/la_alhambra.html"  
      },  
      {  
        "type": [  
          "TouristAttraction",  
          "WorldHeritageSite",  
          "PlaceOfWorship"  
        ],  
        "name": "Catedral de Burgos",  
        "url": "https://www.spain.info/es/que-quieres/arte/monumentos/burgos/catedral_de_burgos.html"  
      }  
    ]  
  },  
  "@context": [  
    "https://smart-data-models.github.io/data-models/context.jsonld"  
  ]  
}  
```  