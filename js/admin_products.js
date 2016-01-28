var codeHint = "Inserire codice prodotto";
var codeError = "Inserisci il codice del prodotto";
var nameHint = "Inserire nome prodotto";
var nameError = "Inserisci il nome del prodotto";
var descHint = "Inserire descrizione prodotto";
var descError = "Descrivi il prodotto in almeno 10 caratteri";
var thumbnailDescHint = "Inserire descrizione breve prodotto";
var thumbnailDescError = "Inserisci la descrizione breve del prodotto";
var imageDefault = "null"; 
var thumbnailDefault = "null";
var errorCode = 1;
var errorName = 1;
var errorDesc = 1;
var errorThumbnailDesc = 1;
var errorImage = 1;
var errorThumbnail = 1;
var insert = false;
var modify = false;
var nameValue = "";
var descValue = "";
var thumbnailDescValue = "";

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

function setCodeTyping() {
    if (document.getElementById("code_insert").value == codeHint || document.getElementById("code_insert").value == codeError) {
        document.getElementById("code_insert").value = "";
        document.getElementById("code_insert").style.color = "black";
    } 
}

function setNameTyping() {
    if(insert) {
        if (document.getElementById("name_insert").value == nameHint || document.getElementById("name_insert").value == nameError) {
            document.getElementById("name_insert").value = "";
            document.getElementById("name_insert").style.color = "black";
        }
    }
    if(modify) {
        if (document.getElementById("name_modify").value == nameError) {
            document.getElementById("name_modify").value = "";
            document.getElementById("name_modify").style.color = "black";
        }
    }
}

function setDescTyping() {
    if(insert) {
        if (document.getElementById("desc_insert").value == descHint || document.getElementById("desc_insert").value == descError) {
            document.getElementById("desc_insert").value = "";
            document.getElementById("desc_insert").style.color = "black";
        }
    }
    if(modify) {
        if (document.getElementById("desc_modify").value == descError) {
            document.getElementById("desc_modify").value = "";
            document.getElementById("desc_modify").style.color = "black";
        }
    }
}

function setThumbnailDescTyping() {
    if(insert) {
        if (document.getElementById("thumbnail_desc_insert").value == thumbnailDescHint || document.getElementById("thumbnail_desc_insert").value == thumbnailDescError) {
            document.getElementById("thumbnail_desc_insert").value = "";
            document.getElementById("thumbnail_desc_insert").style.color = "black";
        }
    }    
    if(modify) {   
        if (document.getElementById("thumbnail_desc_modify").value == thumbnailDescError) {
            document.getElementById("thumbnail_desc_modify").value = "";
            document.getElementById("thumbnail_desc_modify").style.color = "black";
        }
    }
}

function checkCode() {
    var regexp = /\w{3,}/;
    var tag = document.getElementById("code_insert");
    if (tag.value.search(regexp) == -1) {
        tag.value = codeError;
        tag.style.color = "red";
        errorCode = 1;
    } else {
        errorCode = 0;
    }
    checkSubmit();
}

function checkName() {
    var regexp = /\w{3,}/;
    var tag = null;
    if(insert) {
        tag = document.getElementById("name_insert");
        if (tag.value.search(regexp) == -1) {
            tag.value = nameError;
            tag.style.color = "red";
            errorName = 1;
        } else {
            errorName = 0;
        }
        checkSubmit();
    }
    if(modify) {
        tag = document.getElementById("name_modify");
        if (tag.value.search(regexp) == -1) {
            tag.value = nameError;
            tag.style.color = "red";
            errorName = 1;
        } else if(tag.value == nameValue) {
            errorName = 1;
        } else {
            errorName = 0;
        }
        checkSubmit();
    }
}

function checkDesc() {
    var regexp = /\w+/;
    var tag = null;
    if(insert) {
        tag = document.getElementById("desc_insert");
        if (tag.value.search(regexp) == -1) {
            tag.value = descError;
            tag.style.color = "red";
            errorDesc = 1;
        } else {
            errorDesc = 0;
        }
        checkSubmit();
    }
    if(modify) {
        tag = document.getElementById("desc_modify");
        if (tag.value.search(regexp) == -1) {
            tag.value = descError;
            tag.style.color = "red";
            errorDesc = 1;
        } else if(tag.value == descValue){
            errorDesc = 1;
        } else {
            errorDesc = 0;
        }
        checkSubmit();
    }
}

function checkThumbnailDesc() {
    var regexp = /\w+/;
    var tag = null;
    if(insert) {
        tag = document.getElementById("thumbnail_desc_insert");
        if (tag.value.search(regexp) == -1) {
            tag.value = thumbnailDescError;
            tag.style.color = "red";
            errorThumbnailDesc = 1;
        } else {
            errorThumbnailDesc = 0;
        }
        checkSubmit();
    }
    if(modify) {
        tag = document.getElementById("thumbnail_desc_modify");
        if (tag.value.search(regexp) == -1) {
            tag.value = thumbnailDescError;
            tag.style.color = "red";
            errorThumbnailDesc = 1;
        } else if(tag.value == thumbnailDescValue){
            errorThumbnailDesc = 1;
        } else {
            errorThumbnailDesc = 0;
        }
        checkSubmit();
    }
}

function checkImage() {
    var regexp = /\w+\.(gif|png|jpg|jpeg)/i;
    var tag = null;
    if(insert) {
        tag = document.getElementById("image_insert");
        if (tag.value.search(regexp) == -1 || tag.value == imageDefault) {
            tag.style.color = "red";
            tag.innerText = "prova";
            errorImage = 1;
        } else {
            tag.style.color = "black";
            errorImage = 0;
        }
        checkSubmit();
    }
    if(modify) {
        tag = document.getElementById("image_modify");
        if (tag.value == imageDefault) {
            tag.style.color = "red";
            errorImage = 1;
        } else if(tag.value.search(regexp) == -1) {
            tag.style.color = "red";
            errorImage = 1;
        } else {
            tag.style.color = "black";
            errorImage = 0;
        }
        checkSubmit();
    }
}

