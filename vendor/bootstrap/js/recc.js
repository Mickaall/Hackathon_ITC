var Recc = {};

Recc.start = function () {
    $(document).ready(function () {
        Recc.loadRecc();
    });
};

Recc.loadRecc = function () {
    $.get("/recc", function (result) {
        if (result["STATUS"] == "ERROR") {
            alert(result["MSG"]);
        } else {
            var recc = result["RECC"];
            for (i in recc) {
                Recc.renderRecc(recc[i]);
            }
        }
    }, "json");
};

Recc.renderRecc = function (recc) {
    var breedContainer = $("#breed-container");
    var parkContainer = $("#park-container");

    var breed = $("<p />").text(recc.breed);
    var park = $("<p />").text(recc.recommendation);

    breedContainer.append(breed);
    parkContainer.append(park);
};

Recc.start();