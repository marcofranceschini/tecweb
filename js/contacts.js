var nameHint = "Inserire Nome o Azienda";
var nameError = "Inserisci Nome &#47; Azienda";
var mailHint = "Inserire propria Email";
var mailError1 = "Inserisci la tua Email";
var mailError2 = "Email inserita non valida";
var mexHint = "Inserire messaggio";
var mexError = "Inserisci un messaggio";

function setNameHint() {
    var tag = document.getElementById("form_email_name");
    if (tag.value == "" || 
    tag.value == nameHint ||
    tag.value.search(/\w{2,}/) == -1) {
        tag.value = nameHint;
        tag.style.color = "grey";
    }
}

function setMailHint() {
    var tag = document.getElementById("form_email_mail");
    if (tag.value == "" || 
    tag.value == mailHint ||
    tag.value.search(/\w{4,}/) == -1) {
        tag.value = mailHint;
        tag.style.color = "grey";
    }  
}

function setMexHint() {
    var tag = document.getElementById("form_email_mex");
    if (tag.value == "" || 
    tag.value == mexHint ||
    tag.value.search(/\w{4,}/) == -1) {
        tag.value = mexHint;
        tag.style.color = "grey";
    }
}

function setNameError() {
    var regexp = /\w{2,}/;
    var tag = document.getElementById("form_email_name");
    var parent = tag.parentNode;
    if (parent.children.length == 2 && tag.value.search(regexp) == -1) {
        var error = document.createElement("h5");
        error.innerHTML = nameError;
        error.className = "mail_form_error";
        parent.appendChild(error);
    } else if (parent.children.length == 3 && tag.value.search(regexp) != -1) {
        parent.removeChild(parent.children[2]);
    }
    setNameHint();
}

function setMailError() {
    var regexp = /\w{4,}/;
    var tag = document.getElementById("form_email_mail");
    var parent = tag.parentNode;
    var error = document.createElement("h5");
    if (parent.children.length == 2 && tag.value.search(regexp) == -1) {
        error.innerHTML = mailError1;
        error.className = "mail_form_error";
        parent.appendChild(error);
    } else if (tag.value.search(regexp) != -1 && tag.value.search("@") == -1) {
        if (parent.children.length == 3)
            parent.removeChild(parent.children[2]);
        error.innerHTML = mailError2;
        error.className = "mail_form_error";
        parent.appendChild(error);
    } else if (parent.children.length == 3 && tag.value.search(regexp) != -1) {
        parent.removeChild(parent.children[2]);
    }
    setMailHint();
}

function setMexError() {
    var regexp = /\w{4,}/;
    var tag = document.getElementById("form_email_mex");
    var parent = tag.parentNode;
    if (parent.children.length == 2 && tag.value.search(regexp) == -1) {
        var error = document.createElement("h5");
        error.innerHTML = mexError;
        error.className = "mail_form_error";
        parent.appendChild(error);
    } else if (parent.children.length == 3 && tag.value.search(regexp) != -1) {
        parent.removeChild(parent.children[2]);
    }
    setMexHint();
}

document.addEventListener("DOMContentLoaded", function() {
    //Inizializzo placeholder
    setNameHint();
    setMailHint();
    setMexHint(); 
   
    //Assegno onsubmit al form
    document.getElementById("contacts_form").onsubmit = function() {
        var isComplete = true;
        if (document.getElementById("form_email_name").value == nameHint) {
            isComplete = false;
            var parent = document.getElementById("form_email_name").parentNode;
            if (parent.children.length == 2) {
                var error = document.createElement("h5");
                error.innerHTML = nameError;
                error.className = "mail_form_error";
                parent.appendChild(error);
            }
        }
        
        if (document.getElementById("form_email_mail").value == mailHint || document.getElementById("form_email_mail").value.search("@") == -1) {
            isComplete = false;
            var parent = document.getElementById("form_email_mail").parentNode;
            if (parent.children.length == 2) {
                var error = document.createElement("h5");
                error.innerHTML = mailError1;
                error.className = "mail_form_error";
                parent.appendChild(error);
            }
        }
            
        if (document.getElementById("form_email_mex").value == mexHint) {
            isComplete = false;
            var parent = document.getElementById("form_email_mex").parentNode;
            if (parent.children.length == 2) {
                var error = document.createElement("h5");
                error.innerHTML = mexError;
                error.className = "mail_form_error";
                parent.appendChild(error);
            }
        }
        
        if (isComplete) return true;
        else return false;
    };
    
    //Assegno focus agli input
    document.getElementById("form_email_name").addEventListener("focus", function() {
        if (document.getElementById("form_email_name").value == nameHint) {
            document.getElementById("form_email_name").value = "";
            document.getElementById("form_email_name").style.color = "black";
        } 
    }, true);
    document.getElementById("form_email_mail").addEventListener("focus", function() {
        if (document.getElementById("form_email_mail").value == mailHint) {
            document.getElementById("form_email_mail").value = "";
            document.getElementById("form_email_mail").style.color = "black";
        }
    }, true);
    document.getElementById("form_email_mex").addEventListener("focus", function() {
        if (document.getElementById("form_email_mex").value == mexHint) {
            document.getElementById("form_email_mex").value = "";
            document.getElementById("form_email_mex").style.color = "black";
        }
    }, true);
    
    //Assegno blur agli input
    document.getElementById("form_email_name").addEventListener("blur", setNameError, true);
    document.getElementById("form_email_mail").addEventListener("blur", setMailError, true);
    document.getElementById("form_email_mex").addEventListener("blur", setMexError, true);
    
}, true);