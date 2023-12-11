#!/usr/bin/node
function add (a, b) {
  return parseInt(a) + parseInt(b);
}

const num1 = process.argv[2];
const num2 = process.argv[3];
console.log(add(num1, num2));
