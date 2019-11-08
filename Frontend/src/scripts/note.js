$(document).ready(function () {
    var id = window.location.search.substr(1);
    var url = "http://localhost:5000/note/" + id
    $.get(
        url,
        function (data) {
            data = data['data']
            title_div = document.getElementById('title')
            title_div.innerHTML = data[0][2]
            text_div = document.getElementById('text')
            text_div.innerHTML = data[0][3]
        })
})