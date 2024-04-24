#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (!error) {
    const jsonResponse = JSON.parse(body).characters;
    for (let i = 0; i < jsonResponse.length; i++) {
      request(jsonResponse[i], (err, res, bd) => {
        if (!err) {
          console.log(JSON.parse(bd).name);
        }
      });
    }
  }
});
