#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const input = process.argv[2];
request.get(input).on('error', function (err) {
  console.log(err);
}).pipe(fs.createWriteStream(process.argv[3]));
