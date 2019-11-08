$(document).ready(function () {
    var id = window.location.search.substr(1);
    $.get(
        "http://localhost:5000/categories",
        function (data) {
            cat_div = document.getElementById('dynamic_cat')
            cat_array = data['data']
            cat_div.innerHTML += "<a href=\"newcat.html\">Nova Categoria</a>"
            cat_div.innerHTML += " - "
            for (var i = 0; i < cat_array.length; i++) {
                if (cat_array[i][0] == id) {
                    cat_div.innerHTML += "<a href=\"filtered_index.html?" + cat_array[i][0] + "\"><b>" + cat_array[i][1] + '</b>'
                } else {
                    cat_div.innerHTML += "<a href=\"filtered_index.html?" + cat_array[i][0] + "\">" + cat_array[i][1]
                }
                if (cat_array.length - 1 != i)
                    cat_div.innerHTML += ' - '
            }
        }
    );
    var url = "http://localhost:5000/notes/" + id
    $.get(
        url,
        function (data) {
            notes_div = document.getElementById('dynamic_notes')
            notes_array = data['data']
            notes_div.innerHTML += "<a href=\"newnote.html\">Nova Anotação</a>"
            for (var i = 0; i < notes_array.length; i++) {
                notes_div.innerHTML += '<br>'
                notes_div.innerHTML += "<a href=\"note.html?" + notes_array[i][0] + " \">" + notes_array[i][2] + "</a>"
            }
        }
    )
})