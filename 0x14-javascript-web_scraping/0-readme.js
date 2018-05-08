#!/usr/bin/node

const path = process.argv[2];
const fs = require('fs');

fs.readFile(path, 'utf8', (error, display) => {
  if (error) {
    console.log(error);
  } else {
    console.log(display);
  }
});
