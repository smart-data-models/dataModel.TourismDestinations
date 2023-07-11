<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ観光プロフィール  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.TourismDestinations/blob/master/TouristProfile/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**人、旅行、滞在の選択、目的地での消費などの特徴に基づく観光客のプロフィールの記述。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `ageRange[object]`: プロパティ。プロファイルされた人の年齢層。  - `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `avgDailyAccommodationAndBoardExpenditure[object]`: 物件。宿泊施設から請求される宿泊・食事コンセプトの1日平均金額の範囲。  - `avgDailyExpenditure[object]`: プロパティ宿泊施設が請求する1日の平均金額の範囲。  - `avgDailyExtraExpenditure[object]`: プロパティ宿泊施設が請求する追加概念の1日平均金額の範囲  - `board[string]`: プロパティ。通常のボードタイプの予約。列挙：「RO、BB、HB、FB、AI」。  - `bookingChannel[string]`: プロパティ。観光客が予約に使用するチャンネル。  - `country[string]`: 財産国籍 - https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2.  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `gender[string]`: プロパティ。プロファイル対象者の性別。Enum:'女性、男性'。  - `id[*]`: エンティティの一意識別子  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `lodgingCategory[string]`: 物件。宿泊施設の通常のカテゴリー。Enum:'1, 1 Superior, 2, 2 Superior, 3, 3 Superior, 4, 4 Superior, 5, 5 Superior'.  - `lodgingSize[object]`: 物件宿泊施設の部屋数の範囲  - `lodgingType[string]`: 物件通常のタイプの宿泊施設。将来UNE178506を参照する可能性がある。Enum:'ホテル、リゾート、ホステル、モーテル、B&B、アパートホテル、ロッジ'.  - `name[string]`: このアイテムの名前。  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `reservationLeadTime[object]`: 物件予約からチェックインまでの日数  - `roomOfStayType[string]`: 物件予約した宿泊施設の部屋タイプ。Enum:'Apartment, Bungalow, Studio, Single, Double, Family, Junior Suite, Senior/Executive Suite, Royal/Presidential Suite'.  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨します。  - `stayLength[object]`: 物件宿泊数の範囲  - `totalAccommodationAndBoardExpenditure[object]`: 物件。宿泊施設から請求された宿泊・食事コンセプトの合計金額の範囲。  - `totalExpenditure[object]`: 物件。宿泊施設からの請求金額の総額の範囲。  - `totalExtraExpenditure[object]`: プロパティ。宿泊施設が追加コンセプトで請求した合計金額の範囲。  - `travelPartyComposition[string]`: 物件大人と子供の人数に基づく旅行者の構成。Enum:'Single, Single parent, Family, Couple, Friends/Relatives'.  - `type[string]`: プロパティ。NGSI エンティティタイプ。TouristProfile でなければならない。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
TouristProfileエンティティは、宿泊施設での予約と滞在の詳細に従って、特定のタイプの観光客の検索プロファイルの記述を含む。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TouristProfile:    
  description: 'Description of a tourist profile based on the characteristics of a person, trip, choice of stay and spending while in destination.'    
  properties:    
    address:    
      description: The mailing address    
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
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government.'    
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
        streetNr:    
          description: Number identifying a specific property on a public street.    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    ageRange:    
      description: Property. Age range of the person profiled.    
      properties:    
        range:    
          description: Property. Value of ageRange. It uses the ranges defined by sortingOrder.    
          type: string    
        sortingOrder:    
          description: 'Property. Ordered set of different age groups for ageRange. OrderedSet: ''0-1, 2-5, 6-11, 12-17, 18-24, 25-29, 30-34, 35-39, 40-44, 45-49, 50-54, 55-59, 60-64, 65+''.'    
          items:    
            type: string    
          type: array    
      type: object    
      x-ngsi:    
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
    avgDailyAccommodationAndBoardExpenditure:    
      description: Property. Range of avg daily amount of money invoiced by the lodging establishment in accommodation and board concepts.    
      properties:    
        range:    
          description: Property. Value of avgDailyAccommodationAndBoardExpenditure. It uses the ranges defined by sortingOrder.    
          type: string    
        sortingOrder:    
          description: 'Property. Ordered set of range of money amounts for avgDailyAccommodationAndBoardExpenditure. OrderedSet: ''0 to 24 €, 25 to 49 €, 50 to 74 €, 75 to 99 €, 100 to 149 €, 150 to 199 €, 200 to 249 €, 250 to 299 €, 300 to 399 €, 400 to 499 €, 500 to 599 €, 600+ €'''    
          items:    
            type: string    
          type: array    
      type: object    
      x-ngsi:    
        type: Property    
    avgDailyExpenditure:    
      description: Property. Range of avg daily amount of money invoiced by the lodging establishment.    
      properties:    
        range:    
          description: Property. Value of avgDailyExpenditure. It uses the ranges defined by sortingOrder.    
          type: string    
        sortingOrder:    
          description: 'Property. Ordered set of range of money amounts for avgDailyExpenditure. OrderedSet: ''0 to 24 €, 25 to 49 €, 50 to 74 €, 75 to 99 €, 100 to 149 €, 150 to 199 €, 200 to 249 €, 250 to 299 €, 300 to 399 €, 400 to 499 €, 500 to 599 €, 600+ €''.'    
          items:    
            type: string    
          type: array    
      type: object    
      x-ngsi:    
        type: Property    
    avgDailyExtraExpenditure:    
      description: Property. Range of avg daily amount of money invoiced by the lodging establishment in extra concepts    
      properties:    
        range:    
          description: Property. Value of avgDailyExtraExpenditure. It uses the ranges defined by sortingOrder.    
          type: string    
        sortingOrder:    
          description: 'Property. Ordered set of range of money amounts for avgDailyExtraExpenditure. OrderedSet: ''0 to 24 €, 25 to 49 €, 50 to 74 €, 75 to 99 €, 100 to 149 €, 150 to 199 €, 200 to 249 €, 250 to 299 €, 300 to 399 €, 400 to 499 €, 500 to 599 €, 600+ €'''    
          items:    
            type: string    
          type: array    
      type: object    
      x-ngsi:    
        type: Property    
    board:    
      description: 'Property. Usual type of board type reserved. Enum:''RO, BB, HB, FB, AI''.'    
      enum:    
        - RO    
        - BB    
        - HB    
        - FB    
        - AI    
      type: string    
      x-ngsi:    
        type: Property    
    bookingChannel:    
      description: Property. Channel used by the tourist for the reservation.    
      type: string    
      x-ngsi:    
        type: Property    
    country:    
      description: 'Property. Country of nationality - https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2.'    
      type: string    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity.    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    gender:    
      description: 'Property. Gender of the person profiled. Enum:''Female, Male''.'    
      enum:    
        - Female    
        - Male    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &touristprofile_-_properties_-_owner_-_items_-_anyof    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: GeoProperty. Geojson reference to the item. Point    
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
          title: GeoJSON Point    
          type: object    
        - description: GeoProperty. Geojson reference to the item. LineString    
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
          title: GeoJSON LineString    
          type: object    
        - description: GeoProperty. Geojson reference to the item. Polygon    
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
          title: GeoJSON Polygon    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiPoint    
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
          title: GeoJSON MultiPoint    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiLineString    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiPolygon    
          type: object    
      x-ngsi:    
        type: GeoProperty    
    lodgingCategory:    
      description: 'Property. Usual category of the lodging. Enum:''1, 1 Superior, 2, 2 Superior, 3, 3 Superior, 4, 4 Superior, 5, 5 Superior''.'    
      enum:    
        - 1    
        - 1 Superior    
        - 2    
        - 2 Superior    
        - 3    
        - 3 Superior    
        - 4    
        - 4 Superior    
        - 5    
        - 5 Superior    
      type: string    
      x-ngsi:    
        type: Property    
    lodgingSize:    
      description: Property. Range size in number of rooms of the lodging    
      properties:    
        range:    
          description: Property. Value of lodgingSize. It uses the ranges defined by sortingOrder.    
          type: string    
        sortingOrder:    
          description: 'Property. Ordered set of intervals of the quantity of rooms for lodgingSize. OrderedSet: ''0 - 24 very small, 25 - 100 small, 101 - 300 medium, 301 - 700 large, 701 - 1200 very large, 1201+ massive'''    
          items:    
            type: string    
          type: array    
      type: object    
      x-ngsi:    
        type: Property    
    lodgingType:    
      description: 'Property. Usual type of lodging for the stay. Could reference UNE178506 in the future. Enum:''Hotel, Resort, Hostel, Motel, B&B, Aparthotel, Lodge''.'    
      enum:    
        - Hotel    
        - Resort    
        - Hostel    
        - Motel    
        - B&B    
        - Aparthotel    
        - Lodge    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *touristprofile_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    reservationLeadTime:    
      description: Property. Range of days between booking and check-in.    
      properties:    
        range:    
          description: Property. Value of reservationLeadTime. It uses the ranges defined by sortingOrder.    
          type: string    
        sortingOrder:    
          description: 'Property. Ordered set of range of days for reservationLeadTime. OrderedSet: ''1 to 7 days, 8 to 14 days, 15 to 30 days, 31 to 60 days, 61 to 90 days, 91 to 120 days, 121 to 240 days, 241 to 365 days, 366+ days''.'    
          items:    
            type: string    
          type: array    
      type: object    
      x-ngsi:    
        type: Property    
    roomOfStayType:    
      description: 'Property. Usual type of the accommodation room reserved. Enum:''Apartment, Bungalow, Studio, Single, Double, Family, Junior Suite, Senior/Executive Suite, Royal/Presidential Suite''.'    
      enum:    
        - Apartment    
        - Bungalow    
        - Studio    
        - Single    
        - Double    
        - Family    
        - Junior Suite    
        - Senior/Executive Suite    
        - Royal/Presidential Suite    
      type: string    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    stayLength:    
      description: Property. Range of number of staying nights.    
      properties:    
        range:    
          description: Property. Value of stayLength. It uses the ranges defined by sortingOrder.    
          type: string    
        sortingOrder:    
          description: 'Property. Ordered set of range of nights for stayLength. OrderedSet: ''1 night, 2 to 4 nights, 5 to 7 nights, 8 to 14 nights, 15 to 21 nights, 22+ nights''.'    
          items:    
            type: string    
          type: array    
      type: object    
      x-ngsi:    
        type: Property    
    totalAccommodationAndBoardExpenditure:    
      description: Property. Range of total amount of money invoiced by the lodging establishment in accommodation and board concepts.    
      properties:    
        range:    
          description: Property. Value of totalAccommodationAndBoardExpenditure. It uses the ranges defined by sortingOrder.    
          type: string    
        sortingOrder:    
          description: 'Property. Ordered set of range of money amounts for totalAccommodationAndBoardExpenditure. OrderedSet: ''0 to 249 €, 250 to 499 €, 500 to 749 €, 750 to 999 €, 1000 to 1499 €, 1500 to 1999 €, 2000 to 2999 €, 3000 to 3999 €, 4000 to 4999 €, 5000+ €''.'    
          items:    
            type: string    
          type: array    
      type: object    
      x-ngsi:    
        type: Property    
    totalExpenditure:    
      description: Property. Range of total amount of money invoiced by the lodging establishment.    
      properties:    
        range:    
          description: Property. Value of totalExpenditure. It uses the ranges defined by sortingOrder.    
          type: string    
        sortingOrder:    
          description: 'Property. Ordered set of range of money amounts for totalExpenditure. OrderedSet: ''0 to 249 €, 250 to 499 €, 500 to 749 €, 750 to 999 €, 1000 to 1499 €, 1500 to 1999 €, 2000 to 2999 €, 3000 to 3999 €, 4000 to 4999 €, 5000+ €''.'    
          items:    
            type: string    
          type: array    
      type: object    
      x-ngsi:    
        type: Property    
    totalExtraExpenditure:    
      description: Property. Range of total amount of money invoiced by the lodging establishment in extra concepts.    
      properties:    
        range:    
          description: Property. Value of totalExtraExpenditure. It uses the ranges defined by sortingOrder.    
          type: string    
        sortingOrder:    
          description: 'Property. Ordered set of range of money amounts for totalExtraExpenditure. OrderedSet: ''0 to 249 €, 250 to 499 €, 500 to 749 €, 750 to 999 €, 1000 to 1499 €, 1500 to 1999 €, 2000 to 2999 €, 3000 to 3999 €, 4000 to 4999 €, 5000+ €''.'    
          items:    
            type: string    
          type: array    
      type: object    
      x-ngsi:    
        type: Property    
    travelPartyComposition:    
      description: 'Property. Composition of the travelling party based on the number of adults and children. Enum:''Single, Single parent, Family, Couple, Friends/Relatives''.'    
      enum:    
        - Single    
        - Single parent    
        - Family    
        - Couple    
        - Friends/Relatives    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. NGSI Entity type. It has to be TouristProfile.    
      enum:    
        - TouristProfile    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.TourismDestinations/blob/master/TouristProfile/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.TourismDestinations/TouristProfile/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### TouristProfile NGSI-v2 キー値の例  
JSON-LD形式のTouristProfileのkey-valuesの例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:hosp:tourpro:0001",  
  "type": "TouristProfile",  
  "country": "NL",  
  "ageRange": {  
    "range": "30-34",  
    "sortingOrder": [  
      "0-1",  
      "2-5",  
      "6-11",  
      "12-17",  
      "18-24",  
      "25-29",  
      "30-34",  
      "35-39",  
      "40-44",  
      "45-49",  
      "50-54",  
      "55-59",  
      "60-64",  
      "65+"  
    ]  
  },  
  "gender": "Male",  
  "travelPartyComposition": "Couple",  
  "lodgingType": "Resort",  
  "lodgingCategory": "4",  
  "lodgingSize": {  
    "range": "101 - 300 Medium",  
    "sortingOrder": [  
      "0 - 24 Very Small",  
      "25 - 100 Small",  
      "101 - 300 Medium",  
      "301 - 700 Large",  
      "701 - 1200 Very Large",  
      "1201+ Massive"  
    ]  
  },  
  "roomOfStayType": "Double",  
  "board": "HB",  
  "bookingChannel": "Tour Operator",  
  "reservationLeadTime": {  
    "range": "91 to 120 days",  
    "sortingOrder": [  
      "1 to 7 Days",  
      "8 to 14 Days",  
      "15 to 30 Days",  
      "31 to 60 Days",  
      "61 to 90 Days",  
      "91 to 120 Days",  
      "121 to 240 Days",  
      "241 to 365 Days",  
      "366+ Days"  
    ]  
  },  
  "stayLength": {  
    "range": "5 to 7 days",  
    "sortingOrder": [  
      "1 day",  
      "2 to 4 days",  
      "5 to 7 days",  
      "8 to 14 days",  
      "15 to 21 days",  
      "22+ days"  
    ]  
  },  
  "totalExpenditure": {  
    "range": "1250 to 1499 €",  
    "sortingOrder": [  
      "0 to 249 €",  
      "250 to 499 €",  
      "250 to 499 €",  
      "500 to 749 €",  
      "750 to 999 €",  
      "1000 to 1499 €",  
      "1500 to 1999 €",  
      "2000 to 2999 €",  
      "3000 to 3999 €",  
      "4000 to 4999 €",  
      "5000+ €"  
    ]  
  },  
  "totalAccomodationAndBoardExpenditure": {  
    "range": "1000 to 1249 €",  
    "sortingOrder": [  
      "0 to 249 €",  
      "250 to 499 €",  
      "250 to 499 €",  
      "500 to 749 €",  
      "750 to 999 €",  
      "1000 to 1499 €",  
      "1500 to 1999 €",  
      "2000 to 2999 €",  
      "3000 to 3999 €",  
      "4000 to 4999 €",  
      "5000+ €"  
    ]  
  },  
  "totalExtraExpenditure": {  
    "range": "0 to 249 €",  
    "sortingOrder": [  
      "0 to 249 €",  
      "250 to 499 €",  
      "250 to 499 €",  
      "500 to 749 €",  
      "750 to 999 €",  
      "1000 to 1499 €",  
      "1500 to 1999 €",  
      "2000 to 2999 €",  
      "3000 to 3999 €",  
      "4000 to 4999 €",  
      "5000+ €"  
    ]  
  },  
  "avgDailyExpenditure": {  
    "range": "200 to 249 €",  
    "sortingOrder": [  
      "0 to 24 €",  
      "25 to 49 €",  
      "50 to 74 €",  
      "75 to 99 €",  
      "100 to 149 €",  
      "150 to 199 €",  
      "200 to 249 €",  
      "250 to 299 €",  
      "300 to 399 €",  
      "400 to 499 €",  
      "500 to 599 €",  
      "600+ €"  
    ]  
  },  
  "avgDailyAccomodationAndBoardExpenditure": {  
    "range": "200 to 249 €",  
    "sortingOrder": [  
      "0 to 24 €",  
      "25 to 49 €",  
      "50 to 74 €",  
      "75 to 99 €",  
      "100 to 149 €",  
      "150 to 199 €",  
      "200 to 249 €",  
      "250 to 299 €",  
      "300 to 399 €",  
      "400 to 499 €",  
      "500 to 599 €",  
      "600+ €"  
    ]  
  },  
  "avgDailyExtraExpenditure": {  
    "range": "0 to 24 €",  
    "sortingOrder": [  
      "0 to 24 €",  
      "25 to 49 €",  
      "50 to 74 €",  
      "75 to 99 €",  
      "100 to 149 €",  
      "150 to 199 €",  
      "200 to 249 €",  
      "250 to 299 €",  
      "300 to 399 €",  
      "400 to 499 €",  
      "500 to 599 €",  
      "600+ €"  
    ]  
  }  
}  
```  
</details>  
#### TouristProfile NGSI-v2 正規化例  
以下は、正規化された JSON-LD 形式の TouristProfile の例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:hosp:tourpro:0001",  
    "type": "TouristProfile",  
    "country": {  
        "type": "Text",  
        "value": "NL"  
    },  
    "ageRange": {  
            "type": "Text",  
            "value": "30-34"  
    },  
    "gender": {  
        "type": "Text",  
        "value": "Male"  
    },  
    "travelPartyComposition": {  
        "type": "Text",  
        "value": "Couple"  
    },  
    "lodgingType": {  
        "type": "Text",  
        "value": "Resort"  
    },  
    "lodgingCategory": {  
        "type": "Text",  
        "value": "4"  
    },  
    "lodgingSize": {  
        "type": "Text",  
        "value": "101 - 300 Medium"  
    },  
    "roomOfStayType": {  
        "type": "Text",  
        "value": "Double"  
    },  
    "board": {  
        "type": "Text",  
        "value": "HB"  
    },  
    "bookingChannel": {  
        "type": "Text",  
        "value": "Tour Operator"  
    },  
    "reservationLeadTime": {  
        "type": "Text",  
        "value": "91 to 120 days"  
    },  
    "stayLength": {  
        "type": "Text",  
        "value": "5 to 7 days"  
    },  
    "totalExpenditure": {  
        "type": "Text",  
        "value": "1250 to 1499 €"  
    },  
    "totalAccomodationAndBoardExpenditure": {  
        "type": "Text",  
        "value": "1000 to 1249 €"  
    },  
    "totalExtraExpenditure": {  
        "type": "Text",  
        "value": "0 to 249 €"  
    },  
    "avgDailyAccomodationAndBoardExpenditure": {  
        "type": "Text",  
        "value": "200 to 249 €"  
    },  
    "avgDailyExtraExpenditure": {  
        "type": "Text",  
        "value": "0 to 24 €"  
    }  
}  
```  
</details>  
#### TouristProfile NGSI-LD キー値の例  
これはJSON-LD形式のTouristProfileをkey-valuesとした例である。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:hosp:tourpro:0001",  
  "type": "TouristProfile",  
  "country": "NL",  
  "ageRange": {  
    "range": "30-34",  
    "sortingOrder": [  
      "0-1",  
      "2-5",  
      "6-11",  
      "12-17",  
      "18-24",  
      "25-29",  
      "30-34",  
      "35-39",  
      "40-44",  
      "45-49",  
      "50-54",  
      "55-59",  
      "60-64",  
      "65+"  
    ]  
  },  
  "gender": "Male",  
  "travelPartyComposition": "Couple",  
  "lodgingType": "Resort",  
  "lodgingCategory": "4",  
  "lodgingSize": {  
    "range": "101 - 300 Medium",  
    "sortingOrder": [  
      "0 - 24 Very Small",  
      "25 - 100 Small",  
      "101 - 300 Medium",  
      "301 - 700 Large",  
      "701 - 1200 Very Large",  
      "1201+ Massive"  
    ]  
  },  
  "roomOfStayType": "Double",  
  "board": "HB",  
  "bookingChannel": "Tour Operator",  
  "reservationLeadTime": {  
    "range": "91 to 120 days",  
    "sortingOrder": [  
      "1 to 7 Days",  
      "8 to 14 Days",  
      "15 to 30 Days",  
      "31 to 60 Days",  
      "61 to 90 Days",  
      "91 to 120 Days",  
      "121 to 240 Days",  
      "241 to 365 Days",  
      "366+ Days"  
    ]  
  },  
  "stayLength": {  
    "range": "5 to 7 days",  
    "sortingOrder": [  
      "1 day",  
      "2 to 4 days",  
      "5 to 7 days",  
      "8 to 14 days",  
      "15 to 21 days",  
      "22+ days"  
    ]  
  },  
  "totalExpenditure": {  
    "range": "1250 to 1499 €",  
    "sortingOrder": [  
      "0 to 249 €",  
      "250 to 499 €",  
      "250 to 499 €",  
      "500 to 749 €",  
      "750 to 999 €",  
      "1000 to 1499 €",  
      "1500 to 1999 €",  
      "2000 to 2999 €",  
      "3000 to 3999 €",  
      "4000 to 4999 €",  
      "5000+ €"  
    ]  
  },  
  "totalAccomodationAndBoardExpenditure": {  
    "range": "1000 to 1249 €",  
    "sortingOrder": [  
      "0 to 249 €",  
      "250 to 499 €",  
      "250 to 499 €",  
      "500 to 749 €",  
      "750 to 999 €",  
      "1000 to 1499 €",  
      "1500 to 1999 €",  
      "2000 to 2999 €",  
      "3000 to 3999 €",  
      "4000 to 4999 €",  
      "5000+ €"  
    ]  
  },  
  "totalExtraExpenditure": {  
    "range": "0 to 249 €",  
    "sortingOrder": [  
      "0 to 249 €",  
      "250 to 499 €",  
      "250 to 499 €",  
      "500 to 749 €",  
      "750 to 999 €",  
      "1000 to 1499 €",  
      "1500 to 1999 €",  
      "2000 to 2999 €",  
      "3000 to 3999 €",  
      "4000 to 4999 €",  
      "5000+ €"  
    ]  
  },  
  "avgDailyExpenditure": {  
    "range": "200 to 249 €",  
    "sortingOrder": [  
      "0 to 24 €",  
      "25 to 49 €",  
      "50 to 74 €",  
      "75 to 99 €",  
      "100 to 149 €",  
      "150 to 199 €",  
      "200 to 249 €",  
      "250 to 299 €",  
      "300 to 399 €",  
      "400 to 499 €",  
      "500 to 599 €",  
      "600+ €"  
    ]  
  },  
  "avgDailyAccomodationAndBoardExpenditure": {  
    "range": "200 to 249 €",  
    "sortingOrder": [  
      "0 to 24 €",  
      "25 to 49 €",  
      "50 to 74 €",  
      "75 to 99 €",  
      "100 to 149 €",  
      "150 to 199 €",  
      "200 to 249 €",  
      "250 to 299 €",  
      "300 to 399 €",  
      "400 to 499 €",  
      "500 to 599 €",  
      "600+ €"  
    ]  
  },  
  "avgDailyExtraExpenditure": {  
    "range": "0 to 24 €",  
    "sortingOrder": [  
      "0 to 24 €",  
      "25 to 49 €",  
      "50 to 74 €",  
      "75 to 99 €",  
      "100 to 149 €",  
      "150 to 199 €",  
      "200 to 249 €",  
      "250 to 299 €",  
      "300 to 399 €",  
      "400 to 499 €",  
      "500 to 599 €",  
      "600+ €"  
    ]  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.TourismDestinations/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### TouristProfile NGSI-LD 正規化例  
以下は、正規化された JSON-LD 形式の TouristProfile の例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:hosp:tourpro:0001",  
  "type": "TouristProfile",  
  "country": {  
    "type": "Property",  
    "value": "NL"  
  },  
  "ageRange": {  
    "type": "Property",  
    "value": "30-34"  
  },  
  "gender": {  
    "type": "Property",  
    "value": "Male"  
  },  
  "travelPartyComposition": {  
    "type": "Property",  
    "value": "Couple"  
  },  
  "lodgingType": {  
    "type": "Property",  
    "value": "Resort"  
  },  
  "lodgingCategory": {  
    "type": "Property",  
    "value": "4"  
  },  
  "lodgingSize": {  
    "type": "Property",  
    "value": "101 - 300 Medium"  
  },  
  "roomOfStayType": {  
    "type": "Property",  
    "value": "Double"  
  },  
  "board": {  
    "type": "Property",  
    "value": "HB"  
  },  
  "bookingChannel": {  
    "type": "Property",  
    "value": "Tour Operator"  
  },  
  "reservationLeadTime": {  
    "type": "Property",  
    "value": "91 to 120 days"  
  },  
  "stayLength": {  
    "type": "Property",  
    "value": "5 to 7 days"  
  },  
  "totalExpenditure": {  
    "type": "Property",  
    "value": "1250 to 1499 €"  
  },  
  "totalAccomodationAndBoardExpenditure": {  
    "type": "Property",  
    "value": "1000 to 1249 €"  
  },  
  "totalExtraExpenditure": {  
    "type": "Property",  
    "value": "0 to 249 €"  
  },  
  "avgDailyAccomodationAndBoardExpenditure": {  
    "type": "Property",  
    "value": "200 to 249 €"  
  },  
  "avgDailyExtraExpenditure": {  
    "type": "Property",  
    "value": "0 to 24 €"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.TourismDestinations/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
