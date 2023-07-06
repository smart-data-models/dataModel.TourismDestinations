/* (Beta) Export of data model TouristTrip of the subject dataModel.TourismDestinations for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE tripStatus_type AS ENUM ('cancelled', 'closed', 'finished', 'opened', 'postponed', 'rescheduled', 'scheduled', 'suspended');CREATE TYPE TouristTrip_type AS ENUM ('TouristTrip');
CREATE TABLE TouristTrip (accessPlan text, address json, alternateName text, areaServed text, audience json, category json, contentURL text, criticReview json, currencyAccepted json, dataProvider text, dateCreated timestamp, dateLastReported timestamp, dateModified timestamp, description text, duration text, electricTransport json, endDate timestamp, id text, isAccessibleForFree text, itinerary json, language json, location json, locationName text, maximumAttendeeCapacity text, name text, openingHoursSpecification json, owner json, paymentAccepted json, pitch json, priceSpecification json, ratingValueAverage text, refPointOfInterest json, routeType json, seeAlso json, slogan text, source text, starRatingDetailed json, startDate timestamp, subCategory json, subTrip json, superTrip text, thematic json, title text, touristType json, transportServices json, tripPriceFrom text, tripPriceTo text, tripSchedule json, tripStatus tripStatus_type, type TouristTrip_type, webSite text, wheelChairAccessible text);