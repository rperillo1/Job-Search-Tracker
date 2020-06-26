const modal = document.getElementById("jobs-modal");
const nav = document.getElementById("nav-jobs");

nav.addEventListener("click", function () {
  modal.style.display = "block";
});
window.addEventListener("click", function (e) {
  if (e.target == modal) {
    modal.style.display = "none";
  }
});
