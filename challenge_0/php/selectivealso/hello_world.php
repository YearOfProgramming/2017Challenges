<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Hello World!</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <link rel="stylesheet" href="https://code.getmdl.io/1.2.1/material.blue_grey-indigo.min.css" />
    <script defer src="https://code.getmdl.io/1.2.1/material.min.js"></script>
    <link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Roboto:300,400,500,700" type="text/css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.6/css/bootstrap.min.css">
  </head>
  <body>

    <div class="container">
      <div class="col-md-8 col-md-offset-2">
        <br><br><br>
        <form action="hello_world.php" method="post">
          <button type="submit" name="submit" class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">
            Click me!
          </button>
        </form>

        <?php

        if (isset($_POST['submit'])) {
          echo "<h2>Hello World!</h2>";
        }
        ?>

      </div>
    </div>

  </body>
</html>