<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Check if a file was uploaded
    if (isset($_FILES["image"]) && $_FILES["image"]["error"] == UPLOAD_ERR_OK) {
        $uploadDir = __DIR__ . '/uploads/';
        $uploadFile = $uploadDir . basename($_FILES["image"]["name"]);

        // Move the uploaded file to the destination directory
        if (move_uploaded_file($_FILES["image"]["tmp_name"], $uploadFile)) {
            // Call the Python script with the uploaded file as an argument
            $output = shell_exec("python exif.py " . escapeshellarg($uploadFile));

            // Display the Python script's output on the webpage
            echo "<h2>Python Script Output:</h2>";
            echo "<pre>$output</pre>";
        } else {
            echo "<h2>Error uploading file</h2>";
        }
    } else {
        echo "<h2>No file uploaded</h2>";
    }
}
?>
