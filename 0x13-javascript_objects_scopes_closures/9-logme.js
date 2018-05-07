#!/usr/bin/node

let counted = 0;

exports.logMe = function (item) {
  console.log(`${counted}: ${item}`);

  return counted++;
};
