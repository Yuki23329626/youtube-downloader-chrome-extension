<?php

$url = 'http://localhost:5000/api/file?url=https://www.youtube.com/watch?v=yLp9x7Dh2jo&format=mp4-1920*1080'; // The URL to send the GET request to

// Get the file contents
// $fileContents = file_get_contents($url);

// Set the HTTP headers
header('Content-Type: video/mp4'); // Set the appropriate content type for your video file
header('Content-Length: ' . strlen($fileContents));
// header('Content-Disposition: attachment;filename="' . $filename . '"'); // Set the desired file name for the downloaded video

// // Output the file contents
// echo $fileContents;

$headers = get_headers($url, 1);

// Check if the request was successful (HTTP 200 OK)
if ($headers && strpos($headers[0], '200') !== false) {
    // $content = file_get_contents($url); 

    echo $headers[3];
    
    // Print the headers
    foreach ($headers as $name => $value) {
        echo $name . ': ' . $value . "<BR>";
    }
    
    // Print the content
    // echo $fileContents;
} else {
    echo 'Error: Failed to retrieve file.';
}

?>