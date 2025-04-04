const customName = document.getElementById('customname'); // user input
const randomize = document.querySelector('.randomize'); // generate button
const story = document.querySelector('.story'); // story output area

// returns a random value from the provided array
function randomValueFromArray(array) {
  return array[Math.floor(Math.random() * array.length)];
}
const storyText = 'It was 94 fahrenheit outside, so :insertx: went for a walk. When they got to :inserty:, they stared in horror for a few moments, then :insertz:. Bob saw the whole thing, but was not surprised — :insertx: weighs 300 pounds, and it was a hot day.';
const insertX = ['Willy the Goblin', 'Big Daddy', 'Father Christmas'];
const insertY = ['the soup kitchen', 'Disneyland', 'the White House'];
const insertZ = ['spontaneously combusted', 'melted into a puddle on the sidewalk', 'turned into a slug and crawled away'];
