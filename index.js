// console.log("Hello, World!");
// let name = "Hemanth";
// const birthyear = 2000;

// console.log(`My name is ${name} and I was born in ${birthyear}.`);

// let data ="JavaScript is Fun!"

// let trimmedData = data.trim();
// console.log("Trimmed Data:", trimmedData);

// let extractedData = trimmedData.slice(0, 10);   
// console.log("Extracted Data:", extractedData);
/*
let randomNumber = Math.floor(Math.random() * 10) + 1;
console.log("Random Number:", randomNumber);
*/

// let checknumber = 7;

// if (checknumber % 2 === 0) {
//     console.log(`${checknumber} is an even number.`);
// } else {
//     console.log(`${checknumber} is an odd number.`);
// // }
// function greetUser(name) {
//     console.log(`Hello, ${name}! Welcome to my web page.`)                                              ;
// }

// greetUser("Hemanth");
// greetUser("John");
// const calculaterectangleArea = (length, width) => {length * width};

// let calculatedArea = calculaterectangleArea(5, 10);
// console.log("Calculated Area:", calculatedArea);

// function testScope() {
//     var functionVar = "I am a function variable";

//     if (true) {
//         let blockVar = "I am a block variable";

//         console.log("Inside block:");
//         console.log(functionVar); 
//         console.log(blockVar);   
//     }

//     console.log("Outside block but inside function:");
//     console.log(functionVar); 
   
// }

// testScope();
// function greet(name) {
//     console.log(`Hello, ${name}!`);
// }
//  function getUserInput(callback) {
//     const name = "Alice";
//     callback(name);
//  } 

//  getUserInput(greet);

// function calculate(num1, num2, operationcallback) {
//     return operationcallback(num1, num2);
// }

// function add(a, b) {
//     return a + b;
// }

// const sum = calculate(5, 3, add);
// console.log("Sum:", sum);

// const difference = calculate(10, 4, (a, b) => a - b);
// console.log("Difference:", difference);

const car = {
    make: "Toyota",
    model: "Camry",
    year: 2020,
};

// console.log("full car object:", car);
// console.log("Car model:", car.model);
console.log("Original car object:", car);

car.year = 2021;

car.color = "Red";

console.log("Updated car object:", car);

let propToAccess = "make";
console.log('the car' ${propToAccess} is ${car[propToAccess]}`);


