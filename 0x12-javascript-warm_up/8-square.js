#!/usr/bin/node

if (process.argv.length < 3 || isNaN(process.argv[2])) {
  console.log('Missing size');
}
const myVar = process.argv[2];
const x = 'X';
for (let i = 0; i < myVar; i++) {
  console.log(x.repeat(myVar));
}
