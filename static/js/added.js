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