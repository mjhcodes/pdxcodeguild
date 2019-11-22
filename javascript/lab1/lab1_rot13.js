const readline = require("readline-sync");

function reverse(lowerLetters, upperLetters, rotation) {
  lowerLetters = lowerLetters.split("").reverse().join("");
  upperLetters = upperLetters.split("").reverse().join("");
  rotation = Math.abs(rotation);
  return lowerLetters, upperLetters, rotation;
}

function getEncrypedString(rotation, userString, lowerLetters, upperLetters) {
  let encryptedString = '';
  for (i = 0; i < userString.length; i++) {
    index = lowerLetters.indexOf(userString[i]);   

    if (index !== -1)
      encryptedString += lowerLetters[(index + rotation) % 26];
    else if (index === -1) {
      index = upperLetters.indexOf(userString[i]);
      if (index === -1)
        encryptedString += userString[i];
      else
        encryptedString += upperLetters[(index + rotation) % 26];
    }
  }
  return encryptedString;
}

function main() {
  let rotation = parseInt(readline.question("\nenter the rotation: "));
  const userString = readline.question("enter a string: ");
  
  let lowerLetters = "abcdefghijklmnopqrstuvwxyz";
  let upperLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  
  if (rotation < 0) {
    lowerLetters, upperLetters, rotation = reverse(lowerLetters, upperLetters, rotation);
  }
  
  encryptedString = getEncrypedString(rotation, userString, lowerLetters, upperLetters);
  
  console.log(`\n${encryptedString}\n`);
}

main()