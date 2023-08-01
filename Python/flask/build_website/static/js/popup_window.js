// Get the pop-up window element
// const popup = document.getElementById('popup');

// // Function to open the pop-up window
// function openPopup() {
// popup.style.display = 'block';
// }

// // Function to close the pop-up window
// function closePopup() {
// popup.style.display = 'none';
// }

function openPopup(jobid) {
    const popup = document.getElementById(jobid);
    popup.style.display = 'block';
  }
  
function closePopup(jobid) {
    const popup = document.getElementById(jobid);
    popup.style.display = 'none';
}
  