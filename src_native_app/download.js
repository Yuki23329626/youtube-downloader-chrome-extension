current_url = ''

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

    current_url = current_url + format
    console.log('current_url=', current_url)
    // chrome.runtime.sendNativeMessage({ action: 'DOWNLOAD', request_url: target_url });
    // runtime.connectNative

    var port = chrome.runtime.connectNative("com.example.nativeapp");
    port.onMessage.addListener(onReceived);
    port.postMessage(current_url);

}