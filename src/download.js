current_url = ''
// host = 'http://localhost:5000/api/file'
// host = 'http://tux.cs.ccu.edu.tw/~snx108m/start_download.php'
host = 'http://nxshen.csie.io:5000/api/file'


// chrome.tabs.query({ active: true, lastFocusedWindow: true }, tabs => {
//     current_url = tabs[0].url;
//     console.log(tabs)
//     // use `url` here inside the callback because it's asynchronous!
// });

async function getCurrentTab() {
    let queryOptions = { active: true, currentWindow: true };
    // `tab` will either be a `tabs.Tab` instance or `undefined`.
    let [tab] = await chrome.tabs.query(queryOptions);
    console.log('tab', tab)

    return tab.url;
}

document.getElementById("btn_download_mp4_FHD").addEventListener(
    "click",
    function () {
        start_download('mp4')
    },
    false
);

document.getElementById("btn_download_audio").addEventListener(
    "click",
    function () {
        start_download('bestaudio')
    },
    false
);

function onReceived(response) {
    console.log("response:", response);
}

async function start_download(format) {
    format = '&format=' + format
    current_url = await getCurrentTab()
    // console.log('current_url=', current_url)
    document.getElementById("p1").innerHTML = "Processing, please wait...";

    target_url = host + '?url=' + current_url + format
    console.log('target_url=', target_url)
    // chrome.runtime.sendNativeMessage({ action: 'DOWNLOAD', request_url: target_url });
    // runtime.connectNative
    // var port = chrome.runtime.connectNative("com.example.nativeapp");
    // port.onMessage.addListener(onReceived);
    // port.postMessage("hello");

    chrome.downloads.download({
        url: target_url,
        saveAs: false
    }).then((result) => {
        document.getElementById("p1").innerHTML = "Finshed";
        // document.getElementById("p1").innerHTML = result;
    }).catch((err) => {
        document.getElementById("p1").innerHTML = err;
    });

    // Cannot download files via fetch as a chrome extension through fetch()
    // fetch('http://localhost:5000/api/file?url=' + current_url, {cache:"no-store"})
    //     .then(function (response) {
    //         console.log(response)
    //     })
    //     .catch(error => console.error(error));
}