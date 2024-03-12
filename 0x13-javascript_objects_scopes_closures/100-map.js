#!/usr/bin/node
const zList = require('./100-main').list;

const newArray = zList.map((n, i) => n * i);

console.log(zList);
console.log(newArray);
