<!-- 10-Header -->
  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

实体: TourismDwellTimeObserved  
================================
<!-- /10-Header -->
  
<!-- 15-License -->
  

[开放许可证](https://github.com/smart-data-models//dataModel.TourismDestinations/blob/master/TourismDwellTimeObserved/LICENSE.md)  

[自动生成文档](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->
  
<!-- 20-Description -->
  

Global description: **按小时观察游客停留时间（停留时长）在特定位置（市镇），按国籍和停留时间范围划分。**  

version: 0.0.1  
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->
  


## 属性列表  


<sup><sub>[*] 如果一个属性中没有指定类型，那是因为它可能有多种类型或不同的格式/模式</sub></sup>  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)  
	- `addressCountry[string]`: 该国。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 该街道地址所在的地区，以及该地区所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 该地方所在的地区，以及该地区所在的国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 區域是一種行政區劃類型，在一些國家，由地方政府管理  
	- `postOfficeBoxNumber[string]`: 邮政信箱的邮政信箱编号。例如，03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 邮政编码。例如，24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 公共街道上特定房产的识别号码  
- `aggregationType[string]`: 用于此小时观测的聚合类型  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `alternateName[string]`: 该物品的另一个名称  
- `areaServed[string]`: 提供服务或项目的地域区域  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `dataProvider[string]`: 数据提供者  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `dateCreated[date-time]`: 实体创建时间戳。这通常由存储平台分配  
- `dateModified[date-time]`: 实体最后修改的时间戳。这通常由存储平台分配  
- `dateObserved[date-time]`: 观察的日期和时间（ISO8601 UTC）  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)  
- `description[string]`: 对该物品的描述  
- `dwellTimeRange[string]`: 停留时间范围（以分钟为单位，例如0-5，5-15，30-60，120分钟以上）  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `hour[number]`: 本观测的当日小时（0-23）  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `id[*]`: 实体的唯一标识符  
- `location[*]`: Geojson引用该项。它可以是Point、LineString、Polygon、MultiPoint、MultiLineString或MultiPolygon  
- `locationCode[string]`: 位置/市镇的官方代码（例如DICOFRE）  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `locationName[string]`: 位置/市政名称  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `name[string]`: 该物品的名称  
- `nationality[string]`: 访客的国籍。ISO 3166-1 alpha-2 国家代码  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `nationalityName[string]`: 国籍国家的全称（可选）  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `owner[array]`: 包含一个JSON编码的字符序列的列表，引用所有者（们）的唯一Id  
- `seeAlso[*]`: 关于该项目的其他资源的URI列表  
- `source[string]`: 数据的原始来源作为URL  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `totalVisitors[number]`: 本小时内所有停留时间范围的访客总数  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `type[string]`: NGSI 实体类型。它必须是 TourismDwellTimeObserved  
- `visitorCount[number]`: 此停留时间范围内的访客数量  . Model: [https://schema.org/Number](https://schema.org/Number)  
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

所需属性  
- `观察日期`  
- `停留时间范围`  
- `小时`  
- `id`  
- `位置`  
- `位置代码`  
- `国籍`  
- `类型`  
访客数量  
<!-- /35-RequiredProperties -->
  
<!-- 40-NotesYaml -->
  
<!-- /40-NotesYaml -->
  
<!-- 50-DataModelHeader -->
  

## 数据模型属性描述  

按字母顺序排列（点击查看详情）  
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
  

## 示例有效载荷  

#### 旅游停留时间观察 NGSI-v2 键值示例  

以下是JSON格式的TourismDwellTimeObserved示例，以键值对的形式呈现。当使用`options=keyValues`时，它与NGSI-v2兼容，并返回单个实体的上下文数据。  
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

#### 旅游停留时间观察 NGSI-v2 标准化示例  

这是一个TourismDwellTimeObserved的JSON格式示例，已标准化。当不使用选项时，它与NGSI-v2兼容，并返回单个实体的上下文数据。  
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

#### 旅游停留时间观察 NGSI-LD 键值示例  

这是JSON-LD格式的TourismDwellTimeObserved示例，以键值对的形式呈现。当使用`options=keyValues`时，它与NGSI-LD兼容，并返回个体实体的上下文数据。  
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

#### 旅游停留时间观察 NGSI-LD 标准化 示例  

这是一个以JSON-LD格式标准化的TourismDwellTimeObserved示例。当不使用选项时，它与NGSI-LD兼容，并返回个体实体的上下文数据。  
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
  
