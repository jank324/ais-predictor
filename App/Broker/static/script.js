$(document).ready(function() {

    mapboxgl.accessToken = 'pk.eyJ1IjoidmhhbmtlIiwiYSI6ImNqaXBvb3poYzB5OXAzcG1mdnkwOGdqd2gifQ.3kstKqV75vv8miE3GsJRPQ';
    var map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/mapbox/streets-v9',
        center: [6.0, 53.0],
        zoom: 4.5
    })

    $("#uploadFileButton").click(function() {
        console.log("Button click called")

        var form_data = new FormData($('#uploadFile')[0]);
        $.ajax({
            type: 'POST',
            url: '/uploadtrip',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                console.log('Success!');
            },
        });
    })

})

