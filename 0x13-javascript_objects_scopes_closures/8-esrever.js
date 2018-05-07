#!/usr/bin/node

exports.esrever = function (list) {
  myList = [];

  for (let i = list.length - 1, j = 0; i >= 0; i--, j++) {
    myList[j] = list[i];
  }
  return myList;
};
