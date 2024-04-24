#!/usr/bin/node
const request = require('request');

const options = {
  url: process.argv[2],
  json: true
};

let count = 0;

request(options, (error, response) => {
  if (error == null) {
    response.body.results.forEach(film => {
      if (film.characters) {
        for (let i = 0; i < film.characters.length; i++) {
          if (film.characters[i].search('18') > 0)
          count++;
        }
      }
    });
  }
  console.log(count);
});
