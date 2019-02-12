#!/usr/bin/node
'use strict';
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let ar = process.argv.slice(2);
  let newAr = ar.sort();
  newAr.reverse();
  console.log(newAr[1]);
}
