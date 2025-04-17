const fullSize = document.querySelectorAll(".size-full");
const image = document.querySelectorAll(".card-img-top");

function openModal(imageSrc) {
  let modal = document.getElementById("imageModal");
  let modalImage = document.getElementById("modalImage");

  modal.style.display = "flex";
  modalImage.src = imageSrc;
}

function closeModal() {
  document.getElementById("imageModal").style.display = "none";
}

function openSidebar() {
  let sidebar = document.querySelector("..sidebar");
  sidebar.style.display = "flex";
}

function closeSidebar() {
  let sidebar = document.querySelector("..sidebar");
  sidebar.style.display = "none";
}
