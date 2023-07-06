/* (Beta) Export of data model TouristDestination of the subject dataModel.TourismDestinations for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE TouristDestination_type AS ENUM ('TouristDestination');
CREATE TABLE TouristDestination (address json, alternateName text, areaServed text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, id text, includesAttraction json, location json, name text, owner json, seeAlso json, source text, type TouristDestination_type);