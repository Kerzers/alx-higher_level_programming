#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const taskCount = {};
  const Data = JSON.parse(body);
  Data.forEach(item => {
    const userId = item.userId;
    if (item.completed) {
      if (taskCount[userId]) {
        taskCount[userId]++;
      } else {
        taskCount[userId] = 1;
      }
    }
  });
  console.log(taskCount);
});
