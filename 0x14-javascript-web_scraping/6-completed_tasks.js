#!/usr/bin/node
const request = require('request');

const userCompleted = {};
request({ url: process.argv[2], json: true }, (error, response, body) => {
  if (!error) {
    for (let i = 0; i < body.length; i++) {
      if (body[i].completed) {
        if (body[i].userId in userCompleted) {
          userCompleted[body[i].userId]++;
        } else {
          userCompleted[body[i].userId] = 1;
        }
      }
    }
  }
  console.log(userCompleted);
});
