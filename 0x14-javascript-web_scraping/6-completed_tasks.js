#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request.get(url, function (error, body) {
  if (error) {
    console.log(error);
  } else {
    let obj = {};
    let res = JSON.parse(body['body']);
    for (let j = 0; j < res.length; j++) {
      let user = String(res[j]['userId']);
      if (res[j]['completed'] === true && user in obj) {
        obj[user]++;
      } else if (res[j]['completed'] === true) {
        obj[user] = 1;
      }
    }
    console.log(obj);
  }
});
