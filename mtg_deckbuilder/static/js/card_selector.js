
// Find all the HTML elements which contain card names 
let cardChoiceElements = document.querySelectorAll('.card-choices')

// Make a array of all of the card names. 
let cardNames = Array.from(cardChoiceElements).map(e => e.innerHTML)

// Array of cards names the user has chosen
let chosenCardNames = [] 

// Div element that will contain the names of selected cards 
let chosenCardsList = document.querySelector('#chosen-cards')

// For each card, attach an event listener 
cardChoiceElements.forEach( el => el.addEventListener('click', function() {

    // this function is called when the element is clicked 
    // this refers to the element that is clicked
    let name = this.innerHTML   // innerHTML is the text inside an element 

    // if name is not in the list of chosenNames, 
    if (chosenCardNames.indexOf(name) == -1) {    // -1 if not found
        chosenCardNames.push(name)   // adds to the end of the array 

        let newP = document.createElement('p')   // make new Paragraph element 
        newP.innerHTML = name    // set the HTML to the name 
        chosenCardsList.appendChild(newP)   // add to the end of the elements inside the div 
    }
}))

// find the save button
let saveButton = document.querySelector('#save-button')

// event listener 
saveButton.addEventListener('click', function(){
    saveToServer()
})

// where to display messages after API call is made 
let message = document.querySelector('#message')

function saveToServer() {

    let token = Cookies.get('csrftoken')   // use Cookies library to get token

    // make request to server 
    fetch(submitCardChoiceUrl, {
        method: 'POST',    // server expects a POST request 
        body: JSON.stringify( {
            deck_id: deckId,
            cards: chosenCardNames
        } ),   //send data 
        credentials: 'same-origin',    // security 
        headers: {   //security 
            'Content-Type': 'application/json',
            'X-CSRFToken': token
        }
    })
    .then(res => res.json())   // covert bytes to JSON
    .then(data => {
        console.log('data', data)   //now you have data 
        message.innerHTML = data.message    // if works {"message": "ok!"}
        // show message in message element
    })
    .catch(err => console.log(err))   // error, shown in browser dev tools 

}