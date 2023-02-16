// Profile pic modal
var deleteProfilePicModal = document.getElementById("delete-pic-modal");
var deleteProfilePicBtn = document.querySelectorAll(".delete-pic-btn");
var confirmDeletePicBtn = document.getElementById("confirm-pic-delete");
var deleteProfilePicForm = document.getElementById("delete-pic-form");
var closePicModalSpan = document.getElementById("close-pic-modal-span");


// Delete Profile Picture Modal
deleteProfilePicBtn.forEach(function (deleteProfilePicBtn){
    deleteProfilePicBtn.addEventListener("click",function(event) {
        event.preventDefault();
        deleteProfilePicModal.style.display ="block";
        deleteProfilePicModal.modal();
    });
});

confirmDeletePicBtn.onclick = function () {
        deleteProfilePicForm.submit();
    }
//  Close the modal is user clicks x
closePicModalSpan.onclick = function() {
    deleteProfilePicModal.style.display = "none";
}
// Close the modal if user clicks outside of modal area
window.onclick = function(event) {
    if (event.target == deleteProfilePicModal) {
    deleteProfilePicModal.style.display = "none";
    }
}