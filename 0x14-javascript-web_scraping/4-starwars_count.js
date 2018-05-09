#!/usr/bin/node

const wedge = 'https://swapi.co/api/people/18/';
const request = require('request');

request(wedge, function (error, body) {
  if (error) {
    console.log(error);
  } else {
    let films = JSON.parse(body['body']).films;
    console.log(films.length);
  }
});
