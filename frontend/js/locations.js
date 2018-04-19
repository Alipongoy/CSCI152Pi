//difference between lattitudes of spaces
var lngDiff = 0.00003;
var latDiff = 0.000056;
//id:for readability, lat and lng for lat and long, 
//spaces is the number of spaces in the row
var lotQ = {"1-1":{"lat":"36.817893","lng":"-119.751360","spaces":14}};
lotQ["1-2"] = {"lat":"36.817889","lng":"-119.750819","spaces":33};
lotQ["2-1"] = {"lat":"36.817721","lng":"-119.751361","spaces":14};
lotQ["2-2"] = {"lat":"36.817719","lng":"-119.750818","spaces":33};
lotQ["3-1"] = {"lat":"36.817719","lng":"-119.750818","spaces":33};
lotQ["3-2"] = {"lat":"36.817719","lng":"-119.750818","spaces":33};
lotQ["4-1"] = {"lat":"36.817719","lng":"-119.750818","spaces":33};
lotQ["4-2"] = {"lat":"36.817719","lng":"-119.750818","spaces":33};
lotQ["5-1"] = {"lat":"36.817719","lng":"-119.750818","spaces":33};
lotQ["5-2"] = {"lat":"36.817719","lng":"-119.750818","spaces":33};
    //fill to 5-2 for testing 
;
var lotTemplates = {"lotQ":lotQ}; 


//-----not in use anymore-----//
var exampleData = {"lot":"lotQ","genID":"1-1","space":2,"isOpen":true,"timeStamp":"somedate"}
function loadLots () {
	var tempLot = []; 
	var id = 0; //replace id with something connected to the database
	var isOpen = true;
	//create a horizontal parking lot using above array
	for (var i in lotQ) {
		row = lotQ[i];
		var lng = parseFloat(row.lng);
		var lat = parseFloat(row.lat);
		//pushes each space by adding the difference to the lattitude
		for (var i = 0; i < row.spaces; i++) {
			lng += lngDiff;
			tempLot.push({"id":id,"lat":lat,"lng":lng,"isOpen":isOpen});	
			lat += latDiff;
			tempLot.push({"id":id,"lat":lat,"lng":lng,"isOpen":isOpen});
			lat -= latDiff;
		}
	}
	//overwrite the framework lot with the full lot
	lotQ = tempLot;
}
//loadLots();


//add all of the lots to this
var lots = {};
//get data from the midleware server
var sqlData;
//parse all of the data from the server
$.getJSON("http://ab-kc.tk/parking/view.php",function(result) {
    sqlData = result;
    for(var it in sqlData) {
        //set up variables
        var spot = sqlData[it];
        var lat, lng;
        if(spot.space == 1) { //reset the lat and long to default
            lat = parseFloat(lotTemplates[spot.lot][spot.genID].lat);
            lng = parseFloat(lotTemplates[spot.lot][spot.genID].lng);
        } else { //adjust lat or long
            if (spot.space % 2 == 0) {
                lat+= latDiff;
            } else {
                lng+= lngDiff;
                lat-= latDiff;
            }
        }
        //sets the key pair
        var space = {"lat":lat,"lng":lng,"isOpen":spot.isOpen};
        var spaceName = spot.genID+"-"+spot.space;
        //checks if the lot exists already
        if(!lots[spot.lot]) {
            //adds the lot if it doesn't
            lots[spot.lot] = {[spaceName]:space};
        } else {
            //pushes the space into the lot if it does
            lots[spot.lot][spaceName] = space;
        }
    }
});

function viewLot(lot) {
	var isLot = false;
	var parkicon = {
		url: 'img/blue-maker.png',
	}
    var markers = new Array();//make marker array
    lot = lot.charAt(0).toLowerCase() + lot.slice(1)
	//probably make less dependant later
	if(lots[lot]) {
        //needs to be an array, or just feed individually?
        for (var spot in lots[lot]) {
            var space = lots[lot][spot];
            console.log(space.isOpen);
            var marker = new google.maps.Marker({
				position: new google.maps.LatLng(space.lat, space.lng),
				icon: parkicon,
                visible: !!+space.isOpen, // "!!+" converts string to bool 
				label: spot,
            });
            markers.push(marker);
        }
		isLot = true;
	}
	var markerCluster = new MarkerClusterer(map, markers,
		{imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});

	return isLot;
}


var test;
