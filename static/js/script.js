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
    var ingredientElement = document.createElement("DIV");
    ingredientElement.classList.add("ingredient-element");

    var ingredientUsed = document.getElementById("ingredient-used");
    var childCount = ingredientUsed.childElementCount;
    document.getElementById("number-of-ingredients").value = childCount;
    var inputNameField = document.createElement("INPUT");
    var inputNumberField = document.createElement("INPUT");
    var unitTypeField = document.createElement("SPAN");

    var tableName = document.createElement("DIV");
    tableName.classList.add("item-1");
    var tableQuantity = document.createElement("DIV");
    tableQuantity.classList.add("item-2");
    var tableUnit = document.createElement("DIV");
    tableUnit.classList.add("item-3");

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
