#!/usr/bin/node

const f = require('fs');
if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js file1 file2 destFile');
  process.exit(1);
}

const [, , file1, file2, destFile] = process.argv;

f.readFile(file1, 'utf8', (err, data1) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  f.readFile(file2, 'utf8', (err, data2) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }

    const concatenatedContent = data1 + data2;

    f.writeFile(destFile, concatenatedContent, 'utf8', (err) => {
      if (err) {
        console.error(err);
        process.exit(1);
      }
      console.log(`The content of ${file1} and ${file2} has been successfully concatenated and written to ${destFile}`);
    });
  });
});
