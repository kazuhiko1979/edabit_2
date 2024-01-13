const GMT = {
    "Los Angeles": "-08:00",
    "New York": "-05:00",
    "Caracas": "-04:30",
    "Buenos Aires": "-03:00",
    "London": "00:00",
    "Rome": "+01:00",
    "Moscow": "+03:00",
    "Tehran": "+03:30",
    "New Delhi": "+05:30",
    "Beijing": "+08:00",
    "Canberra": "+10:00",
  };
  
  function timeDifference(cityA, timestamp, cityB) {
    const inputDateTime = new Date(timestamp);
    const gmtCityA = getHourMinute(cityA);
    const gmtCityB = getHourMinute(cityB);
  
    const offsetA = GMT[cityA][0] === '-' ? 1 : -1;
    const offsetB = GMT[cityB][0] === '-' ? -1 : 1;
  
    let outputDateTime = new Date(inputDateTime);
    outputDateTime.setHours(outputDateTime.getHours() + offsetA * gmtCityA[0]);
    outputDateTime.setMinutes(outputDateTime.getMinutes() + offsetA * gmtCityA[1]);
  
    outputDateTime.setHours(outputDateTime.getHours() - offsetB * gmtCityB[0]);
    outputDateTime.setMinutes(outputDateTime.getMinutes() - offsetB * gmtCityB[1]);
  
    const result = outputDateTime.toISOString().replace(/T/, ' ').replace(/\..+/, '');
  
    return result;
  }
  
  function getHourMinute(city) {
    const [hours, minutes] = GMT[city].substring(1).split(':').map(Number);
    return [hours, minutes];
  }
  
  // Examples
  console.log(timeDifference("Los Angeles", "2011-04-02T17:23:00", "Canberra"));
  console.log(timeDifference("London", "1983-07-31T23:01:00", "Rome"));
  console.log(timeDifference("New York", "1970-12-31T13:40:00", "Beijing"));
  console.log(timeDifference("London", "1985-08-20T12:23:00", "Buenos Aires"));
  console.log(timeDifference("Rome", "1987-12-21T15:11:00", "New Delhi"));
  console.log(timeDifference("Canberra", "2009-03-01T18:32:00", "Caracas"));
  console.log(timeDifference("Moscow", "1953-09-14T19:54:00", "New York"));
  console.log(timeDifference("Beijing", "1999-11-18T02:03:00", "New Delhi"));
  console.log(timeDifference("Tehran", "1977-06-03T11:18:00", "Moscow"));
  