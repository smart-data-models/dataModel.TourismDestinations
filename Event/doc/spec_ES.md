Entidad: Evento  
===============  
[Licencia abierta](https://github.com/smart-data-models//dataModel.TourismDestinations/blob/master/Event/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Evento próximo o pasado asociado a este lugar, organización o acción.**  

## Lista de propiedades  

- `accessPlan`:  Texto o enlace al plan de acceso al artículo.  - `actor`: Lista de actores o grupo musical.  - `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `audience`: Tipo de público al que afecta este Evento. Una combinación de texto libre (familia, adulto, niños, adolescente, senior, allPublic, ...). Enum:'adulto, allPublic, niños, familia, senior, adolescente'  - `category`: Categoría del viaje. A continuación se ofrece una combinación de texto libre para ser flexible a un contexto específico, como repositorio inicial o cualquier otro valor que necesite una aplicación. Enum:'compras, gastronomía, museo, culto religioso, parques y jardines, historia, actividades al aire libre, excursión, bienestar'  - `composer`: Lista de la persona que escribió la composición.  - `contactPoint`: Los datos para contactar con el artículo.  - `contentURL`: Especifica la URL de la imagen o el vídeo oficial del viaje para obtener más información.  - `criticReview`:   - `currencyAccepted`: Moneda aceptada para el pago si `TripFree` es False. Una combinación de una lista de códigos activos definidos en el modelo. Norma ISO 4217](http://en.wikipedia.org/wiki/ISO_4217), [Criptomonedas](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) , [Sistema de intercambio de divisas](https://en.wikipedia.org/wiki/Local_exchange_trading_system)  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `director`: Lista del director que gestiona la composición.  - `doorTimeClose`: Hora de cierre de las puertas para acceder al espectáculo..  - `doorTimeOpen`: Hora de apertura de puertas para acceder al espectáculo.  - `duration`: La duración de cada espectáculo. El código de la unidad (texto) de medida se da utilizando los [Códigos Comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **HUR** representa **Horas**.  - `electricTransport`:  Lista de los diferentes tipos de transporte eléctrico propuestos por la ciudad. Una combinación de. Enum:'electricBicycle, electricCar, electricMotorBike, electricScooter'  - `endDate`: La fecha y hora de finalización del artículo (en formato de fecha ISO 8601).  - `eventSchedule`: Un Evento asociado a un Cronograma utilizando esta propiedad no debe tener las propiedades `startDate` o `endDate`. En su lugar, éstas se definen dentro del horario asociado, lo que evita cualquier ambigüedad para los clientes que utilizan los datos. La propiedad puede tener valores repetidos para especificar diferentes horarios (diferentes meses o temporadas).***  - `eventStatus`: Estado del evento con respecto a este evento.  - `id`: Identificador único de la entidad  - `isAccessibleForFree`: Una bandera para señalar que el artículo, evento o lugar es accesible de forma gratuita.  - `language`:  Lista del lenguaje formal utilizado durante el viaje expresado a partir del estándar IETF [BCP 47](https://tools.ietf.org/html/bcp47)  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `maximumAttendeeCapacity`: El número total de personas que pueden asistir al Evento en ese lugar.  - `name`: El nombre de este artículo.  - `openingHoursSpecification`: Un valor estructurado que proporciona información sobre el horario de apertura de un lugar o de un determinado servicio dentro de un lugar  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `paymentAccepted`: Pago aceptado si `TripFree` es False. Una combinación de una lista de códigos activos definidos en el modelo. Enum:'Efectivo, tarjeta de crédito, criptomoneda, otro'  - `performer`: Actor o presentador principal o músico o grupo musical del evento.  - `pitch`: Tono del Evento. Cada artículo tiene el formato basado en la [Internacionalización (i18N) - Recomendación del W3C para el multilenguaje](https://www.w3.org/TR/json-ld/#string-internationalization) integrando todos los artículos en una sola propiedad (por ejemplo, el número 71). Cada ítem está representado por una cadena con Valor del Idioma : Valor del Artículo.  - `priceSpecification`: Un valor estructurado que representa un precio o un rango de precios según las categorías o el público.  - `publicAccess`: Una bandera para señalar que el Lugar está abierto a los visitantes públicos. Si se omite esta propiedad no se asume un valor booleano por defecto  - `ratingValueAverage`: Valor de calificación del evento. Directrices de uso: Utilice valores de 0 a 10 dependiendo de su estándar. Es el valor medio de todas las puntuaciones detalladas del atributo `starRatingDetailed`.  - `refPointOfInterest`: Referencia a todos los puntos de interés [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) incluidos en los viajes. La lista de PDI no tiene un orden cronológico.  - `routeType`: Lista de los transportes urbanos (metro, autobús, tranvía, ...) disponibles cerca del viaje según la norma GFTS [STOP](https://developers.google.com/transit/gtfs/reference/#stopstxt). Una combinación de valores. Enum:' autobús, cableCar, cableTram, ferry, funicular, monorraíl, metro, tren, tranvía, trolebús'  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `slogan`: Línea de cabecera de viaje, coincide con el gancho de texto.  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `starRatingDetailed`: Clasificación por estrellas detallada que dio lugar al valor medio expresado en el ratingValue. Instrucciones de uso: Un valor estructurado de 1 a 10 ocurrencias (Estrellas) donde cada elemento es una cadena con el formato: `NúmeroDeEstrellas`: Porcentaje.  - `startDate`: La fecha y hora de inicio de la partida (en formato de fecha ISO 8601).  - `subCategory`: Subcategoría del atributo `category`. A continuación se ofrece una combinación de texto libre para seguir siendo flexible a un contexto específico como ejemplo inicial o cualquier otro valor que necesite una aplicación.  - `subEvent`: Referencia a una lista de eventos menores que forman parte de este evento principal  - `superEvent`: Referencia al Evento Principal que incluye este Evento.  - `thematic`: Una lista de temas como palabras clave  - `title`:  Título del viaje.  - `touristType`: Tipo de turismo según el segmento y la motivación del viaje.  - `transportServices`: Lista de transportes privados disponibles cerca del Viaje. Por ejemplo taxi, uber, vtc, parkingShuttle  - `tripPriceFrom`: Precio mínimo. El código de la unidad (texto) de medida se da utilizando los [Códigos comunes del UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **EUR** representa **€uro**.  - `tripPriceTo`: Precio máximo. El código de la unidad (texto) de medida se da utilizando los [Códigos Comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **EUR** representa **€uro**.  - `type`: Tiene que ser Evento  - `url`: Url con imagen relacionada con el artículo  - `webSite`: Enlace a la página web oficial para más información.  - `wheelChairAccessible`: Acceso posible para personas con movilidad reducida.    
Propiedades requeridas  
- `id`  - `type`    
Este modelo de datos está basado en la norma UNE178503. También es compatible con schema.org. Algunos de los elementos de schema.org han sido adaptados en este archivo https://smart-data-models.github.io/data-models/schema-org.json. Este Tipo puede utilizarse por sí solo para describir un TouristDestination general, o utilizarse como un AdditionalType para añadir propiedades turísticas relevantes a cualquier otro Lugar. Un TouristDestination se define como un Lugar que contiene, o está colocado con, una o más TouristAttractions, a menudo vinculadas por un tema o interés similar a un TouristType particular. La OMT define el Destino (destino principal de un viaje turístico) como el lugar visitado que es fundamental para la decisión de realizar el viaje.  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Event:    
  description: 'Upcoming or past event associated with this place, organization, or action.'    
  properties:    
    accessPlan:    
      description: ' Text or Link to the access plan to the item.'    
      type: Property    
    actor:    
      description: 'List of actors or music group.'    
      items:    
        type: string    
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
      type: Property    
    category:    
      description: 'Category of the Trip. A combination of free text to remain flexible to a specific context is offered below as an initial repository or any other value needed by an application. Enum:''shopping, gastronomy, museum, religiousWorship, parksAndGardens, history, outdoorActivities, excursion, wellness'''    
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
      type: Property    
    composer:    
      description: 'List of person who wrote the composition.'    
      items:    
        type: string    
      type: Property    
    contactPoint:    
      description: 'The details to contact with the item.'    
      properties:    
        contactType:    
          type: string    
        email:    
          description: 'Property. Email address of owner.'    
          format: idn-email    
          type: string    
        name:    
          type: string    
        telephone:    
          type: string    
        url:    
          format: uri    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/ContactPoint    
    contentURL:    
      description: 'Specifies the URL to the official image or video of the Trip for more information.'    
      format: uri    
      type: Property    
    criticReview:    
      items:    
        description: "Property. Review written or published by a source that is recognized for its reviewing activities. Each items have the format based on the  [Internationalization (i18N) - W3C recommendation for multilanguage](https://www.w3.org/TR/json-ld/#string-internationalization) integrating all items in a single property (ex number 71). Each item is represented by a string with 'Language Value' : 'Article Value'"    
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
      type: array    
    currencyAccepted:    
      description: 'Currency accepted for payment if `TripFree` is False. A combination of a list of active codes defined in the model. [Norme ISO 4217](http://en.wikipedia.org/wiki/ISO_4217), [Crypto Currencies](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) , [Exchange Trading System](https://en.wikipedia.org/wiki/Local_exchange_trading_system)'    
      items:    
        enum:    
          - EUR    
          - USD    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/currenciesAccepted    
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
    director:    
      description: 'List of director who manage the composition.'    
      items:    
        type: string    
      type: Property    
    doorTimeClose:    
      description: 'Doors closing time to access the show..'    
      type: Property    
    doorTimeOpen:    
      description: 'Doors opening time to access the show.'    
      type: Property    
    duration:    
      description: 'The duration of each show. The unit code (text) of measurement is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **HUR** represents **Hours**.'    
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
      type: Property    
    endDate:    
      description: 'The end date and time of the item (in ISO 8601 date format).'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/endDate    
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
      type: Property    
    eventStatus:    
      description: 'Event Status regarding this event.'    
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
      type: Property    
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
    language:    
      description: ' List of Formal language used during the Trip expressed from the IETF [BCP 47](https://tools.ietf.org/html/bcp47) standard'    
      items:    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/language    
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
      type: Geoproperty    
    maximumAttendeeCapacity:    
      description: 'The total number of people who can attend to the Event at that location.'    
      type: Property    
    name:    
      description: 'The name of this item.'    
      type: Property    
    openingHoursSpecification:    
      description: 'A structured value providing information about the opening hours of a place or a certain service inside a place'    
      items:    
        properties:    
          closes:    
            format: time    
            type: string    
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
          opens:    
            format: time    
            type: string    
          validFrom:    
            format: date-time    
            type: string    
          validThrough:    
            format: date-time    
            type: string    
      minItems: 1    
      type: Property    
      x-ngsi:    
        model: https://schema.org/openingHoursSpecification    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *event_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/paymentAccepted    
    performer:    
      description: 'Main actor or presenter or musician or musical group of the event.'    
      items:    
        type: string    
      type: Property    
    pitch:    
      description: "Pitch of the Event. Each items have the format based on the [Internationalization (i18N) - W3C recommandation for multilanguage](https://www.w3.org/TR/json-ld/#string-internationalization) integrating all items in a single property (ex number 71). Each item is represented by a string with Language Value : Article Value. "    
      items:    
        properties:    
          article:    
            type: string    
          language:    
            type: string    
        type: object    
      type: Property    
    priceSpecification:    
      description: 'A structured value representing a price or price range depending categories or public.'    
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
      type: Property    
    publicAccess:    
      description: 'A flag to signal that the Place is open to public visitors. If this property is omitted there is no assumed default boolean value'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/publicAccess    
    ratingValueAverage:    
      description: 'Rating value of Event. Usage guidelines: Use values from 0 to 10 depending on your standard. This is the average value of all detailed scores of `starRatingDetailed` attribute'    
      type: Property    
    refPointOfInterest:    
      description: 'Reference to all the Point Of interest [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) included in the trips. The POI list does not have a chronological order.'    
      items:    
        anyOf: *event_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
      type: Property    
    slogan:    
      description: 'Trip header line, matches the text hook. '    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
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
      type: Property    
    startDate:    
      description: 'The start date and time of the item (in ISO 8601 date format).'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/startDate    
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
      type: Property    
    subEvent:    
      description: 'Reference to a list of Minor Events that are part of this major Event'    
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
      type: Property    
    superEvent:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the Major Event that includes this Event.'    
      type: Property    
    thematic:    
      description: 'A list of thematic as keywords'    
      items:    
        type: string    
      type: Property    
    title:    
      description: ' Title of the Trip.'    
      type: Property    
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
    transportServices:    
      description: 'List of private transport available near the Trip. In example taxi, uber, vtc, parkingShuttle '    
      items:    
        enum:    
          - parkingShuttle    
          - taxi    
          - uber    
          - vtc    
        type: string    
      type: Property    
    tripPriceFrom:    
      description: 'Min Price. The unit code (text) of measurement is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **EUR** represents **€uro**.'    
      type: Property    
    tripPriceTo:    
      description: 'Max Price. The unit code (text) of measurement is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **EUR** represents **€uro**.'    
      type: Property    
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
    webSite:    
      description: 'Link to the official website for more information.'    
      format: uri    
      type: Property    
    wheelChairAccessible:    
      description: 'Access possible for Person with Reduced Mobility.'    
      type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
#### Evento NGSI-v2 valores-clave Ejemplo  
Aquí hay un ejemplo de un Evento en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
  ],  
  "@context": [  
    "https://smart-data-models.github.io/data-models/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### Evento NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de un Evento en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### Evento NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un Evento en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### Evento NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un Evento en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:Event:Event:MNCA-EV-NCE-12552-MARIAGEDENFER",  
  "type": "Event",  
  "name": {  
    "type": "Property",  
    "value": "MARIAGE D ENFER"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Elle en revait, il l a fait : ils vont se marier !"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Information sur la piéce de théatre"  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": "https://www.billetreduc.com/260539/evt.htm"  
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
  "areaServed": {  
    "type": "Property",  
    "value": "Gare de Nice"  
  },  
  "dateLastReported": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-03-17T08:45:00Z"  
    }  
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
  "accessPlan": {  
    "type": "Property",  
    "value": "https://www.billetreduc.com/lieu/nice/theatre-bellecour/#planAcces"  
  },  
  "category": {  
    "type": "Property",  
    "value": [  
      "spectacle"  
    ]  
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
  "thematic": {  
    "type": "Property",  
    "value": [  
      "humor"  
    ]  
  },  
  "superEvent": {  
    "type": "Property",  
    "value": "urn:ngsi-ld:Event:Event:MNCA-EV-NCE-12552-FESTIVAL-THEATRE-NICE"  
  },  
  "eventStatus": {  
    "type": "Property",  
    "value": [  
      "scheduled"  
    ]  
  },  
  "locationName": {  
    "type": "Property",  
    "value": "Théâtre Bellecour"  
  },  
  "title": {  
    "type": "Property",  
    "value": "MARIAGE D ENFER"  
  },  
  "slogan": {  
    "type": "Property",  
    "value": "Elle en revait, il l a fait : ils vont se marier !"  
  },  
  "language": {  
    "type": "Property",  
    "value": [  
      "French"  
    ]  
  },  
  "startDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-08-01T01:20:00Z"  
    }  
  },  
  "endDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-10-18T01:20:00Z"  
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
  "duration": {  
    "type": "Property",  
    "value": 1.25  
  },  
  "doorTimeOpen": {  
    "type": "Property",  
    "value": "30 mn before the show"  
  },  
  "doorTimeClose": {  
    "type": "Property",  
    "value": "10 mn before the show"  
  },  
  "pitch": {  
    "type": "Property",  
    "value": [  
      {  
        "language ": "fr",  
        "article": "Heureusement pour Max, la wedding planner c est elle, et elle a déjà tout anticipé dans le moindre détail ! Tout ? Peut-être pas... En tout cas, un mariage ça se gère à deux... Et les conflits aussi ! Quand on dit pour le meilleur et pour le pire, le pire c est certainement les préparatifs d un mariage ! Que vous soyez mariés, fiancés, en couple, juste amis ou célibataire, cette comédie est faite pour vous ! Venez découvrir les coulisses des préparatifs d un mariage haut en couleurs avant de faire le grand saut !"  
      },  
      {  
        "language": "en",  
        "article": "But before that there are some details to settle and Elo knows it well: A beautiful wedding, cannnot be organized just like that! Fortunately for Max, the wedding planner is her, and she has already anticipated everything in every detail! Evrything ? Maybe not... In any case, a marriage is managed by two ... And conflicts too! When we say for better or for worse, the worst is certainly the preparations for a wedding! Whether married, engaged, in a relationship, just friends or single, this comedy is for you! Come and discover the preparations for a colorful wedding before taking the plunge!"  
      }  
    ]  
  },  
  "webSite": {  
    "type": "Property",  
    "value": "http://www.theatrebellecour.com"  
  },  
  "contentURL": {  
    "type": "Property",  
    "value": "https://www.nicetourisme.com/resources/ref/events/12552/mariage-d-enfer_168.jpg"  
  },  
  "url": {  
    "type": "string",  
    "value": "https://www.notikumi.com/2019/6/8/evento-de-revolver-en-salamanca"  
  },  
  "performer": {  
    "type": "Property",  
    "value": [  
      "Lise Giraudier"  
    ]  
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
  "composer": {  
    "type": "Property",  
    "value": [  
      "Céline Cara"  
    ]  
  },  
  "director": {  
    "type": "Property",  
    "value": [  
      "Sébastien El Fassi"  
    ]  
  },  
  "criticReview": {  
    "type": "Property",  
    "value": [  
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
    ]  
  },  
  "ratingValueAverage": {  
    "type": "number",  
    "value": 9.2  
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
  "audience": {  
    "type": "Property",  
    "value": [  
      "allPublic"  
    ]  
  },  
  "wheelChairAccessible": {  
    "type": "boolean",  
    "value": "true"  
  },  
  "maximumAttendeeCapacity": {  
    "type": "number",  
    "value": 60  
  },  
  "isAccessibleForFree": {  
    "type": "boolean",  
    "value": "false"  
  },  
  "eventPriceFrom": {  
    "type": "number",  
    "value": 10.95  
  },  
  "eventPriceTo": {  
    "type": "number",  
    "value": 19.5  
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
  "paymentAccepted": {  
    "type": "Property",  
    "value": [  
      "Cash",  
      "CreditCard"  
    ]  
  },  
  "currencyAccepted": {  
    "type": "Property",  
    "value": [  
      "EUR",  
      "USD"  
    ]  
  },  
  "routeType": {  
    "type": "Property",  
    "value": [  
      "tram",  
      "subway",  
      "bus"  
    ]  
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
  "electricTransport": {  
    "type": "Property",  
    "value": [  
      "electricBicycle",  
      "electricMotorBike"  
    ]  
  },  
  "offeredBy": {  
    "type": "Property",  
    "value": {  
      "type": "Organization",  
      "name": "Notikumi",  
      "url": "https://www.notikumi.com/"  
    }  
  },  
  "touristType": {  
    "type": "Property",  
    "value": "EVENTS AND FESTIVALS TOURISM"  
  },  
  "@context": [  
    "https://smartdatamodelsorg/context.jsonld"  
  ]  
}  
```  
