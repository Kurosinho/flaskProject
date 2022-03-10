function addPokemon(event){
    event.preventDefault();

    const data = new FormData(event.target)

    const value = Object.fromEntries(data.entries())

    let xhr = new XMLHttpRequest()
    xhr.open("POST", '/add_pokemon', true)
    xhr.setRequestHeader('Content-Type', 'application/json')
    xhr.send(data)

    return value
}

const form = document.querySelector('form')
form.addEventListener('submit', addPokemon)

