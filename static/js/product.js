// Taken from boutique-ado walkthrough project
document.querySelectorAll('.btt-link').forEach(function(element) {
    element.addEventListener('click', function(e) {
        window.scrollTo(0, 0);
    });
});

document.getElementById('sort-selector').addEventListener('change', function() {
    var selector = this;
    var currentUrl = new URL(window.location);

    var selectedVal = selector.value;
    if (selectedVal !== "reset") {
        var sortDirection = selectedVal.split("_");
        var sort = sortDirection[0];
        var direction = sortDirection[1];

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl.toString());
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

        window.location.replace(currentUrl.toString());
    }
});