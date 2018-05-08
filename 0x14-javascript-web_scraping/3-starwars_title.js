#!/usr/bin/node

const filmId = process.argv[2];
const url = 'http://swapi.co/api/films/' + filmId;

const request = require('request');

request(url, function (error, body) {
  if (error) {
    console.log(error);
  } else {
    const res = JSON.parse(body['body']);
    console.log(res['title']);
  }
});
