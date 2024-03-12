#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};
for (const key in dict) {
  const ocr = dict[key];
  if (!(ocr in newDict)) {
    newDict[ocr] = [];
  }
  newDict[ocr].push(key);
}
console.log(newDict);
