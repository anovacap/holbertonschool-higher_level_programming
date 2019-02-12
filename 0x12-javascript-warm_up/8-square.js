#!/usr/bin/node

const myVar = process.argv[2];
const x = 'X';
for (let i = 0; i < myVar; i++) {
  console.log(x.repeat(myVar));
}
