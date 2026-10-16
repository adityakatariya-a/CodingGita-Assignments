### Part c:


11.Predict the output:

*Answer:*

    ```js
    console.log(typeof typeof 100);  // output => string
    console.log(typeof typeof "Hi");  // output => string
    console.log(typeof typeof true);  // output => string
    ```


12.Predict the output:

*Answer:*

    ```js
    let a = 10;
    let b = "10";
    console.log(typeof a === typeof b);  // output => false
    console.log(typeof a == typeof b);  // output => false
    ```


13.Predict the output:

*Answer:*

    ```js
    console.log(typeof null === "object");  // output => true
    console.log(typeof [] === "object");  // output => true
    console.log(typeof {} === "object");  // output => true
    ```


14.Predict the output:

*Answer:*

    ```js
    let x;
    console.log(typeof x);  // output => undefined
    x = null;
    console.log(typeof x);  // output => object
    x = 0;
    console.log(typeof x);  // output => number
    ```


15.Predict the output:

*Answer:*

    ```js
    console.log(typeof NaN === "number");  // output => true
    console.log(typeof Infinity === "number");  // output => true
    console.log(typeof (1 / 0));  // output => number
    ```