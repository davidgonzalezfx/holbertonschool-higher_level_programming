#!/usr/bin/node
const request = require('request');
let countFilms = 0;

request(process.argv[2], function (err, response, body) {
  if (err == null) {
    const res = JSON.parse(body);
    const results = res.results;
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].search('18') > 0) {
          countFilms++;
        }
      }
    }
  }
  console.log(countFilms);
});
