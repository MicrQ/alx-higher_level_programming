#!/usr/bin/node
const list = require('./100-main').list;

const newArray = list.map(function (n, i) {
  return n * i;
});

console.log(list);
console.log(newArray);
