var codeHint = "Inserire codice prodotto";
var codeError = "Inserisci il codice del prodotto";
var nameHint = "Inserire nome prodotto";
var nameError = "Inserisci il nome del prodotto";
var descHint = "Inserire descrizione prodotto";
var descError = "Inserisci la descrizione del prodotto";
var thumbnailDescHint = "Inserire descrizione breve prodotto";
var thumbnailDescError = "Inserisci la descrizione breve del prodotto";

//Errori globali
var errors = 0;

function setCodeHint() {
    if (document.getElementById("code_insert").value == "" || document.getElementById("code_insert").value == codeHint) {
        document.getElementById("code_insert").value = codeHint;
        document.getElementById("code_insert").style.color = "grey";
    }
}

function setNameHint() {
    if (document.getElementById("name_insert").value == "" || document.getElementById("name_insert").value == nameHint) {
        document.getElementById("name_insert").value = nameHint;
        document.getElementById("name_insert").style.color = "grey";
    }
}

function setDescHint() {
    if (document.getElementById("desc_insert").value == "" || document.getElementById("desc_insert").value == descHint) {
        document.getElementById("desc_insert").value = descHint;
        document.getElementById("desc_insert").style.color = "grey";
    }
}

function setThumbnailDescHint() {
    if (document.getElementById("thumbnail_desc_insert").value == "" || document.getElementById("thumbnail_desc_insert").value == thumbnailDescHint) {
        document.getElementById("thumbnail_desc_insert").value = thumbnailDescHint;
        document.getElementById("thumbnail_desc_insert").style.color = "grey";
    }
}

document.addEventListener("DOMContentLoaded", function() {
    //Placeholders
    setCodeHint();
    setNameHint();
    setDescHint();
    setThumbnailDescHint();
    
    document.getElementById("code_insert").addEventListener("focus", function() {
        if (document.getElementById("code_insert").value == codeHint || document.getElementById("code_insert").value == codeError) {
            document.getElementById("code_insert").value = "";
            document.getElementById("code_insert").style.color = "black";
            errors = 0;
        } 
    }, true);
    
    document.getElementById("name_insert").addEventListener("focus", function() {
        if (document.getElementById("name_insert").value == nameHint || document.getElementById("name_insert").value == nameError) {
            document.getElementById("name_insert").value = "";
            document.getElementById("name_insert").style.color = "black";
            errors = 0;
        } 
    }, true);
    
    document.getElementById("desc_insert").addEventListener("focus", function() {
        if (document.getElementById("desc_insert").value == descHint || document.getElementById("desc_insert").value == descError) {
            document.getElementById("desc_insert").value = "";
            document.getElementById("desc_insert").style.color = "black";
            errors = 0;
        } 
    }, true);
    
    document.getElementById("thumbnail_desc_insert").addEventListener("focus", function() {
        if (document.getElementById("thumbnail_desc_insert").value == thumbnailDescHint || document.getElementById("thumbnail_desc_insert").value == thumbnailDescError) {
            document.getElementById("thumbnail_desc_insert").value = "";
            document.getElementById("thumbnail_desc_insert").style.color = "black";
            errors = 0;
        } 
    }, true);
    
    //Errori
    document.getElementById("code_insert").addEventListener("blur", function() {
        var regexp = /\w{3,}/;
        var tag = document.getElementById("code_insert");
        if (tag.value.search(regexp) == -1) {
            tag.value = codeError;
            tag.style.color = "red";
            errors = 1;
        }
        //setCodeHint();
    }, true);
    
    document.getElementById("name_insert").addEventListener("blur", function() {
        var regexp = /\w{3,}/;
        var tag = document.getElementById("name_insert");
        if (tag.value.search(regexp) == -1) {
            tag.value = nameError;
            tag.style.color = "red";
            errors = 1;
        }
    }, true);
    
    document.getElementById("desc_insert").addEventListener("blur", function() {
        var regexp = /\w{10,}/;
        var tag = document.getElementById("desc_insert");
        if (tag.value.search(regexp) == -1) {
            tag.value = descError;
            tag.style.color = "red";
            errors = 1;
        }
    }, true);
    
    document.getElementById("thumbnail_desc_insert").addEventListener("blur", function() {
        var regexp = /\w+/;
        var tag = document.getElementById("thumbnail_desc_insert");
        if (tag.value.search(regexp) == -1) {
            tag.value = thumbnailDescError;
            tag.style.color = "red";
            errors = 1;
        }
    }, true);
    
    var imageDefault = document.getElementById("image_insert").value;
    document.getElementById("image_insert").addEventListener("blur", function() {
        var regexp = /\w+/;
        var tag = document.getElementById("image_insert");
        if (tag.value.search(regexp) == -1 || tag.value == imageDefault) {
            tag.style.color = "red";
            errors = 1;
        } else {
            tag.style.color = "black";
            errors = 0;
        }
    }, true);
    document.getElementById("image_insert").addEventListener("change", function() {
        var regexp = /\w+/;
        var tag = document.getElementById("image_insert");
        if (tag.value.search(regexp) == -1 || tag.value == imageDefault) {
            tag.style.color = "red";
            errors = 1;
        } else {
            tag.style.color = "black";
            errors = 0;
        }
    }, true);
    
    var thumbnailDefault = document.getElementById("thumbnail_insert").value;
    document.getElementById("thumbnail_insert").addEventListener("blur", function() {
        var regexp = /\w+/;
        var tag = document.getElementById("thumbnail_insert");
        if (tag.value.search(regexp) == -1 || tag.value == imageDefault) {
            tag.style.color = "red";
            errors = 1;
        } else {
            tag.style.color = "black";
            errors = 0;
        }
    }, true);
    document.getElementById("thumbnail_insert").addEventListener("change", function() {
        var regexp = /\w+/;
        var tag = document.getElementById("thumbnail_insert");
        if (tag.value.search(regexp) == -1 || tag.value == imageDefault) {
            tag.style.color = "red";
            errors = 1;
        } else {
            tag.style.color = "black";
            errors = 0;
        }
    }, true);
    
    //errors.onchange
}, true);