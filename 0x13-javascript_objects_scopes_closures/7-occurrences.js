#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const count = list.reduce((acc, element) => (element === searchElement ? acc + 1 : acc), 0);
  return count;
};
