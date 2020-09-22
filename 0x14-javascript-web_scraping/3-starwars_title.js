#!/usr/bin/node
const request = require('request');

const URL = 'https://swapi-api.hbtn.io/api/films/';
request(URL + process.argv[2], (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body).title);
});
