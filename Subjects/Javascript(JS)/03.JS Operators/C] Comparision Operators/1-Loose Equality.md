### 1. Loose Equality `==`


1. Check whether the string `"25"` is loosely equal to the number `25`. 

**Answer:**

```js
console.log("25"==25); // true
```

---


2. Check if `0 == false` returns true or false.  

**Answer:**

```js
console.log(0 == false);  // true
```

---


3. Predict the output:

**Answer:**

   ```js
   console.log(10 == "10");  // true
   console.log(null == undefined);  // true
   ```

   ---


4. Predict the output:

**Answer:**

   ```js
   console.log("" == 0);  // true
   console.log([] == false);  // true
   ```

   ---


5. Why does `NaN == NaN` return `false`?

**Answer:**

because NaN represents an invalid or numeric result, and JavaScript defines NaN as unequal to every value, including itself.