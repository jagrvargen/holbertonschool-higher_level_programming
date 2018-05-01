#!/usr/bin/node

let base = process.argv[2];

function factorial (x) {
  if (x === 1) {
    return 1;
  }
  return x * factorial(x - 1);
}

if (isNaN(base)) {
  console.log(1);
} else {
  console.log(factorial(base));
}
