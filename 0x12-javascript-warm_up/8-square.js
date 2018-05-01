#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  let size = process.argv[2];
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
