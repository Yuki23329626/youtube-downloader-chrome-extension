current_url = ''
// host = 'http://localhost:5000/api/file'
host = 'http://tux.cs.ccu.edu.tw/~snx108m/start_download.php'

// chrome.tabs.query({ active: true, lastFocusedWindow: true }, tabs => {
//     current_url = tabs[0].url;
//     console.log(tabs)
//     // use `url` here inside the callback because it's asynchronous!
// });

async function getCurrentTab() {
    let queryOptions = { active: true, lastFocusedWindow: true };
    // `tab` will either be a `tabs.Tab` instance or `undefined`.
    let [tab] = await chrome.tabs.query(queryOptions);
    console.log('tab', tab)
    return tab.url;
}

document.getElementById("btn_download_mp4_FHD").addEventListener(
    "click",
    function () { start_download('mp4-1920*1080') },
    false
);

document.getElementById("btn_download_audio").addEventListener(
    "click",
    function () { start_download('bestaudio') },
    false
);

async function start_download(format) {
    format = '&format=' + format
    current_url = await getCurrentTab()
    console.log('current_url=', current_url)
    document.getElementById("p1").innerHTML = "Processing, please wait...";

    chrome.downloads.download({
        url: host + '?url=' + current_url + format,
        saveAs: false
    }).then((result) => {
        document.getElementById("p1").innerHTML = "Finshed";
    }).catch((err) => {
        // document.getElementById("p1").innerHTML = err;
        return err
    });

    // Cannot download files via fetch as a chrome extension through fetch()
    // fetch('http://localhost:5000/api/file?url=' + current_url, {cache:"no-store"})
    //     .then(function (response) {
    //         console.log(response)
    //     })
    //     .catch(error => console.error(error));
}