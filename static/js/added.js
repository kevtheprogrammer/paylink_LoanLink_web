//Client details page images 
function expandImage(imageUrl) {
    document.getElementById('full-screen-image').style.display = 'block';
    document.getElementById('full-screen-image').getElementsByTagName('img')[0].src = imageUrl;
}

function closeFullScreenImage() {
    document.getElementById('full-screen-image').style.display = 'none';
}

$('.message a').click(function(){
    $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
 });


 //Tab Navigation JavaScript 
 document.addEventListener('DOMContentLoaded', function() {
    const tabs = document.querySelectorAll('.tab');
    const tabContents = document.querySelectorAll('.tab-content');

    tabs.forEach(tab => {
        tab.addEventListener('click', function(event) {
            event.preventDefault();

            // Remove active classes
            tabs.forEach(t => t.classList.remove('active', 'border-green-500', 'text-green-600'));
            tabContents.forEach(content => content.classList.add('hidden'));

              // Add active classes
            tab.classList.add('active', 'border-green-500', 'text-green-600');
            document.querySelector(tab.getAttribute('href')).classList.remove('hidden');
        });
    });
});


//Sorting Loan Drop Down Active, Pending and Closed
function toggleDropdown() {
    var dropdown = document.getElementById('dropdown-menu');
    var isExpanded = dropdown.classList.contains('hidden');
    dropdown.classList.toggle('hidden', !isExpanded);
  }

  // Close the dropdown if clicked outside
  window.addEventListener('click', function(event) {
    var dropdown = document.getElementById('dropdown-menu');
    var button = document.querySelector('button[onclick="toggleDropdown()"]');
    if (!button.contains(event.target) && !dropdown.contains(event.target)) {
      dropdown.classList.add('hidden');
    }
  });


//Profile Drop Down Toggle
  function toggleUserMenu() {
    var menu = document.getElementById('user-menu');
    menu.classList.toggle('hidden');
  }

  // Close the dropdown if clicked outside
  window.addEventListener('click', function(event) {
    var menu = document.getElementById('user-menu');
    var button = document.getElementById('user-menu-button');
    if (!button.contains(event.target) && !menu.contains(event.target)) {
      menu.classList.add('hidden');
    }
  });