var API_URL = "http://localhost:5000";
var category_mapping = [
    {
        category: "danger",
        class: "bg-danger"
    },
    {
        category: "warning",
        class: "bg-warning"
    },
    {
        category: "normal",
        class: "bg-success"
    },
];

function apiGet(endpoint, queryString){
    var url = `${API_URL}/${endpoint}`;

    if (queryString){
        url += `${url}?${queryString}`;
    }

   return $.get(url);
}

function renderMeasurementTilesInfo(key, data){
    var foundClass = category_mapping.find(x => x.category == data[key].category);
    $(`#${key}-card`).addClass(foundClass.class);
    $(`#${key}-card-body`).addClass(foundClass.class);
    $("#" + key).html(data[key].value);
}