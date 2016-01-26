var imageDefault = "null"; 
var errorImage = 1;
var modify = false;

function checkImage() {
    var regexp = /\w+\.(gif|png|jpg|jpeg)/i;
    var tag = null;
    tag = document.getElementById("wallpaper_new_img");
    if (tag.value.search(regexp) == -1 || tag.value == imageDefault) {
    	// Inserito un file che non è immagine o 
        tag.style.color = "red";
        errorImage = 1;
    } else {
        tag.style.color = "black";
        errorImage = 0;
    }
    checkSubmit();
}

function checkSubmit() {
    var tag = null;
    tag = document.getElementById("submit_modal_wallpaper");
    if(errorImage) {
	// Manca l'immagine o c'è stato un caricamento errato
	tag.disabled = true;
	tag.style.background =  "gray";
	tag.style.textShadow = "1px 1px 2px black";
     } else {
	tag.disabled = false;
	tag.style.background =  "#A00";
	tag.style.textShadow = "1px 1px 1px #9E3F3F";
     }   
}

document.addEventListener("DOMContentLoaded", function() {
    if(document.getElementById("submit_modal_wallpaper")) {
        // Stringhe di base dell'input type=file
        imageDefault = document.getElementById("wallpaper_new_img").value;
 
        // Inizializzo errori  
        document.getElementById("wallpaper_new_img").addEventListener("blur", checkImage, true);
        document.getElementById("wallpaper_new_img").addEventListener("change", checkImage, true);
    }  
    // Controllo sumbit
    checkSubmit();
}, true);
