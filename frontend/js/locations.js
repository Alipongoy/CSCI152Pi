//$(document).foundation()

function initMap() {

	var map = new google.maps.Map(document.getElementById('map'), {
		zoom: 16,
		center: {lat: 36.812, lng: -119.746},
		styles: 
	[{"elementType": "geometry","stylers": [{"color": "#ebe3cd"}]},{"elementType": "labels.text.fill","stylers": [{"color": "#523735"}]},{"elementType": "labels.text.stroke","stylers": [{"color": "#f5f1e6"}]},{"featureType": "administrative","elementType": "geometry.stroke","stylers": [{"color": "#c9b2a6"}]},{"featureType": "administrative.land_parcel","elementType": "geometry.stroke","stylers": [{"color": "#dcd2be"}]},{"featureType": "administrative.land_parcel","elementType": "labels","stylers": [{"visibility": "off"}]},{"featureType": "administrative.land_parcel","elementType": "labels.text.fill","stylers": [{"color": "#ae9e90"}]},{"featureType": "landscape.natural","elementType": "geometry","stylers": [{"color": "#dfd2ae"}]},{"featureType": "poi","elementType": "geometry","stylers": [{"color": "#dfd2ae"}]},{"featureType": "poi","elementType": "labels.text","stylers": [{"visibility": "off"}]},{"featureType": "poi","elementType": "labels.text.fill","stylers": [{"color": "#93817c"}]},{"featureType": "poi.park","elementType": "geometry.fill","stylers": [{"color": "#a5b076"}]},{"featureType": "poi.park","elementType": "labels.text.fill","stylers": [{"color": "#447530"}]},{"featureType": "road","elementType": "geometry","stylers": [{"color": "#f5f1e6"}]},{"featureType": "road.arterial","elementType": "geometry","stylers": [{"color": "#fdfcf8"}]},{"featureType": "road.highway","elementType": "geometry","stylers": [{"color": "#f8c967"}]},{"featureType": "road.highway","elementType": "geometry.stroke","stylers": [{"color": "#e9bc62"}]},{"featureType": "road.highway.controlled_access","elementType": "geometry","stylers": [{"color": "#e98d58"}]},{"featureType": "road.highway.controlled_access","elementType": "geometry.stroke","stylers": [{"color": "#db8555"}]},{"featureType": "road.local","elementType": "labels","stylers": [{"visibility": "off"}]},{"featureType": "road.local","elementType": "labels.text.fill","stylers": [{"color": "#806b63"}]},{"featureType": "transit.line","elementType": "geometry","stylers": [{"color": "#dfd2ae"}]},{"featureType": "transit.line","elementType": "labels.text.fill","stylers": [{"color": "#8f7d77"}]},{"featureType": "transit.line","elementType": "labels.text.stroke","stylers": [{"color": "#ebe3cd"}]},{"featureType": "transit.station","elementType": "geometry","stylers": [{"color": "#dfd2ae"}]},{"featureType": "water","elementType": "geometry.fill","stylers": [{"color": "#b9d3c2"}]},{"featureType": "water","elementType": "labels.text.fill","stylers": [{"color": "#92998d"}]}]
	});
	// Create an array of alphabetical characters used to label the markers.
	var labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

	// Add some markers to the map.
	// Note: The code uses the JavaScript Array.prototype.map() method to
	// create an array of markers based on a given "locations" array.
	// The map() method here has nothing to do with the Google Maps API.
	var markers = points.map(function(location, i) {
		var point = points[i];
		console.log(point);
		return new google.maps.Marker({
			//map: map,
			position: new google.maps.LatLng(point.lat, point.lng),
			title: point.title,
			html: point.description
			//dist: point.dist,
			//label: labels[i % labels.length]
		});
	});

	// Add a marker clusterer to manage the markers.
	var markerCluster = new MarkerClusterer(map, markers,
		{imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});
}
var points = [{"id":"101","lat":"36.814816381088","lng":"-119.744839668273","title":"Student Parking - P 15 (Lot P)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 15 (Lot P)<\/h3><\/div>"},
	{"id":"120","lat":"36.8165771577786","lng":"-119.750343561172","title":"Student Parking - P 20 (Lot Q)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 20 (Lot Q)<\/h3><\/div>"},
	{"id":"122","lat":"36.815709658227","lng":"-119.742972850799","title":"Student Parking - P 13 (Lot T)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 13 (Lot T)<\/h3><\/div>"},
	{"id":"123","lat":"36.8161434092318","lng":"-119.738954901695","title":"Student Parking - P 11 (Lot Y)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 11 (Lot Y)<\/h3><\/div>"},
	{"id":"124","lat":"36.8162636565999","lng":"-119.743144512176","title":"Student Parking - Horse Unit","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - Horse Unit<\/h3><\/div>"},
	{"id":"125","lat":"36.8165900413612","lng":"-119.741921424865","title":"Student Parking - Beef Unit","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - Beef Unit<\/h3><\/div>"},
	{"id":"126","lat":"36.8163796092403","lng":"-119.736825227737","title":"Student Parking - P 10 (CATI)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 10 (CATI)<\/h3><\/div>"},
	{"id":"127","lat":"36.8154970763915","lng":"-119.737283885478","title":"Student Parking - P 9 (Wet Lab)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 9 (Wet Lab)<\/h3><\/div>"},
	{"id":"128","lat":"36.8137598956321","lng":"-119.741556644439","title":"Student Parking - P 6 (Lot J)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 6 (Lot J)<\/h3><\/div>"},
	{"id":"129","lat":"36.8117542510151","lng":"-119.741551280021","title":"Student Parking - P 5 (Lot A)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 5 (Lot A)<\/h3><\/div>"},
	{"id":"130","lat":"36.8098945806868","lng":"-119.740430116653","title":"Student Parking - P 3 (Lot Z)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 3 (Lot Z)<\/h3><\/div>"},
	{"id":"131","lat":"36.8097485538521","lng":"-119.741492271423","title":"Student Parking - P 2 (Lot V)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 2 (Lot V)<\/h3><\/div>"},
	{"id":"132","lat":"36.8100749663921","lng":"-119.753100872039","title":"Student Parking - P 27 (Lot G)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 27 (Lot G)<\/h3><\/div>"},
	{"id":"133","lat":"36.8102639414371","lng":"-119.749217033386","title":"Rideshare Student Parking - P 30 (Lot E)","dist":-1,"description":"<div id=\"infobubble\"><h3>Rideshare Student Parking - P 30 (Lot E)<\/h3><br \/>Rideshare Only<\/div>"},
	{"id":"134","lat":"36.8127721114883","lng":"-119.757585525512","title":"Student Parking - P 26 (Lot S)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 26 (Lot S)<\/h3><\/div>"},
	{"id":"135","lat":"36.8092718172472","lng":"-119.743600487709","title":"Student Parking - P 1 (Lot C)","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - P 1 (Lot C)<\/h3><\/div>"},
	{"id":"136","lat":"36.811140092369","lng":"-119.739807844161","title":"Student Parking - Save Mart Center","dist":-1,"description":"<div id=\"infobubble\"><h3>Student Parking - Save Mart Center<\/h3><br \/><h5>Lot 1, Lot 2 and Lot 4 Authorized Overflow Student Parking<\/h5><ul><li>Non-Event - Student Parking Permit Required<\/li><li>Evening Event - Student Parking Permit Required, Must exit lot by 3:30PM<\/li><li>Day Event - SMC Parking Permit Required, NO Student Parking<\/li><\/ul><\/div>"}]; 
//all_markers.studentparking=points; 
//points = []; 
