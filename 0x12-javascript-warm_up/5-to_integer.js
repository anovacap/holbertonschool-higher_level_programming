#!/usr/bin/node

const myVar = process.argv[2];
if (!myVar || parseInt(myVar) === isNaN) {
  console.log('Not a number');
} else if (parseInt(myVar) === Number) {
  console.log('My number: %d', parseInt(myVar, 10));
} else {
  console.log('My number: %d', Math.floor(myVar));
}
