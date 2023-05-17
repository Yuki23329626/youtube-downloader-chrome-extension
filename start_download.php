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

// Make an HTTP request to get the response headers
$headers = get_headers($url, 1);

if ($headers !== false && isset($headers['Content-Disposition'])) {
    $contentDisposition = $headers['Content-Disposition'];

    // Extract the filename from the Content-Disposition header
    if (preg_match('/attachment_filename=(.*)/', $contentDisposition, $matches)) {
        $filename = trim($matches[1]);
        echo 'File name: ' . $filename;
    } else {
        echo 'Unable to extract the file name';
    }
} else {
    echo 'Failed to retrieve response headers';
}


?>