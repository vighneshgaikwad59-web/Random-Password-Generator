Random Password Generator

A simple Python script that generates a random password of user-defined length using a fixed pool of characters.
<br>
<hr>

How It Works


The script defines a string chars containing a fixed set of characters (digits and letters) to pick from.
It asks the user to enter a value (core) — this decides how many characters the generated password will have.
Using a for loop, it randomly picks one character at a time from chars (via random.choice) and appends it to the password string.
Once the loop finishes, it prints the final password.
