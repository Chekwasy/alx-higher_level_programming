#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.width; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str = str + c;
      }
      console.log(str);
    }
  }
};
