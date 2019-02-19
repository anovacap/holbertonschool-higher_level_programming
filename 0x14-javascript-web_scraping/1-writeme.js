#!/usr/bin/node

let fs = require('fs');
let data = process.argv[3];
let f = process.argv[2];
fs.writeFile(f, data, function (err, data) {
  if (err) {
    console.log(err);
  }
});
