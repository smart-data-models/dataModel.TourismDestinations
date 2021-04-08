Entität: Ereignis  
=================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.TourismDestinations/blob/master/Event/LICENSE.md)  
Globale Beschreibung: **Kommendes oder vergangenes Ereignis, das mit diesem Ort, dieser Organisation oder dieser Aktion verbunden ist.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `endDate`: Das Enddatum und die Uhrzeit des Elements (im ISO 8601-Datumsformat).  - `id`: Eindeutiger Bezeichner der Entität  - `isAccessibleForFree`: Eine Flagge, die signalisiert, dass der Gegenstand, das Ereignis oder der Ort kostenlos zugänglich ist.  - `location`:   - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `publicAccess`: Ein Flag, das signalisiert, dass der Ort für öffentliche Besucher geöffnet ist. Wenn diese Eigenschaft weggelassen wird, gibt es keinen angenommenen booleschen Standardwert  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `startDate`: Das Startdatum und die Uhrzeit des Elements (im ISO 8601-Datumsformat).  - `touristType`: Die Art des Tourismus hängt vom Segment und der Motivation der Reise ab.  - `type`: Es muss Ereignis sein  - `url`: Url mit Bild, das sich auf den Artikel bezieht    
Erforderliche Eigenschaften  
- `id`  - `type`    
Dieses Datenmodell basiert auf dem Standard UNE178503. Es ist auch mit schema.org kompatibel. Einige der Elemente von schema.org wurden in dieser Datei angepasst https://smart-data-models.github.io/data-models/schema-org.json. Dieser Typ kann allein verwendet werden, um ein allgemeines TouristDestination zu beschreiben, oder er kann als zusätzlicherTyp verwendet werden, um tourismusrelevante Eigenschaften zu jedem anderen Ort hinzuzufügen. Ein TouristDestination ist definiert als ein Ort, der eine oder mehrere TouristAttractions enthält oder mit ihnen verbunden ist, die oft durch ein ähnliches Thema oder Interesse mit einem bestimmten TouristType verbunden sind. Die UNWTO definiert Destination (Hauptziel einer touristischen Reise) als den besuchten Ort, der für die Entscheidung, die Reise zu unternehmen, zentral ist.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Event:    
  description: 'Upcoming or past event associated with this place, organization, or action.'    
  properties:    
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
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/areaServed'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/adddress    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    endDate:    
      description: 'The end date and time of the item (in ISO 8601 date format).'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/endDate    
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
      type: Property    
    isAccessibleForFree:    
      description: 'A flag to signal that the item, event, or place is accessible for free.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/isAccessibleForFree    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
      title: 'GeoJSON Geometry'    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *event_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    publicAccess:    
      description: 'A flag to signal that the Place is open to public visitors. If this property is omitted there is no assumed default boolean value'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/publicAccess    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    startDate:    
      description: 'The start date and time of the item (in ISO 8601 date format).'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/startDate    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'It has to be Event'    
      enum:    
        - Event    
      type: Property    
      x-ngsi:    
        model: https://schema.org/event    
    url:    
      description: 'Url with image related to the item'    
      format: uri    
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### Ereignis NGSI-v2-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein Event im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "uri:ngsi:event:1",  
  "type": "Event",  
  "name": "Concierto de Revólver",  
  "addressLocality": "Salamanca",  
  "postalCode": "37008",  
  "streetAddress": "Calle Monte Olivete, s/n",  
  "startDate": "2019-06-08T21:00:00",  
  "endDate": "2019-06-08T23:00:00",  
  "url": "https://www.notikumi.com/2019/6/8/evento-de-revolver-en-salamanca",  
  "offeredBy": {  
    "type": "Organization",  
    "name": "Notikumi",  
    "url": "https://www.notikumi.com/"  
  },  
  "touristType": "EVENTS AND FESTIVALS TOURISM"  
}  
```  
#### Ereignis NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein Ereignis im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und gibt die Kontextdaten einer einzelnen Entität zurück.  
```json  
{  
  "id": {  
    "type": "string",  
    "value": "uri:ngsi:event:1"  
  },  
  "type": {  
    "type": "string",  
    "value": "Event"  
  },  
  "name": {  
    "type": "string",  
    "value": "Concierto de Revólver"  
  },  
  "addressLocality": {  
    "type": "string",  
    "value": "Salamanca"  
  },  
  "postalCode": {  
    "type": "string",  
    "value": "37008"  
  },  
  "streetAddress": {  
    "type": "string",  
    "value": "Calle Monte Olivete, s/n"  
  },  
  "startDate": {  
    "type": "string",  
    "value": "2019-06-08T21:00:00"  
  },  
  "endDate": {  
    "type": "string",  
    "value": "2019-06-08T23:00:00"  
  },  
  "url": {  
    "type": "string",  
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
    "type": "string",  
    "value": "EVENTS AND FESTIVALS TOURISM"  
  }  
}  
```  
#### Ereignis NGSI-LD-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein Event im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "uri:ngsi:event:1",  
  "type": "Event",  
  "name": "Concierto de Rev\u00f3lver",  
  "addressLocality": "Salamanca",  
  "postalCode": "37008",  
  "streetAddress": "Calle Monte Olivete, s/n",  
  "startDate": "2019-06-08T21:00:00",  
  "endDate": "2019-06-08T23:00:00",  
  "url": "https://www.notikumi.com/2019/6/8/evento-de-revolver-en-salamanca",  
  "offeredBy": {  
    "type": "Organization",  
    "name": "Notikumi",  
    "url": "https://www.notikumi.com/"  
  },  
  "touristType": "EVENTS AND FESTIVALS TOURISM",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### Ereignis NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein Ereignis im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": {  
    "type": "string",  
    "value": "uri:ngsi:event:1"  
  },  
  "type": {  
    "type": "string",  
    "value": "Event"  
  },  
  "name": {  
    "type": "string",  
    "value": "Concierto de Revolver"  
  },  
  "addressLocality": {  
    "type": "string",  
    "value": "Salamanca"  
  },  
  "postalCode": {  
    "type": "string",  
    "value": "37008"  
  },  
  "streetAddress": {  
    "type": "string",  
    "value": "Calle Monte Olivete, s/n"  
  },  
  "startDate": {  
    "type": "string",  
    "value": "2019-06-08T21:00:00"  
  },  
  "endDate": {  
    "type": "string",  
    "value": "2019-06-08T23:00:00"  
  },  
  "url": {  
    "type": "string",  
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
    "type": "string",  
    "value": "EVENTS AND FESTIVALS TOURISM"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
