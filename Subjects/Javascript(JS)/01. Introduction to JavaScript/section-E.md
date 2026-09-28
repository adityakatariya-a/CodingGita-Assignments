# Section E: Code-Based Questions

**Q20. Predict the output of the following code and explain why:**

```javascript
let value = 25;
console.log(typeof value);
value = "JavaScript";
console.log(typeof value);
value = false;
console.log(typeof value);
```

**Output:**

```text
number
string
boolean
```

**Explanation:**  
JavaScript is dynamically typed, so the same variable can store different data types while the program runs. Here, `value` changes from a number to a string and then to a boolean.

---

**Q21. Write a simple HTML + JavaScript program that displays an alert box with the message "Welcome to JavaScript!" when a button is clicked.**

```html
<!DOCTYPE html>
<html>
<head>
  <title>JavaScript Alert Example</title>
</head>
<body>
  <button onclick="showMessage()">Click Me</button>

  <script>
    function showMessage() {
      alert("Welcome to JavaScript!");
    }
  </script>
</body>
</html>
```

---

**Q22. Write JavaScript code to demonstrate event-driven programming.**

```html
<!DOCTYPE html>
<html>
<head>
  <title>Event-Driven Programming</title>
</head>
<body>
  <button id="myBtn">Click Me</button>
  <p id="demo">Waiting for button click...</p>

  <script>
    const myButton = document.getElementById("myBtn");
    const paragraph = document.getElementById("demo");

    myButton.addEventListener("click", function () {
      paragraph.textContent = "Button was clicked!";
    });
  </script>
</body>
</html>
```

**Explanation:**  
The `click` event occurs when the user clicks the button. JavaScript listens for this event and changes the paragraph text.