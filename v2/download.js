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

// chrome.runtime.sendNativeMessage('com.ytdlite.nativeapp', { message: 'Hello from extension!' }, function(response) {
//   if (chrome.runtime.lastError) {
//     console.error('Error:', chrome.runtime.lastError);
//   } else {
//     document.getElementById("p1").innerHTML = response;
//     console.log('Received response: ' + response);
//   }
// });

chrome.runtime.sendNativeMessage(
  'com.ytdlite.nativeapp',
  {text: 'Hello from extension!'},
  function (response) {
    document.getElementById("p1").innerHTML = response;
    console.log('Received ' + response);
  }
);

document.getElementById("btn_download_mp4_FHD").addEventListener(
    "click",
    function () { start_download('mp4') },
    false
);

document.getElementById("btn_download_audio").addEventListener(
    "click",
    function () { start_download('bestaudio') },
    false
);

async function start_download(format) {
}

