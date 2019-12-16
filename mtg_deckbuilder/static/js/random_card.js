// Find the element that should have the random flavor in
let cardParagraph = document.querySelector("#random-card-flavor")

// make request to server
fetch(randomUrl)   
    .then( response => response.json() )   // decode JSON into JavaScript object
    .then (data => {
        let flavor = data.flavor;          // extract info from data object 
        cardParagraph.innerHTML = flavor   // set text of element to flavor
    })
    .catch( err => {
        console.error("Error fetching random card", err)   // errors shown in browser developer tools
    })