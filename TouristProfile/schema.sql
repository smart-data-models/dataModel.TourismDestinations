/* (Beta) Export of data model TouristProfile of the subject dataModel.TourismDestinations for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE TouristProfile_board_type AS ENUM ('RO', 'BB', 'HB', 'FB', 'AI');
CREATE TYPE TouristProfile_gender_type AS ENUM ('Female', 'Male');
CREATE TYPE TouristProfile_lodgingCategory_type AS ENUM ('1', '1 Superior', '2', '2 Superior', '3', '3 Superior', '4', '4 Superior', '5', '5 Superior');
CREATE TYPE TouristProfile_lodgingType_type AS ENUM ('Hotel', 'Resort', 'Hostel', 'Motel', 'B&B', 'Aparthotel', 'Lodge');
CREATE TYPE TouristProfile_roomOfStayType_type AS ENUM ('Apartment', 'Bungalow', 'Studio', 'Single', 'Double', 'Family', 'Junior Suite', 'Senior/Executive Suite', 'Royal/Presidential Suite');
CREATE TYPE TouristProfile_travelPartyComposition_type AS ENUM ('Single', 'Single parent', 'Family', 'Couple', 'Friends/Relatives');
CREATE TYPE TouristProfile_type AS ENUM ('TouristProfile');
CREATE TABLE TouristProfile (
  "address" JSON,
  "ageRange" JSON,
  "alternateName" TEXT,
  "areaServed" TEXT,
  "avgDailyAccommodationAndBoardExpenditure" JSON,
  "avgDailyExpenditure" JSON,
  "avgDailyExtraExpenditure" JSON,
  "board" TouristProfile_board_type,
  "bookingChannel" TEXT,
  "country" TEXT,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "gender" TouristProfile_gender_type,
  "id" TEXT PRIMARY KEY,
  "location" JSON,
  "lodgingCategory" TouristProfile_lodgingCategory_type,
  "lodgingSize" JSON,
  "lodgingType" TouristProfile_lodgingType_type,
  "name" TEXT,
  "owner" JSON,
  "reservationLeadTime" JSON,
  "roomOfStayType" TouristProfile_roomOfStayType_type,
  "seeAlso" JSON,
  "source" TEXT,
  "stayLength" JSON,
  "totalAccommodationAndBoardExpenditure" JSON,
  "totalExpenditure" JSON,
  "totalExtraExpenditure" JSON,
  "travelPartyComposition" TouristProfile_travelPartyComposition_type,
  "type" TouristProfile_type
);