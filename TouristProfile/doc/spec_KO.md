<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

===========
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `ageRange[object]`: 프로파일링 대상자의 연령 범위  
	- `sortingOrder[array]`: ageRange에 대한 다양한 연령대의 정렬된 집합입니다. OrderedSet: '0-1, 2-5, 6-11, 12-17, 18-24, 25-29, 30-34, 35-39, 40-44, 45-49, 50-54, 55-59, 60-64, 65+'    
- `alternateName[string]`: 이 항목의 대체 이름  
	- `sortingOrder[array]`: 평균 일일 숙박 및 보드 지출에 대한 금액 범위의 주문 세트입니다. OrderedSet: '0~24유로, 25~49유로, 50~74유로, 75~99유로, 100~149유로, 150~199유로, 200~249유로, 250~299유로, 300~399유로, 400~499유로, 500~599유로, 600+유로'    
- `avgDailyExpenditure[object]`: 숙박 시설에서 청구하는 일일 평균 금액의 범위  
	- `sortingOrder[array]`: 평균 일일 지출에 대한 금액 범위의 주문 세트입니다. OrderedSet: '0~24유로, 25~49유로, 50~74유로, 75~99유로, 100~149유로, 150~199유로, 200~249유로, 250~299유로, 300~399유로, 400~499유로, 500~599유로, 600유로 이상'    
- `avgDailyExtraExpenditure[object]`: 숙박 시설에서 추가 개념으로 청구하는 일일 평균 금액의 범위  
	- `sortingOrder[array]`: 평균 일일 추가 지출에 대한 금액 범위의 주문 세트입니다. OrderedSet: '0~24유로, 25~49유로, 50~74유로, 75~99유로, 100~149유로, 150~199유로, 200~249유로, 250~299유로, 300~399유로, 400~499유로, 500~599유로, 600유로 이상'    
- `board[string]`: 일반적인 보드 유형이 예약되어 있습니다. Enum:'RO, BB, HB, FB, AI'  
	- `sortingOrder[array]`: 숙박 객실 수량의 주문된 간격 집합입니다. OrderedSet: '0 - 24 매우 작음, 25 - 100 작음, 101 - 300 중간, 301 - 700 대형, 701 - 1200 매우 대형, 1201+ 대형'    
- `lodgingType[string]`: 일반적인 숙박 유형입니다. 향후 UNE178506을 참조할 수 있습니다. 열거형:'호텔, 리조트, 호스텔, 모텔, B&B, 아파트호텔, 롯지'  
	- `sortingOrder[array]`: 예약 리드타임에 대한 일수 범위의 주문 세트입니다. OrderedSet: '1~7일, 8~14일, 15~30일, 31~60일, 61~90일, 91~120일, 121~240일, 241~365일, 366일 이상'    
- `roomOfStayType[string]`: 예약한 숙박 객실의 일반적인 유형입니다. 열거형:'아파트, 방갈로, 스튜디오, 싱글, 더블, 패밀리, 주니어 스위트, 시니어/이그제큐티브 스위트, 로얄/프레지덴셜 스위트'  
	- `sortingOrder[array]`: 숙박 기간에 대한 숙박 기간 범위의 주문 세트입니다. 주문 세트: '1박, 2박~4박, 5~7박, 8박~14박, 15박~21박, 22박 이상'    
- `totalAccommodationAndBoardExpenditure[object]`: 숙박 시설에서 숙박 및 보드 개념으로 청구하는 총 금액의 범위  
	- `sortingOrder[array]`: 총 숙박 및 보드 지출에 대한 금액 범위의 주문 세트입니다. OrderedSet: '0~249유로, 250~499유로, 500~749유로, 750~999유로, 1000~1499유로, 1500~1999유로, 2000~2999유로, 3000~3999유로, 4000~4999유로, 5000+유로'    
- `totalExpenditure[object]`: 숙박 시설에서 청구하는 총 금액의 범위  
	- `sortingOrder[array]`: 총지출에 대한 금액 범위의 정렬된 집합입니다. OrderedSet: '0~249유로, 250~499유로, 500~749유로, 750~999유로, 1000~1499유로, 1500~1999유로, 2000~2999유로, 3000~3999유로, 4000~4999유로, 5000+유로'    
- `totalExtraExpenditure[object]`: 숙박 시설에서 추가 개념으로 청구하는 총 금액의 범위  
	- `sortingOrder[array]`: 총추가지출에 대한 금액 범위의 주문 세트입니다. OrderedSet: '0~249유로, 250~499유로, 500~749유로, 750~999유로, 1000~1499유로, 1500~1999유로, 2000~2999유로, 3000~3999유로, 4000~4999유로, 5000+유로'    
