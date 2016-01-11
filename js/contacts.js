var nameHint = "Inserire Nome o Societ &agrave;";
var nameError = "Inserisci Nome &#47; Societ\340";
var mailHint = "Inserire propria Email";
var mailError1 = "Inserisci la tua Email";
var mailError2 = "Email inserita non valida";
var mexHint = "Inserire messaggio";
var mexError = "Inserisci un messaggio";

function setNameHint() {
    if (document.getElementById("form_email_name").value == "") { //manca or ... (vedi esempi sotto)
        document.getElementById("form_email_name").value = nameHint;
        document.getElementById("form_email_name").style.color = "grey";
    }
}

function setMailHint() {
    if (document.getElementById("form_email_mail").value == "" || document.getElementById("form_email_mail").value == mailHint) {
        document.getElementById("form_email_mail").value = mailHint;
        document.getElementById("form_email_mail").style.color = "grey";
    }  
}

function setMexHint() {
    if (document.getElementById("form_email_mex").value == "" || document.getElementById("form_email_mex").value == mexHint) {
        document.getElementById("form_email_mex").value = mexHint;
        document.getElementById("form_email_mex").style.color = "grey";
    }
}

document.addEventListener("DOMContentLoaded", function() {
    //Inizializzo placeholder
    setNameHint();
    setMailHint();
    setMexHint();    
    
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
    
    //Inizializzo errori
    document.getElementById("form_email_name").addEventListener("blur", function() {
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
    }, true);
    
    document.getElementById("form_email_mail").addEventListener("blur", function() {
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
    }, true);
    
    document.getElementById("form_email_mex").addEventListener("blur", function() {
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
    }, true);
    
}, true);