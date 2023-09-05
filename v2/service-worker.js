// Listen for navigation events
chrome.webNavigation.onBeforeNavigate.addListener(details => {
  // Check if the navigation is happening on a specific URL
  const startingString = "https://www.youtube.com/shorts/";
  if (details.url.startsWith(startingString)) {
    // Modify the URL to redirect
    // Original string
    const originalString = details.url;

    // String to replace
    const replacementString = "https://www.youtube.com/watch?v=";

    // Use regular expression to replace startingString with replacementString
    const modifiedString = originalString.replace(new RegExp(`^${startingString}`), replacementString);
    console.log("modifiedString: ", modifiedString)

    // Redirect the page
    chrome.tabs.update(details.tabId, { url: modifiedString });
  }
});

// // Listen for messages from the popup script.
// chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
//   if (message.action === 'DOWNLOAD') {
//     // Perform the desired action in response to the message.
//     console.log('Action DOWNLOAD triggered in the service-worker script');
//     // download
//     var port = chrome.runtime.connectNative('com.example.nativeapp');
//     port.onMessage.addListener(function (msg) {
//       console.log('NativeApp - Received:', msg);
//     });
//     port.onDisconnect.addListener(function () {
//       console.log('NativeApp - Disconnected');
//     });
//     port.postMessage({ text: 'Hello, my_application' });
//   }
// });
