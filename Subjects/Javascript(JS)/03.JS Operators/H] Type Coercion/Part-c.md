### Part c:

11.Predict the output:

*Answer:*

    ```js
    console.log("5" + 3 + 2);  // output => 532
    console.log(5 + 3 + "2");  // output => 85
    console.log("5" - 3 + 2);  // output => 4
    console.log(5 - "3" + "2");  // output =>22 
    ```


12.Predict the output:

*Answer:*

    ```js
    console.log(true + true);  // output => 2
    console.log(true + false);  // output => 1
    console.log(true + "false");  // output => truefalse
    console.log(false + "true");  // output => falsetrue
    ```


13.Predict the output:

*Answer:*

    ```js
    console.log(null + 5);  // output => 5
    console.log(undefined + 5);  // output => NaN
    console.log(null + "5");  // output => null5
    console.log(undefined + "5");  // output => undefined5
    ```


14.Predict the output:

*Answer:*

    ```js
    console.log([] + []);  // output => ""
    console.log([] + {});  // output => [object Object]
    console.log({} + []);  // output => [object Object]
    console.log({} + {});  // output => [object Object][object Object]
    ```


15.Predict the output:

*Answer:*

    ```js
    let a = "10";
    let b = 5;
    let c = a + b;
    let d = a - b;
    let e = +a + b;
    console.log(c, typeof c);  // output => 105 string
    console.log(d, typeof d);  // output => 5 number
    console.log(e, typeof e);  // output => 15 number
    ```


16.Predict the output:

*Answer:*

    ```js
    console.log(!!"Hello");  // output => true
    console.log(!!"");  // output => false
    console.log(!!0);  // output => false
    console.log(!!1);  // output => true
    console.log(!!null);  // output => false
    console.log(!!undefined);  // output => false
    ```


17.Predict the output:

*Answer:*

    ```js
    console.log(Number(""));  // output => 0
    console.log(Number(" "));  // output => 0
    console.log(Number("0"));  // output => 0
    console.log(Number("  25  "));  // output => 25
    console.log(Number("25px"));  // output => NaN
    ```


18.Predict the output:

*Answer:*

    ```js
    let val1 = "5";
    let val2 = 2;
    console.log(val1 + val2);  // output => 52
    console.log(+val1 + val2);  // output => 7
    console.log(val1 - val2);  // output => 3
    console.log(val1 * val2);  // output => 10
    console.log(val1 / val2);  // output => 2.5
    ```