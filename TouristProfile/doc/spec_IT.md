<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: ProfiloTuristico  
========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.TourismDestinations/blob/master/TouristProfile/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Descrizione di un profilo turistico basato sulle caratteristiche della persona, del viaggio, della scelta del soggiorno e della spesa durante la permanenza nella destinazione.**  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.    
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `ageRange[object]`: Fascia d'età della persona profilata  	- `range[string]`: Valore di ageRange. Utilizza gli intervalli definiti da sortingOrder    
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `avgDailyAccommodationAndBoardExpenditure[object]`: Intervallo dell'importo medio giornaliero fatturato dalla struttura ricettiva in concetti di vitto e alloggio  	- `range[string]`: Valore di avgDailyAccommodationAndBoardExpenditure. Utilizza gli intervalli definiti da sortingOrder    
- `avgDailyExpenditure[object]`: Intervallo dell'importo medio giornaliero fatturato dalla struttura ricettiva  	- `range[string]`: Valore di avgDailyExpenditure. Utilizza gli intervalli definiti da sortingOrder    
- `avgDailyExtraExpenditure[object]`: Intervallo dell'importo medio giornaliero fatturato dalla struttura ricettiva in concetti supplementari  	- `range[string]`: Valore di avgDailyExtraExpenditure. Utilizza gli intervalli definiti da sortingOrder    
- `board[string]`: Tipo di scheda solitamente riservato. Enum:'RO, BB, HB, FB, AI'  - `bookingChannel[string]`: Canale utilizzato dal turista per la prenotazione  - `country[string]`: Paese di nazionalità - https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2  - `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `gender[string]`: Genere della persona profilata. Enum:'Femmina, Maschio'  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `lodgingCategory[string]`: Categoria abituale dell'alloggio. Enum:'1, 1 Superior, 2, 2 Superior, 3, 3 Superior, 4, 4 Superior, 5, 5 Superior'  - `lodgingSize[object]`: Dimensioni dell'alloggio in numero di stanze  	- `range[string]`: Valore di lodgingSize. Utilizza gli intervalli definiti da sortingOrder    
- `lodgingType[string]`: Solito tipo di alloggio per il soggiorno. Potrebbe fare riferimento a UNE178506 in futuro. Enum:'Hotel, Resort, Ostello, Motel, B&B, Aparthotel, Lodge'.  - `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `reservationLeadTime[object]`: Intervallo di giorni tra la prenotazione e il check-in  	- `range[string]`: Valore di reservationLeadTime. Utilizza gli intervalli definiti da sortingOrder    
- `roomOfStayType[string]`: Tipo abituale della camera prenotata. Enum:'Appartamento, Bungalow, Studio, Singola, Doppia, Famiglia, Junior Suite, Senior/Executive Suite, Royal/Presidential Suite'.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `stayLength[object]`: Intervallo del numero di notti di soggiorno  	- `range[string]`: Valore di stayLength. Utilizza gli intervalli definiti da sortingOrder    
- `totalAccommodationAndBoardExpenditure[object]`: Intervallo dell'importo totale fatturato dalla struttura ricettiva in concetti di vitto e alloggio  	- `range[string]`: Valore di totalAccommodationAndBoardExpenditure. Utilizza gli intervalli definiti da sortingOrder    
- `totalExpenditure[object]`: Intervallo dell'importo totale fatturato dalla struttura ricettiva  	- `range[string]`: Valore di TotalExpenditure. Utilizza gli intervalli definiti da sortingOrder    
- `totalExtraExpenditure[object]`: Intervallo dell'importo totale fatturato dalla struttura ricettiva in concetti extra  	- `range[string]`: Valore di totalExtraExpenditure. Utilizza gli intervalli definiti da sortingOrder    
- `travelPartyComposition[string]`: Composizione del gruppo di viaggio in base al numero di adulti e bambini. Enum:'Single, Genitore single, Famiglia, Coppia, Amici/Parenti'.  - `type[string]`: Tipo di entità NGSI. Deve essere ProfiloTuristico  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
L'entità TouristProfile contiene una descrizione del profilo ricercato di un certo tipo di turista in base ai dettagli della sua prenotazione e del suo soggiorno in una struttura ricettiva.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
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
## Esempi di payload  
#### Profilo turistico Valori chiave NGSI-v2 Esempio  
Ecco un esempio di profilo turistico in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### Profilo turistico NGSI-v2 normalizzato Esempio  
Ecco un esempio di TouristProfile in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
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
#### Profilo turistico Valori chiave NGSI-LD Esempio  
Ecco un esempio di profilo turistico in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### Profilo turistico NGSI-LD normalizzato Esempio  
Ecco un esempio di TouristProfile in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
