#!/usr/bin/node

const nombre = parseInt(process.argv[2]);
if (isNaN(nombre)) {
  console.log('Not a Number');
} else {
  console.log('My number:', nombre);
}
