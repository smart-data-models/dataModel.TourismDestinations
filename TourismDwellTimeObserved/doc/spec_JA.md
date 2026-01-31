<!-- 10-Header -->
  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

実体: TourismDwellTimeObserved  
================================
<!-- /10-Header -->
  
<!-- 15-License -->
  

[オープンライセンス](https://github.com/smart-data-models//dataModel.TourismDestinations/blob/master/TourismDwellTimeObserved/LICENSE.md)  

[自動生成された文書](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->
  
<!-- 20-Description -->
  

Global description: **特定の場所（市町村）における来場者滞在時間（滞在期間）の毎時観測、国籍と滞在時間範囲別にセグメント化。**  

version: 0.0.1  
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->
  


## プロパティの一覧  


<sup><sub>[*] 属性に型がないのは、それが複数の型や異なる形式/パターンを持つ可能性があるためです。</sub></sup>  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)  
	- `addressCountry[string]`: その国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 住所が存在する地域、そしてその地域が属する地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: その地域は、自治体が存在し、かつその国に位置する地域です。  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区は、行政区分の一種であり、いくつかの国では、地方自治体によって管理される。  
	- `postOfficeBoxNumber[string]`: ポストオフィスボックス番号は、ポストオフィスボックスアドレスの場合。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 郵便番号。例えば、24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 住所  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 公道上の特定の物件を識別する番号  
- `aggregationType[string]`: この時間観測に使用される集約の種類  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `alternateName[string]`: このアイテムの別名  
- `areaServed[string]`: サービスまたは提供されるアイテムが提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `dataProvider[string]`: データの提供者  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `dateCreated[date-time]`: エンティティ作成タイムスタンプ。このタイムスタンプは、通常、ストレージプラットフォームによって割り当てられます。  
- `dateModified[date-time]`: エンティティの最後の変更のタイムスタンプ。このタイムスタンプは通常、ストレージプラットフォームによって割り当てられる。  
- `dateObserved[date-time]`: 観測の日時（ISO8601 UTC）  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)  
- `description[string]`: このアイテムの説明  
- `dwellTimeRange[string]`: 滞在時間範囲（分単位、例：0-5、5-15、30-60、120分以上）  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `hour[number]`: この観測の日の時間（0-23）  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `id[*]`: エンティティのユニーク識別子  
- `location[*]`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、またはMultiPolygonのいずれかになることができる。  
- `locationCode[string]`: 所在地・市町村の公式コード（例：DICOFRE）  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `locationName[string]`: 所在地/自治体の名前  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `name[string]`: このアイテムの名前  
- `nationality[string]`: 訪問者の国籍。ISO 3166-1 alpha-2 国コード  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `nationalityName[string]`: 国籍国のフルネーム（任意）  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `owner[array]`: 所有者のユニークIDを参照する文字シーケンスをJSONでエンコードしたリスト  
- `seeAlso[*]`: アイテムに関する追加のリソースを指すURIのリスト  
- `source[string]`: データの元の情報源としてのURL  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `totalVisitors[number]`: この時間帯の全ての滞在時間範囲を横断した訪問者総数  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `type[string]`: NGSIエンティティタイプ。TourismDwellTimeObservedでなければならない。  
- `visitorCount[number]`: この滞在時間帯の訪問者数  . Model: [https://schema.org/Number](https://schema.org/Number)  
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

必要なプロパティ  
- `観察日`  
- `dwellTimeRange`  
- `時間`  
- `ID`  
- `ロケーション`  
- `ロケーションコード`  
- `国籍`  
- `タイプ`  
`訪問者数`  
<!-- /35-RequiredProperties -->
  
<!-- 40-NotesYaml -->
  
<!-- /40-NotesYaml -->
  
<!-- 50-DataModelHeader -->
  

## データモデルのプロパティの説明  

アルファベット順に並べ替え（詳細）  
<!-- /50-DataModelHeader -->
  
<!-- 60-ModelYaml -->
  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
TourismDwellTimeObserved:    
  description: Hourly observation of visitor dwell time (permanence duration) at a specific location (municipality), segmented by nationality and dwell time range.    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: The country. For example, Spain    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: The locality in which the street address is, and which is in the region    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: The region in which the locality is, and which is in the country    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: A district is a type of administrative division that, in some countries, is managed by the local government    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: The post office box number for PO box addresses. For example, 03578    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: The postal code. For example, 24004    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    aggregationType:    
      description: Type of aggregation used for this hourly observation    
      enum:    
        - hourly_sum    
        - hourly_average    
        - hourly_snapshot    
        - hourly_estimate    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: Provider of the data    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObserved:    
      description: Date and time of the observation (ISO8601 UTC)    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    dwellTimeRange:    
      description: Dwell time range in minutes (e.g. 0-5, 5-15, 30-60, 120+)    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    hour:    
      description: Hour of the day (0-23) for this observation    
      maximum: 23    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Relationship    
    location:    
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              description: BBox of the  Point    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Point    
              items:    
                type: number    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the LineString    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
          properties:    
            bbox:    
              description: BBox coordinates of the Polygon    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Polygon    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MulitPoint    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MultiLineString    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              description: Coordinates of the MultiPolygon    
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
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    locationCode:    
      description: Official code of the location/municipality (e.g. DICOFRE)    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    locationName:    
      description: Name of the location/municipality    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    nationality:    
      description: Nationality of visitors. ISO 3166-1 alpha-2 country code    
      pattern: ^[A-Z]{2}$    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    nationalityName:    
      description: Full name of the nationality country (optional)    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Relationship    
      type: array    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
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
      description: Original source of the data as a URL    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    totalVisitors:    
      description: Total number of visitors across all dwell time ranges for this hour    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: persons    
    type:    
      description: NGSI entity type. It has to be TourismDwellTimeObserved    
      enum:    
        - TourismDwellTimeObserved    
      type: string    
      x-ngsi:    
        type: Property    
    visitorCount:    
      description: Number of visitors in this dwell time range    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: persons    
  required:    
    - id    
    - type    
    - dateObserved    
    - location    
    - locationCode    
    - nationality    
    - dwellTimeRange    
    - visitorCount    
    - hour    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.TourismDestinations/blob/master/TourismDwellTimeObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Tourism/TourismDwellTimeObserved/schema.json    
  x-model-tags: tourism,dwellTime,statistics    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->
  
<!-- 70-MiddleNotes -->
  
<!-- /70-MiddleNotes -->
  
<!-- 80-Examples -->
  

## 例のペイロード  

#### 観光滞在時間観測 NGSI-v2 キー値の例  

ここは、JSON形式のキー値としてのTourismDwellTimeObservedの例です。これは、`options=keyValues`を使用してNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:TourismDwellTimeObserved:PT:CO1313:DE:20241231T10:30:30-60",  
  "type": "TourismDwellTimeObserved",  
  "dateObserved": "2024-12-31T10:30:00Z",  
  "hour": 10,  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -8.76116,  
      41.37472  
    ]  
  },  
  "locationCode": "CO1313",  
  "locationName": "Póvoa de Varzim",  
  "nationality": "DE",  
  "nationalityName": "Germany",  
  "dwellTimeRange": "30-60",  
  "visitorCount": 15,  
  "aggregationType": "hourly_sum",  
  "dataProvider": "MEO",  
  "source": "MobilityDataPlatform"  
}  
```  
</details>  

#### 観光滞在時間観測 NGSI-v2 正規化例  

ここは、正規化されたJSON形式のTourismDwellTimeObservedの例です。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:TourismDwellTimeObserved:PT:CO1313:DE:20241231T10:30:30-60",  
  "type": "TourismDwellTimeObserved",  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2024-12-31T10:30:00Z"  
  },  
  "hour": {  
    "type": "Number",  
    "value": 10  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -8.7613,  
        41.3879  
      ]  
    }  
  },  
  "locationCode": {  
    "type": "Text",  
    "value": "CO1313"  
  },  
  "locationName": {  
    "type": "Text",  
    "value": "Póvoa de Varzim"  
  },  
  "nationality": {  
    "type": "Text",  
    "value": "DE"  
  },  
  "nationalityName": {  
    "type": "Text",  
    "value": "Germany"  
  },  
  "dwellTimeRange": {  
    "type": "Text",  
    "value": "30-60"  
  },  
  "visitorCount": {  
    "type": "Number",  
    "value": 15  
  },  
  "aggregationType": {  
    "type": "Text",  
    "value": "hourly_sum"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "MEO"  
  },  
  "source": {  
    "type": "Text",  
    "value": "https://api.meo.pt/tourism/v1/permanence_geo"  
  }  
}  
```  
</details>  

