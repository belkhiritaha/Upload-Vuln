<?php

// this file is the upload.php file that receives the uploaded files from the index.php file

// check if the form was submitted
if(isset($_POST["submit"])) {
    // check if the file was uploaded without errors
    if(isset($_FILES["fileToUpload"]) && $_FILES["fileToUpload"]["error"] == 0){
        $filename = $_FILES["fileToUpload"]["name"];
        $filetype = $_FILES["fileToUpload"]["type"];
        $filesize = $_FILES["fileToUpload"]["size"];

        move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], "uploads/" . $_FILES["fileToUpload"]["name"]);
        echo "Your file was uploaded successfully to the uploads/ directory.";
    } else{
        echo "Error: " . $_FILES["fileToUpload"]["error"];
    }
}