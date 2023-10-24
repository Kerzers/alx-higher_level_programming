#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

request.get(`https://swapi-api.alx-tools.com/api/films/${id}/?format=json`,
  (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const filmData = JSON.parse(body);
      const title = filmData.title;
      console.log(title);
    }
  });
