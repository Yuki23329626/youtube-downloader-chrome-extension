// Listen for navigation events
chrome.webNavigation.onBeforeNavigate.addListener(details => {
  // Check if the navigation is happening on a specific URL
  // String to replace
  const startingString = "https://www.youtube.com/shorts/";
  if (details.url.startsWith(startingString)) {
    // Modify the URL to redirect
    // Original string
    const originalString = details.url;

    const replacementString = "https://www.youtube.com/watch?v=";

    // Use regular expression to replace startingString with replacementString
    const modifiedString = originalString.replace(new RegExp(`^${startingString}`), replacementString);
    console.log("modifiedString: ", modifiedString)

    // Redirect the page
    chrome.tabs.update(details.tabId, { url: modifiedString });
  }
});