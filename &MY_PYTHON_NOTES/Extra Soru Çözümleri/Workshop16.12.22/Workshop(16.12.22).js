const letters = new Array(26)
  .fill(0)
  .map((item, i) => String.fromCharCode(65 + i))
  .join("")
  .toLowerCase();

console.log(letters);
const numbers = "0123456789";
const spaces = " ";

const caracters = (letters, numbers, spaces) => {
  const text = prompt("enter a name");

  let number = 0;
  let letter = 0;
  let space = 0;

  for (const i of text) {
    if (letters.includes(i)) {
      letter++;
    } else if (numbers.includes(i)) {
      number++;
    } else if (spaces.includes(i)) {
      space++;
    }
  }
  const cumle = `string has ${letter} letters, ${number} numbers and ${space} space character.`;
  return cumle;
};
console.log(caracters(letters, numbers, spaces));
