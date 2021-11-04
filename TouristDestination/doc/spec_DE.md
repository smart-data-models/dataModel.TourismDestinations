Entität: TouristDestination  
===========================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.TourismDestinations/blob/master/TouristDestination/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Ein touristisches Ziel. Im Prinzip kann jeder Ort ein Reiseziel sein, von einer Stadt, einer Region oder einem Land bis hin zu einem Vergnügungspark oder einem Hotel.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `includesAttraction`:   - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name`: Der Name dieses Artikels.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type`: Es muss TouristDestination sein    
Erforderliche Eigenschaften  
- `id`  - `type`    
Dieses Datenmodell basiert auf dem Standard UNE178503. Es ist auch mit schema.org kompatibel. Einige der Elemente von schema.org wurden in dieser Datei angepasst https://smart-data-models.github.io/data-models/schema-org.json  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
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
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
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
      x-ngsi:    
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
      type: array    
      x-ngsi:    
        model: ""    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *touristdestination_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'It has to be TouristDestination'    
      enum:    
        - TouristDestination    
      type: string    
      x-ngsi:    
        model: https://schema.org/TouristDestination    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### TouristDestination NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für ein TouristDestination im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
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
#### TouristDestination NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein TouristDestination im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
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
#### TouristDestination NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für ein TouristDestination im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
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
#### TouristDestination NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein TouristDestination im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
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
