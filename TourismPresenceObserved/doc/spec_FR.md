<!-- 10-Header -->
  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entité: TourismPresenceObserved  
===============================
<!-- /10-Header -->
  
<!-- 15-License -->
  

[Licence ouverte](https://github.com/smart-data-models//dataModel.TourismDestinations/blob/master/TourismPresenceObserved/LICENSE.md)  

[document généré automatiquement](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->
  
<!-- 20-Description -->
  

Global description: **Observation horaire de la présence des visiteurs à un endroit spécifique (commune), segmentée par nationalité. Chaque entité représente une heure d'observation.**  

version: 0.0.1  
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->
  


## Liste des propriétés  


<sup><sub>[*] Si il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)  
	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse de la rue, et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La région dans laquelle se trouve la localité, et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local  
	- `postOfficeBoxNumber[string]`: Le numéro de boîte postale pour les adresses de boîte postale. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: Numéro identifiant une propriété spécifique sur une rue publique  
- `aggregationType[string]`: Type d'agrégation utilisé pour cette observation horaire  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `alternateName[string]`: Un nom alternatif pour cet article  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `areaServed[string]`: La zone géographique où s'applique le service ou les données  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `dataProvider[string]`: Fournisseur de l'entité de données harmonisées  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `dateCreated[date-time]`: Horodatage de création d'entité. Ceci sera généralement alloué par la plateforme de stockage  
- `dateModified[date-time]`: Horodatage de la dernière modification de l'entité. Ceci sera généralement alloué par la plateforme de stockage  
- `dateObserved[date-time]`: Date et heure de cette observation horaire au format UTC ISO8601. Elle devrait représenter le milieu de l'heure (par exemple 10h30 pour 10h00-10h59)  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)  
- `description[string]`: Une description de cet article  
- `district[string]`: District administratif de l'emplacement  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `hour[number]`: Heure de la journée (0-23) pour cette observation  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `id[*]`: Identifiant unique de l'entité  
- `location[*]`: Référence Geojson de l'élément. Il peut s'agir d'un Point, LineString, Polygon, MultiPoint, MultiLineString ou MultiPolygon  
- `locationCode[string]`: Code officiel du lieu/commune (par exemple, code DICOFRE au Portugal)  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `locationName[string]`: Nom de l'emplacement/commune  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `name[string]`: Le nom de cet article  
- `nationality[string]`: Nationalité des visiteurs exprimée sous la forme d'un code de pays alpha-2 ISO 3166-1 (par exemple ES, FR, PT)  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `nationalityName[string]`: Nom complet du pays de nationalité (facultatif, pour une lisibilité humaine)  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `owner[array]`: Une liste contenant une séquence de caractères codée en JSON faisant référence aux Ids uniques du ou des propriétaires  
- `seeAlso[*]`: Liste d'uri pointant vers des ressources supplémentaires sur l'élément  
- `source[string]`: Source d'origine des données sous forme d'URL  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `type[string]`: Type d'entité NGSI. Il doit s'agir de TourismPresenceObserved  
- `visitorCount[number]`: Nombre de visiteurs observés pendant cette heure spécifique  . Model: [https://schema.org/Number](https://schema.org/Number)  
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

Propriétés requises  
- `dateObservée`  
- `heure`  
- `id`  
- `emplacement`  
- `codeEmplacement`  
- `nationalité`  
- `type`  
- `compteurDeVisiteurs`  
<!-- /35-RequiredProperties -->
  
<!-- 40-NotesYaml -->
  
<!-- /40-NotesYaml -->
  
<!-- 50-DataModelHeader -->
  

## Description du modèle de données des propriétés  

Classé par ordre alphabétique (cliquez pour plus de détails)  
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
  

## Exemples de charges utiles  

#### PrésenceTouristiqueObservée Exemple de valeurs clés NGSI-v2  

Voici un exemple de TourismPresenceObserved au format JSON sous forme de paires clé-valeur. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et retourne les données de contexte d'une entité individuelle.  
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

#### Présence touristique observée Exemple normalisé NGSI-v2  

Voici un exemple de TourismPresenceObserved au format JSON normalisé. Ceci est compatible avec NGSI-v2 lorsqu'on n'utilise pas d'options et retourne les données de contexte d'une entité individuelle.  
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

#### PrésenceTouristiqueObservée Exemple de valeurs clés NGSI-LD  

Voici un exemple de TourismPresenceObserved au format JSON-LD sous forme de paires clé-valeur. Ceci est compatible avec NGSI-LD lors de l'utilisation de `options=keyValues` et retourne les données de contexte d'une entité individuelle.  
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

#### Présence touristique observée Exemple normalisé NGSI-LD  

Voici un exemple de TourismPresenceObserved au format JSON-LD normalisé. Ceci est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et retourne les données de contexte d'une entité individuelle.  
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
  
