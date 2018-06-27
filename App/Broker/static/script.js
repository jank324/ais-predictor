var map;
var tripJSON;
var originMarker;

$(document).ready(function() {

    mapboxgl.accessToken = "pk.eyJ1IjoidmhhbmtlIiwiYSI6ImNqaXBvb3poYzB5OXAzcG1mdnkwOGdqd2gifQ.3kstKqV75vv8miE3GsJRPQ";
    map = new mapboxgl.Map({
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
    html = "<table id=\"tripTable\">";
    for (entry in tripJSON) {
        html += "<tr>";
        html += "<td class=\"startPortCell\">" + tripJSON[entry].start_port + "</td>";
        html += "<td class=\"endPortCell\">" + tripJSON[entry].end_port + "</td>";
        html += "<td class=\"timeCell\">" + tripJSON[entry].time + "</td>";
        html += "<td class=\"latitudeCell\">" + tripJSON[entry].latitude + "</td>"; 
        html += "<td class=\"longitudeCell\">" + tripJSON[entry].longitude + "</td>"
        html += "</tr>";
    }
    html += "</table>";

    $("#panel").html(html);

    $("#tripTable tr").click(function() {
        $(this).addClass("selected").siblings().removeClass("selected");

        latitude = $(this).find(".latitudeCell").html();
        longitude = $(this).find(".longitudeCell").html();
        placeOriginMarker(longitude, latitude);
    })
}

function placeOriginMarker(latitude, longitude) {
    if (originMarker != null) originMarker.remove();
    originMarker = new mapboxgl.Marker()
        .setLngLat([latitude, longitude])
        .addTo(map);
}