#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurences');
} else {
  let mult = process.argv[2]
  for (let i = 0; i < mult; i++) {
    console.log('C is fun');
  }
}
