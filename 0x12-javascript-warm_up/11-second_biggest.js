#!/usr/bin/node
const len = process.argv.length;
let tmp = 0;
let secNum = 0;
let bigNum = Math.floor(Number(process.argv[2]));
if (len < 4) {
  console.log(secNum);
} else {
  secNum = Math.floor(Number(process.argv[3]));
  if (secNum > bigNum) {
    secNum = bigNum;
    bigNum = Math.floor(Number(process.argv[3]));
  }
  for (let i = 2; i < len; i = i + 1) {
    tmp = Math.floor(Number(process.argv[i + 1]));
    if (bigNum < tmp) {
      secNum = bigNum;
      bigNum = tmp;
    }
    if (secNum < tmp && tmp !== bigNum) {
      secNum = tmp;
    }
  }
  console.log(secNum);
}
