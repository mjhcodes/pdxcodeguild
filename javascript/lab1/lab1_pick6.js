// Lab 1 - Pick 6

function pick6() {
  let randNum;
  let ticket = [];
  for (let i = 0; i < 6; i++) {
    randNum = Math.floor(Math.random() * 99) + 1;
    ticket.push(randNum)
  }
  return ticket
}

function getNumMatches(winning, ticket) {
  let numMatches = 0;
  for (let i = 0; i < winning.length; i++) {
    if (winning[i] === ticket[i]) {
      numMatches++
    }
  }
  return numMatches
}

function getWinnings(numMatches) {
  const winningsTable = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000,
  }
  return winningsTable[numMatches]
}

function getROI(earnings, expenses) {
  return (earnings - expenses) / expenses;
}

function main() {
  let balance = 0;
  let expenses = 0;
  let earnings = 0;
  winningTicket = pick6();
  for (let i = 0; i < 100000; i++) {
    customerTicket = pick6();
    balance -= 2;
    expenses += 2;
    numMatches = getNumMatches(winningTicket, customerTicket);
    winnings = getWinnings(numMatches);
    balance += winnings;
    earnings += winnings;
  }
  ROI = getROI(earnings, expenses);
  console.log(`\nEarnings: $${earnings}\nExpenses: $${expenses}\nBalance: $${balance}\nROI: ${ROI}\n`)
}

main()