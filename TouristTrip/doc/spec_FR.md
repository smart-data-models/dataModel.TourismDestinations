Entité : TouristTrip  
====================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.TourismDestinations/blob/master/TouristTrip/LICENSE.md)  
Description globale : **Un voyage touristique. Un itinéraire créé pour visiter un ou plusieurs lieux d'intérêt (TouristAttraction/TouristDestination) souvent liés par un thème, une zone géographique ou un intérêt similaire à un TouristType particulier. L'OMT définit le voyage touristique comme le voyage effectué par des visiteurs**.  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `location`:   - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `sameAs`:   - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `touristType`:   - `type`: Il doit s'agir de TouristDestination    
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
        model: https://schema.org/address    
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
      type: Property    
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
        anyOf: *touristtrip_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    sameAs:    
      format: uri    
      type: string    
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
    touristType:    
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
    type:    
      description: 'It has to be TouristDestination'    
      enum:    
        - TouristTrip    
      type: Property    
      x-ngsi:    
        model: https://schema.org/TouristDestination    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### TouristTrip Valeurs-clés NGSI-v2 Exemple  
Voici un exemple de TouristTrip au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi:touristTrip:1",  
  "type": "TouristTrip",  
  "name": "Descubre Conil",  
  "description": "Viaje para conocer el encanto y los atractivos turísticos de Conil de la Frontera.",  
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
  "video": "https://www.youtube.com/watch?v=IhnvlIzxPLg"  
}  
```  
#### TouristTrip NGSI-v2 normalisé Exemple  
Voici un exemple de TouristTrip au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
      "value": "Viaje para conocer el encanto y los atractivos turísticos de Conil de la Frontera."  
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
  }  
}  
```  
#### TouristTrip Valeurs-clés NGSI-LD Exemple  
Voici un exemple de TouristTrip au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi:touristTrip:1",  
  "type": "TouristTrip",  
  "name": "Descubre Conil",  
  "description": "Viaje para conocer el encanto y los atractivos tur\u00edsticos de Conil de la Frontera.",  
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
      "value": "Viaje para conocer el encanto y los atractivos tur\u00edsticos de Conil de la Frontera."  
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
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
