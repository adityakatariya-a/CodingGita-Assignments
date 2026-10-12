### 7. Greater Than or Equal To `>=`


1. Minimum marks required for distinction is 75. A student scored 75. Check if the student gets distinction.

*Answer:*

```js
let requiredMarks = 75
let scoredMarks = 75
console.log("Is student got distinction:", scoredMarks >= requiredMarks)
```

---


2. Ticket price is ₹300. A person has ₹300. Check if they can buy the ticket.

*Answer:*

```js
let ticketPrice = 300
let personBudget = 300
console.log("Can the person buy ticket:", personBudget >= ticketPrice)
```

---


3. Predict the output:

*Answer:*

   ```js
   console.log(25 >= 25);  // output => true
   console.log(30 >= 25);  // output => true
   console.log(20 >= 25);  // output => false
   ```

---


4. Predict the output:

*Answer:*

   ```js
   console.log("25" >= 25);  // output => true
   console.log("10" >= "2");  // output => false
   console.log(null >= 0);  // output => true
   ```

---


5. What is the result of `undefined >= 0`? Explain.

*Answer:*

 false => undefined will be converted in NaN which gives false on comparing with anything

---


6. A lift can carry maximum 8 people. Currently 8 people are inside. Write a condition using `>=` to check if the lift is full or overloaded.

*Answer:*

```js
let maxCapacity = 8;
let current = 8
console.log("Is lift full:",current >= maxCapacity)
```

---


7. Predict and explain:

*Answer:*

```js
console.log(true >= 1); // Output: true => true will be converted to number(1) so 1>=1
console.log("" >= 0); // Output: true => empty string converted to number is 0 so 0>=0
console.log(NaN >= NaN); // Output: false => NaN compared to anything including itself will give false
```