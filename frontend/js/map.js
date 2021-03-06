var map;
function initMap() {

    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 15.5,
        center: {lat: 36.814, lng: -119.746},
        styles: 
        [{"elementType": "geometry","stylers": [{"color": "#ebe3cd"}]},{"elementType": "labels.text.fill","stylers": [{"color": "#523735"}]},{"elementType": "labels.text.stroke","stylers": [{"color": "#f5f1e6"}]},{"featureType": "administrative","elementType": "geometry.stroke","stylers": [{"color": "#c9b2a6"}]},{"featureType": "administrative.land_parcel","elementType": "geometry.stroke","stylers": [{"color": "#dcd2be"}]},{"featureType": "administrative.land_parcel","elementType": "labels","stylers": [{"visibility": "off"}]},{"featureType": "administrative.land_parcel","elementType": "labels.text.fill","stylers": [{"color": "#ae9e90"}]},{"featureType": "landscape.natural","elementType": "geometry","stylers": [{"color": "#dfd2ae"}]},{"featureType": "poi","elementType": "geometry","stylers": [{"color": "#dfd2ae"}]},{"featureType": "poi","elementType": "labels.text","stylers": [{"visibility": "off"}]},{"featureType": "poi","elementType": "labels.text.fill","stylers": [{"color": "#93817c"}]},{"featureType": "poi.park","elementType": "geometry.fill","stylers": [{"color": "#a5b076"}]},{"featureType": "poi.park","elementType": "labels.text.fill","stylers": [{"color": "#447530"}]},{"featureType": "road","elementType": "geometry","stylers": [{"color": "#f5f1e6"}]},{"featureType": "road.arterial","elementType": "geometry","stylers": [{"color": "#fdfcf8"}]},{"featureType": "road.highway","elementType": "geometry","stylers": [{"color": "#f8c967"}]},{"featureType": "road.highway","elementType": "geometry.stroke","stylers": [{"color": "#e9bc62"}]},{"featureType": "road.highway.controlled_access","elementType": "geometry","stylers": [{"color": "#e98d58"}]},{"featureType": "road.highway.controlled_access","elementType": "geometry.stroke","stylers": [{"color": "#db8555"}]},{"featureType": "road.local","elementType": "labels","stylers": [{"visibility": "off"}]},{"featureType": "road.local","elementType": "labels.text.fill","stylers": [{"color": "#806b63"}]},{"featureType": "transit.line","elementType": "geometry","stylers": [{"color": "#dfd2ae"}]},{"featureType": "transit.line","elementType": "labels.text.fill","stylers": [{"color": "#8f7d77"}]},{"featureType": "transit.line","elementType": "labels.text.stroke","stylers": [{"color": "#ebe3cd"}]},{"featureType": "transit.station","elementType": "geometry","stylers": [{"color": "#dfd2ae"}]},{"featureType": "water","elementType": "geometry.fill","stylers": [{"color": "#b9d3c2"}]},{"featureType": "water","elementType": "labels.text.fill","stylers": [{"color": "#92998d"}]}]
    });
	
	
	// Create the search box and link it to the UI element.
        var input = document.getElementById('inputs');
        var searchBox = new google.maps.places.SearchBox(input);
        map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

        // Bias the SearchBox results towards current map's viewport.
        map.addListener('bounds_changed', function() {
          searchBox.setBounds(map.getBounds());
        });
		
		var markers = [];
        // Listen for the event fired when the user selects a prediction and retrieve
        // more details for that place.
        searchBox.addListener('places_changed', function() {
          var places = searchBox.getPlaces();
          if (places.length == 0) {
            return;
          }
          // Clear out the old markers.
          markers.forEach(function(marker) {
            marker.setMap(null);
          });
          markers = [];
          // For each place, get the icon, name and location.
          var bounds = new google.maps.LatLngBounds();
          places.forEach(function(place) {
            if (!place.geometry) {
              console.log("Returned place contains no geometry");
              return;
            }
            var icon = {
              url: place.icon,
              size: new google.maps.Size(71, 71),
              origin: new google.maps.Point(0, 0),
              anchor: new google.maps.Point(17, 34),
              scaledSize: new google.maps.Size(25, 25)
            };
            // Create a marker for each place.
            markers.push(new google.maps.Marker({
              map: map,
              icon: icon,
              title: place.name,
              position: place.geometry.location
            }));
            if (place.geometry.viewport) {
              // Only geocodes have viewport.
              bounds.union(place.geometry.viewport);
            } else {
              bounds.extend(place.geometry.location);
            }
          });
          map.fitBounds(bounds);
        }); 
	
    // Add some markers to the map.
    // Note: The code uses the JavaScript Array.prototype.map() method to
    // create an array of markers based on a given "locations" array.
    // The map() method here has nothing to do with the Google Maps API.
	
	
	
    // Add some markers to the map.
    // Note: The code uses the JavaScript Array.prototype.map() method to
    // create an array of markers based on a given "locations" array.
    // The map() method here has nothing to do with the Google Maps API.
    var image = {
        url: 'img/blue-maker.png',
        //size: new google.maps.Size(20, 32),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(0, 32)
    }

    var markers = points.map(function(location, i) {
        var point = points[i];
        var marker =  new google.maps.Marker({
            position: new google.maps.LatLng(point.lat, point.lng),
            title: point.name,
            html: point.description,
            //animation: google.maps.Animation.DROP,
            icon: image,
            label: {text:point.name, color: "white"}, //change to number of availible parking spots
            clickable: true
        });
        google.maps.event.addListener(marker, 'click', function(){
            //add changing the zoom into the spaces
            this.setVisible(!viewLot(this.title));
        });
        return marker;
    });
    var imageBounds = {
        north: 36.817988, 
        south: 36.816782, 
        east: -119.749730,
        west: -119.751517
    };
    var lotQOverlay = new google.maps.GroundOverlay('img/lotQ.png',imageBounds);
    lotQOverlay.setMap(map);

    // Add a marker clusterer to manage the markers.
    var markerCluster = new MarkerClusterer(map, markers,
        {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});
}

