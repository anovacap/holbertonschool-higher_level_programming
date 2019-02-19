#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    let x = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(x.repeat(this.width));
    }
  }
  rotate () {
    let newWidth = this.width;
    let newHeight = this.height;
    this.width = newHeight;
    this.height = newWidth;
  }
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
