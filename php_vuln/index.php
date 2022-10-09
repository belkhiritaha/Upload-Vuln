<?php
// this is a website with only an upload form that sends the uploaded files to the uploads/ directory
// the upload form is in the index.php file

echo '<form action="upload.php" method="post" enctype="multipart/form-data">
    Select file to upload:
    <input type="file" name="fileToUpload" id="fileToUpload">
    <input type="submit" value="Upload File" name="submit">
</form>';

echo '<style>
    body {
        background-color: #000;
        color: #fff;
    }

    form {
        margin: 0 auto;
        width: 300px;
        padding: 20px;
        border: 1px solid #fff;
    }
    </style>';

?>