//array that holds all of the locations and names for the different lots
var points = [{"name":"LotP","id":"101","lat":"36.814816381088","lng":"-119.744839668273","title":"Student Parking - P 15 (Lot P)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 15 (Lot P)<\/h3><\/div>"},
    {"name":"LotQ","id":"120","lat":"36.8165771577786","lng":"-119.750343561172","title":"Student Parking - P 20 (Lot Q)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 20 (Lot Q)<\/h3><\/div>"},
    {"name":"LotT","id":"122","lat":"36.815709658227","lng":"-119.742972850799","title":"Student Parking - P 13 (Lot T)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 13 (Lot T)<\/h3><\/div>"},
    {"name":"LotY","id":"123","lat":"36.8161434092318","lng":"-119.738954901695","title":"Student Parking - P 11 (Lot Y)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 11 (Lot Y)<\/h3><\/div>"},
    {"name":"Horse","id":"124","lat":"36.8162636565999","lng":"-119.743144512176","title":"Student Parking - Horse Unit","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - Horse Unit<\/h3><\/div>"},
    {"name":"Beef","id":"125","lat":"36.8165900413612","lng":"-119.741921424865","title":"Student Parking - Beef Unit","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - Beef Unit<\/h3><\/div>"},
    {"name":"CATI","id":"126","lat":"36.8163796092403","lng":"-119.736825227737","title":"Student Parking - P 10 (CATI)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 10 (CATI)<\/h3><\/div>"},
    {"name":"WetLab","id":"127","lat":"36.8154970763915","lng":"-119.737283885478","title":"Student Parking - P 9 (Wet Lab)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 9 (Wet Lab)<\/h3><\/div>"},
    {"name":"LotJ","id":"128","lat":"36.8137598956321","lng":"-119.741556644439","title":"Student Parking - P 6 (Lot J)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 6 (Lot J)<\/h3><\/div>"},
    {"name":"LotA","id":"129","lat":"36.8117542510151","lng":"-119.741551280021","title":"Student Parking - P 5 (Lot A)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 5 (Lot A)<\/h3><\/div>"},
    {"name":"LotZ","id":"130","lat":"36.8098945806868","lng":"-119.740430116653","title":"Student Parking - P 3 (Lot Z)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 3 (Lot Z)<\/h3><\/div>"},
    {"name":"LotV","id":"131","lat":"36.8097485538521","lng":"-119.741492271423","title":"Student Parking - P 2 (Lot V)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 2 (Lot V)<\/h3><\/div>"},
    {"name":"LotG","id":"132","lat":"36.8100749663921","lng":"-119.753100872039","title":"Student Parking - P 27 (Lot G)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 27 (Lot G)<\/h3><\/div>"},
    {"name":"LotE","id":"133","lat":"36.8102639414371","lng":"-119.749217033386","title":"Rideshare Student Parking - P 30 (Lot E)","dist":-1,"description":"<div id=\"infobubble\"><h3>Rideshare Student Parking - P 30 (Lot E)<\/h3><br \/>Rideshare Only<\/div>"},
    {"name":"LotS","id":"134","lat":"36.8127721114883","lng":"-119.757585525512","title":"Student Parking - P 26 (Lot S)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 26 (Lot S)<\/h3><\/div>"},
    {"name":"LotC","id":"135","lat":"36.8092718172472","lng":"-119.743600487709","title":"Student Parking - P 1 (Lot C)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 1 (Lot C)<\/h3><\/div>"},
    {"name":"Overflow","id":"136","lat":"36.811140092369","lng":"-119.739807844161","title":"Student Parking - Save Mart Center","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - Save Mart Center<\/h3><br \/><h5>Lot 1, Lot 2 and Lot 4 Authorized Overflow Student Parking<\/h5><ul><li>Non-Event - Student Parking Permit Required<\/li><li>Evening Event - Student Parking Permit Required, Must exit lot by 3:30PM<\/li><li>Day Event - SMC Parking Permit Required, NO Student Parking<\/li><\/ul><\/div>"}]; 

