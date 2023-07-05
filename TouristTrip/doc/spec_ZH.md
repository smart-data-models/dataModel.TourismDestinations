<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。旅游行程  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.TourismDestinations/blob/master/TouristTrip/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**一个旅游行程。对一个或多个景点（TouristAttraction/TouristDestination）的访问的创建行程，通常由类似的主题、地理区域或兴趣与一个特定的旅游类型相联系。联合国世界旅游组织将旅游行程定义为游客的旅行。  
版本：0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `accessPlan[string]`: 文本或链接到访问计划的行程。  - `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `audience[array]`: 本行程所涉及的公众类型。自由文本的组合（家庭、成人、儿童、青少年、老年人、所有公众，...）。枚举：'成人、所有公众、儿童、家庭、老人、青少年  - `category[array]`: 旅行的类别。下面提供了一个自由文本的组合，以保持对特定环境的灵活性，作为初始存储库或应用程序需要的任何其他值。 enum:'excursion, gastronomy, history, museum, outdoorActivities, parksAndGardens, religiousWorship, shopping, wellness'  - `contentURL[string]`: 指明该行程的官方图片或视频的URL，以获得更多信息。  - `criticReview[object]`: 由一个因其审查活动而被认可的来源撰写或出版的审查。每个项目都有基于[国际化（i18N）--W3C多语言建议]（https://www.w3.org/TR/json-ld/#string-internationalization）的格式，将所有项目整合在一个单一的属性中（例如编号71）。每个项目由一个字符串表示，"语言值"："文章值"。  - `currencyAccepted[array]`: 如果 "TripFree "为False，接受的支付货币。模型中定义的活动代码列表的组合。[Norme ISO 4217](http://en.wikipedia.org/wiki/ISO_4217), [加密货币](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) , [交易所交易系统](https://en.wikipedia.org/wiki/Local_exchange_trading_system)  . Model: [https://schema.org/currenciesAccepted](https://schema.org/currenciesAccepted)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateLastReported[string]`: 最后一次正式更新的ISO 8601格式的数据  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `duration[number]`: 每个节目的持续时间。计量单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**HUR**代表**小时**。  - `electricTransport[array]`: 城市提出的不同类型的电动交通工具清单。一个组合。Enum:'electricBicycle, electricCar, electricMotorBike, electricScooter' （电动自行车、电动汽车、电动摩托车）。  - `endDate[string]`: 结束日期和时间为ISO8601 UTC格式  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `id[*]`: 实体的唯一标识符  - `isAccessibleForFree[boolean]`: 免费或付费旅行（真=免费/假=付费）。  - `itinerary[array]`: 组成旅行的目的地或地方。对于一个目的地顺序很重要的旅行，使用ItemList来指定包含在旅行中的顺序。  - `language[array]`: Trip过程中使用的正式语言列表表示来自IETF [BCP 47](https://tools.ietf.org/html/bcp47)标准。  . Model: [https://schema.org/language](https://schema.org/language)- `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `locationName[string]`: 旅行地点的名称。  - `maximumAttendeeCapacity[number]`: 在该地点可以参加旅行的总人数。  - `name[string]`: 这个项目的名称。  - `openingHoursSpecification[array]`: 一个结构化的值，提供关于一个地方的开放时间或一个地方内的某种服务的信息。  . Model: [https://schema.org/openingHoursSpecification](https://schema.org/openingHoursSpecification)- `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `paymentAccepted[array]`: 如果`TripFree`为False，则接受付款。模型中定义的活动代码列表的组合。Enum:'Cash, CreditCard, CryptoCurrency, other'。  . Model: [https://schema.org/paymentAccepted](https://schema.org/paymentAccepted)- `pitch[object]`: 旅程中的投递。每个项目都有基于[国际化（i18N）--W3C多语言建议]（https://www.w3.org/TR/json-ld/#string-internationalization）的格式，将所有项目整合在一个单一的属性中（例如编号71）。每个项目由一个字符串表示，其语言值：文章值。  - `priceSpecification[array]`: 一个代表价格或价格范围的结构化数值，取决于类别或公众。  - `ratingValueAverage[number]`: 旅行的评级值。使用指南。根据你的标准，使用0到10的值。这是`starRatingDetailed`属性的所有详细分数的平均值。  - `refPointOfInterest[array]`: 参考所有的兴趣点[PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md)包括在旅行中。兴趣点列表没有按时间顺序排列。  - `routeType[array]`: 根据GFTS标准[STOP](https://developers.google.com/transit/gtfs/reference/#stopstxt)，行程附近可用的城市运输工具（地铁、公交、电车...）列表。一组数值的组合。Enum:' 公共汽车, cableCar, cableTram, 轮渡, 缆车, 单轨列车, 地铁, 火车, 有轨电车, 无轨电车' 。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `slogan[string]`: 行程标题行，与文本钩相匹配。  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `starRatingDetailed[object]`: 详细的星级评定，导致了在ratingValue中表示的平均值。使用说明。一个从1到10个出现的结构化数值（星星），其中每个元素是一个格式的字符串。`NumberOfSTar`。百分比。  - `startDate[string]`: 开始日期和时间为ISO8601 UTC格式  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `subCategory[array]`: `category`属性的子类别。下面提供了一个自由文本的组合，以保持对特定环境的灵活性，作为最初的例子，或应用程序需要的任何其他值。  - `subTrip[array]`: 参考属于该主要行程的次要行程的清单  - `superTrip[*]`: 指包括此行程的主要行程。  - `thematic[array]`: 作为关键词的专题清单  - `title[string]`: 旅程的标题。  - `touristType[array]`: 适用于TouristTrip的不同游客类型的枚举。  - `transportServices[array]`: 旅程附近的私人交通工具清单。例如，出租车、uber、VTC、停车车。  - `tripPriceFrom[number]`: 最低价格。计量单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**欧元**代表**欧元**。  - `tripPriceTo[number]`: 最高价格。计量单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**欧元**代表**欧元**。  - `tripSchedule[array]`: 旅程时间表。这允许在一个重复的时间段内设置一个时间表，用来描述一个定期发生的行程。在本节开头的例子说明中，限制使用这个属性。  - `tripStatus[string]`: 关于此行程的行程状态。Enum:'cancelled, closed, finished, opened, postponed, rescheduled, scheduled, suspended'。  - `type[string]`: 它必须是TouristTrip。NGSI实体类型。  - `webSite[string]`: 链接到官方网站了解更多信息。  - `wheelChairAccessible[boolean]`: 行动不便的人可以进入。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
这个数据模型是基于UNE178503标准。它也与schema.org兼容。在这个文件中，schema.org的一些元素被调整为https://smart-data-models.github.io/data-models/schema-org.json。为了保持与schema.org的兼容性，有必要进行小的调整。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TouristTrip:    
  description: 'A tourist trip. A created itinerary of visits to one or more places of interest (TouristAttraction/TouristDestination) often linked by a similar theme, geographic area, or interest to a particular touristType. The UNWTO defines tourism trip as the Trip taken by visitors.'    
  properties:    
    accessPlan:    
      description: 'Text or Link to the access plan to the Trip.'    
      type: string    
      x-ngsi:    
        type: Property    
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
    audience:    
      description: 'Type of public concerned by this Trip. A combination of Free text (family, adult, children, teenager, senior, allPublic, ...). Enum:''adult, allPublic, children, family, senior, teenager'''    
      items:    
        enum:    
          - adult    
          - allPublic    
          - children    
          - family    
          - senior    
          - teenager    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    category:    
      description: 'Category of the Trip. A combination of free text to remain flexible to a specific context is offered below as an initial repository or any other value needed by an application. enum:''excursion, gastronomy, history, museum, outdoorActivities, parksAndGardens, religiousWorship, shopping, wellness'''    
      items:    
        enum:    
          - excursion    
          - gastronomy    
          - history    
          - museum    
          - outdoorActivities    
          - parksAndGardens    
          - religiousWorship    
          - shopping    
          - wellness    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    contentURL:    
      description: 'Specifies the URL to the official image or video of the Trip for more information.'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Property    
    criticReview:    
      description: "Review written or published by a source that is recognized for its reviewing activities. Each items have the format based on the  [Internationalization (i18N) - W3C recommendation for multilanguage](https://www.w3.org/TR/json-ld/#string-internationalization) integrating all items in a single property (ex number 71). Each item is represented by a string with 'Language Value' : 'Article Value'"    
      properties:    
        language:    
          type: string    
        reviews:    
          items:    
            article:    
              type: string    
            origin:    
              type: string    
            ratingValue:    
              type: number    
            starRating:    
              type: number    
          type: array    
      type: object    
      x-ngsi:    
        type: Property    
    currencyAccepted:    
      description: 'Currency accepted for payment if `TripFree` is False. A combination of a list of active codes defined in the model. [Norme ISO 4217](http://en.wikipedia.org/wiki/ISO_4217), [Crypto Currencies](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) , [Exchange Trading System](https://en.wikipedia.org/wiki/Local_exchange_trading_system)'    
      items:    
        enum:    
          - EUR    
          - USD    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/currenciesAccepted    
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
    dateLastReported:    
      description: 'Last official update of the data in ISO 8601 format'    
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
    duration:    
      description: 'The duration of each show. The unit code (text) of measurement is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **HUR** represents **Hours**.'    
      type: number    
      x-ngsi:    
        type: Property    
    electricTransport:    
      description: ' List of the different types of electric transport proposed by the city. A combination of. Enum:''electricBicycle, electricCar, electricMotorBike, electricScooter'''    
      items:    
        enum:    
          - electricBicycle    
          - electricCar    
          - electricMotorBike    
          - electricScooter    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    endDate:    
      description: 'End date and time in an ISO8601 UTC format'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    id:    
      anyOf: &touristtrip_-_properties_-_owner_-_items_-_anyof    
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
    isAccessibleForFree:    
      description: 'Free or paid Trip (True = Free / False = Paid).'    
      type: boolean    
      x-ngsi:    
        type: Property    
    itinerary:    
      description: 'Destinations or places that make up a trip. For a trip where destination order is important use ItemList to specify that order included in the trips.'    
      items:    
        properties:    
          description:    
            type: string    
          image:    
            items:    
              type: string    
            type: array    
          name:    
            type: string    
          position:    
            type: number    
          streetAddress:    
            items:    
              type: string    
            type: array    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    language:    
      description: ' List of Formal language used during the Trip expressed from the IETF [BCP 47](https://tools.ietf.org/html/bcp47) standard'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/language    
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
    locationName:    
      description: 'Name of the trip location.'    
      type: string    
      x-ngsi:    
        type: Property    
    maximumAttendeeCapacity:    
      description: 'The total number of people who can attend to the Trip at that location.'    
      type: number    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    openingHoursSpecification:    
      description: 'A structured value providing information about the opening hours of a place or a certain service inside a place'    
      items:    
        properties:    
          closes:    
            format: time    
            pattern: ^(2[0-3]|[01][0-9]):?([0-5][0-9]):?([0-5][0-9])(\.[0-9]*)?(Z|[+-](?:2[0-3]|[01][0-9])(?::?(?:[0-5][0-9]))?)$    
            type: string    
          dayOfWeek:    
            anyOf:    
              - description: 'Property. Array of days of the week.'    
                enum:    
                  - Monday    
                  - Tuesday    
                  - Wednesday    
                  - Thursday    
                  - Friday    
                  - Saturday    
                  - Sunday    
                  - PublicHolidays    
                type: string    
              - description: 'Property. Array of days of the week.'    
                enum:    
                  - https://schema.org/Monday    
                  - https://schema.org/Tuesday    
                  - https://schema.org/Wednesday    
                  - https://schema.org/Thursday    
                  - https://schema.org/Friday    
                  - https://schema.org/Saturday    
                  - https://schema.org/Sunday    
                  - https://schema.org/PublicHolidays    
                type: string    
            description: 'Property. Model:''http://schema.org/dayOfWeek''. The day of the week for which these opening hours are valid. URLs from GoodRelations (http://purl.org/goodrelations/v1) are used (for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday plus a special entry for PublicHolidays).'    
            type: string    
          opens:    
            format: time    
            pattern: ^(2[0-3]|[01][0-9]):?([0-5][0-9]):?([0-5][0-9])(\.[0-9]*)?(Z|[+-](?:2[0-3]|[01][0-9])(?::?(?:[0-5][0-9]))?)$    
            type: string    
          validFrom:    
            anyOf:    
              - description: 'Property. Model:''http://schema.org/Date.'    
                format: date    
                type: string    
              - description: 'Property. Model:''http://schema.org/DateTime.'    
                format: date-time    
                type: string    
            description: 'Property. The date when the item becomes valid. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format.'    
          validThrough:    
            anyOf:    
              - description: 'Property. Model:''http://schema.org/Date.'    
                format: date    
                type: string    
              - description: 'Property. Model:''http://schema.org/DateTime.'    
                format: date-time    
                type: string    
            description: 'Property. The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format.'    
            type: string    
        type: object    
      minItems: 1    
      type: array    
      x-ngsi:    
        model: https://schema.org/openingHoursSpecification    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *touristtrip_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    paymentAccepted:    
      description: 'Accepted payment if `TripFree` is False. A combination of a list of active codes defined in the model. Enum:''Cash, CreditCard, CryptoCurrency, other'''    
      items:    
        enum:    
          - Cash    
          - CreditCard    
          - CryptoCurrency    
          - other    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/paymentAccepted    
        type: Property    
    pitch:    
      description: "Pitch of the Trip. Each items have the format based on the [Internationalization (i18N) - W3C recommandation for multilanguage](https://www.w3.org/TR/json-ld/#string-internationalization) integrating all items in a single property (ex number 71). Each item is represented by a string with Language Value : Article Value. "    
      properties:    
        article:    
          type: string    
        language:    
          type: string    
      type: object    
      x-ngsi:    
        type: Property    
    priceSpecification:    
      description: 'A structured value representing a price or price range depending categories or public.'    
      items:    
        properties:    
          audience:    
            items:    
              type: string    
            type: array    
          eligibleQuantity:    
            type: number    
          maxPrice:    
            type: number    
          minPrice:    
            type: number    
          price:    
            type: number    
      type: array    
      x-ngsi:    
        type: Property    
    ratingValueAverage:    
      description: 'Rating value of Trips. Usage guidelines: Use values from 0 to 10 depending on your standard. this is the average value of all detailed scores of `starRatingDetailed` attribute'    
      type: number    
      x-ngsi:    
        type: Property    
    refPointOfInterest:    
      description: 'Reference to all the Point Of interest [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) included in the trips. The POI list does not have a chronological order.'    
      items:    
        anyOf: *touristtrip_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Relationship    
    routeType:    
      description: "List of the urban transports (subway, Bus, Tram, ...) available near the Trip according to the GFTS standard [STOP](https://developers.google.com/transit/gtfs/reference/#stopstxt). A combination of values. Enum:' bus, cableCar, cableTram, ferry, funicular, monorail, subway, train, tram, trolleybus'"    
      items:    
        enum:    
          - bus    
          - cableCar    
          - cableTram    
          - ferry    
          - funicular    
          - monorail    
          - subway    
          - train    
          - tram    
          - trolleybus    
        type: string    
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
    slogan:    
      description: 'Trip header line, matches the text hook. '    
      type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    starRatingDetailed:    
      description: 'Detailed star ratings which led to the average value expressed in the ratingValue. Instructions for use: A structured value from 1 to 10 occurrences (Stars) where each element is a string in the format: `NumberOfSTar`: Percent. '    
      properties:    
        1:    
          type: number    
        10:    
          type: number    
        2:    
          type: number    
        3:    
          type: number    
        4:    
          type: number    
        5:    
          type: number    
        6:    
          type: number    
        7:    
          type: number    
        8:    
          type: number    
        9:    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    startDate:    
      description: 'Start date and time in an ISO8601 UTC format'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    subCategory:    
      description: 'Sub-category of the `category` attribute. A combination of free text to remain flexible to a specific context is offered below as an initial example or any other value needed by an application. '    
      items:    
        enum:    
          - --museum--    
          - art    
          - archaeology    
          - contemporaryArt    
          - modernArt    
          - appliedArts    
          - decorativeArts    
          - scienceAndTechnology    
          - fineArts    
          - music    
          - history    
          - sacredArt    
          - specials    
          - literature    
          - medicineAndPharmacy    
          - maritime    
          - transports    
          - military    
          - wax    
          - popularArtsAndTraditions    
          - numismatic    
          - ceramics    
          - sumptuaryArts    
          - naturalScience    
          - prehistoric    
          - ethnology    
          - railway    
          - mining    
          - textile    
          - sculpture    
          - multiDisciplinar    
          - painting    
          - paleonthology    
          - thematic    
          - architecture    
          - museumHouse    
          - universitary    
          - bullfighting    
          - --excursion--    
          - sea    
          - mountain    
          - river    
          - countryside    
          - ancientCity    
          - cultural    
          - culinary    
          - wineRoute    
          - --parksAndGardens--    
          - park    
          - garden    
          - fountain    
          - --religiousWorship--    
          - church    
          - cathedral    
          - synagogue    
          - mosque    
          - buddhistTemple    
          - hinduTemple    
          - monastery    
          - sanctuary    
          - cemetery    
          - sumptuar    
          - --history--    
          - castle    
          - warMemorials    
          - memorial    
          - fortifiedCastles    
          - archaeologicalSite    
          - crypt    
          - cave    
          - --shopping--    
          - departmentStore    
          - luxuryStores    
          - outlet    
          - mall    
          - clothing    
          - mensClothing    
          - womensClothing    
          - childrenClothing    
          - localProducts    
          - souvenir    
          - wine    
          - pastry    
          - chocolate    
          - confectionery    
          - jewelry    
          - watch    
          - shoe    
          - perfume    
          - cosmetics    
          - press    
          - sport    
          - optics    
          - leatherGoods    
          - decoration    
          - market    
          - bike    
          - book    
          - computer    
          - convenience    
          - electronic    
          - florist    
          - furniture    
          - garden    
          - grocery    
          - home    
          - liquor    
          - mobile    
          - movierental    
          - music    
          - pawnShop    
          - tire    
          - toy    
          - --gastronomy--    
          - worldCuisine    
          - traditional    
          - provencal    
          - mediterranean    
          - greek    
          - spanish    
          - brazilian    
          - lebanese    
          - creole    
          - mauritian    
          - reunion    
          - hawaiian    
          - mexican    
          - american    
          - texMex    
          - vegetarian    
          - fish    
          - seafood    
          - indian    
          - vietnamese    
          - thai    
          - laosian    
          - cambodian    
          - chinese    
          - moroccan    
          - tunisian    
          - african    
          - sushi    
          - japanese    
          - scandinavian    
          - russian    
          - pastry    
          - wine    
          - --outdoorActivities--    
          - rafting    
          - canyoning    
          - aquatichiking    
          - hiking    
          - viaferrata    
          - climbing    
          - kitesurfing    
          - canoeing    
          - paddleboarding    
          - jetSki    
          - catamaran    
          - sailing    
          - surfing    
          - deltaPlane    
          - skiing    
          - scooter    
          - karting    
          - --wellness--    
          - spa    
          - haman    
          - jacuzzi    
          - hotSpring    
          - thalasso    
          - bodyCare    
          - swimmingPool    
          - relaxationArea    
          - massage    
          - careCenter    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    subTrip:    
      description: 'Reference to a list of Minor Trips that are part of this major Trip'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      type: array    
      x-ngsi:    
        type: Relationship    
    superTrip:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the Major Trip that includes this Trip.'    
      x-ngsi:    
        type: Relationship    
    thematic:    
      description: 'A list of thematic as keywords'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    title:    
      description: ' Title of the Trip.'    
      type: string    
      x-ngsi:    
        type: Property    
    touristType:    
      description: 'enumeration of different tourist types applicable to the TouristTrip'    
      items:    
        description: 'Property. Model:''https://schema.org/Text''. Type of tourism depending on the segment and the motivation of the trip.'    
        enum:    
          - 'ADVENTURE TOURISM'    
          - 'ASTRONOMY TOURISM'    
          - 'BACKPACKING TOURISM'    
          - 'BEACH AND SUN TOURISM'    
          - 'BEER TOURISM'    
          - 'BIRDING TOURISM'    
          - 'BULLFIGHTING TOURISM'    
          - BUSINESS    
          - 'COMMUNITY-BASED TOURISM'    
          - 'CRUISE TOURISM'    
          - 'CULTURAL TOURISM'    
          - 'CYCLING TOURISM'    
          - 'DIVING TOURISM'    
          - ECOTOURISM    
          - 'EVENTS AND FESTIVALS TOURISM'    
          - 'FAMILY TOURISM'    
          - 'FILM TOURISM'    
          - 'FISHING TOURISM'    
          - 'FOOD TOURISM'    
          - 'GAMBLING TOURISM'    
          - 'GEOLOGICAL TOURISM'    
          - 'HERITAGE TOURISM'    
          - 'HUNTING TOURISM'    
          - 'INDUSTRIAL TOURISM'    
          - 'LANGUAGE TOURISM'    
          - 'LGTBI TOURISM'    
          - 'LUXURY TOURISM'    
          - 'MEDICAL TOURISM'    
          - 'MEMORIAL TOURISM'    
          - 'MICE TOURISM'    
          - 'NATURE TOURISM'    
          - 'OLIVE OIL TOURISM'    
          - 'PARTY TOURISM'    
          - 'PHOTOGRAPHY TOURISM'    
          - 'RELIGIOUS TOURISM'    
          - 'ROMANTIC TOURISM'    
          - 'RURAL TOURISM'    
          - 'SAFARI TOURISM'    
          - 'SAILING TOURISM'    
          - 'SENIOR TOURISM'    
          - 'SHOPPING TOURISM'    
          - 'SHORT BREAK TOURISM'    
          - 'SINGLES TOURISM'    
          - 'SPORTS TOURISM'    
          - TOURISM    
          - 'TREKKING TOURISM'    
          - 'URBAN TOURISM'    
          - 'WATER SPORTS TOURISM'    
          - 'WEDDING & HONEYMOON TOURISM'    
          - 'WELLNESS TOURISM'    
          - 'WHISKY TOURISM'    
          - 'WINE TOURISM'    
          - 'WINTER SPORTS TOURISM'    
          - 'WOMEN TOURISM'    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    transportServices:    
      description: 'List of private transport available near the Trip. In example taxi, uber, vtc, parkingShuttle'    
      items:    
        enum:    
          - taxi    
          - uber    
          - vtc    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    tripPriceFrom:    
      description: 'Min Price. The unit code (text) of measurement is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **EUR** represents **€uro**.'    
      type: number    
      x-ngsi:    
        type: Property    
    tripPriceTo:    
      description: 'Max Price. The unit code (text) of measurement is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **EUR** represents **€uro**.'    
      type: number    
      x-ngsi:    
        type: Property    
    tripSchedule:    
      description: 'Trip Schedule. This allows a schedule to be set over a repeated period of time used to describe an Trip that occurs regularly. In example nota in the beginning of the section for restriction to use this attribute. '    
      items:    
        properties:    
          byDay:    
            type: string    
          byMonth:    
            type: number    
          byMonthDay:    
            type: number    
          byMonthWeek:    
            type: number    
          dayOfWeek:    
            enum:    
              - Monday    
              - Tuesday    
              - Wednesday    
              - Thursday    
              - Friday    
              - Saturday    
              - Sunday    
              - PublicHolidays    
            type: string    
          duration:    
            type: number    
          endDate:    
            format: date-time    
            type: string    
          endTime:    
            format: date-time    
            type: string    
          exceptDate:    
            format: date-time    
            type: string    
          repeatCount:    
            type: number    
          repeatFrequency:    
            type: string    
          startDate:    
            format: date-time    
            type: string    
          startTime:    
            format: date-time    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    tripStatus:    
      description: 'Trip Status regarding this Trip. Enum:''cancelled, closed, finished, opened, postponed, rescheduled, scheduled, suspended'''    
      enum:    
        - cancelled    
        - closed    
        - finished    
        - opened    
        - postponed    
        - rescheduled    
        - scheduled    
        - suspended    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'It has to be TouristTrip. NGSI Entity type.'    
      enum:    
        - TouristTrip    
      type: string    
      x-ngsi:    
        type: Property    
    webSite:    
      description: 'Link to the official website for more information.'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Property    
    wheelChairAccessible:    
      description: 'Access possible for Person with Reduced Mobility.'    
      type: boolean    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.TourismDestinations/blob/master/TouristTrip/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.TourismDestinations/TouristTrip/schema.json    
  x-model-tags: ""    
  x-version: 0.0.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### TouristTrip NGSI-v2 key-values 示例  
下面是一个以JSON-LD格式作为key-values的TouristTrip的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi:touristTrip:1",  
  "type": "TouristTrip",  
  "name": "Musee du Palais Lascaris",  
  "alternateName": "Palais Lascaris",  
  "description": "Le palais Lascaris est une ancienne demeure aristocratique de Nice datant de la premiere moiti du XVII sicle, aujourd'hui un musee des instruments de musique anciens",  
  "touristType": [  
    "FAMILY TOURISM",  
    "WATER SPORTS TOURISM",  
    "FOOD TOURISM",  
    "BEACH AND SUN TOURISM"  
  ],  
  "url": [  
    "https://www.spain.info/es/que-quieres/ciudades-pueblos/otros-destinos/conil_de_la_frontera.html"  
  ],  
  "image": "http://www.turismo.conil.org/PortalTurismo/DocTurismo.nsf/voTodosPorIdiomaUNID/4AC02453BEE8F5CDC125750400315F48/$FILE/IMGP2024.JPG",  
  "sameAs": "https://inventrip.com/conil/trip/1907",  
  "video": "https://www.youtube.com/watch?v=IhnvlIzxPLg",  
  "seeAlso": "https://www.nice.fr/fr/culture/musees-et-galeries/palais-lascaris-le-palais",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.6976766,  
      7.2772458  
    ]  
  },  
  "address": {  
    "streetAddress": "15, rue Droite",  
    "postalCode": "06000",  
    "adressLocality": "Nice",  
    "addressCountry": "France",  
    "adressRegion": "Marseille Nice Avignon Aix - (06)"  
  },  
  "areaServed": "Vieux Nice",  
  "dateLastReported": "2020-03-17T08:45:00Z",  
  "itinerary": [  
    {  
      "position": 1,  
      "name": "Cours Saleya",  
      "streetAdress": [  
        "Cours Saleya",  
        "06300 Nice"  
      ],  
      "image": [  
        "https://www.nicetourisme.com/nice/1507-marche-aux-fruits-legumes-et-maree-du-cours-saleya"  
      ]  
    },  
    {  
      "position": 2,  
      "name": "Centre du patrimoine",  
      "streetAdress": [  
        "14 rue Jules Gilly",  
        "06300 Nice"  
      ],  
      "image": [  
        "https: //nice.city-life.fr/Services/Nice/Services-touristiques/768/Centre-du-Patrimoine?lang=fr"  
      ]  
    },  
    {  
      "position": 3,  
      "name": "Place du j\u00e9sus",  
      "streetAdress": [  
        "Rue du j\u00e9sus",  
        "06300 Nice"  
      ],  
      "image": [  
        "https: //fr.wikipedia.org/wiki/%C3%89glise_Saint-Jacques-le-Majeur_de_Nice"  
      ]  
    },  
    {  
      "position": 4,  
      "name": "Palais Lascaris",  
      "streetAdress": [  
        "15, rue Droite",  
        "06300 Nice"  
      ],  
      "image": [  
        "https: //upload.wikimedia.org/wikipedia/commons/e/ed/Lascaris2.JPG"  
      ]  
    }  
  ],  
  "contactPoint": {  
    "telephone": "+33(0)4 93 62 72 40",  
    "contactType": "customer reception",  
    "email": "palais.lascaris@ville-nice.fr",  
    "availableLanguage": [  
      "English",  
      "French"  
    ]  
  },  
  "accessPlan": "https://www.google.fr/maps/place/Mus%C3%A9e+du+Palais+Lascaris/@43.6976805,7.2750571,17z/data=!3m1!4b1!4m5!3m4!1s0x12cddabca1950653:0x8d425022ef476dde!8m2!3d43.6976766!4d7.2772458?hl=fr",  
  "category": [  
    "museum"  
  ],  
  "subCategory": [  
    "art",  
    "decorativeArts",  
    "history"  
  ],  
  "thematic": [  
    "culture",  
    "museum",  
    "instrument",  
    "music",  
    "monument"  
  ],  
  "locationName": "Palais Lascaris",  
  "title": "Visite du Mus\u00e9e du Palais Lascaris",  
  "slogan": "Une demeure aristocratique joyau du baroque et une remarquable collection d instruments de musiques anciens.",  
  "language": [  
    "french",  
    "english",  
    "spanish",  
    "german"  
  ],  
  "superTrip": "urn:ngsi-ld:Trip:Trip:MNCA-TRIP-NCE-VISTE-DES-MUSEES-NICE",  
  "tripStatus": "opened",  
  "startDate": "2021-01-01T00:00:00Z",  
  "endDate": "2021-12-31T00:00:00Z",  
  "openingHoursSpecification": [  
    {  
      "dayOfWeek": "Monday",  
      "opens": "10:00:00",  
      "closes": "18:00:00"  
    },  
    {  
      "dayOfWeek": "Wednesday",  
      "opens": "10:00:00",  
      "closes": "18:00:00"  
    },  
    {  
      "dayOfWeek": "Thursday",  
      "opens": "10:00:00",  
      "closes": "18:00:00"  
    },  
    {  
      "dayOfWeek": "Friday",  
      "opens": "10:00:00",  
      "closes": "18:00:00"  
    },  
    {  
      "dayOfWeek": "Saturday",  
      "opens": "10:00:00",  
      "closes": "18:00:00"  
    },  
    {  
      "dayOfWeek": "Sunday",  
      "opens": "10:00:00",  
      "closes": "18:00:00"  
    }  
  ],  
  "duration": 1.25,  
  "pitch": {  
    "fr": {  
      "value": {  
        "article": "Dans une ruelle \u00e9troite ce palais baroque allie richesse ornementale et simplicit\u00e9. Son escalier avec ses fresques est somptueux m\u00eame si ses dimensions sont somme toute r\u00e9duites. L\u2019ambiance est chaleureuse avec des plafonds bas ,des pi\u00e8ces \u00e0 l\u2019\u00e9chelle humaine qui en font un lieu intime propice \u00e0 la d\u00e9couverte de la collection d\u2019instruments de musique. Ne manquez pas d\u2019observer les portes de communication."  
      }  
    },  
    "en": {  
      "value": {  
        "article": "In a narrow alley, this baroque palace combines ornamental richness and simplicity. Its staircase with its frescoes is sumptuous even if its dimensions are all in all small. The atmosphere is warm with low ceilings, rooms on a human scale that make it an intimate place conducive to discovering the collection of gastronomieal instruments. Do not miss to observe the communication doors."  
      }  
    }  
  },  
  "webSite": "http://www.palais-lascaris.com",  
  "contentURL": "https://www.nice.fr/uploads/media/paysage/0001/03/Lascaris.JPG",  
  "criticReview": [  
    {  
      "language": "fr",  
      "reviews": [  
        {  
          "article": "Beau palais baroque qui contient des instruments de musique vari\u00e9s dont une harpe-piano \u00e9tonnante, et des portraits tr\u00e8s beaux. A voir, surtout pour l'escalier et la d\u00e9coration des salles.",  
          "origin": "Office du tourisme Nice",  
          "ratingValue": 9,  
          "starRating": 5  
        }  
      ]  
    },  
    {  
      "language": "en",  
      "reviews": [  
        {  
          "article": "Beautiful baroque palace which contains various gastronomical instruments including an astonishing harp-piano, and very beautiful portraits. To see, especially for the staircase and the decoration of the rooms.",  
          "origin": "Trip Advisor",  
          "ratingValue": 8,  
          "starRating": 4  
        }  
      ]  
    }  
  ],  
  "ratingValue": 8.5,  
  "starRatingDetailed": {  
    "5": 92,  
    "4": 6,  
    "3": 2,  
    "2": 0,  
    "1": 0  
  },  
  "audience": [  
    "allPublic"  
  ],  
  "wheelChairAccessible": false,  
  "maximumAttendeeCapacity": 25,  
  "isAccessibleForFree": false,  
  "tripPriceFrom": 0.0,  
  "tripPriceTo": 10.0,  
  "priceSpecification": [  
    {  
      "audience": [  
        "adult"  
      ],  
      "price": 10.0  
    },  
    {  
      "audience": [  
        "senior"  
      ],  
      "price": 5.0  
    },  
    {  
      "audience": [  
        "children"  
      ],  
      "eligibleQuantity": 5,  
      "price": 0.0  
    }  
  ],  
  "paymentAccepted": [  
    "Cash",  
    "CreditCard"  
  ],  
  "currencyAccepted": [  
    "EUR",  
    "USD"  
  ],  
  "routeType": [  
    "tram",  
    "subway",  
    "bus"  
  ],  
  "transportServices": [  
    "taxi"  
  ],  
  "electricTransport": [  
    "electricBicycle",  
    "electricMotorBike"  
  ],  
  "@context": [  
    "https://smart-data-models.github.io/data-models/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### TouristTrip NGSI-v2规范化示例  
下面是一个以JSON-LD格式规范化的TouristTrip的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "touristTrip.1",  
  "type": "TouristTrip",  
  "name": {  
    "type": "Text",  
    "value": "Descubre Conil"  
  },  
  "description": [  
    {  
      "type": "Text",  
      "value": "Viaje para conocer el encanto y los atractivos turísticos de Conil de la Frontera."  
    }  
  ],  
  "touristType": {  
    "type": "StructuredValue",  
    "value": [  
      "FAMILY TOURISM",  
      "WATER SPORTS TOURISM",  
      "FOOD TOURISM",  
      "BEACH AND SUN TOURISM"  
    ]  
  },  
  "url": {  
    "type": "StructuredValue",  
    "value": [  
      "https://www.spain.info/es/que-quieres/ciudades-pueblos/otros-destinos/conil_de_la_frontera.html"  
    ]  
  },  
  "image": {  
    "type": "Text",  
    "value": "http://www.turismo.conil.org/PortalTurismo/DocTurismo.nsf/voTodosPorIdiomaUNID/4AC02453BEE8F5CDC125750400315F48/$FILE/IMGP2024.JPG"  
  },  
  "sameAs": {  
    "type": "Text",  
    "value": "https://inventrip.com/conil/trip/1907"  
  },  
  "video": {  
    "type": "Text",  
    "value": "https://www.youtube.com/watch?v=IhnvlIzxPLg"  
  },  
  "alternateName": {  
    "value": "Palais Lascaris"  
  },  
  "seeAlso": {  
    "value": "https://www.nice.fr/fr/culture/musees-et-galeries/palais-lascaris-le-palais"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        43.6976766,  
        7.2772458  
      ]  
    }  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "streetAddress": "15, rue Droite",  
      "postalCode": "06000",  
      "addressLocality": "Nice",  
      "addressCountry": "France",  
      "addressRegion": "Marseille Nice Avignon Aix - (06)"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Vieux Nice"  
  },  
  "dateLastReported": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z"  
  },  
  "itinerary": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "position": 1,  
        "name": "Cours Saleya",  
        "streetAddress": [  
          "Cours Saleya",  
          "06300 Nice"  
        ],  
        "image": [  
          "https://www.nicetourisme.com/nice/1507-marche-aux-fruits-legumes-et-maree-du-cours-saleya"  
        ]  
      },  
      {  
        "position": 2,  
        "name": "Centre du patrimoine",  
        "streetAddress": [  
          "14 rue Jules Gilly",  
          "06300 Nice"  
        ],  
        "image": [  
          "https: //nice.city-life.fr/Services/Nice/Services-touristiques/768/Centre-du-Patrimoine?lang=fr"  
        ]  
      },  
      {  
        "position": 3,  
        "name": "Place du jÃ©sus",  
        "streetAddress": [  
          "Rue du jÃ©sus",  
          "06300 Nice"  
        ],  
        "image": [  
          "https: //fr.wikipedia.org/wiki/%C3%89glise_Saint-Jacques-le-Majeur_de_Nice"  
        ]  
      },  
      {  
        "position": 4,  
        "name": "Palais Lascaris",  
        "streetAddress": [  
          "15, rue Droite",  
          "06300 Nice"  
        ],  
        "image": [  
          "https: //upload.wikimedia.org/wikipedia/commons/e/ed/Lascaris2.JPG"  
        ]  
      }  
    ]  
  },  
  "contactPoint": {  
    "type": "StructuredValue",  
    "value": {  
      "telephone": "+33(0)4 93 62 72 40",  
      "contactType": "customer reception",  
      "email": "palais.lascaris@ville-nice.fr",  
      "availableLanguage": [  
        "English",  
        "French"  
      ]  
    }  
  },  
  "accessPlan": {  
    "type": "Text",  
    "value": "https://www.google.fr/maps/place/Mus%C3%A9e+du+Palais+Lascaris/@43.6976805,7.2750571,17z/data=!3m1!4b1!4m5!3m4!1s0x12cddabca1950653:0x8d425022ef476dde!8m2!3d43.6976766!4d7.2772458?hl=fr"  
  },  
  "category": {  
    "type": "StructuredValue",  
    "value": [  
      "museum"  
    ]  
  },  
  "subCategory": {  
    "type": "StructuredValue",  
    "value": [  
      "art",  
      "decorativeArts",  
      "history"  
    ]  
  },  
  "thematic": {  
    "type": "StructuredValue",  
    "value": [  
      "culture",  
      "museum",  
      "instrument",  
      "music",  
      "monument"  
    ]  
  },  
  "locationName": {  
    "type": "Text",  
    "value": "Palais Lascaris"  
  },  
  "title": {  
    "type": "Text",  
    "value": "Visite du MusÃ©e du Palais Lascaris"  
  },  
  "slogan": {  
    "type": "Text",  
    "value": "Une demeure aristocratique joyau du baroque et une remarquable collection d instruments de musiques anciens."  
  },  
  "language": {  
    "type": "StructuredValue",  
    "value": [  
      "french",  
      "english",  
      "spanish",  
      "german"  
    ]  
  },  
  "superTrip": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Trip:Trip:MNCA-TRIP-NCE-VISTE-DES-MUSEES-NICE"  
  },  
  "tripStatus": {  
    "type": "Text",  
    "value": "opened"  
  },  
  "startDate": {  
    "type": "DateTime",  
    "value": "01-01-2021T00:00:00Z"  
  },  
  "endDate": {  
    "type": "DateTime",  
    "value": "31-12-2021T00:00:00Z"  
  },  
  "openingHoursSpecification": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "dayOfWeek": "Monday",  
        "opens": "10:00:00",  
        "closes": "18:00:00"  
      },  
      {  
        "dayOfWeek": "Wednesday",  
        "opens": "10:00:00",  
        "closes": "18:00:00"  
      },  
      {  
        "dayOfWeek": "Thursday",  
        "opens": "10:00:00",  
        "closes": "18:00:00"  
      },  
      {  
        "dayOfWeek": "Friday",  
        "opens": "10:00:00",  
        "closes": "18:00:00"  
      },  
      {  
        "dayOfWeek": "Saturday",  
        "opens": "10:00:00",  
        "closes": "18:00:00"  
      },  
      {  
        "dayOfWeek": "Sunday",  
        "opens": "10:00:00",  
        "closes": "18:00:00"  
      }  
    ]  
  },  
  "duration": {  
    "type": "Number",  
    "value": 1.25  
  },  
  "pitch": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "language": "fr",  
        "article": "Dans une ruelle troite ce palais baroque allie richesse ornementale et simplicitÃ©. Son escalier avec ses fresques est somptueux mÃªme si ses dimensions sont somme toute rÃ©duites. Lâambiance est chaleureuse avec des plafonds bas ,des piÃ¨ces Ã  lâÃ©chelle humaine qui en font un lieu intime propice Ã  la dÃ©couverte de la collection dâinstruments de musique. Ne manquez pas dâobserver les portes de communication."  
      },  
      {  
        "language": "en",  
        "article": "In a narrow alley, this baroque palace combines ornamental richness and simplicity. Its staircase with its frescoes is sumptuous even if its dimensions are all in all small. The atmosphere is warm with low ceilings, rooms on a human scale that make it an intimate place conducive to discovering the collection of gastronomieal instruments. Do not miss to observe the communication doors."  
      }  
    ]  
  },  
  "webSite": {  
    "type": "Text",  
    "value": "http://www.palais-lascaris.com"  
  },  
  "contentURL": {  
    "type": "Text",  
    "value": "https://www.nice.fr/uploads/media/paysage/0001/03/Lascaris.JPG"  
  },  
  "criticReview": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "language": "fr",  
        "reviews": [  
          {  
            "article": "Beau palais baroque qui contient des instruments de musique vari\u00e9s dont une harpe-piano \u00e9tonnante, et des portraits tr\u00e8s beaux. A voir, surtout pour l'escalier et la d\u00e9coration des salles.",  
            "origin": "Office du tourisme Nice",  
            "ratingValue": 9,  
            "starRating": 5  
          }  
        ]  
      },  
      {  
        "language": "en",  
        "reviews": [  
          {  
            "article": "Beautiful baroque palace which contains various gastronomical instruments including an astonishing harp-piano, and very beautiful portraits. To see, especially for the staircase and the decoration of the rooms.",  
            "origin": "Trip Advisor",  
            "ratingValue": 8,  
            "starRating": 4  
          }  
        ]  
      }  
    ]  
  },  
  "ratingValue": {  
    "type": "Number",  
    "value": 8.5  
  },  
  "starRatingDetailed": {  
    "type": "StructuredValue",  
    "value": {  
      "5": 92,  
      "4": 6,  
      "3": 2,  
      "2": 0,  
      "1": 0  
    }  
  },  
  "audience": {  
    "type": "StructuredValue",  
    "value": [  
      "AllPublic"  
    ]  
  },  
  "wheelChairAccessible": {  
    "type": "Boolean",  
    "value": false  
  },  
  "maximumAttendeeCapacity": {  
    "type": "Number",  
    "value": 25  
  },  
  "isAccessibleForFree": {  
    "type": "Boolean",  
    "value": false  
  },  
  "tripPriceFrom": {  
    "type": "Number",  
    "value": 0.00  
  },  
  "tripPriceTo": {  
    "type": "Number",  
    "value": 10.00  
  },  
  "priceSpecification": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "audience": "adult",  
        "price": 10.00  
      },  
      {  
        "audience": "senior",  
        "price": 5.00  
      },  
      {  
        "audience": "children",  
        "eligibleQuantity": 5,  
        "price": 0.00  
      }  
    ]  
  },  
  "paymentAccepted": {  
    "type": "StructuredValue",  
    "value": [  
      "Cash",  
      "CreditCard"  
    ]  
  },  
  "currencyAccepted": {  
    "type": "StructuredValue",  
    "value": [  
      "EUR",  
      "USD"  
    ]  
  },  
  "routeType": {  
    "type": "StructuredValue",  
    "value": [  
      "tram",  
      "subway",  
      "bus"  
    ]  
  },  
  "transportServices": {  
    "type": "StructuredValue",  
    "value": [  
      "taxi"  
    ]  
  },  
  "electricTransport": {  
    "type": "StructuredValue",  
    "value": [  
      "electricBicycle",  
      "electricMotorBike"  
    ]  
  }  
}  
```  
</details>  
#### TouristTrip NGSI-LD关键值示例  
这里是一个以JSON-LD格式作为key-values的TouristTrip的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi:touristTrip:1",  
  "type": "TouristTrip",  
  "name": "Musee du Palais Lascaris",  
  "alternateName": "Palais Lascaris",  
  "description": "Le palais Lascaris est une ancienne demeure aristocratique de Nice datant de la premiere moiti du XVII sicle, aujourd'hui un musee des instruments de musique anciens",  
  "touristType": [  
    "FAMILY TOURISM",  
    "WATER SPORTS TOURISM",  
    "FOOD TOURISM",  
    "BEACH AND SUN TOURISM"  
  ],  
  "url": [  
    "https://www.spain.info/es/que-quieres/ciudades-pueblos/otros-destinos/conil_de_la_frontera.html"  
  ],  
  "image": "http://www.turismo.conil.org/PortalTurismo/DocTurismo.nsf/voTodosPorIdiomaUNID/4AC02453BEE8F5CDC125750400315F48/$FILE/IMGP2024.JPG",  
  "sameAs": "https://inventrip.com/conil/trip/1907",  
  "video": "https://www.youtube.com/watch?v=IhnvlIzxPLg",  
  "seeAlso": "https://www.nice.fr/fr/culture/musees-et-galeries/palais-lascaris-le-palais",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.6976766,  
      7.2772458  
    ]  
  },  
  "address": {  
    "streetAddress": "15, rue Droite",  
    "postalCode": "06000",  
    "adressLocality": "Nice",  
    "addressCountry": "France",  
    "adressRegion": "Marseille Nice Avignon Aix - (06)"  
  },  
  "areaServed": "Vieux Nice",  
  "dateLastReported": "2020-03-17T08:45:00Z",  
  "itinerary": [  
    {  
      "position": 1,  
      "name": "Cours Saleya",  
      "streetAdress": [  
        "Cours Saleya",  
        "06300 Nice"  
      ],  
      "image": [  
        "https://www.nicetourisme.com/nice/1507-marche-aux-fruits-legumes-et-maree-du-cours-saleya"  
      ]  
    },  
    {  
      "position": 2,  
      "name": "Centre du patrimoine",  
      "streetAdress": [  
        "14 rue Jules Gilly",  
        "06300 Nice"  
      ],  
      "image": [  
        "https: //nice.city-life.fr/Services/Nice/Services-touristiques/768/Centre-du-Patrimoine?lang=fr"  
      ]  
    },  
    {  
      "position": 3,  
      "name": "Place du j\u00e9sus",  
      "streetAdress": [  
        "Rue du j\u00e9sus",  
        "06300 Nice"  
      ],  
      "image": [  
        "https: //fr.wikipedia.org/wiki/%C3%89glise_Saint-Jacques-le-Majeur_de_Nice"  
      ]  
    },  
    {  
      "position": 4,  
      "name": "Palais Lascaris",  
      "streetAdress": [  
        "15, rue Droite",  
        "06300 Nice"  
      ],  
      "image": [  
        "https: //upload.wikimedia.org/wikipedia/commons/e/ed/Lascaris2.JPG"  
      ]  
    }  
  ],  
  "contactPoint": {  
    "telephone": "+33(0)4 93 62 72 40",  
    "contactType": "customer reception",  
    "email": "palais.lascaris@ville-nice.fr",  
    "availableLanguage": [  
      "English",  
      "French"  
    ]  
  },  
  "accessPlan": "https://www.google.fr/maps/place/Mus%C3%A9e+du+Palais+Lascaris/@43.6976805,7.2750571,17z/data=!3m1!4b1!4m5!3m4!1s0x12cddabca1950653:0x8d425022ef476dde!8m2!3d43.6976766!4d7.2772458?hl=fr",  
  "category": [  
    "museum"  
  ],  
  "subCategory": [  
    "art",  
    "decorativeArts",  
    "history"  
  ],  
  "thematic": [  
    "culture",  
    "museum",  
    "instrument",  
    "music",  
    "monument"  
  ],  
  "locationName": "Palais Lascaris",  
  "title": "Visite du Mus\u00e9e du Palais Lascaris",  
  "slogan": "Une demeure aristocratique joyau du baroque et une remarquable collection d instruments de musiques anciens.",  
  "language": [  
    "french",  
    "english",  
    "spanish",  
    "german"  
  ],  
  "superTrip": "urn:ngsi-ld:Trip:Trip:MNCA-TRIP-NCE-VISTE-DES-MUSEES-NICE",  
  "tripStatus": "opened",  
  "startDate": "2021-01-01T00:00:00Z",  
  "endDate": "2021-12-31T00:00:00Z",  
  "openingHoursSpecification": [  
    {  
      "dayOfWeek": "Monday",  
      "opens": "10:00:00",  
      "closes": "18:00:00"  
    },  
    {  
      "dayOfWeek": "Wednesday",  
      "opens": "10:00:00",  
      "closes": "18:00:00"  
    },  
    {  
      "dayOfWeek": "Thursday",  
      "opens": "10:00:00",  
      "closes": "18:00:00"  
    },  
    {  
      "dayOfWeek": "Friday",  
      "opens": "10:00:00",  
      "closes": "18:00:00"  
    },  
    {  
      "dayOfWeek": "Saturday",  
      "opens": "10:00:00",  
      "closes": "18:00:00"  
    },  
    {  
      "dayOfWeek": "Sunday",  
      "opens": "10:00:00",  
      "closes": "18:00:00"  
    }  
  ],  
  "duration": 1.25,  
  "pitch": {  
    "fr": {  
      "value": {  
        "article": "Dans une ruelle \u00e9troite ce palais baroque allie richesse ornementale et simplicit\u00e9. Son escalier avec ses fresques est somptueux m\u00eame si ses dimensions sont somme toute r\u00e9duites. L\u2019ambiance est chaleureuse avec des plafonds bas ,des pi\u00e8ces \u00e0 l\u2019\u00e9chelle humaine qui en font un lieu intime propice \u00e0 la d\u00e9couverte de la collection d\u2019instruments de musique. Ne manquez pas d\u2019observer les portes de communication."  
      }  
    },  
    "en": {  
      "value": {  
        "article": "In a narrow alley, this baroque palace combines ornamental richness and simplicity. Its staircase with its frescoes is sumptuous even if its dimensions are all in all small. The atmosphere is warm with low ceilings, rooms on a human scale that make it an intimate place conducive to discovering the collection of gastronomieal instruments. Do not miss to observe the communication doors."  
      }  
    }  
  },  
  "webSite": "http://www.palais-lascaris.com",  
  "contentURL": "https://www.nice.fr/uploads/media/paysage/0001/03/Lascaris.JPG",  
  "criticReview": [  
    {  
      "language": "fr",  
      "reviews": [  
        {  
          "article": "Beau palais baroque qui contient des instruments de musique vari\u00e9s dont une harpe-piano \u00e9tonnante, et des portraits tr\u00e8s beaux. A voir, surtout pour l'escalier et la d\u00e9coration des salles.",  
          "origin": "Office du tourisme Nice",  
          "ratingValue": 9,  
          "starRating": 5  
        }  
      ]  
    },  
    {  
      "language": "en",  
      "reviews": [  
        {  
          "article": "Beautiful baroque palace which contains various gastronomical instruments including an astonishing harp-piano, and very beautiful portraits. To see, especially for the staircase and the decoration of the rooms.",  
          "origin": "Trip Advisor",  
          "ratingValue": 8,  
          "starRating": 4  
        }  
      ]  
    }  
  ],  
  "ratingValue": 8.5,  
  "starRatingDetailed": {  
    "5": 92,  
    "4": 6,  
    "3": 2,  
    "2": 0,  
    "1": 0  
  },  
  "audience": [  
    "allPublic"  
  ],  
  "wheelChairAccessible": false,  
  "maximumAttendeeCapacity": 25,  
  "isAccessibleForFree": false,  
  "tripPriceFrom": 0.0,  
  "tripPriceTo": 10.0,  
  "priceSpecification": [  
    {  
      "audience": [  
        "adult"  
      ],  
      "price": 10.0  
    },  
    {  
      "audience": [  
        "senior"  
      ],  
      "price": 5.0  
    },  
    {  
      "audience": [  
        "children"  
      ],  
      "eligibleQuantity": 5,  
      "price": 0.0  
    }  
  ],  
  "paymentAccepted": [  
    "Cash",  
    "CreditCard"  
  ],  
  "currencyAccepted": [  
    "EUR",  
    "USD"  
  ],  
  "routeType": [  
    "tram",  
    "subway",  
    "bus"  
  ],  
  "transportServices": [  
    "taxi"  
  ],  
  "electricTransport": [  
    "electricBicycle",  
    "electricMotorBike"  
  ],  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.TourismDestinations/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### TouristTrip NGSI-LD规范化示例  
下面是一个以JSON-LD格式规范化的TouristTrip的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi:touristTrip:1",  
    "type": "TouristTrip",  
    "accessPlan": {  
        "type": "Property",  
        "value": "https://www.google.fr/maps/place/Mus%C3%A9e+du+Palais+Lascaris/@43.6976805,7.2750571,17z/data=!3m1!4b1!4m5!3m4!1s0x12cddabca1950653:0x8d425022ef476dde!8m2!3d43.6976766!4d7.2772458?hl=fr"  
    },  
    "address": {  
        "type": "Property",  
        "value": {  
            "streetAddress": "15, rue Droite",  
            "postalCode": "06000",  
            "addressLocality": "Nice",  
            "addressCountry": "France",  
            "addressRegion": "Marseille Nice Avignon Aix - (06)"  
        }  
    },  
    "alternateName": {  
        "type": "Property",  
        "value": "Palais Lascaris"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Vieux Nice"  
    },  
    "audience": {  
        "type": "Property",  
        "value": [  
            "AllPublic"  
        ]  
    },  
    "category": {  
        "type": "Property",  
        "value": [  
            "museum"  
        ]  
    },  
    "contactPoint": {  
        "type": "Property",  
        "value": {  
            "telephone": "+33(0)4 93 62 72 40",  
            "contactType": "customer reception",  
            "email": "palais.lascaris@ville-nice.fr",  
            "availableLanguage": [  
                "English",  
                "French"  
            ]  
        }  
    },  
    "contenteURL": {  
        "type": "Property",  
        "value": "https://www.nice.fr/uploads/media/paysage/0001/03/Lascaris.JPG"  
    },  
    "criticReview": {  
        "type": "Property",  
        "value": [  
            {  
                "language": "fr",  
                "reviews": [  
                    {  
                        "article": "Beau palais baroque qui contient des instruments de musique vari\u00e9s dont une harpe-piano \u00e9tonnante, et des portraits tr\u00e8s beaux. A voir, surtout pour l'escalier et la d\u00e9coration des salles.",  
                        "origin": "Office du tourisme Nice",  
                        "ratingValue": 9,  
                        "starRating": 5  
                    }  
                ]  
            },  
            {  
                "language": "en",  
                "reviews": [  
                    {  
                        "article": "Beautiful baroque palace which contains various gastronomical instruments including an astonishing harp-piano, and very beautiful portraits. To see, especially for the staircase and the decoration of the rooms.",  
                        "origin": "Trip Advisor",  
                        "ratingValue": 8,  
                        "starRating": 4  
                    }  
                ]  
            }  
        ]  
    },  
    "currencyAccepted": {  
        "type": "Property",  
        "value": [  
            "EUR",  
            "USD"  
        ]  
    },  
    "dateLastReported": {  
        "type": "DateTime",  
        "value": "2020-03-17T08:45:00Z",  
        "metadata": {  
            "TimeInstant": {  
                "type": "Text",  
                "value": "2020-03-17TT08:45:00Z"  
            }  
        }  
    },  
    "description": [  
        {  
            "type": "Property",  
            "value": "Viaje para conocer el encanto y los atractivos turisticos de Conil de la Frontera."  
        }  
    ],  
    "duration": {  
        "type": "Property",  
        "value": 1.25  
    },  
    "electricTransport": {  
        "type": "Property",  
        "value": [  
            "electricBicycle",  
            "electricMotorBike"  
        ]  
    },  
    "endDate": {  
        "type": "DateTime",  
        "value": "-12-31"  
    },  
    "image": {  
        "type": "Property",  
        "value": "http://www.turismo.conil.org/PortalTurismo/DocTurismo.nsf/voTodosPorIdiomaUNID/4AC02453BEE8F5CDC125750400315F48/$FILE/IMGP2024.JPG"  
    },  
    "isAccessibleForFree": {  
        "type": "Property",  
        "value": false  
    },  
    "itinerary": {  
        "type": "Property",  
        "value": [  
            {  
                "position": 1,  
                "name": "Cours Saleya",  
                "streetAddress": [  
                    "Cours Saleya",  
                    "06300 Nice"  
                ],  
                "image": [  
                    "https://www.nicetourisme.com/nice/1507-marche-aux-fruits-legumes-et-maree-du-cours-saleya"  
                ]  
            },  
            {  
                "position": 2,  
                "name": "Centre du patrimoine",  
                "streetAddress": [  
                    "14 rue Jules Gilly",  
                    "06300 Nice"  
                ],  
                "image": [  
                    "https: //nice.city-life.fr/Services/Nice/Services-touristiques/768/Centre-du-Patrimoine?lang=fr"  
                ]  
            },  
            {  
                "position": 3,  
                "name": "Place du j\u00c3\u00a9sus",  
                "streetAddress": [  
                    "Rue du j\u00c3\u00a9sus",  
                    "06300 Nice"  
                ],  
                "image": [  
                    "https: //fr.wikipedia.org/wiki/%C3%89glise_Saint-Jacques-le-Majeur_de_Nice"  
                ]  
            },  
            {  
                "position": 4,  
                "name": "Palais Lascaris",  
                "streetAddress": [  
                    "15, rue Droite",  
                    "06300 Nice"  
                ],  
                "image": [  
                    "https: //upload.wikimedia.org/wikipedia/commons/e/ed/Lascaris2.JPG"  
                ]  
            }  
        ]  
    },  
    "language": {  
        "type": "Property",  
        "value": [  
            "french",  
            "english",  
            "spanish",  
            "german"  
        ]  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "point",  
            "coordinates": [  
                43.6976766,  
                7.2772458  
            ]  
        }  
    },  
    "locationName": {  
        "type": "Property",  
        "value": "Palais Lascaris"  
    },  
    "maximumAttendeeCapacity": {  
        "type": "Property",  
        "value": 25  
    },  
    "name": {  
        "type": "Property",  
        "value": "Descubre Conil"  
    },  
    "openingHoursSpecification": [  
        {  
            "dayOfWeek": "Monday",  
            "opens": "10:00:00",  
            "closes": "18:00:00"  
        },  
        {  
            "dayOfWeek": "Wednesday",  
            "opens": "10:00:00",  
            "closes": "18:00:00"  
        },  
        {  
            "dayOfWeek": "Thursday",  
            "opens": "10:00:00",  
            "closes": "18:00:00"  
        },  
        {  
            "dayOfWeek": "Friday",  
            "opens": "10:00:00",  
            "closes": "18:00:00"  
        },  
        {  
            "dayOfWeek": "Saturday",  
            "opens": "10:00:00",  
            "closes": "18:00:00"  
        },  
        {  
            "dayOfWeek": "Sunday",  
            "opens": "10:00:00",  
            "closes": "18:00:00"  
        }  
    ],  
    "paymentAccepted": {  
        "type": "Property",  
        "value": [  
            "Cash",  
            "CreditCard"  
        ]  
    },  
    "pitch": {  
        "type": "Property",  
        "value": [  
            {  
                "language": "fr",  
                "article": "Dans une ruelle \u00c3\u00a9troite ce palais baroque allie richesse ornementale et simplicit\u00c3\u00a9. Son escalier avec ses fresques est somptueux m\u00c3\u00aame si ses dimensions sont somme toute r\u00c3\u00a9duites. L\u00e2\u0080\u0099ambiance est chaleureuse avec des plafonds bas ,des pi\u00c3\u00a8ces \u00c3\u00a0 l\u00e2\u0080\u0099\u00c3\u00a9chelle humaine qui en font un lieu intime propice \u00c3\u00a0 la d\u00c3\u00a9couverte de la collection d\u00e2\u0080\u0099instruments de musique. Ne manquez pas d\u00e2\u0080\u0099observer les portes de communication."  
            },  
            {  
                "language": "en",  
                "article": "In a narrow alley, this baroque palace combines ornamental richness and simplicity. Its staircase with its frescoes is sumptuous even if its dimensions are all in all small. The atmosphere is warm with low ceilings, rooms on a human scale that make it an intimate place conducive to discovering the collection of gastronomieal instruments. Do not miss to observe the communication doors."  
            }  
        ]  
    },  
    "priceSpecification": {  
        "type": "Property",  
        "value": [  
            {  
                "audience": "adult",  
                "price": 10.0  
            },  
            {  
                "audience": "senior",  
                "price": 5.0  
            },  
            {  
                "audience": "children",  
                "eligibleQuantity": 5,  
                "price": 0.0  
            }  
        ]  
    },  
    "ratingValue": {  
        "type": "Property",  
        "value": 8.5  
    },  
    "routeType": {  
        "type": "Property",  
        "value": [  
            "tram",  
            "subway",  
            "bus"  
        ]  
    },  
    "sameAs": {  
        "type": "Property",  
        "value": "https://inventrip.com/conil/trip/1907"  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": "https://www.nice.fr/fr/culture/musees-et-galeries/palais-lascaris-le-palais"  
    },  
    "slogan": {  
        "type": "Property",  
        "value": "Une demeure aristocratique joyau du baroque et une remarquable collection d instruments de musiques anciens."  
    },  
    "starRatingDetailed": {  
        "type": "Property",  
        "value": {  
            "5": 92,  
            "4": 6,  
            "3": 2,  
            "2": 0,  
            "1": 0  
        }  
    },  
    "startDate": {  
        "type": "DateTime",  
        "value": "-01-01"  
    },  
    "subCategory": {  
        "type": "Property",  
        "value": [  
            "art",  
            "decorativeArts",  
            "history"  
        ]  
    },  
    "superTrip": {  
        "type": "Property",  
        "value": "urn:ngsi-ld:Trip:Trip:MNCA-TRIP-NCE-VISTE-DES-MUSEES-NICE"  
    },  
    "thematic": {  
        "type": "Property",  
        "value": [  
            "culture",  
            "museum",  
            "instrument",  
            "music",  
            "monument"  
        ]  
    },  
    "title": {  
        "type": "Property",  
        "value": "Visite du Mus\u00c3\u00a9e du Palais Lascaris"  
    },  
    "touristType": {  
        "type": "Property",  
        "value": [  
            "FAMILY TOURISM",  
            "WATER SPORTS TOURISM",  
            "FOOD TOURISM",  
            "BEACH AND SUN TOURISM"  
        ]  
    },  
    "transportServices": {  
        "type": "Property",  
        "value": [  
            "taxi"  
        ]  
    },  
    "tripPriceFrom": {  
        "type": "Property",  
        "value": 0.0  
    },  
    "tripPriceTo": {  
        "type": "Property",  
        "value": 10.0  
    },  
    "tripStatus": {  
        "type": "Property",  
        "value": "opened"  
    },  
    "url": {  
        "type": "Property",  
        "value": [  
            "https://www.spain.info/es/que-quieres/ciudades-pueblos/otros-destinos/conil_de_la_frontera.html"  
        ]  
    },  
    "video": {  
        "type": "Property",  
        "value": "https://www.youtube.com/watch?v=IhnvlIzxPLg"  
    },  
    "webSite": {  
        "type": "Property",  
        "value": "http://www.palais-lascaris.com"  
    },  
    "wheelChairAccessible": {  
        "type": "Property",  
        "value": false  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
