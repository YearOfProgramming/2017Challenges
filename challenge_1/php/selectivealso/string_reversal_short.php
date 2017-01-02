<!-- Here is a very short version without being proper and all that -->
<form action="string_reversal_short.php" method="post">
  <input type="text" name="string">
  <button type="submit" name="submit">Reverse</button>
</form>

<!-- This is php shorthand for an if statement -->
<!-- i wouldn't use this irl -->
<?php echo isset($_POST['submit']) ? strrev($_POST['string']) : null; ?>