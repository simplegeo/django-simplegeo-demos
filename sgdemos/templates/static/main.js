
    var client = new simplegeo.PlacesClient('Vf3J6tsAMuUNWnwh6b5VWYmm5hGrfQz4');

    var map;
    var brooklyn = new google.maps.LatLng(40.704424, -73.961334);
    var MY_MAPTYPE_ID = 'hiphop';
 
    function initialize() {
        var stylez = [
            {
                featureType: "all",
                elementType: "all",
                stylers: [
                    {
                        invert_lightness: true
                    }
                ]
            },
            {
                featureType: "road",
                elementType: "labels",
                stylers: [
                    {
                        visibility: "off"
                    }
                ]
            }
        ];

    var mapOptions = {
        zoom: 14,
        center: brooklyn,
        mapTypeControlOptions: {
            mapTypeIds: [google.maps.MapTypeId.ROADMAP, MY_MAPTYPE_ID]
        },
        mapTypeId: MY_MAPTYPE_ID
    };
 
    map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);

    var styledMapOptions = {
        name: "Hip-Hop"
    };
 
    var jayzMapType = new google.maps.StyledMapType(stylez, styledMapOptions);
  
    map.mapTypes.set(MY_MAPTYPE_ID, jayzMapType);
    var markers = [];
    google.maps.event.addListener(map, 'idle', function() {
        var position = map.getCenter();
        var sg_lat = position.Ha;
        var sg_lon = position.Ia;
        var options = {"q":"pizza","num":100};
        client.search(sg_lat, sg_lon, options, function(err, data) {
            if (err) {
                console.error(err);
            } else {
                markers = [];
                var features = data['features'];
                createMarkers(features);
            }
        })
    });

    function createMarkers(features) {
        for(var j = 0; j < features.length; j++){
            var lat = features[j]['geometry']['coordinates'][1];
            var lon = features[j]['geometry']['coordinates'][0];
            var location = new google.maps.LatLng(lat,lon);
            
            var marker = new google.maps.Marker({position: location, map: map, title: "Hello World!"});

            var place_name = features[j]['properties']['name'];
            var place_address = features[j]['properties']['address'];
            var place_phone = features[j]['properties']['phone'];
            var contentString = '<h4>' + place_name + '</h4>';
            contentString += '<p>' + place_address + '</p>';
            contentString += '<p>' + place_phone + '</p>';
            
            google.maps.event.addListener(marker, 'click', (function(mark,content){ 
                return function() {
                    var infowindow = new google.maps.InfoWindow({
                        content: content
                    });
                    infowindow.open(map, mark);
                }
            })(marker, contentString));
    
            markers.push(marker);
        }
    }
}
