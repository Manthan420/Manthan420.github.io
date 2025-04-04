const customName = document.getElementById('customname'); // user input
const randomize = document.querySelector('.randomize'); // generate button
const story = document.querySelector('.story'); // story output area

// returns a random value from the provided array
function randomValueFromArray(array) {
  return array[Math.floor(Math.random() * array.length)];
}
