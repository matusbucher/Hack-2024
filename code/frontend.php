<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather LorAI</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Weather LorAI</h1>
        <p class="intro-text">
            Pick a date and get a weather lore!
        </p>
        <form method="post" class="weather-form">
            <div class="form-group">
                <label for="DateD">Day:</label>
                <select name="DateD" id="DateD" class="form-control">
                    <?php
                    for($i = 1; $i <= 31; $i++) {
                        if ($i < 10) {
                            echo "<option value=0$i.";
                        }
                        else {
                        echo "<option value=$i.";
                        }
                        if (isset($_POST["DateD"]) && $i == $_POST["DateD"]) echo ' selected';
                        else if ($i == date("j")) echo ' selected';
                        echo ">$i</option>\n";
                    } 
                    ?>
                </select>
            </div>
            <div class="form-group">
                <label for="DateM">Month:</label>
                <select name="DateM" id="DateM" class="form-control">
                    <?php 
                    for($i = 1; $i <= 12; $i++) {
                        if ($i < 10) {
                            echo "<option value=0$i.";
                        }
                        else {
                        echo "<option value=$i.";
                        }
                        if (isset($_POST["DateM"]) && $i == $_POST["DateM"]) echo ' selected';
                        else if ($i == date("n")) echo ' selected';
                        echo ">$i</option>\n";
                    } 
                    ?>
                </select>
            </div>
            <button type="submit" name="submit" class="btn btn-primary">Generate lore!</button>
        </form>
        <?php
        if (isset($_POST["submit"])) {
            $api_url = "http://127.0.0.1:5000/?date=".$_POST["DateD"].$_POST["DateM"];
            $response = explode("&", file_get_contents($api_url));
            echo "<div class='weather-result'>";
            echo "<strong>Weather lore for " . $_POST["DateD"] . $_POST["DateM"] . "<br><br> " . $response[0] . "</strong><br>";
            echo "</div>";
            echo "<div> Reasoning: $response[1] </div>";
        } 
        ?>
    </div>
</body>
</html>
