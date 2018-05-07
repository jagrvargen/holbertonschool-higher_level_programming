#!/usr/bin/node

const square = require('./5-square.js');

module.exports = class Square extends square {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(String(c).repeat(this.height));
      }
    }
  }
};
