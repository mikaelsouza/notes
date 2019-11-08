function submitCatData() {
    var cat_name = document.getElementById('title').value
    console.log(cat_name)
    data = { 'cat_name': cat_name }

    $.post(
        "http://localhost:50002/insert/category", data,
        function (result) {
            console.log(result)
            window.location.href = "index.html"
        }
    )
}