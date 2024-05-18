document.addEventListener('DOMContentLoaded', function() {
    let addModal = document.getElementById("addModal");
    let editModal = document.getElementById("editModal");

    let openAddModalBtn = document.getElementById("openAddModalBtn");
    let openEditModalBtn = document.getElementById("openEditModalBtn");

    let closeAddModal = document.getElementById("closeAddModal");
    let closeEditModal = document.getElementById("closeEditModal");

    if (openAddModalBtn) {
        openAddModalBtn.onclick = function() {
            console.log("Add button clicked");
            addModal.style.display = "block";
        }
    }

    if (openEditModalBtn) {
        openEditModalBtn.onclick = function() {
            console.log("Edit button clicked");
            editModal.style.display = "block";
        }
    }

    if (closeAddModal) {
        closeAddModal.onclick = function() {
            addModal.style.display = "none";
        }
    }

    if (closeEditModal) {
        closeEditModal.onclick = function() {
            editModal.style.display = "none";
        }
    }

    window.onclick = function(event) {
        if (event.target == addModal) {
            addModal.style.display = "none";
        }
        if (event.target == editModal) {
            editModal.style.display = "none";
        }
    }
});
