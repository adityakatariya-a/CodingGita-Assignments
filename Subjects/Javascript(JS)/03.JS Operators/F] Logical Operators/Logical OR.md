### 2. Logical OR `||`


Write a JavaScript program for each:

1. A user can login with either a correct password (`passwordCorrect = true`) or a valid OTP (`otpValid = false`). Check if login is allowed using `||`.

*Answer:*

```js
let passwordCorrect = true;
let otpValid = false;
let loginPossible = passwordCorrect || otpValid;
console.log("Is Login Possible? -",loginPossible)
```


2. A discount applies if the user is a member (`isMember = false`) or has a coupon (`hasCoupon = true`). Check using `||`.

*Answer:*

```js
let isMember = false;
let hasCoupon = true;
let getDiscount = isMember || hasCoupon;
console.log("Will customer get discount? -",getDiscount)
```


3. Entry is allowed if age is above `18` (`age = 16`) **or** height is above `150` cm (`height = 155`). Check using `||`.

*Answer:*

```js
let age = 16;
let height = 155;
let isAllowed = (age>18) || (height>150);
console.log("Is entry Allowed? -",isAllowed)
```


4. A form is valid if either email is given (`emailGiven = true`) or phone is given (`phoneGiven = false`). Check using `||`.

*Answer:*

```js
let emailGiven = true;
let phoneGiven = false;
let valid = emailGiven || phoneGiven;
console.log("Is the form valid?",valid)
```


5. A game level opens if score is above `1000` (`score = 900`) **or** time bonus is collected (`timeBonus = true`). Check using `||`.

*Answer:*

```js
let score = 900;
let timeBonus = true;
let level = (score>1000) || timeBonus
console.log("Is the level Open? -",level)
```


### Additional Questions (Logical OR `||`)

6. Predict the output:
   ```js
   let a = 0;
   let b = false;
   let c = "";
   let d = null;
   let e = 42;
   let result = a || b || c || d || e;
   console.log(result);  // output => 42
   ```

7. Predict the output:
   ```js
   let x = "Hello" || 0;
   let y = 0 || "Hi";
   console.log(x, y);  // output => Hello Hi
   ```

8. Predict the output:
   ```js
   let a = 10;
   let b = 20;
   let result = (a < 5) || (b > 15);
   console.log(result);  // output => true
   ```

9. Predict the output:
   ```js
   let val = 5;
   let condition = val || (val = 0);
   console.log(condition);  // output => 5
   console.log(val);  // output => 5
   ```

10. Predict the output:
    ```js
    let x = "" || 0 || false || null || undefined || "OK";
    console.log(x);  // output => OK
    ```