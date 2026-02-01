<!-- 10-Header -->
  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

实体: TourismPresenceObserved  
===============================
<!-- /10-Header -->
  
<!-- 15-License -->
  

[开放许可证](https://github.com/smart-data-models//dataModel.TourismDestinations/blob/master/TourismPresenceObserved/LICENSE.md)  

[自动生成的文档](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->
  
<!-- 20-Description -->
  

Global description: **按小时观察特定地点（市镇）访客存在情况，按国籍划分。每个实体代表一小时的观察。**  

version: 0.0.1  
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->
  


## 属性列表  


<sup><sub>[*] 如果一个属性中没有指定类型，那是因为它可能有多种类型或不同的格式/模式</sub></sup>  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)  
	- `addressCountry[string]`: 该国。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 街道地址所在的地区，以及该地区所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 该地所在的地区，以及该地区所在的国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 區域是一種行政區劃類型，在某些國家，由地方政府管理  
	- `postOfficeBoxNumber[string]`: 邮政信箱的邮政信箱号码。例如，03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 邮政编码。例如，24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 公共街道上特定房产的识别号码  
- `aggregationType[string]`: 用于此小时观测的聚合类型  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `alternateName[string]`: 该物品的另一个名称  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `areaServed[string]`: 服务或数据适用的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `dataProvider[string]`: 提供的和谐数据实体  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `dateCreated[date-time]`: 实体创建时间戳。这通常由存储平台分配  
- `dateModified[date-time]`: 实体的最后修改时间戳。这通常由存储平台分配  
- `dateObserved[date-time]`: 此小时观测的日期和时间，以ISO8601 UTC格式表示，应代表一小时的中间时间（例如10:30代表10:00-10:59）  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)  
- `description[string]`: 对该项的描述  
- `district[string]`: 所在地行政区  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `hour[number]`: 本次观测的当日小时（0-23）  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `id[*]`: 实体的唯一标识符  
- `location[*]`: GeoJSON引用该项。它可以是点、线字符串、多边形、多点、多线字符串或多多边形  
- `locationCode[string]`: 该位置/市镇的官方代码（例如葡萄牙的DICOFRE代码）  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `locationName[string]`: 地點/市政名稱  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `name[string]`: 该物品的名称  
- `nationality[string]`: 访问者的国籍以ISO 3166-1 alpha-2国家代码表示（例如ES，FR，PT）  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `nationalityName[string]`: 国家的全称（可选，为了方便人类阅读）  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `owner[array]`: 包含一个JSON编码的序列的列表，该序列引用了所有者（们）的唯一ID  
- `seeAlso[*]`: 关于该项目的附加资源的URI列表  
- `source[string]`: 数据的原始来源作为URL  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `type[string]`: NGSI 实体类型。它必须是 TourismPresenceObserved  
- `visitorCount[number]`: 在此特定小时内观察到的访客人数  . Model: [https://schema.org/Number](https://schema.org/Number)  
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

必需属性  
- `观察日期`  
- `小时`  
- `id`  
- `位置`  
- `位置代码`  
- `国籍`  
- `类型`  
- `访客数量`  
<!-- /35-RequiredProperties -->
  
<!-- 40-NotesYaml -->
  
<!-- /40-NotesYaml -->
  
<!-- 50-DataModelHeader -->
  

## 数据模型属性描述  

按字母顺序排列（点击查看详细信息）  
<!-- /50-DataModelHeader -->
  
<!-- 60-ModelYaml -->
  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
TourismPresenceObserved:    
  description: Hourly observation of visitor presence at a specific location (municipality), segmented by nationality. Each entity represents one hour of observation.    
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
        model: https://schema.org/Text    
        type: Property    
    areaServed:    
      description: The geographic area where the service or data applies    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: Provider of the harmonised data entity    
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
      description: Date and time of this hourly observation in ISO8601 UTC format. It should represent the middle of the hour (e.g. 10:30 for 10:00–10:59)    
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
    district:    
      description: Administrative district of the location    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    hour:    
      description: Hour of the day (0–23) for this observation    
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
      description: Official code of the location/municipality (e.g. DICOFRE code in Portugal)    
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
      description: Nationality of visitors expressed as ISO 3166-1 alpha-2 country code (e.g. ES, FR, PT)    
      pattern: ^[A-Z]{2}$    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    nationalityName:    
      description: Full name of the nationality country (optional, for human readability)    
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
    type:    
      description: NGSI entity type. It has to be TourismPresenceObserved    
      enum:    
        - TourismPresenceObserved    
      type: string    
      x-ngsi:    
        type: Property    
    visitorCount:    
      description: Number of visitors observed during this specific hour    
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
    - visitorCount    
    - hour    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.TourismDestinations/blob/master/TourismPresenceObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Tourism/TourismPresenceObserved/schema.json    
  x-model-tags: tourism,presence,statistics    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->
  
<!-- 70-MiddleNotes -->
  
<!-- /70-MiddleNotes -->
  
<!-- 80-Examples -->
  

## 示例有效载荷  

#### 旅游业存在观察到的NGSI-v2键值示例  

这是JSON格式的TourismPresenceObserved示例，以键值对的形式呈现。当使用`options=keyValues`时，它与NGSI-v2兼容，并返回个体实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:TourismPresenceObserved:PT:OUTROS-GDPR:IN:20241231T10",  
  "type": "TourismPresenceObserved",  
  "dateObserved": "2024-12-31T10:30:00Z",  
  "hour": 10,  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      0,  
      0  
    ]  
  },  
  "locationCode": "Outros - GDPR",  
  "locationName": "Outros - GDPR",  
  "nationality": "IN",  
  "nationalityName": "India",  
  "visitorCount": 54,  
  "aggregationType": "hourly_sum",  
  "dataProvider": "INE"  
}  
```  
</details>  

#### 旅游存在观察NGSI-v2标准化示例  

这是一个以JSON格式标准化的TourismPresenceObserved示例。当不使用选项时，它与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:TourismPresenceObserved:PT:OUTROS-GDPR:IN:20241231T10",  
  "type": "TourismPresenceObserved",  
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
      "coordinates": [  
        0,  
        0  
      ]  
    }  
  },  
  "locationCode": {  
    "type": "Property",  
    "value": "Outros - GDPR"  
  },  
  "locationName": {  
    "type": "Property",  
    "value": "Outros - GDPR"  
  },  
  "nationality": {  
    "type": "Property",  
    "value": "IN"  
  },  
  "nationalityName": {  
    "type": "Property",  
    "value": "India"  
  },  
  "visitorCount": {  
    "type": "Property",  
    "value": 54  
  },  
  "aggregationType": {  
    "type": "Property",  
    "value": "hourly_sum"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "INE"  
  }  
}  
```  
</details>  

