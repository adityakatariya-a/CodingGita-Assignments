### 8. Less Than or Equal To `<=`


1. Maximum speed limit is 60 km/h. A vehicle is travelling at 60 km/h. Check if it is within the limit.

*Answer:*

```js
let speedLimit = 60
let vehicleSpeed = 60
console.log("Is vehicle driving in limit:", vehicleSpeed <= speedLimit)
```

---


2. A student needs at least 40 marks to pass. He scored 39. Check if he has failed.

*Answer:*

```js
let passingMarks = 40;
let score = 39;
console.log("Is student failed:",score <= passingMarks)
```

---


3. Predict the output:

*Answer:*

   ```js
   console.log(15 <= 20);  // output => true
   console.log(20 <= 15);  // output => false
   console.log(15 <= 15);  // output => true
   ```

---


4. Predict the output:

*Answer:*

   ```js
   console.log("15" <= 20);  // output => true
   console.log("30" <= "5");  // output => true
   console.log(null <= 0);  // output => true
   ```

---


5. What is the result of `undefined <= 0`? Explain.

*Answer:*

false => undefined will be converted to NaN which gives false on comparing with anything.

6. A bag can hold maximum 10 books. Currently it has 10 books. Write a condition using `<=` to check if more books can be added.

*Answer:*

```js
let maxCapacity = 10;
let current = 10;
console.log("Is bag full:", current <= maxCapacity)
```

---


7. Predict and explain:

*Answer:*

```js
console.log(false <= 0); // Output: true => false converted to number is 0 so 0<=0
console.log("" <= 0); // Output: true => value of empty string in number is 0 so 0<=0
console.log(NaN <= 5); // Output: false => Comparing NaN with anything will give false
```