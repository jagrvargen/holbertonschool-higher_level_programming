#!/usr/bin/node

const url = process.argv[2];
const path = process.argv[3];
const request = require('request');
const fs = require('fs');

request
  .get(url)
  .on('error', function(error) {
    console.log(error);
  })
  .pipe(fs.createWriteStream(path));
