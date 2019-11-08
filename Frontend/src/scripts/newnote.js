$(document).ready(function () {
    $.get(
        "http://localhost:50002/categories",
        function (data) {
            cat_array = data['data']

            select = document.getElementById('category')


            for (var i = 0; i < cat_array.length; i++) {
                var el = document.createElement("option");
                var opt = cat_array[i][0];
                var text = cat_array[i][1];
                el.value = opt;
                el.textContent = text;
                select.appendChild(el);
            }
        }
    );
})

function submitNoteData() {
    var title = document.getElementById('title').value
    var cat = document.getElementById('category').value
    var notes = document.getElementById('data').value

    data = { 'title': title, 'data': notes, 'cat_id': cat }

    $.post(
        "http://localhost:50002/insert/note", data,
        function (result) {
            console.log(result)
            window.location.href = "index.html"
        }
    )
}