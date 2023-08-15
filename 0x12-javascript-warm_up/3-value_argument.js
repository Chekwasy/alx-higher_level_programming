#!/usr/bin/node
let stringg = '';
if (typeof process.argv[2] === 'undefined')
    stringg = 'No argument'
else
    stringg = process.argv[2]
console.log(stringg);
