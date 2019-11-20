const readline = require("readline-sync");

function getEncryptedString(alphabet, userString) {
  let encryptedString = ""
  for (let i = 0; i < userString.length; i++) {
    let n = alphabet.indexOf(userString[i]);
    n < 13 ? n += 13 : n -= 13;
    encryptedString = encryptedString.concat(alphabet[n]);
  }
  return encryptedString
}

function main() {
  const alphabet = "abcdefghijklmnopqrstuvwxyz";
  let userString = readline.question("\nenter a string: ").toLowerCase();
  encryptedString = getEncryptedString(alphabet, userString);
  console.log(`${encryptedString}\n`);
}

main()