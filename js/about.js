var About = {};

About.start = function(){
	$(document).ready(function() {
		About.loadCategories();
		About.loadLocations();
		About.loadAlerts();
		About.bindForms();
	});
};

// -----------------------------------------------------------
// CATEGORIES ------------------------------------------------
// -----------------------------------------------------------

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
// -----------------------------------------------------------

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

// -----------------------------------------------------------
// ADD ALERT -------------------------------------------------
// -----------------------------------------------------------

About.bindForms = function(){

	var addAlertForm = $("form#add-product");
	addAlertForm.submit(function(e){
		e.preventDefault();
		var submittedForm = $(this);
		$.post("/alert",submittedForm.serialize(),function(result){
			if (result["STATUS"] == "ERROR"){
				alert(result["MSG"]);
			}else{
				alert("failure");
			}
		},"json");
		return false;
	});
};

About.loadAlerts = function(){
	// $("#alerts-holder").empty();
	$.get("/alerts",function(result){
		if (result["STATUS"] == "ERROR"){
			alert(result["MSG"]);
		}else{
			var alerts = result["ALERTS"];
			for (i in alerts){
				About.renderAlert(alerts[i]);
			}
		}
	},"json");
};

About.renderAlert = function(alert){
	var alertsHolder = $("#alerts-holder");
	alertTitle = $("<div />").addClass("a-title").text(alert.category);
	alertText = $("<div />").addClass("a-text").text(alert.description);
	alertLocation = $("<div />").addClass("a-loc").text(alert.location);
	alertTitle.append(alertText);
	alertTitle.append(alertLocation);
	alertsHolder.append(alertTitle);
};

About.start();
