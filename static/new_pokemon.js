function addPokemon(event){
    event.preventDefault();

    const data = new FormData(document.querySelector('form'))

    const value = Object.fromEntries(data.entries())
    console.log(data)

    let xhr = new XMLHttpRequest()
    xhr.open("POST", '/add_pokemon', true)
    xhr.setRequestHeader('Content-Type', 'application/json')
    console.log(value)
    console.log(xhr)
    xhr.send(JSON.stringify(value))

    return value
}

const form = document.querySelector('form')
form.addEventListener('submit', addPokemon)

