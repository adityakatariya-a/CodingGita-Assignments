# Bonus Mixed Practice Questions:

19.Predict the output:

*Answer:*

    ```js
    let count = 5;
    console.log(typeof count++);  // output => number
    console.log(count);  // output => 6
    console.log(typeof ++count);  // output => number
    console.log(count);  // output => 7
    ```


20.Predict the output:

*Answer:*

    ```js
    let x = "10";
    let y = ++x;
    console.log(x, y, typeof x, typeof y);  // output => 11 11 number number
    ```


21.Predict the output:

*Answer:*

    ```js
    let a = "5";
    let b = a++;
    console.log(a, b, typeof a, typeof b);  // output => 6 5 number number
    ```


22.Predict the output:

*Answer:*

    ```js
    console.log(typeof (1 + "2"));  // output => string
    console.log(typeof (1 - "2"));  // output => number
    console.log(typeof (1 * "2"));  // output => number
    console.log(typeof (1 / "2"));  // output => number
    ```


23.Predict the output:

*Answer:*

    ```js
    let val = null;
    console.log(typeof val);  // output => object
    console.log(val + 1);  // output => 1
    console.log(val - 1);  // output => -1
    console.log(val * 1);  // output => 0
    console.log(Boolean(val));  // output => false
    ```