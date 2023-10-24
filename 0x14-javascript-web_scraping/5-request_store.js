#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const pathFile = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  fs.writeFile(pathFile, body, { encoding: 'utf8', flag: 'w' }, (err) => {
    if (err) {
      console.error(err);
    }
  });
});
