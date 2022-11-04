<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティTouristDestination  
========================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.TourismDestinations/blob/master/TouristDestination/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな説明。**観光地（tourist destination）。原則的に、都市、地域、国から遊園地やホテルまで、どんな場所でも観光地になりえます。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `id[*]`: エンティティの一意な識別子  - `includesAttraction[array]`:   . Model: []()- `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `name[string]`: このアイテムの名称です。  - `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type[string]`: TouristDestinationである必要があります。  . Model: [https://schema.org/TouristDestination](https://schema.org/TouristDestination)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
このデータモデルは、UNE178503規格に準拠しています。また、schema.orgと互換性がある。このファイルでは、schema.org の要素の一部が適応されています。https://smart-data-models.github.io/data-models/schema-org.json  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        type: GeoProperty    
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
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.TourismDestinations/blob/master/TouristDestination/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.TourismDestinations/TouristDestination/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### TouristDestination NGSI-v2 key-value の例。  
ここでは、TouristDestinationをJSON-LD形式でkey-valuesにした例を示す。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータが返される。  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### TouristDestination NGSI-v2 正規化例  
以下は、TouristDestinationをJSON-LD形式で正規化した例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### TouristDestination NGSI-LD key-value Example  
ここでは、TouristDestinationをJSON-LD形式でkey-valuesとした例を示す。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "ngsi:uri:TouristDestination:1",  
    "type": "TouristDestination",  
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
    "name": "Sitios Patrimonio de la Humanidad in Spain",  
    "@context": [  
        "https://smart-data-models.github.io/data-models/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.TourismDestinations/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### TouristDestination NGSI-LD 正規化例  
以下は、TouristDestinationをJSON-LD形式で正規化した例である。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
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
    "name": {  
        "type": "string",  
        "value": "Sitios Patrimonio de la Humanidad os spain"  
    },  
    "@context": [  
        "https://smart-data-models.github.io/data-models/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.TourismDestinations/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