- `travelPartyComposition[string]`: 성인과 어린이 수를 기준으로 한 여행 일행의 구성입니다. Enum:'싱글, 편부모, 가족, 커플, 친구/친척'  
<!-- 35-RequiredProperties -->

- `id`  
<!-- 40-RequiredProperties -->

<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

TouristProfile:    
  description: 'Description of a tourist profile based on the characteristics of a person, trip, choice of stay and spending while in destination.'    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
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
    ageRange:    
      description: Age range of the person profiled    
      properties:    
        range:    
          description: Value of ageRange. It uses the ranges defined by sortingOrder    
          type: string    
          x-ngsi:    
            type: Property    
        sortingOrder:    
          description: 'Ordered set of different age groups for ageRange. OrderedSet: ''0-1, 2-5, 6-11, 12-17, 18-24, 25-29, 30-34, 35-39, 40-44, 45-49, 50-54, 55-59, 60-64, 65+'''    
          items:    
            type: string    
          type: array    
          x-ngsi:    
            type: Property    
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
      description: Range of avg daily amount of money invoiced by the lodging establishment in accommodation and board concepts    
      properties:    
        range:    
          description: Value of avgDailyAccommodationAndBoardExpenditure. It uses the ranges defined by sortingOrder    
          type: string    
          x-ngsi:    
            type: Property    
        sortingOrder:    
          description: 'Ordered set of range of money amounts for avgDailyAccommodationAndBoardExpenditure. OrderedSet: ''0 to 24 €, 25 to 49 €, 50 to 74 €, 75 to 99 €, 100 to 149 €, 150 to 199 €, 200 to 249 €, 250 to 299 €, 300 to 399 €, 400 to 499 €, 500 to 599 €, 600+ €'''    
          items:    
            type: string    
          type: array    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    avgDailyExpenditure:    
      description: Range of avg daily amount of money invoiced by the lodging establishment    
      properties:    
        range:    
          description: Value of avgDailyExpenditure. It uses the ranges defined by sortingOrder    
          type: string    
          x-ngsi:    
            type: Property    
        sortingOrder:    
          description: 'Ordered set of range of money amounts for avgDailyExpenditure. OrderedSet: ''0 to 24 €, 25 to 49 €, 50 to 74 €, 75 to 99 €, 100 to 149 €, 150 to 199 €, 200 to 249 €, 250 to 299 €, 300 to 399 €, 400 to 499 €, 500 to 599 €, 600+ €'''    
          items:    
            type: string    
          type: array    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    avgDailyExtraExpenditure:    
      description: Range of avg daily amount of money invoiced by the lodging establishment in extra concepts    
      properties:    
        range:    
          description: Value of avgDailyExtraExpenditure. It uses the ranges defined by sortingOrder    
          type: string    
          x-ngsi:    
            type: Property    
        sortingOrder:    
          description: 'Ordered set of range of money amounts for avgDailyExtraExpenditure. OrderedSet: ''0 to 24 €, 25 to 49 €, 50 to 74 €, 75 to 99 €, 100 to 149 €, 150 to 199 €, 200 to 249 €, 250 to 299 €, 300 to 399 €, 400 to 499 €, 500 to 599 €, 600+ €'''    
          items:    
            type: string    
          type: array    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    board:    
      description: 'Usual type of board type reserved. Enum:''RO, BB, HB, FB, AI'''    
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
      description: Channel used by the tourist for the reservation    
      type: string    
      x-ngsi:    
        type: Property    
    country:    
      description: 'Country of nationality - https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2'    
      type: string    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
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
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    gender:    
      description: 'Gender of the person profiled. Enum:''Female, Male'''    
      enum:    
        - Female    
        - Male    
      type: string    
      x-ngsi:    
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
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
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
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
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
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
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
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
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
      x-ngsi:    
        type: GeoProperty    
    lodgingCategory:    
      description: 'Usual category of the lodging. Enum:''1, 1 Superior, 2, 2 Superior, 3, 3 Superior, 4, 4 Superior, 5, 5 Superior'''    
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
      description: Range size in number of rooms of the lodging    
      properties:    
        range:    
          description: Value of lodgingSize. It uses the ranges defined by sortingOrder    
          type: string    
          x-ngsi:    
            type: Property    
        sortingOrder:    
          description: 'Ordered set of intervals of the quantity of rooms for lodgingSize. OrderedSet: ''0 - 24 very small, 25 - 100 small, 101 - 300 medium, 301 - 700 large, 701 - 1200 very large, 1201+ massive'''    
          items:    
            type: string    
          type: array    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    lodgingType:    
      description: 'Usual type of lodging for the stay. Could reference UNE178506 in the future. Enum:''Hotel, Resort, Hostel, Motel, B&B, Aparthotel, Lodge'''    
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
      description: The name of this item    
      type: string    
      x-ngsi:    
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
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    reservationLeadTime:    
      description: Range of days between booking and check-in    
      properties:    
        range:    
          description: Value of reservationLeadTime. It uses the ranges defined by sortingOrder    
          type: string    
          x-ngsi:    
            type: Property    
        sortingOrder:    
          description: 'Ordered set of range of days for reservationLeadTime. OrderedSet: ''1 to 7 days, 8 to 14 days, 15 to 30 days, 31 to 60 days, 61 to 90 days, 91 to 120 days, 121 to 240 days, 241 to 365 days, 366+ days'''    
          items:    
            type: string    
          type: array    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    roomOfStayType:    
      description: 'Usual type of the accommodation room reserved. Enum:''Apartment, Bungalow, Studio, Single, Double, Family, Junior Suite, Senior/Executive Suite, Royal/Presidential Suite'''    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    stayLength:    
      description: Range of number of staying nights    
      properties:    
        range:    
          description: Value of stayLength. It uses the ranges defined by sortingOrder    
          type: string    
          x-ngsi:    
            type: Property    
        sortingOrder:    
          description: 'Ordered set of range of nights for stayLength. OrderedSet: ''1 night, 2 to 4 nights, 5 to 7 nights, 8 to 14 nights, 15 to 21 nights, 22+ nights'''    
          items:    
            type: string    
          type: array    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    totalAccommodationAndBoardExpenditure:    
      description: Range of total amount of money invoiced by the lodging establishment in accommodation and board concepts    
      properties:    
        range:    
          description: Value of totalAccommodationAndBoardExpenditure. It uses the ranges defined by sortingOrder    
          type: string    
          x-ngsi:    
            type: Property    
        sortingOrder:    
          description: 'Ordered set of range of money amounts for totalAccommodationAndBoardExpenditure. OrderedSet: ''0 to 249 €, 250 to 499 €, 500 to 749 €, 750 to 999 €, 1000 to 1499 €, 1500 to 1999 €, 2000 to 2999 €, 3000 to 3999 €, 4000 to 4999 €, 5000+ €'''    
          items:    
            type: string    
          type: array    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    totalExpenditure:    
      description: Range of total amount of money invoiced by the lodging establishment    
      properties:    
        range:    
          description: Value of totalExpenditure. It uses the ranges defined by sortingOrder    
          type: string    
          x-ngsi:    
            type: Property    
        sortingOrder:    
          description: 'Ordered set of range of money amounts for totalExpenditure. OrderedSet: ''0 to 249 €, 250 to 499 €, 500 to 749 €, 750 to 999 €, 1000 to 1499 €, 1500 to 1999 €, 2000 to 2999 €, 3000 to 3999 €, 4000 to 4999 €, 5000+ €'''    
          items:    
            type: string    
          type: array    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    totalExtraExpenditure:    
      description: Range of total amount of money invoiced by the lodging establishment in extra concepts    
      properties:    
        range:    
          description: Value of totalExtraExpenditure. It uses the ranges defined by sortingOrder    
          type: string    
          x-ngsi:    
            type: Property    
        sortingOrder:    
          description: 'Ordered set of range of money amounts for totalExtraExpenditure. OrderedSet: ''0 to 249 €, 250 to 499 €, 500 to 749 €, 750 to 999 €, 1000 to 1499 €, 1500 to 1999 €, 2000 to 2999 €, 3000 to 3999 €, 4000 to 4999 €, 5000+ €'''    
          items:    
            type: string    
          type: array    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    travelPartyComposition:    
      description: 'Composition of the travelling party based on the number of adults and children. Enum:''Single, Single parent, Family, Couple, Friends/Relatives'''    
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
      description: NGSI Entity type. It has to be TouristProfile    
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
  x-model-tags: 'TOURiLab, Sustainability'    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->
<!-- 70-MiddleNotes -->
<!-- /70-MiddleNotes -->
<!-- 80-Examples -->



<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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

<!-- /95-Units -->
<!-- 97-LastFooter -->
---  
