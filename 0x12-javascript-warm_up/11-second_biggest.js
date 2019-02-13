#!/usr/bin/node
'use strict';
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let ar = process.argv.slice(2);
  let newAr = ar.sort((a, b) => a - b);
  if (Math.sign(newAr[1]) === -1) {
    console.log(parseInt(newAr[1], 10));
  } else {
    newAr.reverse();
    console.log(parseInt(newAr[1], 10));
  }
}
