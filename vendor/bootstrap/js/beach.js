var GanMeir = {};

GanMeir.start = function () {
    $(document).ready(function () {
        GanMeir.loadAlerts();
    });
};

GanMeir.loadAlerts = function () {
    // $("#alerts-holder").empty();
    $.get("/alerts-b", function (result) {
        if (result["STATUS"] == "ERROR") {
            alert(result["MSG"]);
        } else {
            var alerts = result["ALERTS"];
            for (i in alerts) {
                GanMeir.renderAlert(alerts[i]);
                console.log(alerts[i]);
            }
        }
    }, "json");
};

GanMeir.renderAlert = function (alert) {
    var alertContainer = $("#alert-container");

    var card = $("<div />").addClass("card mb-4");
    var cardbody = $("<div />").addClass("card-body");
    var row = $("<div />").addClass("row");
    var col = $("<div />").addClass("col-lg-6");
    var cardtext = $("<p />").addClass("card-text a-text").text(alert.description);
    var footer = $("<div />").addClass("card-footer text-muted a-title").text(alert.category);

    row.append(col);
    row.append(cardtext);
    cardbody.append(row);
    card.append(cardbody);
    card.append(footer);
    alertContainer.append(card);
};

GanMeir.start();