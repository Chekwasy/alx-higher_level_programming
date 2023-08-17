#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str = str + 'X';
      }
      console.log(str);
    }
  }

  rotate () {
    let tmp = 0;
    tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
