#!/usr/bin/node
function add(a, b) { return (a + b) }

const firstno = Math.floor(Number(process.argv[2]));
const secondno = Math.floor(Number(process.argv[3]));
console.log(add(firstno, secondno));
