document.addEventListener('DOMContentLoaded', function() {
    let addModal = document.getElementById("addModal");
    let editModal = document.getElementById("editModal");
    let editItemModal = document.getElementById("editItemModal");

    let openAddModalBtn = document.getElementById("openAddModalBtn");
    let openEditModalBtn = document.getElementById("openEditModalBtn");
    let openEditItemModalBtns = document.querySelectorAll(".openEditItemModalBtn");

    let closeAddModal = document.getElementById("closeAddModal");
    let closeEditModal = document.getElementById("closeEditModal");
    let closeEditItemModal = document.getElementById("closeEditItemModal");

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

    openEditItemModalBtns.forEach(function(btn) {
        btn.onclick = function() {
            console.log("Edit item button clicked");
            const itemId = btn.getAttribute('data-id');
            const form = document.getElementById('editBudgetItemForm');
            form.setAttribute('action', `/update-item/${itemId}`);
            editItemModal.style.display = "block";
        }
    });

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

    if (closeEditItemModal) {
        closeEditItemModal.onclick = function() {
            editItemModal.style.display = "none";
        }
    }

    window.onclick = function(event) {
        if (event.target == addModal) {
            addModal.style.display = "none";
        }
        if (event.target == editModal) {
            editModal.style.display = "none";
        }
        if (event.target == editItemModal) {
            editItemModal.style.display = "none";
        }
    }
});
