#!/usr/bin/node

const dict = require('./101-data').dict;
const sortedDict = Object.entries(dict).reduce((acc, [userId, occurences]) => {
  acc[occurences] = acc[occurences] || [];
  acc[occurences].push(userId);
  return acc;
}, {});
console.log(sortedDict);
