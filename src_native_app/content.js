
document.addEventListener('yt-navigate-start', function () {
})

function process(){
  const startingString = "https://www.youtube.com/shorts/";
  var currentUrl = window.location.href;
  console.log("content-url: ", currentUrl)

  if (currentUrl.startsWith(startingString)) {
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
}

// // This function will be executed on every click event within the YouTube page.
// function handleClick(event) {
//   console.log('----- handleClick start -----')
//   // Prevent default behavior (navigation)
//   event.preventDefault();
//   event.stopPropagation();

//   // Find the nearest ancestor anchor element
//   const clickedElement = event.target;
//   const anchorElement = clickedElement.closest('a');

//     // redirect the url if match
//     if(anchorElement){
//       const href = anchorElement.getAttribute('href');
//       console.log('Clicked Anchor Href:', href);
//       if(href.startsWith('/shorts/')){
//         console.log('FK you')
//       }
//     } else {
//       console.log("anchorElement is null");
//     }

//   // Log the clicked element's outerHTML for demonstration purposes
//   console.log('Clicked Element:', event.target.outerHTML);

//   // You can add your own custom logic here to perform actions other than navigation.
//   console.log('----- handleClick end -----')
// }

// // Attach the click event listener to the document
// document.addEventListener("click", handleClick, true);

// === Legacy ===

// async function handleLinkClick(event) {
//   event.preventDefault();
//   console.log('event.target.outerHTML:', event.target.outerHTML);
//   const clickedElement = event.target;
  
//   // Find the nearest ancestor anchor element
//   const anchorElement = clickedElement.closest('a');

//   // redirect the url if match
//   if(anchorElement){
//     const href = anchorElement.getAttribute('href');
//     console.log('Clicked Anchor Href:', href);
//   } else {
//     console.log("anchorElement is null");
//   }
//   // alert('Clicked Anchor Href:' + href);
// }

// // Attach the event listener to all <a> elements
// const links = document.querySelectorAll(
//   '*'
//   // '.ytp-inline-preview-scrim, .ytd-playlist-thumbnail, .yt-core-image'
// );
// links.forEach(link => {
//   link.addEventListener('click', handleLinkClick);
// });
