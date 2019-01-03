var GanMeir = {};

GanMeir.start = function(){
	$(document).ready(function() {
		GanMeir.loadAlerts();
	});
};

GanMeir.loadAlerts = function(){
    // $("#alerts-holder").empty();
    console.log("load")
	$.get("/alerts-gm",function(result){
		if (result["STATUS"] == "ERROR"){
			alert(result["MSG"]);
		}else{
			var alerts = result["ALERTS"];
			for (i in alerts){
				GanMeir.renderAlert(alerts[i]);
			}
		}
	},"json");
};

GanMeir.renderAlert = function(alert){
    console.log("render")
    var alertContainer = $("#alerts-container");

    var card = $("<div />").addClass("card mb-4");
    var cardbody = $("<div />").addClass("card-body");
    var row = $("<div />").addClass("row");
    var col = $("<div />").addClass("col-lg-6");
    var cardtext = $("<div />").addClass("card-text");
    var footer = $("<div />").addClass("card-footer text-muted");

    row.append(col);
    row.append(cardtext).addClass("a-text").text(alert.description);
    cardbody.append(row);
    card.append(cardbody);
    card.append(footer).addClass("a-title").text(alert.category);
    alertContainer.append(card);
};

GanMeir.start();