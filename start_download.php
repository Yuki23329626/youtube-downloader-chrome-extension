<?php

$url = 'http://localhost:5000/api/file?url=https://www.youtube.com/watch?v=yLp9x7Dh2jo&format=mp4-1920*1080'; // The URL to send the GET request to

// // Get the file contents
// $fileContents = file_get_contents($url);

// // Set the HTTP headers
// header('Content-Type: video/mp4'); // Set the appropriate content type for your video file
// header('Content-Length: ' . strlen($fileContents));
// header('Content-Disposition: attachment;filename="' . $filename . '"'); // Set the desired file name for the downloaded video

// // Output the file contents
// echo $fileContents;

// Create a stream context to include headers in the request
$options = array(
    'http' => array(
        'header' => 'Content-Type: application/x-www-form-urlencoded\r\n' .
                    'Custom-Header: value\r\n'
    )
);

$context = stream_context_create($options);

// Retrieve the file contents along with the headers
$response = file_get_contents($url, false, $context);

if ($response !== false) {
    // Split the response into headers and content
    list($headers, $content) = explode("\r\n\r\n", $response, 2);

    // Output the headers
    echo "Headers:\n";
    echo $headers;

    // Output the content
    echo "Content:\n";
    echo $content;
} else {
    echo 'Failed to retrieve the file';
}


?>