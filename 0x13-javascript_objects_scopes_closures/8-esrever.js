#!/usr/bin/node
exports.esrever = function (list) {
  const nlist = [];
  const len = list.length;
  for (let i = len - 1; i >= 0; i--) {
    nlist.push(list[i]);
  }
  return nlist;
};
