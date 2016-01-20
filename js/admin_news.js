var imageHint = "Inserire immagine";


function setImageHint() {
    if (document.getElementById("wallpaper_img").value == "" || document.getElementById("wallpaper_img").value == imageHint) {
        document.getElementById("wallpaper_img").value = imageHint;
        document.getElementById("wallpaper_img").style.color = "grey";
    }
}

document.addEventListener("DOMContentLoaded", function() {
    // Inizializzo placeholder
    setImageHint();    
    
    document.getElementById("wallpaper_img").addEventListener("focus", function() {
        if (document.getElementById("wallpaper_img").value == imageHint) {
            document.getElementById("wallpaper_img").value = "";
            document.getElementById("wallpaper_img").style.color = "black";
        } 
    }, true);
    
    // Inizializzo errori
    document.getElementById("wallpaper_img").addEventListener("blur", function() {
        var regexp = /\w{2,}/;
        var tag = document.getElementById("wallpaper_img");
        var parent = tag.parentNode;
        if (parent.children.length == 2 && tag.value.search(regexp) == -1) {
            var error = document.createElement("h5");
            error.innerHTML = nameError;
            //error.className = "mail_form_error";
            parent.appendChild(error);
        } else if (parent.children.length == 3 && tag.value.search(regexp) != -1) {
            parent.removeChild(parent.children[2]);
        }
        setImageHint();
    }, true);    
}, true);
