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
 window.toggleTab = function (evt, tab) {
  var i, tabs, tabContent;

  // Hide all tab content
  tabContent = document.getElementsByClassName("tab-content");
  for (i = 0; i < tabContent.length; i++) {
    tabContent[i].style.display = "none";
  }

  // Remove the "active" class from all tabs
  tabs = document.getElementsByClassName("tab");
  for (i = 0; i < tabs.length; i++) {
    tabs[i].className = tabs[i].className.replace(" active", "").replace("active", "");
  }

  // Show the current tab's content and add "active" class to the clicked tab
  document.getElementById(tab).style.display = "block";
  evt.currentTarget.className += " active";
}


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

  // attache client modal
 

  function AttachClient(){
  const openModal = document.querySelector('#modal')
  openModal.hidden = false;
  }

  

function CloseModal(){
  const closeModal = document.querySelector("#modal");
  closeModal.hidden = true;
}

// // Listen for click events on buttons with the class 'client-details-btn'
// document.querySelectorAll('.client-details-btn').forEach(button => {
//   button.addEventListener('click', function () {
//       const clientId = this.getAttribute('data-client-id');
//       console.log(clientId);
      
      
//       // Send AJAX request to get client details
//       fetch(`client-attachement/${clientId}/`)
//           .then(response => response.json())
//           .then(data => {
//               if (data.error) {
//                   alert(data.error);
//               } else {
//                   // Populate modal with client data
//                   document.getElementById('client-name').textContent = data.first_name;
//                   // document.getElementById('client-email').textContent = data.email;
//                   // document.getElementById('client-phone').textContent = data.phone_number;
//                   // document.getElementById('client-address').textContent = data.address;

//                   // Open the modal
//                   AttachClient();
//               }
//           })
//           .catch(error => console.error('Error fetching client details:', error));
//   });
// });



function closeNotification(){
  const notification = document.querySelector("#close-notification");
  if (notification) {
    notification.style.display = 'none'; // Hides the notification
}else(
  console.log('Button not clicked')
  
)



}


document.addEventListener('DOMContentLoaded', function () {
  // This code will run only after the DOM is fully loaded
  const buttons = document.querySelectorAll('.client-details-btn');
  
  if (buttons.length === 0) {
      console.error('No buttons with class "client-details-btn" found.');
      return;  // Exit if no buttons are found
  }

  buttons.forEach(button => {
      button.addEventListener('click', function () {
          const clientId = this.getAttribute('data-client-id');

          fetch(`/user/client-attachement/${clientId}/`)
              .then(response => response.json())
              .then(data => {
                  if (data.error) {
                      alert(data.error);
                  } else {
                      // Update modal with client data
                      document.getElementById('client-name').textContent = data.first_name;
                      document.getElementById('client-email').textContent = data.email;
                      document.getElementById('id-number').textContent = data.id_number;
                      document.getElementById('last-name').textContent = data.last_name;
                      document.getElementById('client-id').textContent = data.client_id;

                      // Open the modal
                      document.getElementById('client-details-modal').style.display = 'block';
                  }
              })
              .catch(error => console.error('Error fetching client details:', error));
      });
  });
});

function updateLoanLink(event) {
  event.preventDefault();  // Prevent the default link click behavior
  
  // Get the client ID from the DOM
  var clientId = document.getElementById('client-id').textContent;

  // Construct the dynamic URL
  var baseUrl = "/user/pass-clientID/";  
  var dynamicUrl = baseUrl + clientId; 

  // Redirect the user to the dynamic URL
  window.location.href = dynamicUrl;
}

function periodOptions() {
  const months = document.querySelector("#months");
  const weeks = document.querySelector("#weeks");

  // Toggle visibility based on current display states
  if (weeks.style.display === 'none' || weeks.style.display === '') {
    // If weeks are hidden or not set, show weeks and hide months
    weeks.style.display = 'block';
    months.style.display = 'none';
  } else {
    // Otherwise, show months and hide weeks
    weeks.style.display = 'none';
    months.style.display = 'block';
  }
}



function addLoanModal(event){
  event.preventDefault();

  const openModal = document.querySelector('#modal')
  openModal.hidden = false;

}



