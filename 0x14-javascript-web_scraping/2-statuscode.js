#!/usr/bin/node

const request = require('request');
const input = process.argv[2];
const options = {
  url: input,
  method: 'GET',
  headers: {
    'Accept': 'application/json',
    'Accept-Charset': 'utf-8'
  }
};
request(options, function (err, res, headers) {
  if (err) {
    console.log(err);
  } else {
    console.log('code:', res.statusCode);
  }
});
