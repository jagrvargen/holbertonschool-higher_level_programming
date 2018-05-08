#!/usr/bin/node

const url = process.argv[2];
const wedge = 'https://swapi.co/api/people/18/';
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const res = JSON.parse(body['body']);
    let count = 0;
    const results = res['body'];
    for (let i = 0; i < results.length; i++) {
      for (let j = 0; j < results[i]['characters'].length; j++) {
        if (results[i]['characters'][j] === wedge) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
