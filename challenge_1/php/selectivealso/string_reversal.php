<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Reverse a String</title>
    <!-- MDL and Bootstrap -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <link rel="stylesheet" href="https://code.getmdl.io/1.2.1/material.blue_grey-indigo.min.css" />
    <script defer src="https://code.getmdl.io/1.2.1/material.min.js"></script>
    <link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Roboto:300,400,500,700" type="text/css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.6/css/bootstrap.min.css">
    <!-- End MDL & BS -->
  </head>
  <body>
    <!-- Just some bootstrap formatting to make it look better -->
    <div class="container">
      <div class="col-md-8 col-md-offset-2">
        <br><br><br>
        <!-- Begin Form -->
        <form action="string_reversal.php" method="post">
          <!-- MDL Textfield for string input -->
          <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
            <input class="mdl-textfield__input" value="" name="string" type="text" id="string">
            <label class="mdl-textfield__label" for="string">Input a String</label>
          </div>
          <!-- End Textfield -->
          <br>
          <!-- MDL Submit Button -->
          <button type="submit" name="submit" class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">
            Reverse
          </button>
          <!-- End Submit -->
        </form>
        <!-- End Form -->

        <?php

          // if the form was submitted
          if (isset($_POST['submit'])) {
            // echo a title
            echo "<h2>Your Reversed String:</h2>";
            // and echo the reversed string
            echo strrev($_POST['string']);
          }

        ?>

      </div>   <!-- end col -->
    </div>     <!-- end container -->
  </body>
</html>