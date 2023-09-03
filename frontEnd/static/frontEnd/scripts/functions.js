// function to make navbar appear and disappear

function toggleNavBar() {
    navBar = document.getElementById("navbar")
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
    contentBase = document.getElementById("content");
    contentBase.innerHTML = newText;
    // if there's a visible menu button, hide the navbar after clicking
    menuButton = document.getElementById("navBarCollapser");
    menuButtonDisplay = getComputedStyle(menuButton).display;
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
    console.log(info)
    titlePar = document.getElementById("demoVideoTitle");
    titlePar.innerHTML = info.title;
    vidElem = document.getElementById("videoDemoPlayer");
    vidElem.poster = info.thumbnail;
    vidSource = document.createElement("source");
    vidSource.src = info.manifest
    vidElem.appendChild(vidSource);
}


