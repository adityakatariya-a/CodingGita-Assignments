# Section F: Practical / Application Based

**Q23. Complete HTML + JavaScript Code**

```html
<!DOCTYPE html>
<html>
<head>
  <title>My First JavaScript Page</title>
</head>
<body>
  <h1>My First JavaScript Page</h1>

  <button id="clickButton">Click Me</button>

  <script>
    console.log("JavaScript is running successfully!");

    const clickButton = document.getElementById("clickButton");

    clickButton.addEventListener("click", function () {
      alert("Hello, B.Tech Student!");
      document.body.style.backgroundColor = "lightblue";
    });
  </script>
</body>
</html>
```