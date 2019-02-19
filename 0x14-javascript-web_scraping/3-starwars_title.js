#!/usr/bin/node

const request = require('request');
const input = 'http://swapi.co/api/films/' + process.argv[2];
request(input, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let json = JSON.parse(body);
    console.log(json.title);
  }
});
