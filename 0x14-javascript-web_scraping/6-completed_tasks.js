#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let js = {};
    let json = JSON.parse(body);
    for (let i = 0; i < json.length; i++) {
      let todo = json[i];
      if (todo['completed'] === true) {
        if (js[todo['userId']] !== undefined) {
          js[todo['userId']] += 1;
        } else {
          js[todo['userId']] = 1;
        }
      }
    }
    console.log(js);
  }
});
