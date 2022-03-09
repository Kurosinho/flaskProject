
async function fetchPokemon() {
    const response = await fetch('http://localhost:5000/get_pokemon')
    const data = await response.json()

    let table = '<thead><tr><th>Name</th><th>Owner</th></tr></thead><tbody>'

    data.forEach(function(n) {
        table += '<tr><td>'+n.name+'</tr></td>'
        table += '<tr><td>'+n.owner+'</tr></td>'
    })

    table += '</tbody>'
    $('#allPokemon').empty().innerHTML()

}
