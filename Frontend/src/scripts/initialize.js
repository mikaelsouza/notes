$(document).ready(function () {
    $.post(
        "http://localhost:50002/initialize", {},
        function (result) {
            console.log(result)
            window.location.href = "index.html"
        }
    )
})

