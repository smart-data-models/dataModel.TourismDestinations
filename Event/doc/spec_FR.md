Entité : Événement  
==================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.TourismDestinations/blob/master/Event/LICENSE.md)  

## Liste des biens  

Propriétés requises  
- Aucune propriété requise  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
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
## Exemples de charges utiles  
#### Événement NGSI V2 valeurs clés Exemple  
Voici un exemple d'un événement au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
#### Événement NGSI V2 normalisé Exemple  
Voici un exemple d'un événement au format JSON tel que normalisé. Il est compatible avec la version 2 du NGSI lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
#### Événement NGSI-LD valeurs clés Exemple  
Voici un exemple d'événement au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
#### Événement NGSI-LD normalisé Exemple  
Voici un exemple d'un événement au format JSON-LD tel que normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
