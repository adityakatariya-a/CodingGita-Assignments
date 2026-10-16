### 1. Logical AND `&&`


Write a JavaScript program for each:

1. Stored username is `"admin"` and password is `1234`. Check if both are valid using `&&` and print the result.

*Answer:*

```js
let username = "admin";
let password = 1234;
let inputUsername = "aditya";
let inputPassword = 1234;
let validation = username==inputUsername && password==inputPassword;
console.log("Is user valid? - ",validation)
```


2. A user is logged in (`isLoggedIn = true`) and has permission (`hasPermission = true`). Check if they can access a page using `&&`.

*Answer:*

```js
let isLoggedIn = true;
let hasPermission = true;
let access = isLoggedIn && hasPermission;
console.log("Can access the page?",access);
```


3. A product is in stock (`inStock = true`) and its price is less than ₹1000 (`price = 800`). Check if it can be bought using `&&`.

*Answer:*

```js
let inStock = true;
let price = 800;
let canBought = inStock && price<1000;
console.log("Product can be bought?",canBought);
```


4. A student has marks `75` and attendance `80`. Passing requires marks greater than `65` **and** attendance greater than `70`. Check using `&&`.

*Answer:*

```js
let marks = 75;
let attendance = 80;
let ispassed = (marks>65) && (attendance>70);
console.log("Is student passed?",ispassed)
```


5. Two conditions: `isWeekend = true` and `isHoliday = false`. A party happens only if both are true. Check using `&&`.

*Answer:*

```js
let isWeekend = true;
let isHoliday = false;
let partyHappen = isWeekend && isHoliday;
console.log("Is party happen?",partyHappen)
```


### Additional Questions (Logical AND `&&`)

6. Predict the output:
   ```js
   let a = 0;
   let b = 10;
   let result = a && b;
   console.log(result);  // output => 0
   ```

7. Predict the output:
   ```js
   let x = 5;
   let y = 10;
   let result = (x > 3 && y) || 0;
   console.log(result);  // output => 10
   ```

8. Predict the output:
   ```js
   let p = "Hello";
   let q = "";
   let r = "World";
   let result = p && q && r;
   console.log(result);  // output =>  
   ```

9. Predict the output:
   ```js
   let val = 5;
   let condition = val && (val = 0);
   console.log(condition);
   console.log(val);  // output => 0
   ```

10. Predict the output:
    ```js
    let x = 10;
    let y = 20;
    let result = (x && y) && (x > y);
    console.log(result);  // output => false
    ```