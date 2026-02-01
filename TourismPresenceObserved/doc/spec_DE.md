<!-- 10-Header -->
  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entität: TourismPresenceObserved  
===============================
<!-- /10-Header -->
  
<!-- 15-License -->
  

[Offene Lizenz](https://github.com/smart-data-models//dataModel.TourismDestinations/blob/master/TourismPresenceObserved/LICENSE.md)  

[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->
  
<!-- 20-Description -->
  

Global description: **Stündliche Beobachtung der Besucherpräsenz an einem bestimmten Ort (Gemeinde), nach Nationalität segmentiert. Jede Entität repräsentiert eine Stunde Beobachtung.**  

version: 0.0.1  
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->
  


## Liste der Eigenschaften  


<sup><sub>[*] Wenn es in einem Attribut keinen Typ gibt, liegt das daran, dass es mehrere Typen oder unterschiedliche Formate/Muster haben könnte</sub></sup>  
- `address[object]`: Die Postadresse  . Model: [https://schema.org/address](https://schema.org/address)  
	- `addressCountry[string]`: Das Land. Zum Beispiel Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: Die Ortschaft, in der sich die Straßenadresse befindet und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: Die Region, in der sich die Ortschaft befindet und die im Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird  
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: Die Straßenadresse  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: Nummer, die ein bestimmtes Grundstück auf einer öffentlichen Straße identifiziert  
- `aggregationType[string]`: Art der Aggregation, die für diese stündliche Beobachtung verwendet wird  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `areaServed[string]`: Das geografische Gebiet, auf das sich der Dienst oder die Daten beziehen  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `dataProvider[string]`: Anbieter der harmonisierten Datenentität  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `dateCreated[date-time]`: Zeitstempel für die Erstellung der Entität. Dieser wird in der Regel von der Speicherplattform zugewiesen  
- `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform zugewiesen  
- `dateObserved[date-time]`: Datum und Uhrzeit dieser stündlichen Beobachtung im ISO8601-UTC-Format. Es sollte die Mitte der Stunde darstellen (z. B. 10:30 für 10:00–10:59)  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)  
- `description[string]`: Eine Beschreibung dieses Artikels  
- `district[string]`: Verwaltungsbezirk des Ortes  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `hour[number]`: Stunde des Tages (0–23) für diese Beobachtung  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `id[*]`: Eindeutiger Identifikator der Entität  
- `location[*]`: Geojson-Referenz zum Artikel. Es kann Punkt, Linienzug, Polygon, MultiPunkt, MultiLinienzug oder MultiPolygon sein  
- `locationCode[string]`: Offizieller Code des Ortes/Gemeinde (z. B. DICOFRE-Code in Portugal)  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `locationName[string]`: Name des Ortes/Gemeinde  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `name[string]`: Der Name dieses Artikels  
- `nationality[string]`: Staatsangehörigkeit der Besucher als ISO-3166-1-alpha-2-Ländercode (z. B. ES, FR, PT)  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `nationalityName[string]`: Vollständiger Name des Nationalitätslandes (optional, für bessere Lesbarkeit)  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `owner[array]`: Eine Liste, die eine JSON-kodierte Zeichenfolge enthält, die auf die eindeutigen IDs des/die Besitzer(s) verweist  
- `seeAlso[*]`: Liste von URIs, die auf zusätzliche Ressourcen über das Element verweisen  
- `source[string]`: Ursprüngliche Quelle der Daten als URL  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `type[string]`: NGSI-Entitätentyp. Es muss TourismPresenceObserved sein  
- `visitorCount[number]`: Anzahl der Besucher, die während dieser spezifischen Stunde beobachtet wurden  . Model: [https://schema.org/Number](https://schema.org/Number)  
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

Erforderliche Eigenschaften  
- `DatumDerBeobachtung`  
- `Stunde`  
- `id`  
- `Ort`  
- `Standortcode`  
- `Nationalität`  
- `Typ`  
- `besucherzahl`  
<!-- /35-RequiredProperties -->
  
<!-- 40-NotesYaml -->
  
<!-- /40-NotesYaml -->
  
<!-- 50-DataModelHeader -->
  

## Datenmodellbeschreibung von Eigenschaften  

Nach dem Alphabet sortiert (klicken für Details)  
<!-- /50-DataModelHeader -->
  
<!-- 60-ModelYaml -->
  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
TourismPresenceObserved:    
  description: Hourly observation of visitor presence at a specific location (municipality), segmented by nationality. Each entity represents one hour of observation.    
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
        model: https://schema.org/Text    
        type: Property    
    areaServed:    
      description: The geographic area where the service or data applies    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: Provider of the harmonised data entity    
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
      description: Date and time of this hourly observation in ISO8601 UTC format. It should represent the middle of the hour (e.g. 10:30 for 10:00–10:59)    
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
    district:    
      description: Administrative district of the location    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    hour:    
      description: Hour of the day (0–23) for this observation    
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
      description: Official code of the location/municipality (e.g. DICOFRE code in Portugal)    
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
      description: Nationality of visitors expressed as ISO 3166-1 alpha-2 country code (e.g. ES, FR, PT)    
      pattern: ^[A-Z]{2}$    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    nationalityName:    
      description: Full name of the nationality country (optional, for human readability)    
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
    type:    
      description: NGSI entity type. It has to be TourismPresenceObserved    
      enum:    
        - TourismPresenceObserved    
      type: string    
      x-ngsi:    
        type: Property    
    visitorCount:    
      description: Number of visitors observed during this specific hour    
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
    - visitorCount    
    - hour    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.TourismDestinations/blob/master/TourismPresenceObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Tourism/TourismPresenceObserved/schema.json    
  x-model-tags: tourism,presence,statistics    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->
  
<!-- 70-MiddleNotes -->
  
<!-- /70-MiddleNotes -->
  
<!-- 80-Examples -->
  

## Beispielnutzlasten  

#### TourismusPräsenzBeobachtet NGSI-v2 Schlüssel-Wert-Beispiel  

Hier ist ein Beispiel für ein TourismPresenceObserved im JSON-Format als Schlüssel-Werte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und es die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:TourismPresenceObserved:PT:OUTROS-GDPR:IN:20241231T10",  
  "type": "TourismPresenceObserved",  
  "dateObserved": "2024-12-31T10:30:00Z",  
  "hour": 10,  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      0,  
      0  
    ]  
  },  
  "locationCode": "Outros - GDPR",  
  "locationName": "Outros - GDPR",  
  "nationality": "IN",  
  "nationalityName": "India",  
  "visitorCount": 54,  
  "aggregationType": "hourly_sum",  
  "dataProvider": "INE"  
}  
```  
</details>  

#### TourismusPräsenzBeobachtet NGSI-v2 normalisiertes Beispiel  

Hier ist ein Beispiel für ein TourismPresenceObserved im JSON-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und gibt die Kontextdaten einer einzelnen Entität zurück.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:TourismPresenceObserved:PT:OUTROS-GDPR:IN:20241231T10",  
  "type": "TourismPresenceObserved",  
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
      "coordinates": [  
        0,  
        0  
      ]  
    }  
  },  
  "locationCode": {  
    "type": "Property",  
    "value": "Outros - GDPR"  
  },  
  "locationName": {  
    "type": "Property",  
    "value": "Outros - GDPR"  
  },  
  "nationality": {  
    "type": "Property",  
    "value": "IN"  
  },  
  "nationalityName": {  
    "type": "Property",  
    "value": "India"  
  },  
  "visitorCount": {  
    "type": "Property",  
    "value": 54  
  },  
  "aggregationType": {  
    "type": "Property",  
    "value": "hourly_sum"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "INE"  
  }  
}  
```  
</details>  

#### TourismusPräsenzBeobachtet NGSI-LD Schlüssel-Wert-Beispiel  

Hier ist ein Beispiel für ein TourismPresenceObserved im JSON-LD-Format als Schlüssel-Wert-Paare. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und es die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:TourismPresenceObserved:PT:OUTROS-GDPR:IN:20241231T10",  
  "type": "TourismPresenceObserved",  
  "dateObserved": "2024-12-31T10:30:00Z",  
  "hour": 10,  
  "location": {  
    "type": "Point",  
    "coordinates": [0, 0]  
  },  
  "locationCode": "Outros - GDPR",  
  "locationName": "Outros - GDPR",  
  "nationality": "IN",  
  "nationalityName": "India",  
  "visitorCount": 54,  
  "aggregationType": "hourly_sum",  
  "dataProvider": "INE",  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://smart-data-models.github.io/dataModel.Transportation/context.jsonld"  
  ]  
}  
```  
</details>  

#### TourismusPräsenzBeobachtet NGSI-LD normalisiertes Beispiel  

Hier ist ein Beispiel für ein TourismPresenceObserved im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und es die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:TourismPresenceObserved:PT:OUTROS-GDPR:IN:20241231T10",  
  "type": "TourismPresenceObserved",  
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
      "coordinates": [0, 0]  
    }  
  },  
  "locationCode": {  
    "type": "Property",  
    "value": "Outros - GDPR"  
  },  
  "locationName": {  
    "type": "Property",  
    "value": "Outros - GDPR"  
  },  
  "nationality": {  
    "type": "Property",  
    "value": "IN"  
  },  
  "nationalityName": {  
    "type": "Property",  
    "value": "India"  
  },  
  "visitorCount": {  
    "type": "Property",  
    "value": 54  
  },  
  "aggregationType": {  
    "type": "Property",  
    "value": "hourly_sum"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "INE"  
  },  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://smart-data-models.github.io/dataModel.Transportation/context.jsonld"  
  ]  
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
  
