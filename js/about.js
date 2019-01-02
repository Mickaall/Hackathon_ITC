var About = {};

About.start = function(){
	$(document).ready(function() {
		About.loadCategories();
		About.loadLocations();
	});
};

// -----------------------------------------------------------
// CATEGORIES ------------------------------------------------

About.loadCategories = function(){
	$.get("/categories",function(result){
		if (result["STATUS"] == "ERROR"){
			alert(result["MSG"]);
		}else{
			var categories = result["CATEGORIES"];
			for (i in categories){
				About.renderCategory(categories[i].name, categories[i].id);
			}
		}
	},"json");
};

About.renderCategory = function(catName, catId){
	//Update the categories dropdown in the product form
	var categorySelect = $("select#choose-cat");
	var catOp = $("<option />").attr("value",catId).text(catName);
	categorySelect.append(catOp);
};


// -----------------------------------------------------------
// LOCATIONS -------------------------------------------------

About.loadLocations = function(){
	$.get("/locations",function(result){
		if (result["STATUS"] == "ERROR"){
			alert(result["MSG"]);
		}else{
			var locations = result["LOCATIONS"];
			for (var i in locations){
				About.renderLocation(locations[i].name, locations[i].id);
			}
		}
	},"json");
};

About.renderLocation = function(locName, locId){
	//Update the locations dropdown in the product form
	var locationSelect = $("select#choose-loc");
	var locOp = $("<option />").attr("value",locId).text(locName);
	locationSelect.append(locOp);
};

About.start();


var loc =document.getElementById("container")
loc.window.location="map.html"