#### 観光滞在時間観測 NGSI-LD キー値の例  

ここはJSON-LD形式のkey-valuesとしてのTourismDwellTimeObservedの例です。これは、`options=keyValues`を使用してNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:TourismDwellTimeObserved:PT:CO1313:DE:20241231T10:30:30-60",  
  "type": "TourismDwellTimeObserved",  
  "dateObserved": "2024-12-31T10:30:00Z",  
  "hour": 10,  
  "location": {  
    "type": "Point",  
    "coordinates": [-8.7613, 41.3879]  
  },  
  "locationCode": "CO1313",  
  "locationName": "Póvoa de Varzim",  
  "nationality": "DE",  
  "nationalityName": "Germany",  
  "dwellTimeRange": "30-60",  
  "visitorCount": 15,  
  "aggregationType": "hourly_sum",  
  "dataProvider": "MEO",  
  "source": "https://api.meo.pt/tourism/v1/permanence_geo",  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  

#### 観光滞在時間観測 NGSI-LD 正規化例  

ここは、正規化されたJSON-LD形式のTourismDwellTimeObservedの例です。これは、オプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:TourismDwellTimeObserved:PT:CO1313:DE:20241231T10:30:30-60",  
  "type": "TourismDwellTimeObserved",  
  "dateObserved": {  
    "type": "Property",  
    "value": "2024-12-31T10:30:00Z"  
  },  
  "hour": {  
    "type": "Property",  
    "value": 10  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [-8.7613, 41.3879]  
    }  
  },  
  "locationCode": {  
    "type": "Property",  
    "value": "CO1313"  
  },  
  "locationName": {  
    "type": "Property",  
    "value": "Póvoa de Varzim"  
  },  
  "nationality": {  
    "type": "Property",  
    "value": "DE"  
  },  
  "nationalityName": {  
    "type": "Property",  
    "value": "Germany"  
  },  
  "dwellTimeRange": {  
    "type": "Property",  
    "value": "30-60"  
  },  
  "visitorCount": {  
    "type": "Property",  
    "value": 15  
  },  
  "aggregationType": {  
    "type": "Property",  
    "value": "hourly_sum"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "MEO"  
  },  
  "source": {  
    "type": "Property",  
    "value": "https://api.meo.pt/tourism/v1/permanence_geo"  
  }  
}  
```  
</details><!-- /80-Examples -->
  
<!-- 90-FooterNotes -->
  
<!-- /90-FooterNotes -->
  
<!-- 95-Units -->
  

See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->
  
<!-- 97-LastFooter -->
  
---  

[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->
  
