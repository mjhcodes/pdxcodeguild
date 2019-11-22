const readline = require("readline-sync");

const conversionTable = {
  "ft": 0.3048,
  "mi": 1609.34,
  "m": 1,
  "km": 1000,
  "yard": 0.9144,
  "inch": 0.0254,
}

function convertToMeters(distance, unit) {
  return distance * conversionTable[unit];
}

function main() {
  let userDistance = parseInt(readline.question("What is the distance? "));
  let userUnit = readline.question("What are the units? ");
  let meters = convertToMeters(userDistance, userUnit);
  console.log(`${userDistance} ${userUnit} is ${meters.toFixed(4)} m`);
}

main()