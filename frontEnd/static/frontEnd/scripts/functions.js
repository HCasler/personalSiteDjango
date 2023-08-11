// function to bring up the content when clicking a link

async function displayPageContent(subpage) {
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
}