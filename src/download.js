current_url = ''
chrome.tabs.query({ active: true, lastFocusedWindow: true }, tabs => {
    current_url = tabs[0].url;
    // console.log(current_url)
    // use `url` here inside the callback because it's asynchronous!
});

document.getElementById("btn_download").addEventListener("click", start_download);

function start_download() {
    console.log(current_url)
    document.getElementById("p1").innerHTML = current_url;

    chrome.downloads.download({
        url: 'http://localhost:5000/api/file?url=' + current_url,
        saveAs: false
      });

    // Cannot download files via fetch as a chrome extension through fetch()
    // fetch('http://localhost:5000/api/file?url=' + current_url, {cache:"no-store"})
    //     .then(function (response) {
    //         console.log(response)
    //     })
    //     .catch(error => console.error(error));
}
