// JavaScript to toggle the information display
function toggleInformation() {
  var information = document.getElementById("information");
  if (information.style.display === "none") {
    information.style.display = "block";
  } else {
    information.style.display = "none";
  }
}

var image = document.getElementById("image");
image.addEventListener("click", toggleInformation);
