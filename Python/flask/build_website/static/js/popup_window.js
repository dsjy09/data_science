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
 
window.addEventListener('resize', () => {
  setPopupSize();
});

function setPopupSize() {
  const popupContent = document.querySelector('.popup-content');
  const screenWidth = window.innerWidth;
  const screenHeight = window.innerHeight;
  const maxPopupWidth = screenWidth * 0.9; // 90% of screen width
  const maxPopupHeight = screenHeight * 0.9; // 90% of screen height
  popupContent.style.maxWidth = maxPopupWidth + 'px';
  popupContent.style.maxHeight = maxPopupHeight + 'px';
}

// Set initial size on page load
setPopupSize();