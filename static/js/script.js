/*jshint esversion: 6 */

function onIngredientChange() {
    "use strict";
    var search = document.getElementById("IngredientName").value;
    var ingredientList = document.getElementById("ingredient-list").children;
    for (var ingredient of ingredientList) {
        if (ingredient.innerHTML.includes(search)) {
            ingredient.classList.remove("hidden");
        }
        else {
            ingredient.classList.add("hidden");
        }
    }
    //document.getElementById("demo").innerHTML = "You selected: " + x;
}

function moveItem(itemName, unitType) {
    "use strict";
    var ingredientElement = document.createElement("TR");
    ingredientElement.classList.add("ingredientElement");

    var ingredientUsed = document.getElementById("ingredient-used");
    var childCount = ingredientUsed.childElementCount;
    document.getElementById("number-of-ingredients").value = childCount;
    var inputNameField = document.createElement("INPUT");
    var inputNumberField = document.createElement("INPUT");
    var unitTypeField = document.createElement("SPAN");

    var tableName = document.createElement("TD");
    var tableQuantity = document.createElement("TD");
    var tableUnit = document.createElement("TD");

    unitTypeField.innerHTML = unitType;

    inputNameField.setAttribute("name", childCount+"name");
    inputNameField.value = itemName;

    inputNameField.classList.add("hidden");


    inputNumberField.setAttribute("name", childCount+"number");

    inputNumberField.setAttribute("type", "number");
    inputNumberField.value = 1;
    var label = document.createElement("LABEL");

    label.setAttribute("for", childCount+"number");
    label.innerText = itemName;

    ingredientElement.appendChild(tableName);
    ingredientElement.appendChild(tableQuantity);
    ingredientElement.appendChild(tableUnit);
    tableName.appendChild(label);
    tableName.appendChild(inputNameField);
    tableQuantity.appendChild(inputNumberField);
    tableUnit.appendChild(unitTypeField);
    ingredientUsed.appendChild(ingredientElement);
}
