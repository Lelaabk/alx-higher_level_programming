#!/usr/bin/node

const fs = require('fs');
const fa = fs.readFileSync(process.argv[2]).toString();
const sa = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], fa + sa);
