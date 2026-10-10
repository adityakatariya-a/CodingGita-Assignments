### 6. Less Than `<`


1. A box can hold maximum 50 kg. Current weight is 42 kg. Check if more items can still be added.  

*Answer:*

```js
let currentWeight = 42;
let maxWeight = 50;
console.log(currentWeight < maxWeight);
```

---


2. Age of a person is 16. Minimum age required is 18. Check if the person is underage.

*Answer:*

```js
let age = 16;
let minimumAge = 18;
console.log(age < minimumAge);
```

---


3. Predict the output:

*Answer:*

```js
console.log(8 < 12);  // true
console.log(20 < 10);  // false
console.log(7 < 7);  // false
```

---


4. Predict the output:

*Answer:*

```js
console.log("8" < 10);  // true
console.log("20" < "3");  // true
console.log("hello" < 5);  // false
```

---


5. What is the result of `null < 0` and `undefined < 0`? Explain.

*Answer:*

```js
console.log(null < 0);  // false
console.log(undefined < 0);  // false
```

---


6. A tank capacity is 500 litres. Current water level is 375 litres. Write a condition using `<` to check if it is not full.


*Answer:*

```js
let currentWater = 375;
let tankCapacity = 500;
if (currentWater < tankCapacity) {
    console.log("The tank is not full.");
}
```

---


7. Predict and explain:

*Answer:*

```js
console.log(false < true);  // true => JavaScript converts false to 0 and true to 1. Therefore, 0 < 1 is true.
console.log("5" < "15");  // false => Both operands are strings, so JavaScript compares them lexicographically. The first character
// "5" comes after "1", so the result is false.
console.log(NaN < 10);  // false => A relational comparison involving NaN always returns false.
```