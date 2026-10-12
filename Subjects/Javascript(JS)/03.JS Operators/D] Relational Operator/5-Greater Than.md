### 5. Greater Than `>`


1. A student’s marks are 78. The passing marks are 40. Check whether the student has scored more than the passing marks.

*Answer:*

```js
let studentMarks = 78;
let passingMarks = 40;
console.log(studentMarks > passingMarks);  // true
```

---


2. Temperature today is 35°C and yesterday it was 28°C. Check if today is hotter.

*Answer:*

```js
let todayTemp = 35;
let yesterdayTemp = 28;
console.log(todayTemp > yesterdayTemp);  // true
```

---


3. Predict the output:

*Answer:*

```js
console.log(15 > 10);  // true
console.log(10 > 15);  // false
console.log(10 > 10);  // false
```

---


4. Predict the output:

*Answer:*

```js
console.log("20" > 15);  // true  => beacause string contains number and it can convert into number type
console.log("5" > "10");  // false => if both sides has string then it determines on the basis of ascii values 
console.log("abc" > 10);  // false
```

---


5. What is the result of `null > 0` and `undefined > 0`? Explain.

*Answer:*

```js
console.log(null > 0);  // false  => value of null in numbers is 0 and 0 > 0 is false
console.log(undefined > 0);  // false => value of undefined is NaN and NaN > 0 is false
```

---


6. A shop has 120 items in stock. A customer wants to buy 85 items. Write a condition using `>` to check if stock is sufficient.

*Answer:*

```js
let stock = 120;
let wanted = 85;
console.log(stock > wanted);
```

---


7. Predict and explain:

*Answer:*

```js
console.log(true > false); // true => true = 1 and false = 0 , 1 > 0 
console.log("10" > "2");  // false => false because both operands are strings.
console.log(NaN > 5);  // false => any relational comparison involving NaN returns false.
```