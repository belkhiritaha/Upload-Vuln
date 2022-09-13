<!----- This is the main page of the 4gagZZ website that displays memes posted by ZZ users ----->
<!----- This website is inspired by the petpet rcbee HackTheBox challenge and is built to showcase the web upload vulnerabilities ----->


<?php
    // getMemes function to look for .jpg files in the memes folder and return them as an array
    function getMemes() {
        $memes = array();
        $dir = "memes/";
        $files = scandir($dir);
        foreach ($files as $file) {
            if (preg_match("/.jpg$/", $file)) {
                $memes[] = $file;
            }
        }
        return $memes;
    }
?>

<html>
    <head>
        <title>4gagZZ</title>
    </head>

    <body>
        <div id="header">
            <h1 class="title-header">4gagZZ</h1>
            <img src="logo.png" alt="4gagZZ" width="200" height="200">
        </div>

        <hr>

        <div id="content">
            <h2 class="title-content">Memes</h2>
            <div id="memes">
                <?php
                    $memes = array();
                    $memes = getMemes();
                    foreach($memes as $meme) {
                        echo '<div class="meme">';
                        echo '<img src="' . $meme['image'] . '" alt="' . $meme['title'] . '" width="200" height="200">';
                        echo '<p class="meme-title">' . $meme['title'] . '</p>';
                        echo '<p class="meme-description">' . $meme['description'] . '</p>';
                        echo '</div>';
                    }
                ?>
            </div>
    </body>