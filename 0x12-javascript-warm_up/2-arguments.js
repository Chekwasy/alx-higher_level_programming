#!/usr/bin/node
console.log(typeof process.argv[2] === 'undefined' ? 'No argument' : typeof process.argv[3] === 'undefined'? 'Argument found' : 'Arguments found');
