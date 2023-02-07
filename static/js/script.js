//  Profile delete modal
var deleteProfileModal = document.getElementById("delete-profile-modal");
var deleteProfileBtn = document.getElementById("delete-profile-btn");
var confirmDeleteBtn = document.getElementById("confirm-delete")
var deleteProfileForm = document.getElementById("delete-form");
var closeModalSpan = document.getElementById("close-modal-span");
// Profile pic modal
var deleteProfilePicModal = document.getElementById("delete-pic-modal");
var deleteProfilePicBtn = document.getElementById("delete-pic-btn");
var confirmDeletePicBtn = document.getElementById("confirm-pic-delete");
var deleteProfilePicForm = document.getElementById("delete-pic-form");
var closePicModalSpan = document.getElementById("close-pic-modal-span");


// Delete Profile Modal
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


// Delete Profile Picture Modal
deleteProfilePicBtn.addEventListener("click",function(event) {
    event.preventDefault();
    deleteProfilePicModal.style.display ="block";
    deleteProfilePicModal.modal();
})

confirmDeletePicBtn.onclick = function () {
        deleteProfilePicForm.submit();
    }
//  Close the modal is user clicks x
closePicModalSpan.onclick = function() {
    deleteProfilePicModal.style.display = "none";
}
// Close the modal if user clicks outside of modal area
window.onclick = function(event) {
    if (event.target == modal) {
    deleteProfilePicModal.style.display = "none";
    }
}