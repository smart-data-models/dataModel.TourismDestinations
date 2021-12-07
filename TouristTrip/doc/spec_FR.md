Entité : TouristTrip  
====================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.TourismDestinations/blob/master/TouristTrip/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Un voyage touristique. Un itinéraire créé pour visiter un ou plusieurs lieux d'intérêt (TouristAttraction/TouristDestination) souvent liés par un thème, une zone géographique ou un intérêt similaire à un TouristType particulier. L'OMT définit le voyage touristique comme le voyage effectué par des visiteurs**.  

## Liste des propriétés  

- `accessPlan`: Texte ou lien vers le plan d'accès au voyage.  - `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `audience`: Type de public concerné par ce Voyage. Une combinaison de textes libres (famille, adulte, enfants, adolescent, senior, tout public, ...). Enum : "adulte, allPublic, enfants, famille, senior, adolescent".  - `category`: Catégorie de l'excursion. Une combinaison de texte libre permettant de rester flexible à un contexte spécifique est proposée ci-dessous comme référentiel initial ou toute autre valeur nécessaire à une application. enum : 'excursion, gastronomie, histoire, musée, outdoorActivities, parksAndGardens, religiousWorship, shopping, wellness' (excursion, gastronomie, histoire, musée, activités de plein air, parcs et jardins, culte religieux, shopping, bien-être)  - `contentURL`: Spécifie l'URL de l'image ou de la vidéo officielle du voyage pour plus d'informations.  - `criticReview`: Examen écrit ou publié par une source reconnue pour ses activités d'examen. Chaque article a un format basé sur la [Internationalization (i18N) - W3C recommendation for multilanguage] (https://www.w3.org/TR/json-ld/#string-internationalization) intégrant tous les articles dans une seule propriété (ex numéro 71). Chaque article est représenté par une chaîne de caractères avec 'Language Value' : 'Article Value'.  - `currencyAccepted`: Devise acceptée pour le paiement si `TripFree` est False. Une combinaison d'une liste de codes actifs définis dans le modèle. [Norme ISO 4217](http://en.wikipedia.org/wiki/ISO_4217), [Crypto Monnaies](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) , [Système de négociation en bourse](https://en.wikipedia.org/wiki/Local_exchange_trading_system)  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateLastReported`: Dernière mise à jour officielle des données au format ISO 8601  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `duration`: La durée de chaque émission. Le code d'unité (texte) de mesure est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **HUR** représente **Heures**.  - `electricTransport`:  Liste des différents types de transport électrique proposés par la ville. Une combinaison de . Enum:'electricBicycle, electricCar, electricMotorBike, electricScooter' (bicyclette électrique, voiture électrique, moto électrique, scooter électrique)  - `endDate`: Date et heure de fin dans un format ISO8601 UTC  - `id`: Identifiant unique de l'entité  - `isAccessibleForFree`: Voyage gratuit ou payant (Vrai = Gratuit / Faux = Payant).  - `itinerary`: Destinations ou lieux qui composent un voyage. Pour un voyage où l'ordre des destinations est important, utilisez ItemList pour spécifier cet ordre dans les voyages.  - `language`:  Liste du langage formel utilisé pendant le voyage exprimé à partir de la norme IETF [BCP 47](https://tools.ietf.org/html/bcp47)  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `locationName`: Nom du lieu du voyage.  - `maximumAttendeeCapacity`: Le nombre total de personnes qui peuvent assister au voyage à cet endroit.  - `name`: Le nom de cet élément.  - `openingHoursSpecification`: Une valeur structurée fournissant des informations sur les heures d'ouverture d'un lieu ou d'un certain service à l'intérieur d'un lieu.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `paymentAccepted`: Paiement accepté si `TripFree` est False. Une combinaison d'une liste de codes actifs définis dans le modèle. Enum : 'Cash, CreditCard, CryptoCurrency, other' (espèces, cartes de crédit, crypto-monnaies, autres)  - `pitch`: Pitch of the Trip. Chaque article a le format basé sur la [Internationalisation (i18N) - Recommandation du W3C pour le multilinguisme] (https://www.w3.org/TR/json-ld/#string-internationalization) intégrant tous les articles dans une seule propriété (ex numéro 71). Chaque élément est représenté par une chaîne de caractères avec Valeur de la langue : Valeur de l'article.  - `priceSpecification`: Une valeur structurée représentant un prix ou une fourchette de prix selon les catégories ou le public.  - `ratingValueAverage`: Valeur d'évaluation des voyages. Directives d'utilisation : Utilisez des valeurs de 0 à 10 en fonction de votre standard. Il s'agit de la valeur moyenne de toutes les notes détaillées de l'attribut `starRatingDetailed`.  - `refPointOfInterest`: Référence à tous les points d'intérêt [PointOfInterest] (https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) inclus dans les voyages. La liste des POI n'a pas d'ordre chronologique.  - `routeType`: Liste des transports urbains (métro, Bus, Tram, ...) disponibles à proximité du Voyage selon la norme GFTS [STOP](https://developers.google.com/transit/gtfs/reference/#stopstxt). Une combinaison de valeurs. Enum:' bus, cableCar, cableTram, ferry, funiculaire, monorail, métro, train, tram, trolleybus'.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `slogan`: Ligne d'en-tête de voyage, correspond au crochet de texte.  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `starRatingDetailed`: Les évaluations détaillées par étoiles qui ont conduit à la valeur moyenne exprimée dans le ratingValue. Mode d'emploi : Une valeur structurée de 1 à 10 occurrences (étoiles) où chaque élément est une chaîne au format : `NumberOfSTar` : Pourcentage.  - `startDate`: Date et heure de début dans un format ISO8601 UTC  - `subCategory`: Sous-catégorie de l'attribut `category`. Une combinaison de texte libre pour rester flexible à un contexte spécifique est proposée ci-dessous comme un premier exemple ou toute autre valeur nécessaire à une application.  - `subTrip`: Référence à une liste de trajets mineurs qui font partie de ce trajet principal.  - `superTrip`: Référence au Voyage principal qui inclut ce Voyage.  - `thematic`: Une liste de thèmes en tant que mots-clés  - `title`:  Titre du voyage.  - `touristType`: énumération des différents types de touristes applicables au TouristTrip  - `transportServices`: Liste des transports privés disponibles à proximité du Voyage. Par exemple taxi, uber, vtc, parkingShuttle  - `tripPriceFrom`: Prix minimum. Le code d'unité (texte) de mesure est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **EUR** représente **€uro**.  - `tripPriceTo`: Prix maximum. Le code de l'unité (texte) de mesure est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **EUR** représente **€uro**.  - `tripSchedule`: Programme de déplacement. Cet attribut permet de définir un horaire sur une période de temps répétée, utilisé pour décrire un déplacement qui se produit régulièrement. Dans l'exemple nota au début de la section pour la restriction d'utilisation de cet attribut.  - `tripStatus`: Statut du voyage concernant ce voyage. Enum : 'cancelled, closed, finished, opened, postponed, rescheduled, scheduled, suspended' (annulé, fermé, terminé, ouvert, reporté, reprogrammé, prévu, suspendu)  - `type`: Il doit s'agir de TouristDestination. Type NGSI  - `webSite`: Lien vers le site officiel pour plus d'informations.  - `wheelChairAccessible`: Accès possible pour les personnes à mobilité réduite.    
Propriétés requises  
- `id`  - `type`    
Ce modèle de données est basé sur la norme UNE178503. Il est également compatible avec schema.org. Certains des éléments de schema.org ont été adaptés dans ce fichier https://smart-data-models.github.io/data-models/schema-org.json. Des ajustements mineurs ont été nécessaires pour garder la compatibilité avec schema.org.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
            type: string    
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
          opens:    
            format: time    
            type: string    
          validFrom:    
            format: date-time    
            type: string    
          validThrough:    
            format: date-time    
            type: string    
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
      description: 'It has to be TouristDestination. NGSI type'    
      enum:    
        - TouristTrip    
      type: string    
      x-ngsi:    
        model: https://schema.org/TouristDestination    
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
  x-version: 0.0.2    
```  
</details>    
## Exemples de charges utiles  
#### TouristTrip Valeurs-clés NGSI-v2 Exemple  
Voici un exemple de TouristTrip au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
  "contenteURL": "https://www.nice.fr/uploads/media/paysage/0001/03/Lascaris.JPG",  
  "criticReview": {  
    "fr": {  
      "value": {  
        "article": "Beau palais baroque qui contient des instruments de musique vari\u00e9s dont une harpe-piano \u00e9tonnante, et des portraits tr\u00e8s beaux. A voir, surtout pour l'escalier et la d\u00e9coration des salles.",  
        "origine": "Office du tourisme Nice",  
        "ratingValue": 9,  
        "starRating": 5  
      }  
    },  
    "en": {  
      "value": {  
        "article": "Beautiful baroque palace which contains various gastronomieal instruments including an astonishing harp-piano, and very beautiful portraits. To see, especially for the staircase and the decoration of the rooms.",  
        "origine": "Trip Advisor",  
        "ratingValue": 8,  
        "starRating": 4  
      }  
    }  
  },  
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
#### TouristTrip NGSI-v2 normalisé Exemple  
Voici un exemple de TouristTrip au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
        "review": {  
          "value": {  
            "article": "Beau palais baroque qui contient des instruments de musique varios dont une harpe-piano tonnante, et des portraits trÃ¨s beaux. A voir, surtout pour l'escalier et la decoration des salles.",  
            "origin": "Office du tourisme Nice",  
            "ratingValue": 9,  
            "starRating": 5  
          }  
        }  
      },  
      {  
        "language": "en",  
        "review": {  
          "value": {  
            "article": "Beautiful baroque palace which contains various gastronomical instruments including an astonishing harp-piano, and very beautiful portraits. To see, especially for the staircase and the decoration of the rooms.",  
            "origin": "Trip Advisor",  
            "ratingValue": 8,  
            "starRating": 4  
          }  
        }  
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
#### TouristTrip Valeurs-clés NGSI-LD Exemple  
Voici un exemple de TouristTrip au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
  "contenteURL": "https://www.nice.fr/uploads/media/paysage/0001/03/Lascaris.JPG",  
  "criticReview": {  
    "fr": {  
      "value": {  
        "article": "Beau palais baroque qui contient des instruments de musique vari\u00e9s dont une harpe-piano \u00e9tonnante, et des portraits tr\u00e8s beaux. A voir, surtout pour l'escalier et la d\u00e9coration des salles.",  
        "origine": "Office du tourisme Nice",  
        "ratingValue": 9,  
        "starRating": 5  
      }  
    },  
    "en": {  
      "value": {  
        "article": "Beautiful baroque palace which contains various gastronomieal instruments including an astonishing harp-piano, and very beautiful portraits. To see, especially for the staircase and the decoration of the rooms.",  
        "origine": "Trip Advisor",  
        "ratingValue": 8,  
        "starRating": 4  
      }  
    }  
  },  
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
      "audience": ["adult"],  
      "price": 10.0  
    },  
    {  
      "audience": ["senior"],  
      "price": 5.0  
    },  
    {  
      "audience": ["children"],  
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
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### Voyage touristique NGSI-LD normalisé Exemple  
Voici un exemple de TouristTrip au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi:touristTrip:1",  
  "type": "TouristTrip",  
  "name": {  
    "type": "Property",  
    "value": "Descubre Conil"  
  },  
  "description": [  
    {  
      "type": "Property",  
      "value": "Viaje para conocer el encanto y los atractivos turisticos de Conil de la Frontera."  
    }  
  ],  
  "touristType": {  
    "type": "Property",  
    "value": [  
      "FAMILY TOURISM",  
      "WATER SPORTS TOURISM",  
      "FOOD TOURISM",  
      "BEACH AND SUN TOURISM"  
    ]  
  },  
  "url": {  
    "type": "Property",  
    "value": [  
      "https://www.spain.info/es/que-quieres/ciudades-pueblos/otros-destinos/conil_de_la_frontera.html"  
    ]  
  },  
  "image": {  
    "type": "Property",  
    "value": "http://www.turismo.conil.org/PortalTurismo/DocTurismo.nsf/voTodosPorIdiomaUNID/4AC02453BEE8F5CDC125750400315F48/$FILE/IMGP2024.JPG"  
  },  
  "sameAs": {  
    "type": "Property",  
    "value": "https://inventrip.com/conil/trip/1907"  
  },  
  "video": {  
    "type": "Property",  
    "value": "https://www.youtube.com/watch?v=IhnvlIzxPLg"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Palais Lascaris"  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": "https://www.nice.fr/fr/culture/musees-et-galeries/palais-lascaris-le-palais"  
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
  "areaServed": {  
    "type": "Property",  
    "value": "Vieux Nice"  
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
  "accessPlan": {  
    "type": "Property",  
    "value": "https://www.google.fr/maps/place/Mus%C3%A9e+du+Palais+Lascaris/@43.6976805,7.2750571,17z/data=!3m1!4b1!4m5!3m4!1s0x12cddabca1950653:0x8d425022ef476dde!8m2!3d43.6976766!4d7.2772458?hl=fr"  
  },  
  "category": {  
    "type": "Property",  
    "value": [  
      "museum"  
    ]  
  },  
  "subCategory": {  
    "type": "Property",  
    "value": [  
      "art",  
      "decorativeArts",  
      "history"  
    ]  
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
  "locationName": {  
    "type": "Property",  
    "value": "Palais Lascaris"  
  },  
  "title": {  
    "type": "Property",  
    "value": "Visite du MusÃ©e du Palais Lascaris"  
  },  
  "slogan": {  
    "type": "Property",  
    "value": "Une demeure aristocratique joyau du baroque et une remarquable collection d instruments de musiques anciens."  
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
  "superTrip": {  
    "type": "Property",  
    "value": "urn:ngsi-ld:Trip:Trip:MNCA-TRIP-NCE-VISTE-DES-MUSEES-NICE"  
  },  
  "tripStatus": {  
    "type": "Property",  
    "value": "opened"  
  },  
  "startDate": {  
    "type": "DateTime",  
    "value": "-01-01"  
  },  
  "endDate": {  
    "type": "DateTime",  
    "value": "-12-31"  
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
  "duration": {  
    "type": "Property",  
    "value": 1.25  
  },  
  "pitch": {  
    "type": "Property",  
    "value": [  
      {  
        "language": "fr",  
        "article": "Dans une ruelle Ã©troite ce palais baroque allie richesse ornementale et simplicitÃ©. Son escalier avec ses fresques est somptueux mÃªme si ses dimensions sont somme toute rÃ©duites. Lâambiance est chaleureuse avec des plafonds bas ,des piÃ¨ces Ã  lâÃ©chelle humaine qui en font un lieu intime propice Ã  la dÃ©couverte de la collection dâinstruments de musique. Ne manquez pas dâobserver les portes de communication."  
      },  
      {  
        "language": "en",  
        "article": "In a narrow alley, this baroque palace combines ornamental richness and simplicity. Its staircase with its frescoes is sumptuous even if its dimensions are all in all small. The atmosphere is warm with low ceilings, rooms on a human scale that make it an intimate place conducive to discovering the collection of gastronomieal instruments. Do not miss to observe the communication doors."  
      }  
    ]  
  },  
  "webSite": {  
    "type": "Property",  
    "value": "http://www.palais-lascaris.com"  
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
        "review": {  
          "type": "Property",  
          "value": {  
            "article": "Beau palais baroque qui contient des instruments de musique variÃ©s dont une harpe-piano Ã©tonnante, et des portraits trÃ¨s beaux. A voir, surtout pour l'escalier et la dÃ©coration des salles.",  
            "origine": "Office du tourisme Nice",  
            "ratingValue": 9,  
            "starRating": 5  
          }  
        }  
      },  
      {  
        "language": "en",  
        "review": {  
          "type": "Property",  
          "value": {  
            "article": "Beautiful baroque palace which contains various gastronomieal instruments including an astonishing harp-piano, and very beautiful portraits. To see, especially for the staircase and the decoration of the rooms.",  
            "origine": "Trip Advisor",  
            "ratingValue": 8,  
            "starRating": 4  
          }  
        }  
      }  
    ]  
  },  
  "ratingValue": {  
    "type": "Property",  
    "value": 8.5  
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
  "audience": {  
    "type": "Property",  
    "value": [  
      "AllPublic"  
    ]  
  },  
  "wheelChairAccessible": {  
    "type": "Property",  
    "value": false  
  },  
  "maximumAttendeeCapacity": {  
    "type": "Property",  
    "value": 25  
  },  
  "isAccessibleForFree": {  
    "type": "Property",  
    "value": false  
  },  
  "tripPriceFrom": {  
    "type": "Property",  
    "value": 0.00  
  },  
  "tripPriceTo": {  
    "type": "Property",  
    "value": 10.00  
  },  
  "priceSpecification": {  
    "type": "Property",  
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
    "type": "Property",  
    "value": [  
      "Cash",  
      "CreditCard"  
    ]  
  },  
  "currencyAccepted": {  
    "type": "Property",  
    "value": [  
      "EUR",  
      "USD"  
    ]  
  },  
  "routeType": {  
    "type": "Property",  
    "value": [  
      "tram",  
      "subway",  
      "bus"  
    ]  
  },  
  "transportServices": {  
    "type": "Property",  
    "value": [  
      "taxi"  
    ]  
  },  
  "electricTransport": {  
    "type": "Property",  
    "value": [  
      "electricBicycle",  
      "electricMotorBike"  
    ]  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
