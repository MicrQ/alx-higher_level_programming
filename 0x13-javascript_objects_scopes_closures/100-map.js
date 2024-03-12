#!/usr/bin/node
const list = require('./100-main').list;

const newArray = list.map((n, i) => n * i);

console.log(list);
console.log(newArray);
