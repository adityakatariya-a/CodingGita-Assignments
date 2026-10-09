### 3. Subtract and Assign `-=`

1. Health is `100`. Player takes `35` damage. Update health using `-=`.

**Answer:**

```js
let health = 100;
health -= 35;
console.log(health)
```

---

2. Stock of 300 items is reduced by 45 after a sale. Update using `-=`.

**Answer:**

```js
let stock = 300;
stock -= 45;
console.log(stock)
```

---

3. Predict the output:

**Answer:**

   ```js
   let lives = 5;
   lives -= 2;
   console.log(lives);  // output => 3
   ```

---

4. Predict the output:

**Answer:**

   ```js
   let num = "40";
   num -= 15;
   console.log(num); // output => 25
   ```

---

5. What is the result of `let x = "abc"; x -= 5;`? Explain.

**Answer:**

Output is NaN (not a number) , because x assigns abc which is character and numbers should not subtract from character . if a string contains numbers then js convert its type into number , but if string contains character then it does not convert in this situation.

