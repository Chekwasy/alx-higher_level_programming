#!/usr/bin/node
var add = function(a, b) { return (a + b);};
add.prototype.log = function(a, b) { return (a + b);};
exports.add = add;
