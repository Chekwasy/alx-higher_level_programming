#!/usr/bin/node
let stringg = '';
if (typeof process.argv[2] === 'undefined')
    stringg = 'No argument';
else if (typeof process.argv[3] === 'undefined')
    stringg = 'Argument found';
else
    stringg = 'Arguments found';
console.log(stringg);
