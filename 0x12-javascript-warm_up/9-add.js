#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}

const x = process.argv[2];
const y = process.argv[3];

if (isNaN(x) || isNaN(y)) {
  console.log(NaN);
} else {
  add(Number(x), Number(y));
}
