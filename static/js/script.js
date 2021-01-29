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

function moveItem(itemName) {
    "use strict";
    var ingredientElement = document.createElement("DIV");
    ingredientElement.classList.add("ingredientElement");

    var ingredientUsed = document.getElementById("ingredient-used");
    var childCount = ingredientUsed.childElementCount + 1;
    document.getElementById("number-of-ingredients").value = childCount;
    var inputNameField = document.createElement("INPUT");
    var inputNumberField = document.createElement("INPUT");


    inputNameField.setAttribute("name", childCount+"name");
    inputNameField.value = itemName

    inputNameField.classList.add("hidden");


    inputNumberField.setAttribute("name", childCount+"number");

    inputNumberField.setAttribute("type", "number");
    inputNumberField.value = 1;
    var label = document.createElement("LABEL");

    label.setAttribute("for", childCount+"number");
    label.innerText = itemName;

    ingredientElement.appendChild(label);
    ingredientElement.appendChild(inputNameField);
    ingredientElement.appendChild(inputNumberField);
    ingredientUsed.appendChild(ingredientElement);
}
