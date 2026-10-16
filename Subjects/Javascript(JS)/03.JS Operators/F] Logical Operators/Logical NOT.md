### 3. Logical NOT `!`


Write a JavaScript program for each:

1. A user is not banned (`isBanned = false`). Check if they can login by negating `isBanned` using `!`.

*Answer:*

```js
let isBanned = false;
let canLogin = !isBanned
console.log("Can login? -",canLogin)
```


2. A task is not completed (`isCompleted = false`). Check if it is still pending using `!`.

*Answer:*

```js
let isCompleted = false;
let stillPending = !isCompleted
console.log("Is task pending? -",stillPending)
```


3. A light is on (`isOn = true`). Check if it is off using `!`.

*Answer:*

```js
let isOn = true;
let isOff = !isOn;
console.log("Is the light off? -",isOff)
```


4. A subscription is not active (`isActive = false`). Check if the user cannot access premium content using `!`.

*Answer:*

```js
let isActive = false;
let cannotAccess = !isActive
console.log("User can't access premium content? -",cannotAccess)
```


5. A file is not read‑only (`isReadOnly = false`). Check if it can be edited using `!`.

*Answer:*

```js
let isReadOnly = false;
let canBeEdited = !isReadOnly;
console.log("File can be edited? -",canBeEdited)
```


### Additional Questions (Logical NOT `!`)

6. Predict the output:
   ```js
   let a = 0;
   let b = 1;
   console.log(!a, !b);  // output => true false
   ```

7. Predict the output:
   ```js
   let x = "Hello";
   let y = "";
   console.log(!x, !y);  // output => false true
   ```

8. Predict the output:
   ```js
   let val = 5;
   let result = !val;
   console.log(result);  // output => false
   ```

9. Predict the output:
   ```js
   let a = 10;
   let b = 20;
   let result = !(a && b);
   console.log(result);  // output => false
   ```

10. Predict the output:
    ```js
    let x = 0;
    let y = 1;
    let result = !(x || y);
    console.log(result);  // output => false
    ```