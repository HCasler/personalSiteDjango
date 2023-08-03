// function to bring up the content when clicking a link

async function displayPageContent(subpage) {
    // retrieve the content
    const response = await fetch(subpage);
    const newText = await response.text();
    // stick it on the page
    contentBase = document.getElementById("content");
    contentBase.innerHTML = newText;
}