[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: ViaggioTuristico  
========================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.TourismDestinations/blob/master/TouristTrip/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Un viaggio turistico. Un itinerario creato di visite a uno o più luoghi di interesse (TouristAttraction/TouristDestination) spesso collegati da un tema, un'area geografica o un interesse simile a un particolare touristType. L'UNWTO definisce il viaggio turistico come il viaggio intrapreso dai visitatori **.  
versione: 0.0.3  

## Elenco delle proprietà  

- `accessPlan`: Testo o link al piano di accesso al viaggio.  - `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  - `audience`: Tipo di pubblico interessato da questo Viaggio. Una combinazione di testo libero (famiglia, adulto, bambini, adolescente, senior, tutto il pubblico, ...). Enum:'adulto, tutto il pubblico, bambini, famiglia, senior, adolescente'.  - `category`: Categoria del viaggio. Una combinazione di testo libero per rimanere flessibile a un contesto specifico è offerta di seguito come repository iniziale o qualsiasi altro valore necessario a un'applicazione. enum:'escursione, gastronomia, storia, museo, attività all'aperto, parchi e giardini, culto religioso, shopping, benessere'  - `contentURL`: Specifica l'URL dell'immagine o del video ufficiale del Viaggio per maggiori informazioni.  - `criticReview`: Recensione scritta o pubblicata da una fonte riconosciuta per le sue attività di revisione. Ogni voce ha un formato basato sulla [Internationalization (i18N) - W3C recommendation for multilanguage](https://www.w3.org/TR/json-ld/#string-internationalization) che integra tutte le voci in un'unica proprietà (ex numero 71). Ogni voce è rappresentata da una stringa con "Valore lingua" : "Valore articolo".  - `currencyAccepted`: Valuta accettata per il pagamento se `TripFree` è False. Una combinazione di un elenco di codici attivi definiti nel modello. [Norme ISO 4217](http://en.wikipedia.org/wiki/ISO_4217), [Criptovalute](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) , [Exchange Trading System](https://en.wikipedia.org/wiki/Local_exchange_trading_system)  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateLastReported`: Ultimo aggiornamento ufficiale dei dati in formato ISO 8601  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `description`: Descrizione dell'articolo  - `duration`: La durata di ogni spettacolo. Il codice dell'unità di misura (testo) è indicato utilizzando i [Codici comuni UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **HUR** rappresenta **ore**.  - `electricTransport`:  Elenco dei diversi tipi di trasporto elettrico proposti dalla città. Una combinazione di. Enum:'bicicletta elettrica, auto elettrica, moto elettrica, scooter elettrico'.  - `endDate`: Data e ora finale in formato ISO8601 UTC  - `id`: Identificatore univoco dell'entità  - `isAccessibleForFree`: Viaggio gratuito o a pagamento (Vero = gratuito / Falso = a pagamento).  - `itinerary`: Destinazioni o luoghi che compongono un viaggio. Per un viaggio in cui l'ordine delle destinazioni è importante, utilizzare ItemList per specificare l'ordine di inclusione nel viaggio.  - `language`:  Elenco del linguaggio formale utilizzato durante il Viaggio espresso dallo standard IETF [BCP 47](https://tools.ietf.org/html/bcp47)  - `location`: Riferimento Geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `locationName`: Nome della località di viaggio.  - `maximumAttendeeCapacity`: Il numero totale di persone che possono partecipare alla gita in quel luogo.  - `name`: Il nome di questo elemento.  - `openingHoursSpecification`: Un valore strutturato che fornisce informazioni sugli orari di apertura di un luogo o di un determinato servizio all'interno di un luogo.  - `owner`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `paymentAccepted`: Pagamento accettato se `TripFree` è Falso. Una combinazione di un elenco di codici attivi definiti nel modello. Enum:'Contanti, carta di credito, criptovaluta, altro'.  - `pitch`: Piazzola del viaggio. Ogni voce ha un formato basato su [Internationalization (i18N) - W3C recommandation for multilanguage] (https://www.w3.org/TR/json-ld/#string-internationalization) che integra tutte le voci in un'unica proprietà (es. numero 71). Ogni voce è rappresentata da una stringa con Valore lingua: Valore articolo.  - `priceSpecification`: Un valore strutturato che rappresenta un prezzo o una fascia di prezzo a seconda delle categorie o del pubblico.  - `ratingValueAverage`: Valore di valutazione dei viaggi. Linee guida per l'uso: Utilizzare valori da 0 a 10, a seconda degli standard. è il valore medio di tutti i punteggi dettagliati dell'attributo `starRatingDetailed`.  - `refPointOfInterest`: Riferimento a tutti i punti di interesse [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) inclusi nei viaggi. L'elenco dei POI non ha un ordine cronologico.  - `routeType`: Elenco dei trasporti urbani (metropolitana, autobus, tram, ...) disponibili nei pressi del viaggio secondo lo standard GFTS [STOP](https://developers.google.com/transit/gtfs/reference/#stopstxt). Una combinazione di valori. Enum:" autobus, cableCar, cableTram, traghetto, funicolare, monorotaia, metropolitana, treno, tram, filobus".  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `slogan`: Riga di intestazione del viaggio, corrisponde al gancio di testo.  - `source`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `starRatingDetailed`: Valutazione dettagliata delle stelle che ha portato al valore medio espresso nel ratingValue. Istruzioni per l'uso: Un valore strutturato da 1 a 10 occorrenze (Stelle) in cui ogni elemento è una stringa nel formato: `NumberOfSTar`: Percentuale.  - `startDate`: Data e ora di inizio in formato ISO8601 UTC  - `subCategory`: Sottocategoria dell'attributo `category`. Una combinazione di testo libero per rimanere flessibile a un contesto specifico è offerta qui di seguito come esempio iniziale o qualsiasi altro valore necessario a un'applicazione.  - `subTrip`: Riferimento a un elenco di viaggi minori che fanno parte di questo viaggio principale.  - `superTrip`: Riferimento al Viaggio Principale che include questo Viaggio.  - `thematic`: Un elenco di parole chiave tematiche  - `title`:  Titolo del viaggio.  - `touristType`: enumerazione di diversi tipi di turisti applicabili al TouristTrip  - `transportServices`: Elenco dei mezzi di trasporto privati disponibili nei pressi del Viaggio. Ad esempio taxi, uber, vtc, parcheggioShuttle  - `tripPriceFrom`: Prezzo minimo. Il codice dell'unità di misura (testo) è indicato utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **EUR** rappresenta **€uro**.  - `tripPriceTo`: Prezzo massimo. Il codice dell'unità di misura (testo) è indicato utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Ad esempio, **EUR** rappresenta **€uro**.  - `tripSchedule`: Programma di viaggio. Consente di impostare un programma per un periodo di tempo ripetuto, utilizzato per descrivere un viaggio che si verifica regolarmente. Per le restrizioni all'uso di questo attributo, vedere le note di esempio all'inizio della sezione.  - `tripStatus`: Stato del viaggio per questo viaggio. Enum:'cancellato, chiuso, finito, aperto, rinviato, riprogrammato, programmato, sospeso'.  - `type`: Deve essere TouristTrip. Tipo di entità NGSI.  - `webSite`: Link al sito web ufficiale per ulteriori informazioni.  - `wheelChairAccessible`: Accesso possibile per le persone con mobilità ridotta.    
Proprietà richieste  
- `id`  - `type`    
Questo modello di dati si basa sullo standard UNE178503. È anche compatibile con schema.org. Alcuni elementi di schema.org sono stati adattati in questo file https://smart-data-models.github.io/data-models/schema-org.json. Sono stati necessari piccoli aggiustamenti per mantenere la compatibilità con schema.org.  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
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
## Esempi di payload  
#### TouristTrip NGSI-v2 valori-chiave Esempio  
Ecco un esempio di TouristTrip in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### TouristTrip NGSI-v2 normalizzato Esempio  
Ecco un esempio di TouristTrip in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
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
#### TouristTrip Valori chiave NGSI-LD Esempio  
Ecco un esempio di TouristTrip in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
    "id": "urn:ngsi:touristTrip:1",  
    "type": "TouristTrip",  
    "accessPlan": "https://www.google.fr/maps/place/Mus%C3%A9e+du+Palais+Lascaris/@43.6976805,7.2750571,17z/data=!3m1!4b1!4m5!3m4!1s0x12cddabca1950653:0x8d425022ef476dde!8m2!3d43.6976766!4d7.2772458?hl=fr",  
    "address": {  
        "streetAddress": "15, rue Droite",  
        "postalCode": "06000",  
        "adressLocality": "Nice",  
        "addressCountry": "France",  
        "adressRegion": "Marseille Nice Avignon Aix - (06)"  
    },  
    "alternateName": "Palais Lascaris",  
    "areaServed": "Vieux Nice",  
    "audience": [  
        "allPublic"  
    ],  
    "category": [  
        "museum"  
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
    "currencyAccepted": [  
        "EUR",  
        "USD"  
    ],  
    "dateLastReported": "2020-03-17T08:45:00Z",  
    "description": "Le palais Lascaris est une ancienne demeure aristocratique de Nice datant de la premiere moiti du XVII sicle, aujourd'hui un musee des instruments de musique anciens",  
    "duration": 1.25,  
    "electricTransport": [  
        "electricBicycle",  
        "electricMotorBike"  
    ],  
    "endDate": "2021-12-31T00:00:00Z",  
    "image": "http://www.turismo.conil.org/PortalTurismo/DocTurismo.nsf/voTodosPorIdiomaUNID/4AC02453BEE8F5CDC125750400315F48/$FILE/IMGP2024.JPG",  
    "isAccessibleForFree": false,  
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
    "language": [  
        "french",  
        "english",  
        "spanish",  
        "german"  
    ],  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            43.6976766,  
            7.2772458  
        ]  
    },  
    "locationName": "Palais Lascaris",  
    "maximumAttendeeCapacity": 25,  
    "name": "Musee du Palais Lascaris",  
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
    "paymentAccepted": [  
        "Cash",  
        "CreditCard"  
    ],  
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
    "ratingValue": 8.5,  
    "routeType": [  
        "tram",  
        "subway",  
        "bus"  
    ],  
    "sameAs": "https://inventrip.com/conil/trip/1907",  
    "seeAlso": "https://www.nice.fr/fr/culture/musees-et-galeries/palais-lascaris-le-palais",  
    "slogan": "Une demeure aristocratique joyau du baroque et une remarquable collection d instruments de musiques anciens.",  
    "starRatingDetailed": {  
        "5": 92,  
        "4": 6,  
        "3": 2,  
        "2": 0,  
        "1": 0  
    },  
    "startDate": "2021-01-01T00:00:00Z",  
    "subCategory": [  
        "art",  
        "decorativeArts",  
        "history"  
    ],  
    "superTrip": "urn:ngsi-ld:Trip:Trip:MNCA-TRIP-NCE-VISTE-DES-MUSEES-NICE",  
    "thematic": [  
        "culture",  
        "museum",  
        "instrument",  
        "music",  
        "monument"  
    ],  
    "title": "Visite du Mus\u00e9e du Palais Lascaris",  
    "touristType": [  
        "FAMILY TOURISM",  
        "WATER SPORTS TOURISM",  
        "FOOD TOURISM",  
        "BEACH AND SUN TOURISM"  
    ],  
    "transportServices": [  
        "taxi"  
    ],  
    "tripPriceFrom": 0.0,  
    "tripPriceTo": 10.0,  
    "tripStatus": "opened",  
    "url": [  
        "https://www.spain.info/es/que-quieres/ciudades-pueblos/otros-destinos/conil_de_la_frontera.html"  
    ],  
    "video": "https://www.youtube.com/watch?v=IhnvlIzxPLg",  
    "webSite": "http://www.palais-lascaris.com",  
    "wheelChairAccessible": false,  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.TourismDestinations/master/context.jsonld"  
    ]  
}  
```  
#### TouristTrip NGSI-LD normalizzato Esempio  
Ecco un esempio di TouristTrip in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
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
                "review": {  
                    "type": "Property",  
                    "value": {  
                        "article": "Beau palais baroque qui contient des instruments de musique vari\u00c3\u00a9s dont une harpe-piano \u00c3\u00a9tonnante, et des portraits tr\u00c3\u00a8s beaux. A voir, surtout pour l'escalier et la d\u00c3\u00a9coration des salles.",  
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
    "@context": []  
}  
```  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
