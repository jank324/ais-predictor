var tripJSON;

$(document).ready(function() {

    mapboxgl.accessToken = "pk.eyJ1IjoidmhhbmtlIiwiYSI6ImNqaXBvb3poYzB5OXAzcG1mdnkwOGdqd2gifQ.3kstKqV75vv8miE3GsJRPQ";
    var map = new mapboxgl.Map({
        container: "map",
        style: "mapbox://styles/mapbox/streets-v9",
        center: [6.0, 53.0],
        zoom: 4.5
    })

    $("#fileUpload").submit(function() {
        var form_data = new FormData($("#fileUpload")[0]);
        $.ajax({
            type: "POST",
            url: "/trip",
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(response) {
                tripJSON = JSON.parse(response)
                showTripData(tripJSON);
            },
        });
        return false;
    })

})

function showTripData(tripJSON) {
    html = "<table>";
    for (entry in tripJSON) {
        html += "<tr><td>" + tripJSON[entry].time + "</td><td>" + tripJSON[entry].latitude + "</td><td>" + tripJSON[entry].longitude + "</td></tr>";
    }
    html += "</table>";

    $("#panel").html(html);
}