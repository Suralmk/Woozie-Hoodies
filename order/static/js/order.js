// Get the input field and the table
var input = document.querySelector(".order_filter");
const table = document.querySelector(".orders_table");
var rows = table.getElementsByTagName("tr");

// Add event listener for input changes
input.addEventListener("input", function() {
  var filter = input.value.toLowerCase();
    console.log(filter)
  for (var i = 1; i < rows.length; i++) {
    var row = rows[i];
    var cells = row.getElementsByTagName("td");
    var found = false; 

    for (var j = 0; j < cells.length; j++) {
      var cell = cells[j];
      if (cell) {
        var textValue = cell.textContent || cell.innerText;
        if (textValue.toLowerCase().indexOf(filter) > -1) {
          found = true;
          break; 
        }
      }
    }

    if (found) {
      row.style.display = ""; 
    } else {
      row.style.display = "none"; 
    }
  }
});


var select = document.querySelector(".order_select");
var rows = table.getElementsByTagName("tr");
select.addEventListener("change", function() {
    var filter = select.value.toLowerCase(); 
      for (var i = 1; i < rows.length; i++) {
        var row = rows[i];
        var nameCell = row.getElementsByTagName("td")[3];
        var name = nameCell.className.trim().toLowerCase(); 
        if (filter === "all" || name === filter) {
            row.style.display = ""; 
        } else {
            row.style.display = "none"; 
        }
    }
  });
