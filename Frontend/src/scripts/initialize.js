$(document).ready(function () {
    $.post(
        "http://localhost:5000/initialize", {},
        function (result) {
            console.log(result)
            window.location.href = "index.html"
        }
    )
})