const dropArea = document.getElementById('drop-area');
const fileInput = document.getElementById('file-input');
const actualFileInput = document.getElementById('actual-file-input');
const fileNameSpan = document.getElementById('file-name');
const fileInfo = document.getElementById('file-info');

function handleDragOver(event) {
    event.preventDefault();
    dropArea.classList.add('border-blue-500', 'bg-gray-50');
}

function handleDrop(event) {
    event.preventDefault();
    dropArea.classList.remove('border-blue-500', 'bg-gray-50');

    const files = event.dataTransfer.files;
    if (files.length > 0) {
        handleFile(files[0]);
    }
}




function handleFileSelect(event) {
    const file = event.target.files[0];
    if (file) {
        handleFile(file);
    }
}

function handleFile(file) {
    fileNameSpan.textContent = file.name;
    fileInfo.classList.remove('hidden');

    // Attach the file to the hidden file input (this is for form submission)
    actualFileInput.files = fileInput.files;
}



 // JavaScript for drag and drop functionality
 document.addEventListener('DOMContentLoaded', () => {
  const dropArea = document.getElementById('drop-area');
  const fileInput = document.getElementById('fileInput');
  const dragText = document.getElementById('dragText');

  // Prevent default behaviors
  ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
      dropArea.addEventListener(eventName, (e) => e.preventDefault());
      dropArea.addEventListener(eventName, (e) => e.stopPropagation());
  });

  // Highlight drop area when item is dragged over it
  ['dragenter', 'dragover'].forEach(eventName => {
      dropArea.addEventListener(eventName, () => dropArea.classList.add('bg-slate-100'));
  });

  // Unhighlight drop area when item is dragged out
  ['dragleave', 'drop'].forEach(eventName => {
      dropArea.addEventListener(eventName, () => dropArea.classList.remove('bg-slate-100'));
  });

  // Handle file drop
  dropArea.addEventListener('drop', (e) => {
      const files = e.dataTransfer.files;
      fileInput.files = files;
      dragText.textContent = files[0].name;
  });

  // Handle file selection via input
  fileInput.addEventListener('change', (e) => {
      dragText.textContent = e.target.files[0].name;
  });
});

document.addEventListener('DOMContentLoaded', function () {
  // Get modal elements
  const modal = document.getElementById('client-details-modal');
  const modalClose = document.querySelector('.close');
  
  // Function to open modal
  function openModal() {
      modal.style.display = 'block';
  }
  
  // Function to close modal
  modalClose.addEventListener('click', function () {
      modal.style.display = 'none';
  });
  
  // Listen for click events on buttons with the class 'client-details-btn'
  document.querySelectorAll('.client-details-btn').forEach(button => {
      button.addEventListener('click', function () {
          const clientId = this.getAttribute('data-client-id');
          
          // Send AJAX request to get client details
          fetch(`/client/${clientId}/`)
              .then(response => response.json())
              .then(data => {
                  if (data.error) {
                      alert(data.error);
                  } else {
                      // Populate modal with client data
                      document.getElementById('client-name').textContent = data.name;
                      document.getElementById('client-email').textContent = data.email;
                      document.getElementById('client-phone').textContent = data.phone;
                      document.getElementById('client-address').textContent = data.address;

                      // Open the modal
                      openModal();
                  }
              })
              .catch(error => console.error('Error fetching client details:', error));
      });
  });
});



//Loan products dynamic form selection
document.getElementById('loan-type').addEventListener('change', function () {
  const selectedOption = this.options[this.selectedIndex];
  const rate = selectedOption.getAttribute('data-rate');
  const interestMethod = selectedOption.getAttribute('data-interest');
  const period = selectedOption.getAttribute('data-period');
  const loanProductId = selectedOption.getAttribute('data-loanproduct');

  // Update the Rate, Interest Rate Method, and Period fields
  document.getElementById('rate').value = rate || '';
  document.getElementById('interest-method').value = interestMethod || '';
  document.getElementById('period').value = period || '';
  document.getElementById('loan-product-id').value = loanProductId || '';


});
