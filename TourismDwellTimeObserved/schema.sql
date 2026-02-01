/* (Beta) Export of data model TourismDwellTimeObserved of the subject dataModel.TourismDestinations 
for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE aggregationType_type AS ENUM ('hourly_sum', 'hourly_average', 'hourly_snapshot', 'hourly_estimate');
CREATE TYPE TourismDwellTimeObserved_type AS ENUM ('TourismDwellTimeObserved');

CREATE TABLE TourismDwellTimeObserved (
    address JSON,
    aggregationType aggregationType_type,
    alternateName TEXT,
    areaServed TEXT,
    dataProvider TEXT,
    dateCreated TIMESTAMP,
    dateModified TIMESTAMP,
    dateObserved TIMESTAMP,
    description TEXT,
    dwellTimeRange TEXT,
    hour NUMERIC,
    id TEXT PRIMARY KEY,
    location JSON,
    locationCode TEXT,
    locationName TEXT,
    name TEXT,
    nationality TEXT,
    nationalityName TEXT,
    owner JSON,
    seeAlso JSON,
    source TEXT,
    totalVisitors NUMERIC,
    type TourismDwellTimeObserved_type,
    visitorCount NUMERIC
);