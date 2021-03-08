function openForm(num) {
    if (num) {
        document.getElementById("Table").style.display = "none";
        document.getElementById("Work_list").style.display = "block";
    }
    else {
        document.getElementById("Progress").style.display = "block";
    }
}

function closeForm(num) {
    if (num) {
        document.getElementById("Work_list").style.display = "none";
        document.getElementById("Progress").style.display = "none";
        document.getElementById("Table").style.display = "block";
    }
    else {
        document.getElementById("Progress").style.display = "none";
    }
}


function clickRadio(el) {
    var siblings = document.querySelectorAll("input[type='radio'][name='" + el.name + "']");
    for (var i = 0; i < siblings.length; i++) {
      if (siblings[i] != el)
        siblings[i].oldChecked = false;
    }
    if (el.oldChecked)
      el.checked = false;
    el.oldChecked = el.checked;
}