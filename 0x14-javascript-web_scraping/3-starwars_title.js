#!/usr/bin/node

const film_id = process.argv[2];
const url = "http://swapi.co/api/films/" + film_id;

const request = require('request');

request(url, function (error, body) {
  if (error) {
    console.log(error);
  } else {
    const res = JSON.parse(body['body']);
    console.log(res['title']);
  }
});
