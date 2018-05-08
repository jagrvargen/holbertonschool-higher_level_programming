#!/usr/bin/node

const path = process.argv[2];
const fs = require('fs');

const display = fs.readFileSync(path, 'utf8');
console.log(display);
