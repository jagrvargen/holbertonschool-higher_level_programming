#!/usr/bin/node

const square = require('./5-square.js');

module.exports = class Square extends square {
  constructor (size) {
    super(size);
    this.size = size;
  }
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      for (let i = 0; i < this.size; i++) {
        console.log(c.repeat(this.size));
      }
    }
  }
};
