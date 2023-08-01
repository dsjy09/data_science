/*add filter buttons on top of page*/

document.addEventListener('DOMContentLoaded', function() {
    const filterButtons = document.querySelectorAll('.filter-button');
    const gridItems = document.querySelectorAll('.grid-item');

    filterButtons.forEach(function(button) {
      button.addEventListener('click', function() {
        const filter = button.getAttribute('data-filter');
        filterItems(filter);
        setActiveButton(button);
      });
    });

    function filterItems(filter) {
      gridItems.forEach(function(item) {
        if (filter === 'all' || item.classList.contains(filter)) {
          item.classList.remove('hidden');
        } else {
          item.classList.add('hidden');
        }
      });
    }

    function setActiveButton(button) {
      filterButtons.forEach(function(btn) {
        btn.classList.remove('active');
      });
      button.classList.add('active');
    }

    // Activate the "All" button by default
    setActiveButton(filterButtons[0]);
  });