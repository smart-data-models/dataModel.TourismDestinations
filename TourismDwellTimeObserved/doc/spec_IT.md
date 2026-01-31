<!-- 10-Header -->
  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entità: TourismDwellTimeObserved  
================================
<!-- /10-Header -->
  
<!-- 15-License -->
  

[Licenza aperta](https://github.com/smart-data-models//dataModel.TourismDestinations/blob/master/TourismDwellTimeObserved/LICENSE.md)  

[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->
  
<!-- 20-Description -->
  

Global description: **Osservazione oraria della durata di permanenza dei visitatori (durata di permanenza) in una posizione specifica (comune), segmentata per nazionalità e fascia di durata di permanenza.**  

version: 0.0.1  
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->
  


## Elenco delle proprietà  


<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o formati/modello diversi</sub></sup>  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)  
	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La località in cui si trova l'indirizzo di via e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestito dal governo locale  
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'indirizzo di via  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: Numero che identifica una proprietà specifica in una strada pubblica  
- `aggregationType[string]`: Tipo di aggregazione utilizzato per questa osservazione oraria  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `alternateName[string]`: Un nome alternativo per questo elemento  
- `areaServed[string]`: L'area geografica in cui viene fornito un servizio o un articolo offerto  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `dataProvider[string]`: Fornitore dei dati  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `dateCreated[date-time]`: Timestamp di creazione dell'entità. Questo verrà solitamente assegnato dalla piattaforma di archiviazione  
- `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Questo di solito verrà assegnato dalla piattaforma di archiviazione  
- `dateObserved[date-time]`: Data e ora dell'osservazione (ISO8601 UTC)  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)  
- `description[string]`: Una descrizione di questo articolo  
- `dwellTimeRange[string]`: Intervallo di tempo di soggiorno in minuti (ad es. 0-5, 5-15, 30-60, 120+)  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `hour[number]`: Ora del giorno (0-23) per questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `id[*]`: Identificatore univoco dell'entità  
- `location[*]`: Riferimento Geojson all'elemento. Può essere Punto, LineString, Poligono, MultiPunto, MultiLineString o MultiPoligono  
- `locationCode[string]`: Codice ufficiale della località/comune (ad es. DICOFRE)  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `locationName[string]`: Nome della località/comune  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `name[string]`: Il nome di questo elemento  
- `nationality[string]`: Nazionalità dei visitatori. Codice paese ISO 3166-1 alpha-2  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `nationalityName[string]`: Nome completo del paese di nazionalità (opzionale)  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `owner[array]`: Una lista che contiene una sequenza di caratteri codificata in JSON che fa riferimento agli Id univoci del/dei proprietario/i  
- `seeAlso[*]`: Elenco di uri che puntano a risorse aggiuntive sull'elemento  
- `source[string]`: Fonte originale dei dati come URL  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `totalVisitors[number]`: Numero totale di visitatori in tutti gli intervalli di tempo di soggiorno per questa ora  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `type[string]`: Tipo di entità NGSI. Deve essere TourismDwellTimeObserved  
- `visitorCount[number]`: Numero di visitatori in questo intervallo di tempo di soggiorno  . Model: [https://schema.org/Number](https://schema.org/Number)  
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

Proprietà richieste  
- `dataOsservata`  
- `dwellTimeRange` non richiede traduzione, tuttavia una possibile traduzione potrebbe essere: 
- `intervalloDiTempoDiSoggiorno`  
- `ora`  
- `id`  
- `posizione`  
- `codicePosizione`  
- `nazionalità`  
- `tipo`  
- `contoVisitatori`  
<!-- /35-RequiredProperties -->
  
<!-- 40-NotesYaml -->
  
<!-- /40-NotesYaml -->
  
<!-- 50-DataModelHeader -->
  

## Descrizione del modello di dati delle proprietà  

Ordinati in ordine alfabetico (clicca per i dettagli)  
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
  

## Payload di esempio  

#### Tempo di soggiorno del turismo osservato Esempio di valori chiave NGSI-v2  

Ecco un esempio di TourismDwellTimeObserved in formato JSON come chiavi-valori. Ciò è compatibile con NGSI-v2 quando si utilizza `options=keyValues` e restituisce i dati di contesto di un'entità individuale.  
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

#### Tempo di permanenza del turismo osservato Esempio normalizzato NGSI-v2  

Ecco un esempio di TourismDwellTimeObserved in formato JSON come normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di un'entità individuale.  
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

#### Tempo di soggiorno del turismo osservato Esempio di valori chiave NGSI-LD  

Ecco un esempio di TourismDwellTimeObserved in formato JSON-LD come chiavi-valori. Ciò è compatibile con NGSI-LD quando si utilizza `options=keyValues` e restituisce i dati di contesto di un'entità individuale.  
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

#### Tempo di soggiorno del turismo osservato Esempio normalizzato NGSI-LD  

Ecco un esempio di TourismDwellTimeObserved in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di un'entità individuale.  
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
  
