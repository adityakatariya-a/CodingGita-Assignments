### 4. Strict Inequality `!==`


1. Check whether `"18" !== 18` returns true or false.

**Answer:**

```js
console.log("18" !== 18);  // true
```

---


2. Check if `0 !== false` and `null !== undefined`.

**Answer:**

```js
console.log(0 !== false);  // true
console.log(null !== undefined);  // true
```

---


3. Predict the output:

**Answer:**

   ```js
   console.log(5 !== "5");  // true
   console.log(true !== 1);  // true
   ```

---


4. Predict the output:

**Answer:**

   ```js
   console.log("" !== 0);  // true
   console.log(NaN !== NaN);  //true
   ```

---


5. Write a condition that checks if a variable `input` is strictly not equal to the string `"0"`.

**Answer:**

```js
if (input !== "0") {
  console.log("Input is not the string 0");
}
```