<?php

$host = 'http://localhost:5000/api/file'; // The URL to send the GET request to

$url = $_GET['url'];
$format = $_GET['format'];

$fianl_request = $host . '?url=' . $url . '&format=' . $format;

echo 'test:' . $fianl_request;

// Get the file contents
$fileContents = file_get_contents($fianl_request);

// Set the HTTP headers
// header('Content-Type: video/mp4'); // Set the appropriate content type for your video file
// header('Content-Length: ' . strlen($fileContents));
// header('Content-Disposition: attachment;filename="' . $filename . '"'); // Set the desired file name for the downloaded video

// // Output the file contents
// echo $fileContents;

$headers = get_headers($fianl_request);

// Check if the request was successful (HTTP 200 OK)
if ($headers && strpos($headers[0], '200') !== false) {
    // $content = file_get_contents($fianl_request); 

    // echo $headers[0];

    header($headers[4]); // Set the appropriate content type for your video file
    header($headers[5]);
    header($headers[3]); // Set the desired file name for the downloaded video

    // // Print the headers
    // foreach ($headers as $name => $value) {
    //     echo $name . ': ' . $value . "<BR>";
    // }

    echo $fileContents;
} else {
    echo 'Error: Failed to retrieve file.';
}

?>