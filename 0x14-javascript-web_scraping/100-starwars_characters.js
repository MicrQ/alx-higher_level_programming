#!/usr/bin/node
const request = require('request');
const options = {
  url: 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2],
  json: true
};
request(options, (error, response, body) => {
  if (!error) {
    for (let i = 0; i < body.characters.length; i++) {
      request({ url: body.characters[i], json: true }, (err, res, bd) => {
        if (!err) {
          console.log(bd.name);
        }
      });
    }
  }
});
