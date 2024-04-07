<!DOCTYPE html>
<html>
<head>
    <title>Weather LorAI</title>
</head>
<body>
    <?php
    if (isset($_POST["submit"])) {
		$api_url = "http://127.0.0.1:5000/?date=".$_POST["DateD"].$_POST["DateM"];
        
        $response = file_get_contents($api_url);

        echo "Weather lore for ".$_POST["DateD"].$_POST["DateM"].": ".$response;
	} 
    else {
        echo "Pick a date and get a weather lorAI!";
    }
    ?>
    <form method="post">
        <select name="DateD" id="DateD">
		<?php 
        for($i = 1; $i <= 31; $i++) {
            if ($i < 10) {
                echo "<option value=0$i.";
            }
            else {
                echo "<option value=$i.";
            }
		if ($i == date("j")) echo ' selected';
		echo ">$i</option>\n";
        } 
        ?>
	    </select>.
	    <select name="DateM" id="DateM">
		<?php 
        for($i = 1; $i <= 12; $i++) {
            if ($i < 10) {
                echo "<option value=0$i.";
            }
            else {
                echo "<option value=$i.";
            }
		if ($i == date("n")) echo ' selected';
		echo ">$i</option>\n";
        }  
        ?>
	    </select>
        <input type="submit" name="submit" value="Generate lore!">
    </form>
</body>
</html>