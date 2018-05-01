#!/usr/bin/node

function sortNum (a, b) {
  return a - b;
}

if (process.argv.length - 2 < 2) {
  console.log(0);
} else {
  const size = process.argv.length - 2;
  let myArr = new Array(size);

  for (let i = 0; i < size; i++) {
    myArr[i] = process.argv[i + 2];
  }
  myArr.sort(sortNum);

  console.log(myArr[myArr.length - 2]);
}
