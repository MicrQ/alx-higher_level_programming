#!/usr/bin/node
const request = require('request');

const options = {
  url: process.argv[2],
  json: true
};

let count = 0;

request(options, (error, response) => {
  if (!error) {
    response.body.results.forEach(film => {
    if (film.characters && film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
    });
  }
  console.log(count);
});
