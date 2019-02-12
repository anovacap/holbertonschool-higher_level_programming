#!/usr/bin/node

const myVar1 = process.argv[2];
const myVar2 = process.argv[3];
if (myVar1 && !myVar2) {
  console.log('%s is undefined', myVar1);
} else if (myVar2) {
  console.log('%s is %s', myVar1, myVar2);
} else {
  console.log('undefined is undefined');
}
