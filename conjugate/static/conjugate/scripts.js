document.addEventListener("DOMContentLoaded", function() {
    
    // Set onclick function of select all button
    document.querySelector('#select-all').onclick = function () {
        var check = false;

        // Grab select array and length
        selectArray = document.querySelector("#id_tenses");
        selectLength = selectArray.length;
        
        // Check if any options are already selected
        for (var i = 0; i < selectLength; i++) {
            if (selectArray[i].selected === true) {
                check = true;
            }
        }

        // If all options are already selected, unselect them all
        // Otherwise, select all options
        if (check === false) {
            for (var x = 0; x < selectLength; x++) {
                selectArray[x].selected = true;
            };
        } else {
            for (var x = 0; x < selectLength; x++) {
                selectArray[x].selected = false;
            };
        }
    }
    
});
