[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティイベント  
==========  
[オープンライセンス](https://github.com/smart-data-models//dataModel.TourismDestinations/blob/master/Event/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述です。**この場所、組織、またはアクションに関連する近日中または過去のイベント.**。  
バージョン: 0.0.1  

## プロパティ一覧  

- `accessPlan`: アイテムへのアクセスプランのテキストまたはリンクです。  - `actor`: 俳優や音楽グループのリスト。  - `address`: 郵送先住所  - `alternateName`: この項目の別称  - `areaServed`: サービスまたは提供品が提供される地理的な地域  - `audience`: 本イベントが関係する一般人の種類。Free text (family, adult, children, teenager, senior, allPublic, ...) の組合せ。Enum:'adult, allPublic, children, family, senior, teenager'.  - `category`: イベントのカテゴリ。特定のコンテキストに柔軟性を保つためのフリーテキストの組み合わせは、初期リポジトリまたはアプリケーションによって必要とされる任意の他の値として、以下に提供されます。Enum:'shopping, gastronomy, museum, religiousWorship, parksAndGardens, history, outdoorActivities, excursion, wellness'.  - `composer`: 作曲した人のリスト。  - `contactPoint`: 商品に関するお問い合わせ先です。  - `contentURL`: イベントの公式画像や動画の詳細へのURLを指定します。  - `criticReview`: レビュー活動で認められている情報源によって書かれた、または公開されたレビュー。各項目は、[Internationalization (i18N) - W3C recommendation for multilanguage](https://www.w3.org/TR/json-ld/#string-internationalization) に基づくフォーマットを持ち、全ての項目が一つのプロパティに統合されています（例：番号71）。各項目は、'Language Value' : 'Article Value' の文字列で表現されます。  - `currencyAccepted`: isAccessibleForFree` が False の場合に支払いに利用できる通貨。モデルで定義されたアクティブコードのリストの組み合わせ。[標準ISO 4217](http://en.wikipedia.org/wiki/ISO_4217), [暗号通貨](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) , [取引所取引システム](https://en.wikipedia.org/wiki/Local_exchange_trading_system)  - `dataProvider`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description`: このアイテムの説明  - `director`: 編成を管理するディレクターの一覧です。  - `doorTimeClose`: 入場は閉場時間までです。  - `doorTimeOpen`: 開場時間から入場できます。  - `duration`: 各番組の放送時間。計測の単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を使って与えられます。例えば、**HUR** は **Hours** を表します。  - `electricTransport`: 市が提案する電気交通の種類をリストアップ。の組み合わせ。Enum:'electricBicycle, electricCar, electricMotorBike, electricScooter'.  - `endDate`: 項目の終了日時（ISO 8601の日付形式）。  - `eventPriceFrom`: 最低価格です。計測の単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を使って示されます。例えば、**EUR**は、**€uro**を表します。  - `eventPriceTo`: 最大価格です。計測の単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を使って示されます。例えば、**EUR** は **€uro** を表します。  - `eventSchedule`: このプロパティを使用してスケジュールに関連付けられたイベントは、`startDate`または`endDate`プロパティを持つべきではありません。これらは代わりに関連するスケジュール内で定義され、データを使用するクライアントのあいまいさを避けることができます。このプロパティは、異なるスケジュール（異なる月や季節）を指定するために、繰り返し値を持つかもしれません***。  - `eventStatus`: このイベントに関するイベントステータス。  - `id`: エンティティの一意な識別子  - `isAccessibleForFree`: そのアイテム、イベント、または場所が無料でアクセスできることを示すフラグです。  - `language`: IETF [BCP 47](https://tools.ietf.org/html/bcp47)規格を参考にしたイベント中の形式言語の一覧です。  - `location`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `maximumAttendeeCapacity`: その場所で開催されるイベントの参加可能人数の合計です。  - `name`: このアイテムの名称です。  - `openingHoursSpecification`: ある場所の営業時間や、ある場所の中の特定のサービスに関する情報を提供する構造化された値  - `owner`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `paymentAccepted`: isAccessibleForFree`がFalseの場合に受理される支払い。モデルで定義されたアクティブコードのリストの組み合わせ。Enum:'Cash, CreditCard, CryptoCurrency, other' （現金、クレジットカード、暗号通貨、その他）。  - `performer`: イベントの主な出演者、司会者、ミュージシャン、音楽グループ。  - `pitch`: イベントのピッチ。各項目は、[Internationalization (i18N) - W3C recommandation for multilanguage](https://www.w3.org/TR/json-ld/#string-internationalization) に基づくフォーマットを持ち、全ての項目が一つのプロパティに統合されています（例：番号71）。各項目は、Language Value : Article Value の文字列で表現されます。  - `priceSpecification`: カテゴリやパブリックによって、価格や価格帯を表す構造化された値。  - `publicAccess`: (2)公開フラグ 場所の公開を示すフラグ。このプロパティが省略された場合、デフォルトのブール値は想定されない。  - `ratingValueAverage`: イベントの評価値。使用上のガイドライン。0から10までの値を基準にしてください。これは `starRatingDetailed` 属性のすべての詳細スコアの平均値である。  - `refPointOfInterest`: イベントに含まれる全てのPoint Of Interest [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md)を参照する。POIリストは時系列ではありません。  - `routeType`: GFTS規格[STOP](https://developers.google.com/transit/gtfs/reference/#stopstxt)に基づき、イベント周辺で利用可能な都市交通（地下鉄、バス、トラム、...）の一覧です。値の組み合わせ。Enum:' bus, cableCar, cableTram, ferry, funicular, monorail, subway, train, tram, trolleybus'.  - `seeAlso`: 項目に関する追加リソースを指すURIのリスト。  - `slogan`: イベントヘッダーライン、テキストフックにマッチします。  - `source`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `starRatingDetailed`: ratingValueで表される平均値につながった詳細な星評価。使用方法を説明する。1から10の出現回数(Stars)の構造化された値で、各要素は以下のような形式の文字列である。NumberOfSTar`:パーセンテージ  - `startDate`: 項目の開始日時（ISO 8601の日付形式）。  - `subCategory`: category` 属性のサブカテゴリです。特定の文脈に柔軟に対応するためのフリーテキストの組み合わせは、最初の例として、またはアプリケーションが必要とするその他の値として、以下に提供されます。  - `subEvent`: このメジャーイベントの一部であるマイナーイベントのリストへの参照。  - `superEvent`: 本イベントを含む主要イベントに関する言及。  - `thematic`: キーワードとなるテーマ別リスト  - `title`: イベントのタイトル  - `touristType`: セグメントや旅行の動機に応じた観光の種類。  - `transportServices`: イベント会場付近で利用可能な民間交通機関のリストです。例：タクシー、ウーバー、VTC、パーキングシャトルなど  - `type`: イベントである必要があります。NGSIエンティティタイプ  - `url`: アイテムに関連する画像を含むURL  - `webSite`: 詳細は公式サイトにリンクしています。  - `wheelChairAccessible`: 移動に不自由のある方のアクセスも可能です。    
必要なプロパティ  
- `id`  - `type`    
このデータモデルは、UNE178503規格に準拠しています。また、schema.orgと互換性がある。このファイル https://smart-data-models.github.io/data-models/schema-org.json では、schema.org の要素の一部が適応されている。この型はそれ自体で一般的なTouristDestinationを記述するために使用することができ、また他のPlaceに観光関連のプロパティを追加するためのadditionalTypeとして使用することができる。このタイプは、一般的な観光地を記述するために単独で使用されることも、他の場所に観光 関連プロパティを追加するための additionalType として使用されることもできる。UNWTO は、Destination（観光旅行の主要目的地）を、旅行を決定する上で中心となる訪問地と定義している。  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Event:    
  description: 'Upcoming or past event associated with this place, organization, or action.'    
  properties:    
    accessPlan:    
      description: ' Text or Link to the access plan to the item.'    
      type: string    
      x-ngsi:    
        type: Property    
    actor:    
      description: 'List of actors or music group.'    
      items:    
        type: string    
      type: array    
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
      description: 'Type of public concerned by this Event. A combination of Free text (family, adult, children, teenager, senior, allPublic, ...). Enum:''adult, allPublic, children, family, senior, teenager'''    
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
      description: 'Category of the Event. A combination of free text to remain flexible to a specific context is offered below as an initial repository or any other value needed by an application. Enum:''shopping, gastronomy, museum, religiousWorship, parksAndGardens, history, outdoorActivities, excursion, wellness'''    
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
          - spectacle    
          - wellness    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    composer:    
      description: 'List of person who wrote the composition.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    contactPoint:    
      description: 'The details to contact with the item.'    
      properties:    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Supersedes serviceArea.'    
          type: string    
        availabilityRestriction:    
          anyOf:    
            - description: 'Property. Array of identifiers format of any NGSI entity.'    
              items:    
                maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
              type: array    
            - description: 'Property. Array of identifiers format of any NGSI entity.'    
              items:    
                format: uri    
                type: string    
              type: array    
          description: 'Relationship. Model:''http://schema.org/hoursAvailable''. This property links a contact point to information about when the contact point is not available. The details are provided using the Opening Hours Specification class.'    
        availableLanguage:    
          anyOf:    
            - anyOf:    
                - type: string    
                - items:    
                    type: string    
                  type: array    
          description: 'Property. Model:''http://schema.org/availableLanguage''. A language someone may use with or at the item, service or place. Please use one of the language codes from the IETF BCP 47 standard. It is implemented the Text option but it could be also Language'    
        contactOption:    
          anyOf:    
            - type: string    
            - items:    
                type: string    
              type: array    
          description: 'Property. Model:''http://schema.org/contactOption''. An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers).'    
        contactType:    
          description: 'Property. Contact type of this item.'    
          type: string    
        email:    
          description: 'Property. Email address of owner.'    
          format: idn-email    
          type: string    
        faxNumber:    
          description: 'Property. Model:''http://schema.org/Text''. The fax number.'    
          type: string    
        name:    
          description: 'Property. The name of this item.'    
          type: string    
        productSupported:    
          description: 'Property. Model:''http://schema.org/Text''. The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. "iPhone") or a general category of products or services (e.g. "smartphones").'    
          type: string    
        telephone:    
          description: 'Property. Telephone of this contact.'    
          type: string    
        url:    
          description: 'Property. URL which provides a description or further information about this item.'    
          format: uri    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/ContactPoint    
        type: Property    
    contentURL:    
      description: 'Specifies the URL to the official image or video of the Event for more information.'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Property    
    criticReview:    
      description: "Review written or published by a source that is recognized for its reviewing activities. Each items have the format based on the  [Internationalization (i18N) - W3C recommendation for multilanguage](https://www.w3.org/TR/json-ld/#string-internationalization) integrating all items in a single property (ex number 71). Each item is represented by a string with 'Language Value' : 'Article Value'"    
      items:    
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
      type: array    
      x-ngsi:    
        type: Property    
    currencyAccepted:    
      description: 'Currency accepted for payment if `isAccessibleForFree` is False. A combination of a list of active codes defined in the model. [Standard ISO 4217](http://en.wikipedia.org/wiki/ISO_4217), [Crypto Currencies](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) , [Exchange Trading System](https://en.wikipedia.org/wiki/Local_exchange_trading_system)'    
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
    director:    
      description: 'List of director who manage the composition.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    doorTimeClose:    
      description: 'Doors closing time to access the show..'    
      type: string    
      x-ngsi:    
        type: Property    
    doorTimeOpen:    
      description: 'Doors opening time to access the show.'    
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
      description: 'The end date and time of the item (in ISO 8601 date format).'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/endDate    
        type: Property    
    eventPriceFrom:    
      description: 'Min Price. The unit code (text) of measurement is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **EUR** represents **€uro**.'    
      type: number    
      x-ngsi:    
        type: Property    
    eventPriceTo:    
      description: 'Max Price. The unit code (text) of measurement is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **EUR** represents **€uro**.'    
      type: number    
      x-ngsi:    
        type: Property    
    eventSchedule:    
      description: 'An Event that is associated with a Schedule using this property should not have `startDate` or `endDate` properties. These are instead defined within the associated Schedule, this avoids any ambiguity for clients using the data. The property might have repeated values to specify different schedules (different months or seasons).*** '    
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
          exceptDate:    
            format: date-time    
            type: string    
          repeatCount:    
            type: number    
          repeatFrequency:    
            type: string    
      type: array    
      x-ngsi:    
        type: Property    
    eventStatus:    
      description: 'Event Status regarding this event.'    
      items:    
        enum:    
          - opened    
          - closed    
          - suspended    
          - cancelled    
          - scheduled    
          - finished    
          - postponed    
          - rescheduled    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &event_-_properties_-_owner_-_items_-_anyof    
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
      description: 'A flag to signal that the item, event, or place is accessible for free.'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/isAccessibleForFree    
        type: Property    
    language:    
      description: 'List of Formal language used during the Event expressed from the IETF [BCP 47](https://tools.ietf.org/html/bcp47) standard'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/language    
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
    maximumAttendeeCapacity:    
      description: 'The total number of people who can attend to the Event at that location.'    
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
        anyOf: *event_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    paymentAccepted:    
      description: 'Accepted payment if `isAccessibleForFree` is False. A combination of a list of active codes defined in the model. Enum:''Cash, CreditCard, CryptoCurrency, other'''    
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
    performer:    
      description: 'Main actor or presenter or musician or musical group of the event.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    pitch:    
      description: "Pitch of the Event. Each items have the format based on the [Internationalization (i18N) - W3C recommandation for multilanguage](https://www.w3.org/TR/json-ld/#string-internationalization) integrating all items in a single property (ex number 71). Each item is represented by a string with Language Value : Article Value. "    
      items:    
        properties:    
          article:    
            type: string    
          language:    
            type: string    
        type: object    
      type: array    
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
          categoryDescription:    
            type: string    
          eligibleQuantity:    
            type: number    
          maxPrice:    
            type: number    
          minPrice:    
            type: number    
          price:    
            type: number    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    publicAccess:    
      description: 'A flag to signal that the Place is open to public visitors. If this property is omitted there is no assumed default boolean value'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/publicAccess    
        type: Property    
    ratingValueAverage:    
      description: 'Rating value of Event. Usage guidelines: Use values from 0 to 10 depending on your standard. This is the average value of all detailed scores of `starRatingDetailed` attribute'    
      type: number    
      x-ngsi:    
        type: Property    
    refPointOfInterest:    
      description: 'Reference to all the Point Of interest [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) included in the Event. The POI list does not have a chronological order.'    
      items:    
        anyOf: *event_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Relationship    
    routeType:    
      description: "List of the urban transports (subway, Bus, Tram, ...) available near the event according to the GFTS standard [STOP](https://developers.google.com/transit/gtfs/reference/#stopstxt). A combination of values. Enum:' bus, cableCar, cableTram, ferry, funicular, monorail, subway, train, tram, trolleybus'"    
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
      description: 'Event header line, matches the text hook. '    
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
      description: 'The start date and time of the item (in ISO 8601 date format).'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/startDate    
        type: Property    
    subCategory:    
      description: 'Sub-category of the `category` attribute. A combination of free text to remain flexible to a specific context is offered below as an initial example or any other value needed by an application. '    
      items:    
        enum:    
          - --museum--    
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
    subEvent:    
      description: 'Reference to a list of Minor Events that are part of this major Event'    
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
        type: Property    
    superEvent:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the Major Event that includes this Event.'    
      x-ngsi:    
        type: Property    
    thematic:    
      description: 'A list of thematic as keywords'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    title:    
      description: ' Title of the Event.'    
      type: string    
      x-ngsi:    
        type: Property    
    touristType:    
      description: 'Type of tourism depending on the segment and the motivation of the trip.'    
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
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    transportServices:    
      description: 'List of private transport available near the Event. In example taxi, uber, vtc, parkingShuttle '    
      items:    
        enum:    
          - parkingShuttle    
          - taxi    
          - uber    
          - vtc    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    type:    
      description: 'It has to be Event. NGSI entity type'    
      enum:    
        - Event    
      type: string    
      x-ngsi:    
        model: https://schema.org/event    
        type: Property    
    url:    
      description: 'Url with image related to the item'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
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
  x-license-url: https://github.com/smart-data-models/dataModel.TourismDestinations/blob/master/Event/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.TourismDestinations/Event/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## ペイロードの例  
#### イベント NGSI-v2 キー値例  
ここでは、EventをJSON-LD形式でkey-valuesとした場合の例を示す。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:Event:Event:MNCA-EV-NCE-12552-MARIAGEDENFER",  
  "type": "Event",  
  "name": "MARIAGE D ENFER",  
  "alternateName": "Elle en revait, il l a fait : ils vont se marier !",  
  "description": "Information sur la piéce de théatre",  
  "seeAlso": "https://www.billetreduc.com/260539/evt.htm",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.7062,  
      7.26267  
    ]  
  },  
  "address": {  
    "streetAddress": "14 rue Trachel - Bat. B",  
    "postalCode": "06000",  
    "addressLocality": "Nice",  
    "addressCountry": "France",  
    "addressRegion": "Marseille Nice Avignon Aix - (06)"  
  },  
  "areaServed": "Gare de Nice",  
  "dateLastReported": "2020-03-17T08:45:00Z",  
  "contactPoint": {  
    "telephone": "+33(0)4 93 87 08 87",  
    "contactType": "customer reception",  
    "email": "theatrebellecour@gmail.com",  
    "availableLanguage": [  
      "English",  
      "French"  
    ]  
  },  
  "accessPlan": "https://www.billetreduc.com/lieu/nice/theatre-bellecour/#planAcces",  
  "category": [  
    "spectacle"  
  ],  
  "subCategory": [  
    "cabaret",  
    "theater",  
    "boulevard",  
    "vaudeville",  
    "humor"  
  ],  
  "thematic": [  
    "humor"  
  ],  
  "superEvent": "urn:ngsi-ld:Event:Event:MNCA-EV-NCE-12552-FESTIVAL-THEATRE-NICE",  
  "eventStatus": [  
    "scheduled"  
  ],  
  "locationName": "Théâtre Bellecour",  
  "title": "MARIAGE D ENFER",  
  "slogan": "Elle en revait, il l a fait : ils vont se marier !",  
  "language": [  
    "French"  
  ],  
  "startDate": "2020-08-01T01:20:00Z",  
  "endDate": "2020-10-18T01:20:00Z",  
  "openingHoursSpecification": [  
    {  
      "validFrom": "2020-08-08T00:00:00Z",  
      "validThrough": "2020-08-31T00:00:00Z",  
      "dayOfWeek": "Saturday",  
      "Opens": "21.00"  
    },  
    {  
      "validFrom": "2020-08-08T00:00:00Z",  
      "validThrough": "2020-08-31T00:00:00Z",  
      "dayOfWeek": "Sunday",  
      "Opens": "19.00"  
    },  
    {  
      "validFrom": "2020-09-01T00:00:00Z",  
      "validThrough": "2020-10-18T00:00:00Z",  
      "dayOfWeek": "Friday",  
      "Opens": "21.00"  
    },  
    {  
      "validFrom": "2020-09-01T00:00:00Z",  
      "validThrough": "2020-10-18T00:00:00Z",  
      "dayOfWeek": "Saturday"  
    },  
    {  
      "validFrom": "2020-09-01T00:00:00Z",  
      "validThrough": "2020-10-18T00:00:00Z",  
      "dayOfWeek": "Sunday",  
      "Opens": "19.00"  
    }  
  ],  
  "duration": 1.25,  
  "doorTimeOpen": "30 mn before the show",  
  "doorTimeClose": "10 mn before the show",  
  "pitch": [  
    {  
      "language ": "fr",  
      "article": "Heureusement pour Max, la wedding planner c est elle, et elle a déjà tout anticipé dans le moindre détail ! Tout ? Peut-être pas... En tout cas, un mariage ça se gère à deux... Et les conflits aussi ! Quand on dit pour le meilleur et pour le pire, le pire c est certainement les préparatifs d un mariage ! Que vous soyez mariés, fiancés, en couple, juste amis ou célibataire, cette comédie est faite pour vous ! Venez découvrir les coulisses des préparatifs d un mariage haut en couleurs avant de faire le grand saut !"  
    },  
    {  
      "language": "en",  
      "article": "But before that there are some details to settle and Elo knows it well: A beautiful wedding, cannnot be organized just like that! Fortunately for Max, the wedding planner is her, and she has already anticipated everything in every detail! Evrything ? Maybe not... In any case, a marriage is managed by two ... And conflicts too! When we say for better or for worse, the worst is certainly the preparations for a wedding! Whether married, engaged, in a relationship, just friends or single, this comedy is for you! Come and discover the preparations for a colorful wedding before taking the plunge!"  
    }  
  ],  
  "webSite": "http://www.theatrebellecour.com",  
  "contentURL": "https://www.nicetourisme.com/resources/ref/events/12552/mariage-d-enfer_168.jpg",  
  "performer": [  
    "Lise Giraudier"  
  ],  
  "actor": [  
    "Lise Giraudier",  
    "Richard Zanca",  
    "Vanessa Bellagamba",  
    "Yann Bruno-Martinez"  
  ],  
  "composer": [  
    "Céline Cara"  
  ],  
  "director": [  
    "Sébastien El Fassi"  
  ],  
  "criticReview": [  
    {  
      "language": "fr",  
      "reviews": [  
        {  
          "article": "Comédie à ne pas rater. Tout y est la mère, la belle mère, les copains et avant tout les rires les quiproquos, les retournements et tout cela  enchaîne avec une grande vitesse.  Alors allez  pour feliciter les époux et rire de bon coeur avec eux.",  
          "origin": "Revue Theatrale - L. Dupont",  
          "ratingValue": 9,  
          "starRating": 6  
        }  
      ]  
    }  
  ],  
  "ratingValueAverage": 9.2,  
  "starRatingDetailed": {  
    "5": 94,  
    "4": 6,  
    "3": 0,  
    "2": 0,  
    "1": 0  
  },  
  "audience": [  
    "allPublic"  
  ],  
  "wheelChairAccessible": true,  
  "maximumAttendeeCapacity": 60,  
  "isAccessibleForFree": false,  
  "eventPriceFrom": 10.95,  
  "eventPriceTo": 19.5,  
  "priceSpecification": [  
    {  
      "categoryDescription": "Category 1 : Seat Range 1 to 2",  
      "eligibleQuantity": 20,  
      "price": 19.5  
    },  
    {  
      "categoryDescription": "Category 2 : Seat Range 3 to 6",  
      "eligibleQuantity": 40,  
      "price": 15.95  
    },  
    {  
      "categoryDescription": "Special price from Monday to Wednesday : Category 1 - 2",  
      "eligibleQuantity": 60,  
      "price": 10.95  
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
    "taxi",  
    "uber",  
    "vtc",  
    "parkingShuttle"  
  ],  
  "electricTransport": [  
    "electricBicycle",  
    "electricMotorBike"  
  ]  
}  
```  
#### イベント NGSI-v2 正規化例  
以下は、正規化された JSON-LD 形式の Event の例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": {  
    "type": "Text",  
    "value": "uri:ngsi:event:1"  
  },  
  "type": {  
    "type": "Text",  
    "value": "Event"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Concierto de Revólver"  
  },  
  "address": {  
    "addressLocality": "Salamanca",  
    "postalCode": "37008",  
    "streetAddress": "Calle Monte Olivete, s/n"  
  },  
  "startDate": {  
    "type": "Text",  
    "value": "2019-06-08T21:00:00"  
  },  
  "endDate": {  
    "type": "Text",  
    "value": "2019-06-08T23:00:00"  
  },  
  "url": {  
    "type": "Text",  
    "value": "https://www.notikumi.com/2019/6/8/evento-de-revolver-en-salamanca"  
  },  
  "offeredBy": {  
    "type": "object",  
    "value": {  
      "type": "Organization",  
      "name": "Notikumi",  
      "url": "https://www.notikumi.com/"  
    }  
  },  
  "touristType": {  
    "type": "Text",  
    "value": "EVENTS AND FESTIVALS TOURISM"  
  }  
}  
```  
#### イベント NGSI-LD キー値例  
ここでは、EventをJSON-LD形式でkey-valuesとした場合の例を示す。これは `options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
    "id": "uri:ngsi:event:1",  
    "type": "Event",  
    "address": {  
        "addressLocality": "Salamanca",  
        "postalCode": "37008",  
        "streetAddress": "Calle Monte Olivete, s/n"  
    },  
    "endDate": "2019-06-08T23:00:00",  
    "name": "Concierto de Revolver",  
    "offeredBy": {  
        "type": "Organization",  
        "name": "Notikumi",  
        "url": "https://www.notikumi.com/"  
    },  
    "startDate": "2019-06-08T21:00:00",  
    "touristType": "EVENTS AND FESTIVALS TOURISM",  
    "url": "https://www.notikumi.com/2019/6/8/evento-de-revolver-en-salamanca",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.TourismDestinations/master/context.jsonld"  
    ]  
}  
```  
#### イベント NGSI-LD 正規化例  
ここでは、JSON-LD フォーマットの Event を正規化した例を示す。これはオプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
    "id": "urn:ngsi-ld:Event:Event:MNCA-EV-NCE-12552-MARIAGEDENFER",  
    "type": "Event",  
    "accessPlan": {  
        "type": "Property",  
        "value": "https://www.billetreduc.com/lieu/nice/theatre-bellecour/#planAcces"  
    },  
    "actor": {  
        "type": "Property",  
        "value": [  
            "Lise Giraudier",  
            "Richard Zanca",  
            "Vanessa Bellagamba",  
            "Yann Bruno-Martinez"  
        ]  
    },  
    "address": {  
        "type": "Property",  
        "value": {  
            "streetAddress": "14 rue Trachel - Bat. B",  
            "postalCode": "06000",  
            "addressLocality": "Nice",  
            "addressCountry": "France",  
            "addressRegion": "Marseille Nice Avignon Aix - (06)"  
        }  
    },  
    "alternateName": {  
        "type": "Property",  
        "value": "Elle en revait, il l a fait : ils vont se marier !"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Gare de Nice"  
    },  
    "audience": {  
        "type": "Property",  
        "value": [  
            "allPublic"  
        ]  
    },  
    "category": {  
        "type": "Property",  
        "value": [  
            "spectacle"  
        ]  
    },  
    "composer": {  
        "type": "Property",  
        "value": [  
            "C\u00e9line Cara"  
        ]  
    },  
    "contactPoint": {  
        "type": "Property",  
        "value": {  
            "telephone": "+33(0)4 93 87 08 87",  
            "contactType": "customer reception",  
            "email": "theatrebellecour@gmail.com",  
            "availableLanguage": [  
                "English",  
                "French"  
            ]  
        }  
    },  
    "contentURL": {  
        "type": "Property",  
        "value": "https://www.nicetourisme.com/resources/ref/events/12552/mariage-d-enfer_168.jpg"  
    },  
    "criticReview": {  
        "type": "Property",  
        "value": [  
            {  
                "language": "fr",  
                "reviews": [  
                    {  
                        "article": "Com\u00e9die \u00e0 ne pas rater. Tout y est la m\u00e8re, la belle m\u00e8re, les copains et avant tout les rires les quiproquos, les retournements et tout cela  encha\u00eene avec une grande vitesse.  Alors allez  pour feliciter les \u00e9poux et rire de bon coeur avec eux.",  
                        "origin": "Revue Theatrale - L. Dupont",  
                        "ratingValue": 9,  
                        "starRating": 6  
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
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-03-17T08:45:00Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Information sur la pi\u00e9ce de th\u00e9atre"  
    },  
    "director": {  
        "type": "Property",  
        "value": [  
            "S\u00e9bastien El Fassi"  
        ]  
    },  
    "doorTimeClose": {  
        "type": "Property",  
        "value": "10 mn before the show"  
    },  
    "doorTimeOpen": {  
        "type": "Property",  
        "value": "30 mn before the show"  
    },  
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
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-10-18T01:20:00Z"  
        }  
    },  
    "eventPriceFrom": {  
        "type": "number",  
        "value": 10.95  
    },  
    "eventPriceTo": {  
        "type": "number",  
        "value": 19.5  
    },  
    "eventStatus": {  
        "type": "Property",  
        "value": [  
            "scheduled"  
        ]  
    },  
    "isAccessibleForFree": {  
        "type": "boolean",  
        "value": "false"  
    },  
    "language": {  
        "type": "Property",  
        "value": [  
            "French"  
        ]  
    },  
    "location": {  
        "type": "Geoproperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                43.7062,  
                7.26267  
            ]  
        }  
    },  
    "locationName": {  
        "type": "Property",  
        "value": "Th\u00e9\u00e2tre Bellecour"  
    },  
    "maximumAttendeeCapacity": {  
        "type": "number",  
        "value": 60  
    },  
    "name": {  
        "type": "Property",  
        "value": "MARIAGE D ENFER"  
    },  
    "offeredBy": {  
        "type": "Property",  
        "value": {  
            "type": "Organization",  
            "name": "Notikumi",  
            "url": "https://www.notikumi.com/"  
        }  
    },  
    "openingHoursSpecification": {  
        "type": "Property",  
        "value": [  
            {  
                "validFrom": "2020-08-08T00:00:00Z",  
                "validThrough": "2020-08-31T00:00:00Z",  
                "dayOfWeek": "Saturday",  
                "Opens": "21.00"  
            },  
            {  
                "validFrom": "2020-08-08T00:00:00Z",  
                "validThrough": "2020-08-31T00:00:00Z",  
                "dayOfWeek": "Sunday",  
                "Opens": "19.00"  
            },  
            {  
                "validFrom": "2020-09-01T00:00:00Z",  
                "validThrough": "2020-10-18T00:00:00Z",  
                "dayOfWeek": "Friday",  
                "Opens": "21.00"  
            },  
            {  
                "validFrom": "2020-09-01T00:00:00Z",  
                "validThrough": "2020-10-18T00:00:00Z",  
                "dayOfWeek": "Saturday"  
            },  
            {  
                "validFrom": "2020-09-01T00:00:00Z",  
                "validThrough": "2020-10-18T00:00:00Z",  
                "dayOfWeek": "Sunday",  
                "Opens": "19.00"  
            }  
        ]  
    },  
    "paymentAccepted": {  
        "type": "Property",  
        "value": [  
            "Cash",  
            "CreditCard"  
        ]  
    },  
    "performer": {  
        "type": "Property",  
        "value": [  
            "Lise Giraudier"  
        ]  
    },  
    "pitch": {  
        "type": "Property",  
        "value": [  
            {  
                "language ": "fr",  
                "article": "Heureusement pour Max, la wedding planner c est elle, et elle a d\u00e9j\u00e0 tout anticip\u00e9 dans le moindre d\u00e9tail ! Tout ? Peut-\u00eatre pas... En tout cas, un mariage \u00e7a se g\u00e8re \u00e0 deux... Et les conflits aussi ! Quand on dit pour le meilleur et pour le pire, le pire c est certainement les pr\u00e9paratifs d un mariage ! Que vous soyez mari\u00e9s, fianc\u00e9s, en couple, juste amis ou c\u00e9libataire, cette com\u00e9die est faite pour vous ! Venez d\u00e9couvrir les coulisses des pr\u00e9paratifs d un mariage haut en couleurs avant de faire le grand saut !"  
            },  
            {  
                "language": "en",  
                "article": "But before that there are some details to settle and Elo knows it well: A beautiful wedding, cannnot be organized just like that! Fortunately for Max, the wedding planner is her, and she has already anticipated everything in every detail! Evrything ? Maybe not... In any case, a marriage is managed by two ... And conflicts too! When we say for better or for worse, the worst is certainly the preparations for a wedding! Whether married, engaged, in a relationship, just friends or single, this comedy is for you! Come and discover the preparations for a colorful wedding before taking the plunge!"  
            }  
        ]  
    },  
    "priceSpecification": {  
        "type": "Property",  
        "value": [  
            {  
                "categoryDescription": "Category 1 : Seat Range 1 to 2",  
                "eligibleQuantity": 20,  
                "price": 19.5  
            },  
            {  
                "categoryDescription": "Category 2 : Seat Range 3 to 6",  
                "eligibleQuantity": 40,  
                "price": 15.95  
            },  
            {  
                "categoryDescription": "Special price from Monday to Wednesday : Category 1 - 2",  
                "eligibleQuantity": 60,  
                "price": 10.95  
            }  
        ]  
    },  
    "ratingValueAverage": {  
        "type": "number",  
        "value": 9.2  
    },  
    "routeType": {  
        "type": "Property",  
        "value": [  
            "tram",  
            "subway",  
            "bus"  
        ]  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": "https://www.billetreduc.com/260539/evt.htm"  
    },  
    "slogan": {  
        "type": "Property",  
        "value": "Elle en revait, il l a fait : ils vont se marier !"  
    },  
    "starRatingDetailed": {  
        "type": "object",  
        "value": {  
            "5": 94,  
            "4": 6,  
            "3": 0,  
            "2": 0,  
            "1": 0  
        }  
    },  
    "startDate": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-08-01T01:20:00Z"  
        }  
    },  
    "subCategory": {  
        "type": "Property",  
        "value": [  
            "cabaret",  
            "theater",  
            "boulevard",  
            "vaudeville",  
            "humor"  
        ]  
    },  
    "superEvent": {  
        "type": "Property",  
        "value": "urn:ngsi-ld:Event:Event:MNCA-EV-NCE-12552-FESTIVAL-THEATRE-NICE"  
    },  
    "thematic": {  
        "type": "Property",  
        "value": [  
            "humor"  
        ]  
    },  
    "title": {  
        "type": "Property",  
        "value": "MARIAGE D ENFER"  
    },  
    "touristType": {  
        "type": "Property",  
        "value": "EVENTS AND FESTIVALS TOURISM"  
    },  
    "transportServices": {  
        "type": "Property",  
        "value": [  
            "taxi",  
            "uber",  
            "vtc",  
            "parkingShuttle"  
        ]  
    },  
    "url": {  
        "type": "string",  
        "value": "https://www.notikumi.com/2019/6/8/evento-de-revolver-en-salamanca"  
    },  
    "webSite": {  
        "type": "Property",  
        "value": "http://www.theatrebellecour.com"  
    },  
    "wheelChairAccessible": {  
        "type": "boolean",  
        "value": "true"  
    },  
    "@context": [  
        "https://smartdatamodelsorg/context.jsonld"  
    ]  
}  
```  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
