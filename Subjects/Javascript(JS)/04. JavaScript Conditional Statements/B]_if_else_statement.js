// B] if...else Statement


// Q.1 Write a program to check whether a number is even or odd.
// answer:
let num = 35;
if (num%2==0){
    console.log("Even number")
}else{
    console.log("Odd number")
}


// Q.2 Check if a person is eligible to vote (age ≥ 18). Print “Eligible” or “Not Eligible”.
// answer:
let age = 23;
if (age>=18){
    console.log("Eligible")
}else{
    console.log("Not Eligible")
}


// Q.3 Write a program that checks whether a number is positive or negative.
// answer:
let number = 0;
if (number>=0){
    console.log("Positive number")
}else{
    console.log("Negative number")
}


// Q.4 Check if a student has passed or failed based on marks (pass mark = 35).
// answer:
let marks = 79;
if (marks>=35){
    console.log("Passed")
}else{
    console.log("Failed")
}


// Q.5 Write a program to check whether a given character is an uppercase letter or not.
//(Hint: Use character comparison)
// answer:
let char = "d";
if (char>="A" && char<="Z"){
    console.log("Uppercase")
}else{
    console.log("Lowercase")
}


//Q.6 Check if a number is divisible by 3 or not. Print appropriate messages.
// answer:
let num1 = 75;
if (num1%3==0){
    console.log("Divisible by 3")
}else{
    console.log("Not Divisible by 3")
}


//Q.7 Write a program that takes a password as input. If the password is “admin123”, print “Login Successful”, otherwise print “Incorrect Password”.
// answer:
let password = "admin1"
if (password=="admin123"){
    console.log("Login Successful")
}else{
    console.log("Incorrect Password")
}


//Q.8 Check whether a given year is a leap year or not using the basic rule (divisible by 4).
// answer:
let year = 2024;
if (year%4==0){
    console.log("Leap year")
}else{
    console.log("Not a Leap year")
}


//Q.9 Write a program to find the greater of two numbers using if...else.
// answer:
let x = 48;
let y = 59;
if (x>y){
    console.log("a is greater")
}else{
    console.log("b is greater")
}


//Q.10 Check if a number is positive, negative, or zero using only if...else (you may use nested or multiple conditions carefully).
// answer:
let num2 = 0;
if(num2>=0){
    if(num2==0){
        console.log("Zero")
    }else{
        console.log("Positive")
    }
}else{
    console.log("Negative")
}