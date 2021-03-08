function openForm(num) {
    if (num == 1)
    {
         document.getElementById("Add_work").style.display = "block";
         document.getElementById("Add_student").style.display = "none";
         document.getElementById("Add_director").style.display = "none";
    }
    else if (num ==2)
    {
         document.getElementById("Add_work").style.display = "none";
         document.getElementById("Add_student").style.display = "block";
         document.getElementById("Add_director").style.display = "none";
    }
    else if (num ==3)
    {
         document.getElementById("Add_work").style.display = "none";
         document.getElementById("Add_student").style.display = "none";
         document.getElementById("Add_director").style.display = "block";
    }
}

/*function closeForm(num) {

    if (num == 1)
    {
         document.getElementById("Add_work").style.display = "block";
         document.getElementById("Add_student").style.display = "block";
         document.getElementById("Add_director").style.display = "block";
    }
    elif (num ==2)
    {
         document.getElementById("Add_work").style.display = "block";
         document.getElementById("Add_student").style.display = "block";
         document.getElementById("Add_director").style.display = "block";
    }
    elif (num ==3)
    {
         document.getElementById("Add_work").style.display = "block";
         document.getElementById("Add_student").style.display = "block";
         document.getElementById("Add_director").style.display = "block";
    }

}*/


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