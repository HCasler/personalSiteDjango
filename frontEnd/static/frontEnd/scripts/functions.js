// function to make navbar appear and disappear

function toggleNavBar() {
    var navBar = document.getElementById("navbar")
    if (navBar.style.display !== "none") {
      navBar.style.display = "none";
    } else {
      navBar.style.display = "block";
    }
}


// function to bring up the content when clicking a link

async function displayPageContent(subpage, pageName) {
    // strip off any http or https part, then the site
    // will try to treat it as a subPage
    subpage = subpage.replace('http://', '')
    subpage = subpage.replace('https://', '')
    // retrieve the content
    const response = await fetch(subpage, {
        'headers': {
            'X-LOAD-AS-SUBPAGE':'True',
        },
    });
    const newText = await response.text();
    // stick it on the page
    var contentBase = document.getElementById("content");
    contentBase.innerHTML = newText;
    // if there's a visible menu button, hide the navbar after clicking
    var menuButton = document.getElementById("navBarCollapser");
    var menuButtonDisplay = getComputedStyle(menuButton).display;
    if (menuButtonDisplay !== "none") {
        toggleNavBar();
    }
    const loadEvent = new Event(pageName+"Load");
    contentBase.dispatchEvent(loadEvent);
}


// function to gather data on the sample video
async function getVideoInfo(evt) {
    const response = await fetch('video/topVideoInfo');
    const info = await response.json();
    console.log(info);
    var creditStr = "credit: "+info.credit+"; ";
    var titlePar = document.getElementById("demoVideoTitle");
    titlePar.innerHTML = info.title;
    var creditPar = document.getElementById("videoCredit");
    creditPar.innerHTML = creditStr;
    var origLink = document.createElement("a");
    origLink.href = info.url;
    origLink.target = "_blank";
    origLink.rel = "noopener noreferrer"
    origLink.innerHTML = "original here";
    creditPar.appendChild(origLink);


    var video = document.getElementById('videoDemoPlayer');
    video.poster  = info.thumbnail;
    if (video.canPlayType('application/vnd.apple.mpegurl')) {
        var vidSource = document.createElement("source");
        vidSource.src = info.manifest;
        video.appendChild(vidSource);
        video.src = info.manifest;
        var subTrack = document.createElement("track");
        subTrack.label = "English";
        subTrack.srclang="en";
        subTrack.src = "video/"+info.id+"/subtitles/engSubs.vtt"
        video.appendChild(subTrack);
    } 
    else if (Hls.isSupported()) {
        var hls = new Hls({
            debug: true,
        });
        hls.loadSource(info.manifest);
        hls.attachMedia(video);
    }
}


