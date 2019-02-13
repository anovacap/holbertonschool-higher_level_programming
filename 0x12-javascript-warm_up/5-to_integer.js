#!/usr/bin/node

const myVar = process.argv[2];
if (!myVar || isNaN(myVar)) {
  console.log('Not a number');
} else if (parseInt(myVar) === Number) {
  console.log('My number: %d', parseInt(myVar, 10));
} else {
  console.log('My number: %d', Math.floor(parseInt(myVar, 10)));
}
