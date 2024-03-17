const integers = /(?<![.\d+-])(?:[+-]?\d+)(?![.\d])/g;
const floats = /(?<![.\d+-])(?:[+-]?(?:\d+\.\d+|\d*\.\d+))(?![.\d])/g;
const positive = /(?<![.\d+-])(?:\+?\d*\.?\d+)(?![.\d])/g;
const negative = /(?<![.\d+-])(?:-\d*\.?\d+)(?![.\d])/g;
const numbers = /(?<![.\d+-])(?:[+-]?\d*\.?\d+)(?![.\d])/g;

const txt = " 123.456 2 +7 -88 -.25 9.10.11 -4. +-34 -0.6 --5 ";

console.log(txt.match(integers));
console.log(txt.match(floats));
console.log(txt.match(positive));
console.log(txt.match(negative));
console.log(txt.match(numbers));
