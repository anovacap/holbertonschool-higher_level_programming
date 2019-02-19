#!/usr/bin/node

const request = require('request');
const input = process.argv[2];
request(input, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    let results = JSON.parse(body).results;
    for (let i = 0; i < results.length; i++) {
      let chars = results[i]['characters'];
      for (let j = 0; j < chars.length; j++) {
        if (chars[j].includes('/18')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
