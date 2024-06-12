// function openModalAfterDelay() {
//     setTimeout(function() {
//         var modal = document.getElementById("popup-form");
//         modal.style.display = "block";
//     }, 5000); // 5000 milliseconds = 5 seconds
// }

// // Function to close the modal
// function closeModal() {
//     var modal = document.getElementById("popup-form");
//     modal.style.display = "none";
// }

// // Call the function to open the modal after 5 seconds
// openModalAfterDelay();


//   window.onload = function() {
//     setTimeout(function() {
//       if (!localStorage.getItem('popupShown')) {
//         document.getElementById('popup-form').style.display = 'block';
//       }
//     }, 5000); // Show popup after 5 seconds

//     document.getElementById('closeButton').onclick = function() {
//       document.getElementById('popup-form').style.display = 'none';
//       localStorage.setItem('popupShown', true);
//     };
//   };

window.onload = function() {
 
    var popupShown = localStorage.getItem('popupShown');
    
    console.log(popupShown)

    if (!popupShown) {
        
        setTimeout(function() {
            document.getElementById('popup-form').style.display = 'block';
        }, 2000); // Show popup after 5 seconds
    }

    document.getElementById('closeButton').onclick = function() {
        document.getElementById('popup-form').style.display = 'none';
        localStorage.setItem('popupShown', true);
    };

    // Check if the form has been submitted
    var formSubmitted = localStorage.getItem('formSubmitted');
    if (formSubmitted) {
        // Clear the flag to prevent the form from appearing again
        localStorage.removeItem('popupShown');
    }
};
