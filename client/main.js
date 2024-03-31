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

function GetLastMeasurement(){
   return $.get(`${API_URL}/last`);
}

function getCssClassByCategory(category){
    var foundClass = category_mapping.find(x => x.category == category);
    return foundClass.class;
}

function renderMeasurementTilesInfo(key, data){
    var cssClass = getCssClassByCategory(data[key].category);
    $(`#${key}-card`).addClass(cssClass);
    $(`#${key}-card-body`).addClass(cssClass);
    $("#" + key).html(data[key].value);
}