function checkThumbnail() {
    var regexp = /\w+\.(gif|png|jpg|jpeg)/i;
    var tag = null;
    if(insert) {
        tag = document.getElementById("thumbnail_insert");
        if (tag.value.search(regexp) == -1 || tag.value == thumbnailDefault) {
            tag.style.color = "red";
            errorThumbnail = 1;
        } else {
            tag.style.color = "black";
            errorThumbnail = 0;
        }
        checkSubmit();
    }
    if(modify) {
        tag = document.getElementById("thumbnail_modify");
        if (tag.value == thumbnailDefault) {
            tag.style.color = "red";
            errorThumbnail = 1;
        } else if(tag.value.search(regexp) == -1) {
            tag.style.color = "red";
            errorThumbnail = 1;
        } else {
            tag.style.color = "black";
            errorThumbnail = 0;
        }
        checkSubmit();
    }
}

function checkSubmit() {
    var tag = null;
    if(insert) {
        tag = document.getElementById("submit_modal");
            if(errorCode || errorName || errorDesc || errorThumbnailDesc || errorImage || errorThumbnail) {
            tag.disabled = true;
            tag.style.background =  "gray";
            tag.style.textShadow = "1px 1px 2px black";
        } else {
            tag.disabled = false;
            tag.style.background =  "#A00";
            tag.style.textShadow = "1px 1px 1px #9E3F3F";
        }
    }
    if(modify) {
        tag = document.getElementById("submit_modal_modify");
        if(errorCode && errorName && errorDesc && errorThumbnailDesc && errorImage && errorThumbnail) {
            tag.disabled = true;
            tag.style.background =  "gray";
            tag.style.textShadow = "1px 1px 2px black";
        } else {
            tag.disabled = false;
            tag.style.background =  "#A00";
            tag.style.textShadow = "1px 1px 1px #9E3F3F";
        }
    }
    
}

document.addEventListener("DOMContentLoaded", function() {
    if(document.getElementById("form_modal_insert")) {
        insert = true;
        //Stringhe di base dell'input type=file
        imageDefault = document.getElementById("image_insert").value;
        thumbnailDefault = document.getElementById("thumbnail_insert").value;
        
        //Placeholders
        setCodeHint();
        setNameHint();
        setDescHint();
        setThumbnailDescHint();
    
        //Svuotamenti
        document.getElementById("code_insert").addEventListener("focus", setCodeTyping, true);    
        document.getElementById("name_insert").addEventListener("focus", setNameTyping, true);    
        document.getElementById("desc_insert").addEventListener("focus", setDescTyping, true);    
        document.getElementById("thumbnail_desc_insert").addEventListener("focus", setThumbnailDescTyping, true);
        
        //Errori
        document.getElementById("code_insert").addEventListener("blur", checkCode, true);    
        document.getElementById("name_insert").addEventListener("blur", checkName, true);    
        document.getElementById("desc_insert").addEventListener("blur", checkDesc, true);    
        document.getElementById("thumbnail_desc_insert").addEventListener("blur", checkThumbnailDesc, true);    
        document.getElementById("image_insert").addEventListener("blur", checkImage, true);
        document.getElementById("image_insert").addEventListener("change", checkImage, true);
        document.getElementById("thumbnail_insert").addEventListener("blur", checkThumbnail, true);
        document.getElementById("thumbnail_insert").addEventListener("change", checkThumbnail, true);

	//Controllo sumbit
    	checkSubmit();
    }
    if(document.getElementById("form_modal_modify")) {
        modify = true;
        //Inizializzo le variabili di errore e di controllo
        /*errorCode = 1;
        errorName = 1;
        errorDesc = 0;
        errorThumbnailDesc = 0;
        errorImage = 0;
        errorThumbnail = 0;*/
        nameValue = document.getElementById("name_modify").value;
        descValue = document.getElementById("desc_modify").value;
        thumbnailDescValue = document.getElementById("thumbnail_desc_modify").value;
        
        //Stringhe di base dell'input type=file
        imageDefault = document.getElementById("image_modify").value;
        thumbnailDefault = document.getElementById("thumbnail_modify").value;
            
        //Svuotamenti
        document.getElementById("code_modify").addEventListener("focus", setCodeTyping, true);    
        document.getElementById("name_modify").addEventListener("focus", setNameTyping, true);    
        document.getElementById("desc_modify").addEventListener("focus", setDescTyping, true);    
        document.getElementById("thumbnail_desc_modify").addEventListener("focus", setThumbnailDescTyping, true);
    
        //Errori
        document.getElementById("code_modify").addEventListener("blur", checkCode, true);    
        document.getElementById("name_modify").addEventListener("blur", checkName, true);    
        document.getElementById("desc_modify").addEventListener("blur", checkDesc, true);    
        document.getElementById("thumbnail_desc_modify").addEventListener("blur", checkThumbnailDesc, true);    
        document.getElementById("image_modify").addEventListener("blur", checkImage, true);
        document.getElementById("image_modify").addEventListener("change", checkImage, true);
        document.getElementById("thumbnail_modify").addEventListener("blur", checkThumbnail, true);
        document.getElementById("thumbnail_modify").addEventListener("change", checkThumbnail, true);

	//Controllo sumbit
    	checkSubmit();
    }
}, true);