#### 旅游存在观察NGSI-LD关键值示例  

以下是JSON-LD格式的TourismPresenceObserved示例，以键值对的形式呈现。当使用`options=keyValues`时，它与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:TourismPresenceObserved:PT:OUTROS-GDPR:IN:20241231T10",  
  "type": "TourismPresenceObserved",  
  "dateObserved": "2024-12-31T10:30:00Z",  
  "hour": 10,  
  "location": {  
    "type": "Point",  
    "coordinates": [0, 0]  
  },  
  "locationCode": "Outros - GDPR",  
  "locationName": "Outros - GDPR",  
  "nationality": "IN",  
  "nationalityName": "India",  
  "visitorCount": 54,  
  "aggregationType": "hourly_sum",  
  "dataProvider": "INE",  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://smart-data-models.github.io/dataModel.Transportation/context.jsonld"  
  ]  
}  
```  
</details>  

#### 旅游存在观察NGSI-LD标准化示例  

这是一个以JSON-LD格式标准化的TourismPresenceObserved示例。当不使用选项时，它与NGSI-LD兼容，并返回个体实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:TourismPresenceObserved:PT:OUTROS-GDPR:IN:20241231T10",  
  "type": "TourismPresenceObserved",  
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
      "coordinates": [0, 0]  
    }  
  },  
  "locationCode": {  
    "type": "Property",  
    "value": "Outros - GDPR"  
  },  
  "locationName": {  
    "type": "Property",  
    "value": "Outros - GDPR"  
  },  
  "nationality": {  
    "type": "Property",  
    "value": "IN"  
  },  
  "nationalityName": {  
    "type": "Property",  
    "value": "India"  
  },  
  "visitorCount": {  
    "type": "Property",  
    "value": 54  
  },  
  "aggregationType": {  
    "type": "Property",  
    "value": "hourly_sum"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "INE"  
  },  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://smart-data-models.github.io/dataModel.Transportation/context.jsonld"  
  ]  
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
  
