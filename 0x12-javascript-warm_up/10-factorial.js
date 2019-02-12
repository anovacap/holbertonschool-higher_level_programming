#!/usr/bin/node

const myVar = parseInt(process.argv[2], 10);
function factorial (n) {
  if (n === 0 || n === 1 || isNaN(n)) {
    return (1);
  }
  return factorial(n - 1) * n;
}
console.log(factorial(myVar));
