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

    $(".uploadButton").click(function() {
        $("#fileInput").trigger("click");
    })
    $("#fileInput").change(uploadFile);
    //$("#fileUpload").submit(uploadFile);

})

function uploadFile() {
    var tripFile = $("#fileInput")[0].files[0];

    var formData = new FormData();
    formData.append("tripfile", tripFile);

    $.ajax({
        type: "POST",
        url: "/trip",
        data: formData,
        contentType: false,
        cache: false,
        processData: false,
        success: function(response) {
            tripJSON = JSON.parse(response)
            showTripData(tripJSON);
        },
    });

    return false;
}

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
    $(".listing").html(html);

    $("#tripTable tr").click(function() {
        $(this).addClass("selected").siblings().removeClass("selected");

        var originPoint = tripJSON[$(this).index()];
        placeOriginMarker(originPoint.longitude, originPoint.latitude);
        getPrediction(originPoint);
    })

    map.addLayer({
        "id": "route",
        "type": "line",
        "source": {
            "type": "geojson",
            "data": {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "LineString",
                    "coordinates": []
                }
            }
        },
        "layout": {
            "line-join": "round",
            "line-cap": "round"
        },
        "paint": {
            "line-color": "#888",
            "line-width": 8
        }
    })
}

function placeOriginMarker(latitude, longitude) {
    if (originMarker != null) originMarker.remove();
    originMarker = new mapboxgl.Marker()
        .setLngLat([latitude, longitude])
        .addTo(map);
}

function getPrediction(originPoint) {
    $.ajax({ 
        type: "POST", 
        url: "/prediction", 
        contentType: "application/json",
        data: JSON.stringify(originPoint),
        success: function(response) {
            console.log(response);
            plotTrip(response["route"]);
        }
    }); 
}

function plotTrip(trip) {
    var tripGeoJSON = {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "LineString",
            "coordinates": []
        }
    };

    for (record in trip) {
        var routePoint = [trip[record]["longitude"], trip[record]["latitude"]];
        tripGeoJSON.geometry.coordinates.push(routePoint);
    }

    map.getSource("route").setData(tripGeoJSON);
}