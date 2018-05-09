#!/usr/bin/node

const url = process.argv[2];
const wedge = '18';
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let films = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < films.length; i++) {
      let chars = films[i]['characters'];
      for (let j = 0; j < chars.length; j++) {
        if (chars[j].includes(wedge)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
