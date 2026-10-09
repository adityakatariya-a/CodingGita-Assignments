### 3. Strict Equality `===`


1. Check whether `"25" === 25` returns true or false. Explain why.

**Answer**

```js
console.log("25" === 25);  // false
```

---


2. Check if `0 === false` and `null === undefined`.

**Answer:**

```js
console.log(0 === false);  // false
console.log(null === undefined);  // false
```

---


3. Predict the output:

**Answer:**

   ```js
   console.log(10 === "10"); // false
   console.log(true === 1);  // false
   ```

---


4. Predict the output:

**Answer:**

   ```js
   console.log("" === 0);  // false
   console.log([] === false);  // false
   ```

---


5. Why is `===` preferred over `==` in most real-world code?

**Answer:**

=== is preferred over == because it checks equality without performing type conversion. This makes your code more predictable and helps prevent unexpected bugs.