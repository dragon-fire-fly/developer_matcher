var deleteProfileModal = document.getElementById("delete-profile-modal");
var deleteProfileBtn = document.getElementById("delete-profile-btn");
var confirmDeleteBtn = document.getElementById("confirm-delete")
var deleteProfileForm = document.getElementById("delete-form");
var closeModalSpan = document.getElementById("close-modal-span");

deleteProfileBtn.onclick = function(event) {
    event.preventDefault();
    deleteProfileModal.style.display ="block";
    ('#delete-account-modal').modal();
}

confirmDeleteBtn.onclick = function () {
        deleteProfileForm.submit();
    }

//  Close the modal is user clicks x
closeModalSpan.onclick = function() {
    deleteProfileModal.style.display = "none";
}

// Close the modal if user clicks outside of modal area
window.onclick = function(event) {
    if (event.target == modal) {
    deleteProfileModal.style.display = "none";
    }
}
