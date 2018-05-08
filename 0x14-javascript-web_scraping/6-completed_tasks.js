#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request.get(url, function (error, body) {
  if (error) {
    console.log(error);
  } else {
    let obj = {};
    res = JSON.parse(body['body'])
    for (let i = 1; i < 11; i++) {
      obj[String(i)] = 0;
    }
    for (let j = 0; j < res.length; j++) {
      if (res[j]['completed'] === true) {
	obj[String(res[j]['userId'])]++;
      }
    }
    console.log(obj);
  }
});
