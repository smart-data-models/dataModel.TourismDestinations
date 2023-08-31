<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: ConsumoComportamento  
============================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.TourismDestinations/blob/master/ConsumptionBehaviour/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Questo modello è stato progettato per registrare e tracciare il consumo di varie risorse come elettricità, gasolio e acqua in un periodo specifico.  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `endDate[string]`: Proprietà. Data di fine del consumo.  - `finalMeasurement[number]`: Proprietà. Misurazione finale della risorsa.  - `id[*]`: Identificatore univoco dell'entità  - `initialMeasurement[number]`: Proprietà. Misurazione iniziale della risorsa.  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `resourceType[string]`: Proprietà. Tipo di risorsa consumata.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `sourceOfConsumption[*]`: Relazione. L'oggetto che genera il consumo.  - `startDate[string]`: Proprietà. Data di inizio del consumo.  - `type[string]`: Proprietà. Tipo di entità ConsumptionBehaviour.  - `usersInvolved[number]`: Proprietà. Numero di persone/utenti coinvolti nel consumo.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ConsumptionBehaviour:    
  description: 'This model is designed to record and track the consumption of various resources such as electricity, diesel, and water over a specified period.'    
  properties:    
    address:    
      description: The mailing address    
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
        district:    
          description: 'Property. A district is a type of administrative division that, in some countries, is managed by the local government'    
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
        streetNr:    
          description: Property. Number identifying a specific property on a public street    
          type: string    
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
    endDate:    
      description: Property. End date of the consumption.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    finalMeasurement:    
      description: Property. Final measurement of the resource.    
      type: number    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &consumptionbehaviour_-_properties_-_owner_-_items_-_anyof    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    initialMeasurement:    
      description: Property. Initial measurement of the resource.    
      type: number    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: GeoProperty. Geojson reference to the item. Point    
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
        - description: GeoProperty. Geojson reference to the item. LineString    
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
        - description: GeoProperty. Geojson reference to the item. Polygon    
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
        - description: GeoProperty. Geojson reference to the item. MultiPoint    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *consumptionbehaviour_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    resourceType:    
      description: Property. Type of resource consumed.    
      enum:    
        - Diesel    
        - Petrol    
        - Electricity    
        - Gas    
        - Water    
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
    sourceOfConsumption:    
      anyOf: *consumptionbehaviour_-_properties_-_owner_-_items_-_anyof    
      description: Relationship. The object that is generating the consumption.    
      x-ngsi:    
        type: Property    
    startDate:    
      description: Property. Start date of the consumption.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. Entity type ConsumptionBehaviour.    
      enum:    
        - ConsumptionBehaviour    
      type: string    
      x-ngsi:    
        type: Property    
    usersInvolved:    
      description: Property. Number of persons/users involved in the consumption.    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.TourismDestinations/blob/master/ConsumptionBehaviour/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.TourismDestinations/ConsumptionBehaviour/schema.json,    
  x-model-tags: 'TOURiLab, Sustainability'    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### ConsumoComportamento Valori chiave NGSI-v2 Esempio  
Ecco un esempio di ConsumptionBehaviour in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:ConsumptionBehaviour:VC17",  
    "type": "ConsumptionBehaviour",  
    "resourceType": "Diesel",  
    "sourceOfConsumption": "urn:ngsi-ld:Vehicle:VC0001",  
    "startDate": "2018-09-21T12:00:00Z",  
    "endDate": "2018-09-21T12:00:00Z",  
    "initialMeasurement": 455555,  
    "finalMeasurement": 456123,  
    "usersInvolved": 2  
}  
```  
</details>  
#### ConsumoComportamento NGSI-v2 normalizzato Esempio  
Ecco un esempio di ConsumptionBehaviour in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ConsumptionBehaviour:VC17",  
  "type": "ConsumptionBehaviour",  
  "resourceType": {  
    "type": "Text",  
    "value": "Diesel"  
  },  
  "sourceOfConsumption": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:Vehicle:VC0001"  
  },  
  "startDate": {  
    "type": "DateTime",  
    "value": "2018-09-21T12:00:00Z"  
  },  
  "endDate": {  
    "type": "DateTime",  
    "value": "2018-09-21T12:00:00Z"  
  },  
  "initialMeasurement": {  
    "type": "Number",  
    "value": 455555  
  },  
  "finalMeasurement": {  
    "type": "Number",  
    "value": 456123  
  },  
  "usersInvolved": {  
    "type": "Number",  
    "value": 2  
  }  
}  
```  
</details>  
#### ConsumoComportamento Valori chiave NGSI-LD Esempio  
Ecco un esempio di ConsumptionBehaviour in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ConsumptionBehaviour:VC17",  
  "type": "ConsumptionBehaviour",  
  "resourceType": "Diesel",  
  "sourceOfConsumption": "urn:ngsi-ld:Vehicle:VC0001",  
  "startDate": "2018-09-21T12:00:00Z",  
  "endDate": "2018-09-21T12:00:00Z",  
  "initialMeasurement": 455555,  
  "finalMeasurement": 456123,  
  "usersInvolved": 2,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.TourismDestinations/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### ConsumoComportamento NGSI-LD normalizzato Esempio  
Ecco un esempio di ConsumptionBehaviour in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "sourceOfConsumption": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:Vehicle:VC0001"  
  },  
  "startDate": {  
    "type": "Property",  
    "value": {  
      "@value": "2018-09-21T12:00:00Z",  
      "@type": "date-time"  
    }  
  },  
  "endDate": {  
    "type": "Property",  
    "value": {  
      "@value": "2018-09-21T12:00:00Z",  
      "@type": "date-time"  
    }  
  },  
  "initialMeasurement": {  
    "type": "Property",  
    "value": 455555  
  },  
  "finalMeasurement": {  
    "type": "Property",  
    "value": 456123  
  },  
  "usersInvolved": {  
    "type": "Property",  
    "value": 2  
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
