function sendMail() {
    var link = "fabianotavallini@gmail.com"
             + "?cc=" + escape(document.getElementById('form_email_mail').value)
             + "&subject=Richiesta dal sito"
             + "&body=(Messaggio da " + escape(document.getElementById('form_email_name').value) " " + escape(document.getElementById('form_email_mex').value);

    window.location.href = link;
}
