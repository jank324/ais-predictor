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

    if (tripFile.size > 10000000 || !tripFile.name.endsWith(".arff")) {
        $("body").html("<div class=\"failImage\"></div>");
        return;
    }

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
        html += "<td class=\"startPortCell\"> " + tripJSON[entry].start_port + " </td>";
        html += "<td class=\"endPortCell\"> " + tripJSON[entry].end_port + " </td>";
        html += "<td class=\"timeCell\"> " + milisToDateString(tripJSON[entry].time) + "  </td>";
        html += "<td class=\"latitudeCell\"> " + tripJSON[entry].latitude + " </td>"; 
        html += "<td class=\"longitudeCell\"> " + tripJSON[entry].longitude + " </td>"
        html += "</tr>";
    }
    html += "</table>";
    $(".listing").html(html);

    $("#tripTable tr").click(function() {
        $(this).addClass("selected").siblings().removeClass("selected");

        $(".info").html("<span>Waiting for prediction ...</span>");
        var originPoint = tripJSON[$(this).index()];
        placeOriginMarker(originPoint.longitude, originPoint.latitude);
        if (originPoint.route == "rot_ham") {
            map.flyTo({center: [6.254, 52.767], zoom: 6.350});
        } else if (originPoint.route == "fel_rot") {
            map.flyTo({center: [2.813, 51.961], zoom: 6.800});
        }

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

function milisToDateString(unixMilis) {
    var date = new Date(unixMilis);
    var day = date.getDate();
    var month = date.getMonth() + 1;
    var year = date.getFullYear();
    var hours = date.getHours();
    var minutes = date.getMinutes();
    
    if (day < 10) {
        day = "0" + day;
    }
    if (month < 10) {
        month = "0" + month;
    }
    if (hours < 10) {
        hours = "0" + hours;
    }
    if (minutes < 10) {
        minutes = "0" + minutes;
    }

    return day + "." + month + "." + year + "-" + hours + ":" + minutes;
}

function deltaMinutesToString(deltaMinutes) {
    var hours   = Math.floor(deltaMinutes / 60);
    var minutes = Math.floor(deltaMinutes - (hours * 60));

    if (hours < 10) {
        hours   = "0" + hours;
    }
    if (minutes < 10) {
        minutes = "0" + minutes;
    }
    
    return hours + ":" + minutes;
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
            plotTrip(response["route"]);
            displayRemainingTime(response["time"]);
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

function displayRemainingTime(time) {
    $(".info").html("<span><b>" + deltaMinutesToString(time) + "</b> hours remaining until arrival</span>");
}