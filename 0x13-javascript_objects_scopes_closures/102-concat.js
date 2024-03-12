#!/usr/bin/node
const fs = require('fs');
const args = process.argv;

fs.readFile(args[2], 'utf-8', (err, fileA) => {
  if (err) throw err;
  fs.readFile(args[3], 'utf-8', (err, fileB) => {
    if (err) throw err;
    const docs = fileA + fileB;
    fs.writeFile(args[4], docs, (err) => {
      if (err) throw err;
    });
  });
});
