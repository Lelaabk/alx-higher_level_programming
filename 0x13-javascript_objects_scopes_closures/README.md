# Project: 0x13. JavaScript - Objects, Scopes and Closures

## Description

This project covers fundamental concepts in JavaScript, including objects, scopes, and closures. The tasks involve creating and manipulating classes to understand the principles of object-oriented programming in JavaScript.

## Learning Objectives

- Understand why JavaScript programming is amazing.
- Learn how to create an object in JavaScript.
- Grasp the meaning of `this` in JavaScript.
- Understand what `undefined` means.
- Recognize why variable type and scope are important.
- Comprehend the concept of closures in JavaScript.
- Understand what a prototype is.
- Learn how to inherit an object from another.

## Project Timeline

- Project started on: December 12, 2023, 4:00 AM
- Project must be completed by: December 13, 2023, 4:00 AM
- Checker was released on: December 12, 2023, 10:00 AM
- An auto review will be launched at the deadline.

## Resources

- [JavaScript object basics](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics)
- [Object-oriented JavaScript (read all examples!)](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)
- [Class - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
- [super - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
- [extends - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
- [Object prototypes](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)
- [Inheritance in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)
- [Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
- [this/self](https://alistapart.com/article/getoutbindingsituations/)
- [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x).
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/node`.
- A `README.md` file, at the root of the folder, is mandatory.
- Code should be semistandard compliant. Rules of Standard + semicolons on top. Also, as reference: AirBnB style.
- All files must be executable.
- The length of your files will be tested using `wc`.
- You are not allowed to use `var`.

### Installation and Dependencies

- Install Node 14:
  ```bash
  $ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
  $ sudo apt-get install -y nodejs
  ```
- Install semistandard:
  ```bash
  $ sudo npm install semistandard --global
  ```

## Project Structure

The project is organized into several tasks, each focusing on a specific aspect of JavaScript. Below is an overview of the tasks:

### Task 0: Rectangle #0

- File: `0-rectangle.js`
- Description: Write an empty class `Rectangle` that defines a rectangle.

### Task 1: Rectangle #1

- File: `1-rectangle.js`
- Description: Write a class `Rectangle` that defines a rectangle, taking width and height as arguments in the constructor.

### Task 2: Rectangle #2

- File: `2-rectangle.js`
- Description: Enhance the `Rectangle` class from Task 1 to handle cases where width or height is 0 or not a positive integer.

### Task 3: Rectangle #3

- File: `3-rectangle.js`
- Description: Extend the `Rectangle` class to include an instance method called `print()` that prints the rectangle using the character 'X'.

### Task 4: Rectangle #4

- File: `4-rectangle.js`
- Description: Expand the `Rectangle` class to include additional instance methods: `rotate()` and `double()`.

### Task 5: Square #0

- File: `5-square.js`
- Description: Write a class `Square` that defines a square and inherits from the `Rectangle` class.

### Task 6: Square #1

- File: `6-square.js`
- Description: Extend the `Square` class from Task 5 to include an instance method `charPrint(c)` that prints the square using the character `c`.

### Task 7: Occurrences

- File: `7-occurrences.js`
- Description: Write a function `nbOccurences` that returns the number of occurrences of a specified element in a list.

### Task 8: Esrever

- File: `8-esrever.js`
- Description: Write a function `esrever` that returns the reversed version of a list without using the built-in `reverse` method.

### Task 9: Log me

- File: `9-logme.js`
- Description: Write a function `logMe` that prints the number of arguments already printed and the new argument value.

### Task 10: Number conversion

- File: `10-converter.js`
- Description: Write a function `converter` that converts a number from base 10 to another base passed as an argument.

## Copyright and Plagiarism

- You are tasked to come up with solutions for the tasks to meet the learning objectives.
- Plagiarism is strictly forbidden and will result in removal from the program.
- You are not allowed to publish any content of this project.

## Acknowledgments

- Copyright © 2023 ALX, All rights reserved.
