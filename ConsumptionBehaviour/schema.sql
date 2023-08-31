/* (Beta) Export of data model ConsumptionBehaviour of the subject dataModel.TourismDestinations for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE resourceType_type AS ENUM ('Diesel', 'Petrol', 'Electricity', 'Gas', 'Water');CREATE TYPE ConsumptionBehaviour_type AS ENUM ('ConsumptionBehaviour');
CREATE TABLE ConsumptionBehaviour (address json, alternateName text, areaServed text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, endDate timestamp, finalMeasurement text, id text, initialMeasurement text, location json, name text, owner json, resourceType resourceType_type, seeAlso json, source text, sourceOfConsumption json, startDate timestamp, type ConsumptionBehaviour_type, usersInvolved text);