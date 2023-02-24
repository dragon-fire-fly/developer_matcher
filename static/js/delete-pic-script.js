// Profile pic modal
var deleteProfilePicModal = document.getElementById("deletePicModal");
var closePicModalSpan = document.getElementById("close-pic-modal-span");

var deleteProfilePicBtn = document.querySelectorAll(".delete-pic-btn");
var confirmDeletePicBtn; // define the variable outside the event listener

// Delete Profile Picture Modal
deleteProfilePicBtn.forEach(function (deleteProfilePicBtn){
    deleteProfilePicBtn.addEventListener("click",function(event) {
        event.preventDefault();
        var deleteProfilePicForm = this.closest(".delete-pic-form");
        confirmDeletePicBtn = document.getElementById("confirm-pic-delete"); // update the variable inside the event listener
        $('#deletePicModal').modal();
        confirmDeletePicBtn.onclick = function () {
            deleteProfilePicForm.submit();
        }
    });
});

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