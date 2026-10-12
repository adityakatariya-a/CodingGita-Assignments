### Part b:


6. Start with `x = 5`.  
   - Create `y = x++`  
   - Print both `x` and `y`.  
   Explain why the values are different.

*Answer:*

```js
let x = 5;
let y = x++;
console.log(x,y);  // x = 6 and y = 5 , because we use postfix that use current value  and then icreament.
```

---

7. Start with `a = 5`.  
   - Create `b = ++a`  
   - Print both `a` and `b`.  
   Explain the difference from the previous question.

*Answer:*

```js
let a = 5;
let b = ++a;
console.log(a,b);  // a = 6 and b = 6 , because we use prefix that icreases value first , then use new value
```

---

8. Start with `lives = 3`.  
   - Use post-decrement (`lives--`) and store the result in `previousLives`.  
   - Print both variables.

*Answer:*

```js
let lives = 3;
let previousLives = lives--;
console.log(lives , previousLives);
```

---

9. Start with `attempts = 0`.  
   - Use pre-increment (`++attempts`) and store the result in `currentAttempts`.  
   - Print both variables.

*Answer:*

```js
let attempts = 0;
let currentAttempts = ++attempts;
console.log(attempts);
console.log(currentAttempts);
```

---

10. Start with `points = 100`.  
    - Increase it using `++`  
    - Then decrease it using `--`  
    - Print the final value.

*Answer:*

```js
let points = 100;
points++;
points--;
console.log(points);
```