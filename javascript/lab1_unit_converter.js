const readline = require("readline-sync");

function convertToMeters(feet) {
  return feet * 0.3048;
}

function main() {
  let userInput = parseInt(readline.question("What is the distance in feet? "));
  let meters = convertToMeters(userInput);
  console.log(`${userInput} ft is ${meters.toFixed(4)} m`);
}

main()