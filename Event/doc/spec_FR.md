<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Événement  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.TourismDestinations/blob/master/Event/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Événement à venir ou passé associé à ce lieu, cette organisation ou cette action**.  
version : 0.2.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `accessPlan[string]`:  Texte ou lien vers le plan d'accès à l'article  - `actor[array]`: Liste d'acteurs ou de groupes musicaux  - `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.    
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `audience[array]`: Type de public concerné par cet événement. Combinaison de textes libres (famille, adulte, enfants, adolescents, seniors, tout public, ...). Enum : "adulte, tout public, enfant, famille, senior, adolescent  - `category[array]`: Catégorie de l'événement. Une combinaison de texte libre permettant de s'adapter à un contexte spécifique est proposée ci-dessous comme référentiel initial ou toute autre valeur requise par une application. Enum : "shopping, gastronomie, musée, culte, parcs et jardins, histoire, activités de plein air, excursion, bien-être".  - `composer[array]`: Liste de la personne qui a écrit la composition  - `contactPoint[object]`: Les coordonnées à contacter avec l'article  . Model: [https://schema.org/ContactPoint](https://schema.org/ContactPoint)	- `areaServed[string]`: Zone géographique dans laquelle un service ou un article est proposé. Remplace serviceArea    
	- `availabilityRestriction[*]`: Cette propriété relie un point de contact à des informations sur les cas où le point de contact n'est pas disponible. Les détails sont fournis à l'aide de la classe de spécification des heures d'ouverture.  . Model: [http://schema.org/hoursAvailable](http://schema.org/hoursAvailable)  
	- `availableLanguage[*]`: Langue que quelqu'un peut utiliser avec ou dans l'article, le service ou le lieu. Veuillez utiliser l'un des codes de langue de la norme IETF BCP 47. L'option Texte est mise en œuvre, mais il peut s'agir également de l'option Langue.  . Model: [http://schema.org/availableLanguage](http://schema.org/availableLanguage)  
	- `contactOption[*]`: Une option disponible sur ce point de contact (par exemple, un numéro gratuit ou une assistance pour les malentendants).  . Model: [http://schema.org/contactOption](http://schema.org/contactOption)  
	- `contactType[string]`: Type de contact de cet article    
	- `email[idn-email]`: Adresse électronique du propriétaire    
	- `faxNumber[string]`: Le numéro de fax  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `name[string]`: Le nom de cet élément    
	- `productSupported[string]`: Le produit ou le service auquel se rapporte ce point de contact d'assistance (par exemple, l'assistance produit pour une ligne de produits particulière). Il peut s'agir d'un produit ou d'une ligne de produits spécifique (par exemple "iPhone") ou d'une catégorie générale de produits ou de services (par exemple "smartphones").  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `telephone[string]`: Téléphone de ce contact    
- `contentURL[uri]`: Spécifie l'URL de l'image ou de la vidéo officielle de l'événement pour plus d'informations.  - `criticReview[array]`: Revue écrite ou publiée par une source reconnue pour ses activités de revue. Chaque article a un format basé sur l'[Internationalisation (i18N) - Recommandation du W3C pour le multilinguisme] (https://www.w3.org/TR/json-ld/#string-internationalization) intégrant tous les articles dans une propriété unique (ex numéro 71). Chaque élément est représenté par une chaîne de caractères avec 'Valeur de la langue' : 'Valeur de l'article'  - `currencyAccepted[array]`: Monnaie acceptée pour le paiement si `isAccessibleForFree` est False. Combinaison d'une liste de codes actifs définis dans le modèle. [Norme ISO 4217](http://en.wikipedia.org/wiki/ISO_4217), [Crypto-monnaies](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) , [Système d'échange de devises](https://en.wikipedia.org/wiki/Local_exchange_trading_system)  . Model: [https://schema.org/currenciesAccepted](https://schema.org/currenciesAccepted)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `director[array]`: Liste des directeurs qui gèrent la composition  - `doorTimeClose[string]`: Heure de fermeture des portes pour accéder au spectacle  - `doorTimeOpen[string]`: Heure d'ouverture des portes pour accéder au spectacle  - `duration[number]`: La durée de chaque émission. Le code d'unité (texte) de mesure est donné en utilisant les [codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **HUR** représente **Heures**  - `electricTransport[array]`:  Liste des différents types de transport électrique proposés par la ville. Une combinaison de. Enum : "electricBicycle, electricCar, electricMotorBike, electricScooter" (bicyclette électrique, voiture électrique, moto électrique, scooter électrique)  - `endDate[date-time]`: La date et l'heure de fin de l'élément (dans le format de date ISO 8601).  . Model: [https://schema.org/endDate](https://schema.org/endDate)- `eventPriceFrom[number]`: Prix min. Le code d'unité (texte) de mesure est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **EUR** représente **€uro**.  - `eventPriceTo[number]`: Prix maximum. Le code d'unité (texte) de mesure est donné en utilisant les [codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **EUR** représente **€uro**.  - `eventSchedule[array]`: Un événement associé à une programmation à l'aide de cette propriété ne doit pas avoir de propriétés `startDate` ou `endDate`. Celles-ci sont définies dans l'horaire associé, ce qui évite toute ambiguïté pour les clients qui utilisent les données. La propriété peut avoir des valeurs répétées pour spécifier différents calendriers (différents mois ou saisons).  - `eventStatus[array]`: Statut de l'événement  - `id[*]`: Identifiant unique de l'entité  - `isAccessibleForFree[boolean]`: Un drapeau signalant que l'objet, l'événement ou le lieu est accessible gratuitement.  . Model: [https://schema.org/isAccessibleForFree](https://schema.org/isAccessibleForFree)- `language[array]`: Liste des langages formels utilisés lors de l'événement, exprimés à partir de la norme IETF [BCP 47] (https://tools.ietf.org/html/bcp47)  . Model: [https://schema.org/language](https://schema.org/language)- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `maximumAttendeeCapacity[number]`: Le nombre total de personnes pouvant assister à l'événement à cet endroit.  - `name[string]`: Le nom de cet élément  - `openingHoursSpecification[array]`: Valeur structurée fournissant des informations sur les heures d'ouverture d'un lieu ou d'un certain service à l'intérieur d'un lieu.  . Model: [https://schema.org/openingHoursSpecification](https://schema.org/openingHoursSpecification)- `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `paymentAccepted[array]`: Paiement accepté si `isAccessibleForFree` est False. Combinaison d'une liste de codes actifs définis dans le modèle. Enum : "Cash, CreditCard, CryptoCurrency, other" (Espèces, cartes de crédit, crypto-monnaies, autres)  . Model: [https://schema.org/paymentAccepted](https://schema.org/paymentAccepted)- `performer[array]`: Acteur, présentateur, musicien ou groupe musical principal de l'événement  - `pitch[array]`: Pitch de l'événement. Chaque élément a un format basé sur l'[Internationalisation (i18N) - Recommandation du W3C pour le multilinguisme] (https://www.w3.org/TR/json-ld/#string-internationalization) intégrant tous les éléments dans une propriété unique (par exemple, le numéro 71). Chaque élément est représenté par une chaîne de caractères avec Language Value : Article Value.  - `priceSpecification[array]`: Une valeur structurée représentant un prix ou une fourchette de prix en fonction des catégories ou du public.  - `publicAccess[boolean]`: Un drapeau signalant que le lieu est ouvert aux visiteurs publics. Si cette propriété est omise, il n'y a pas de valeur booléenne par défaut.  . Model: [https://schema.org/publicAccess](https://schema.org/publicAccess)- `ratingValueAverage[number]`: Valeur d'évaluation de l'événement. Conseils d'utilisation : Utilisez des valeurs comprises entre 0 et 10 en fonction de vos normes. Il s'agit de la valeur moyenne de toutes les notes détaillées de l'attribut `starRatingDetailed`.  - `refPointOfInterest[array]`: Référence à tous les points d'intérêt [Point OfInterest] (https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) inclus dans l'événement. La liste des POI n'a pas d'ordre chronologique.  - `routeType[array]`: Liste des transports urbains (métro, bus, tramway, ...) disponibles à proximité de l'événement conformément à la norme GFTS [STOP] (https://developers.google.com/transit/gtfs/reference/#stopstxt). Une combinaison de valeurs. Enum:' bus, cableCar, cableTram, ferry, funiculaire, monorail, métro, train, tram, trolleybus'  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `slogan[string]`: Ligne d'en-tête de l'événement, correspondant au crochet de texte.  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `starRatingDetailed[object]`: Les notes détaillées par étoiles qui ont conduit à la valeur moyenne exprimée dans la valeur de la note. Mode d'emploi : Une valeur structurée de 1 à 10 occurrences (étoiles) où chaque élément est une chaîne au format : `NumberOfSTar` : Pourcentage.  	- `1`:     
	- `10`:     
	- `2`:     
	- `3`:     
	- `4`:     
	- `5`:     
	- `6`:     
	- `7`:     
	- `8`:     
- `startDate[date-time]`: La date et l'heure de début de l'élément (au format ISO 8601).  . Model: [https://schema.org/startDate](https://schema.org/startDate)- `subCategory[array]`: Sous-catégorie de l'attribut `category`. Une combinaison de texte libre permettant de s'adapter à un contexte spécifique est proposée ci-dessous à titre d'exemple initial ou pour toute autre valeur requise par une application.  - `subEvent[array]`: Référence à une liste d'événements mineurs faisant partie de cet événement majeur  - `superEvent[*]`: Référence à l'événement majeur qui inclut cet événement  - `thematic[array]`: Une liste de mots-clés thématiques  - `title[string]`:  Titre de l'événement  - `touristType[string]`: Type de tourisme en fonction du segment et de la motivation du voyage.  . Model: [https://schema.org/Text](https://schema.org/Text)- `transportServices[array]`: Liste des transports privés disponibles à proximité de l'événement. Par exemple, taxi, uber, vtc, parking, navette.  - `type[string]`: Il doit s'agir d'un événement. Type d'entité NGSI  . Model: [https://schema.org/event](https://schema.org/event)- `url[uri]`: URL qui fournit une description ou des informations complémentaires sur cet élément  - `webSite[uri]`: Lien vers le site officiel pour plus d'informations  - `wheelChairAccessible[boolean]`: Accès possible pour les personnes à mobilité réduite  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Ce modèle de données est basé sur la norme UNE178503. Il est également compatible avec schema.org. Certains éléments de schema.org ont été adaptés dans ce fichier https://smart-data-models.github.io/data-models/schema-org.json. Ce type peut être utilisé seul pour décrire une destination touristique générale, ou être utilisé comme un type supplémentaire pour ajouter des propriétés touristiques à tout autre lieu. Une TouristDestination est définie comme un lieu qui contient ou est associé à une ou plusieurs TouristAttractions, souvent liées par un thème ou un intérêt similaire à un touristType particulier. L'OMT définit la Destination (destination principale d'un voyage touristique) comme le lieu visité qui est au cœur de la décision d'entreprendre le voyage.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Event:    
  description: 'Upcoming or past event associated with this place, organization, or action.'    
  properties:    
    accessPlan:    
      description: ' Text or Link to the access plan to the item'    
      type: string    
      x-ngsi:    
        type: Property    
    actor:    
      description: List of actors or music group    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
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
      description: List of person who wrote the composition    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    contactPoint:    
      description: The details to contact with the item    
      properties:    
        areaServed:    
          description: The geographic area where a service or offered item is provided. Supersedes serviceArea    
          type: string    
          x-ngsi:    
            type: Property    
        availabilityRestriction:    
          anyOf:    
            - description: Array of identifiers format of any NGSI entity    
              items:    
                maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
              type: array    
              x-ngsi:    
                type: Property    
            - description: Array of identifiers format of any NGSI entity    
              items:    
                format: uri    
                type: string    
              type: array    
              x-ngsi:    
                type: Property    
          description: This property links a contact point to information about when the contact point is not available. The details are provided using the Opening Hours Specification class    
          x-ngsi:    
            model: http://schema.org/hoursAvailable    
            type: Relationship    
        availableLanguage:    
          anyOf:    
            - anyOf:    
                - type: string    
                - items:    
                    type: string    
                  type: array    
          description: 'A language someone may use with or at the item, service or place. Please use one of the language codes from the IETF BCP 47 standard. It is implemented the Text option but it could be also Language'    
          x-ngsi:    
            model: http://schema.org/availableLanguage    
            type: Property    
        contactOption:    
          anyOf:    
            - type: string    
            - items:    
                type: string    
              type: array    
          description: An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers)    
          x-ngsi:    
            model: http://schema.org/contactOption    
            type: Property    
        contactType:    
          description: Contact type of this item    
          type: string    
          x-ngsi:    
            type: Property    
        email:    
          description: Email address of owner    
          format: idn-email    
          type: string    
          x-ngsi:    
            type: Property    
        faxNumber:    
          description: The fax number    
          type: string    
          x-ngsi:    
            model: http://schema.org/Text    
            type: Property    
        name:    
          description: The name of this item    
          type: string    
          x-ngsi:    
            type: Property    
        productSupported:    
          description: The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. 'iPhone') or a general category of products or services (e.g. 'smartphones')    
          type: string    
          x-ngsi:    
            model: http://schema.org/Text    
            type: Property    
        telephone:    
          description: Telephone of this contact    
          type: string    
          x-ngsi:    
            type: Property    
        url:    
          description: URL which provides a description or further information about this item    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/ContactPoint    
        type: Property    
    contentURL:    
      description: Specifies the URL to the official image or video of the Event for more information    
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
              properties:    
                article:    
                  type: string    
                origin:    
                  type: string    
                ratingValue:    
                  type: number    
                starRating:    
                  type: number    
              type: object    
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
    director:    
      description: List of director who manage the composition    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    doorTimeClose:    
      description: Doors closing time to access the show    
      type: string    
      x-ngsi:    
        type: Property    
    doorTimeOpen:    
      description: Doors opening time to access the show    
      type: string    
      x-ngsi:    
        type: Property    
    duration:    
      description: 'The duration of each show. The unit code (text) of measurement is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **HUR** represents **Hours**'    
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
      description: The end date and time of the item (in ISO 8601 date format).    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/endDate    
        type: Property    
    eventPriceFrom:    
      description: 'Min Price. The unit code (text) of measurement is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **EUR** represents **€uro**'    
      type: number    
      x-ngsi:    
        type: Property    
    eventPriceTo:    
      description: 'Max Price. The unit code (text) of measurement is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **EUR** represents **€uro**'    
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
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    eventStatus:    
      description: Event Status regarding this event    
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
    maximumAttendeeCapacity:    
      description: The total number of people who can attend to the Event at that location    
      type: number    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    openingHoursSpecification:    
      description: A structured value providing information about the opening hours of a place or a certain service inside a place    
      items:    
        properties:    
          closes:    
            description: ' 	The closing hour of the place or service on the given day(s) of the week'    
            format: time    
            type: string    
            x-ngsi:    
              type: Property    
          dayOfWeek:    
            anyOf:    
              - description: Array of days of the week    
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
                x-ngsi:    
                  type: Property    
              - description: Array of days of the week    
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
                x-ngsi:    
                  type: Property    
            description: 'The day of the week for which these opening hours are valid. URLs from GoodRelations (http://purl.org/goodrelations/v1) are used (for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday plus a special entry for PublicHolidays)'    
            type: string    
            x-ngsi:    
              model: http://schema.org/dayOfWeek    
              type: Property    
          opens:    
            description: The opening hour of the place or service on the given day(s) of the week    
            format: time    
            type: string    
            x-ngsi:    
              type: Property    
          validFrom:    
            anyOf:    
              - description: ""    
                format: date    
                type: string    
                x-ngsi:    
                  model: http://schema.org/Date    
                  type: Property    
              - description: ""    
                format: date-time    
                type: string    
                x-ngsi:    
                  model: http://schema.org/DateTime    
                  type: Property    
            description: 'The date when the item becomes valid. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format'    
            x-ngsi:    
              type: Property    
          validThrough:    
            anyOf:    
              - description: ""    
                format: date    
                type: string    
                x-ngsi:    
                  model: http://schema.org/Date    
                  type: Property    
              - description: ""    
                format: date-time    
                type: string    
                x-ngsi:    
                  model: http://schema.org/DateTime    
                  type: Property    
            description: 'The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format'    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
      minItems: 1    
      type: array    
      x-ngsi:    
        model: https://schema.org/openingHoursSpecification    
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
      description: Main actor or presenter or musician or musical group of the event    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    pitch:    
      description: "Pitch of the Event. Each items have the format based on the [Internationalization (i18N) - W3C recommendation for multilanguage](https://www.w3.org/TR/json-ld/#string-internationalization) integrating all items in a single property (ex number 71). Each item is represented by a string with Language Value : Article Value. "    
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
      description: A structured value representing a price or price range depending categories or public    
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
      description: A flag to signal that the Place is open to public visitors. If this property is omitted there is no assumed default boolean value    
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
      description: 'Reference to all the Point Of interest [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) included in the Event. The POI list does not have a chronological order'    
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
    slogan:    
      description: 'Event header line, matches the text hook. '    
      type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
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
      description: The start date and time of the item (in ISO 8601 date format).    
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
      description: Reference to a list of Minor Events that are part of this major Event    
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
      type: array    
      x-ngsi:    
        type: Property    
    superEvent:    
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
      description: Reference to the Major Event that includes this Event    
      x-ngsi:    
        type: Property    
    thematic:    
      description: A list of thematic as keywords    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    title:    
      description: ' Title of the Event'    
      type: string    
      x-ngsi:    
        type: Property    
    touristType:    
      description: Type of tourism depending on the segment and the motivation of the trip.    
      enum:    
        - ADVENTURE TOURISM    
        - ASTRONOMY TOURISM    
        - BACKPACKING TOURISM    
        - BEACH AND SUN TOURISM    
        - BEER TOURISM    
        - BIRDING TOURISM    
        - BULLFIGHTING TOURISM    
        - BUSINESS    
        - COMMUNITY-BASED TOURISM    
        - CRUISE TOURISM    
        - CULTURAL TOURISM    
        - CYCLING TOURISM    
        - DIVING TOURISM    
        - ECOTOURISM    
        - EVENTS AND FESTIVALS TOURISM    
        - FAMILY TOURISM    
        - FILM TOURISM    
        - FISHING TOURISM    
        - FOOD TOURISM    
        - GAMBLING TOURISM    
        - GEOLOGICAL TOURISM    
        - HERITAGE TOURISM    
        - HUNTING TOURISM    
        - INDUSTRIAL TOURISM    
        - LANGUAGE TOURISM    
        - LGTBI TOURISM    
        - LUXURY TOURISM    
        - MEDICAL TOURISM    
        - MEMORIAL TOURISM    
        - MICE TOURISM    
        - NATURE TOURISM    
        - OLIVE OIL TOURISM    
        - PARTY TOURISM    
        - PHOTOGRAPHY TOURISM    
        - RELIGIOUS TOURISM    
        - ROMANTIC TOURISM    
        - RURAL TOURISM    
        - SAFARI TOURISM    
        - SAILING TOURISM    
        - SENIOR TOURISM    
        - SHOPPING TOURISM    
        - SHORT BREAK TOURISM    
        - SINGLES TOURISM    
        - SPORTS TOURISM    
        - TOURISM    
        - TREKKING TOURISM    
        - URBAN TOURISM    
        - WATER SPORTS TOURISM    
        - WEDDING & HONEYMOON TOURISM    
        - WELLNESS TOURISM    
        - WHISKY TOURISM    
        - WINE TOURISM    
        - WINTER SPORTS TOURISM    
        - WOMEN TOURISM    
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
      description: It has to be Event. NGSI entity type    
      enum:    
        - Event    
      type: string    
      x-ngsi:    
        model: https://schema.org/event    
        type: Property    
    url:    
      description: URL which provides a description or further information about this item    
      format: uri    
      type: string    
      x-ngsi:    
        type: Property    
    webSite:    
      description: Link to the official website for more information    
      format: uri    
      type: string    
      x-ngsi:    
        type: Property    
    wheelChairAccessible:    
      description: Access possible for Person with Reduced Mobility    
      type: boolean    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.TourismDestinations/blob/master/Event/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.TourismDestinations/Event/schema.json    
  x-model-tags: ""    
  x-version: 0.2.0    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### Événement Valeurs clés de l'INSIG-v2 Exemple  
Voici un exemple d'événement au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### Événement NGSI-v2 normalisé Exemple  
Voici un exemple d'événement au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### Événement Valeurs clés NGSI-LD Exemple  
Voici un exemple d'événement au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### Événement NGSI-LD normalisé Exemple  
Voici un exemple d'événement au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
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
        "https://raw.githubusercontent.com/smart-data-models/dataModel.TourismDestinations/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
