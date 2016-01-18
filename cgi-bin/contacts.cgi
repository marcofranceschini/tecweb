#!/usr/bin/perl
#!C:/Perl64/bin/perl.exe

use CGI;
use Net::SMTP::TLS;
use CGI qw(:standard Vars);
use CGI::Carp qw(fatalsToBrowser);

print "Content-Type: text/html\n\n";

$mail = '/usr/sbin/sendmail';

my %FORM = Vars();

$name = $FORM{"name"};
$from = $FORM{"mail"};
$body = $FORM{"mex"};

#Da usare il lab
#<link href="../tecwebproject/css/style_1024_max.css" rel="stylesheet" type="text/css" />
#<link href="../tecwebproject/css/style_768.css" rel="stylesheet" type="text/css" />
#<link href="../tecwebproject/css/style_480.css" rel="stylesheet" type="text/css" />
#<link href="../tecwebproject/css/style_1024_min.css" rel="stylesheet" type="text/css" />

my $tabIndexCount = 0;
sub tabindex {
    $tabIndexCount++;
    return (\$tabIndexCount); #ritorna il RIFERIMENTO alla variabile
}
my $cgi = CGI->new();
if (defined $cgi->param('tabindex') && $cgi->param('tabindex') ne '') {
    $tabIndexCount = $tabIndexCount - $cgi->param('tabindex');
}

print <<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<title>Contatti - Ju Rapida</title>
		<meta name="title" content="Contatti - Ju Rapida S.N.C." />
		<meta name="description" content="Contatti dell'azienda." />
		<meta name="keywords" content="ju rapida, contatti, telefono, fax, email;" />
		<meta name="author" content="Fabiano Tavallini, Marco Franceschini, Daniele Favaro" />
		<meta name="copyright" content="Ju Rapida S.N.C." />
		<meta name="viewport" content="width=device-width"/>
		<link href="../css/style_1024_max.css" rel="stylesheet" type="text/css" />
		<link href="../css/style_768.css" rel="stylesheet" type="text/css" />
		<link href="../css/style_480.css" rel="stylesheet" type="text/css" />
		<link href="../css/style_1024_min.css" rel="stylesheet" type="text/css" />
        <link href="../css/style_print.css" rel="stylesheet" type="text/css" />
		<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" type='text/css' />
		<link href='https://fonts.googleapis.com/css?family=Maven+Pro:400,700' rel='stylesheet' type='text/css' />
		<link rel="icon" type="image/png" href="../res/images/icon.png" />
   		<script type="text/javascript" src="../js/contacts.js"></script>
	</head>
	<body>
        <div><a class="skip_menu" href="contacts.cgi?tabindex=4#content_contacts" tabindex="${tabindex()}">Salta la navigazione</a></div>
		<div id="header">
			<div id="contacts">
				<p><i class="material-icons md-18">&#xE0CD;</i> +39 0422 445566</p>
				<p><i class="material-icons md-18">&#xE0BE;</i> jurapida@gmail.com</p>
			</div>
			<div id="navbar">
				<a href="../cgi-bin/index.cgi"><img id="logo" src="../res/images/logo_bianco.png" alt="Logo Ju Rapida" /></a>
				<ul id="menu"> 
					<li><a href="../cgi-bin/index.cgi" tabindex="${tabindex()}"><span xml:lang="en">Home</span></a></li>
					<li><a href="../pages/products.html" tabindex="${tabindex()}">Prodotti</a></li>
					<li><span id="current">Contatti</span></li>
					<li><a href="../pages/about.html" tabindex="${tabindex()}">Chi siamo</a></li>
				</ul>
			</div>
			<div id="breadcrumb">
				<a href="../cgi-bin/index.cgi"><img src="../res/images/ic_home.png" alt="Home page"</img></a> &gt; Contatti
			</div>
		</div>
		
		<div id="content_contacts">
			<div>
				<p>Inviaci la tua richiesta in qualsiasi momento della giornata</p>
				<ul id="contact_list">
					<li>Telefono: <span class="contact"><i class="material-icons md-24">&#xE0CD;</i>+39 0422 445566</span></li>
					<li>Fax: <span class="contact"><i class="material-icons md-24">&#xE8AD;</i>+39 0422 445566</span></li>
					<li>Email: <span class="contact"><i class="material-icons md-24">&#xE0BE;</i>jurapida\@gmail.com</span></li>
				</ul>
			</div>
EOF
if (%FORM && $name =~ /[a-zA-Z0-9]/ && length($name) > 1 && $from =~ /[a-zA-Z0-9]/ && index($from, '@') != -1 && length($from) > 3 && $body =~ /[a-zA-Z0-9]/ && length($body) > 3) {
    #Causa bug della libreria presente nei server in laboratorio, il seguente codice per l'invio della email è stato commentato.
    #Il bug è risolvibile cambiando una riga in un file della libreria, ma a scopi didattici eseguiamo solo un facsimile del risultato.
#    my $smtp = new Net::SMTP::TLS(
#       'smtp.gmail.com',
#		Port    =>  587,
#		User    => 	'request.jurapida',
#       Password=> 	'bellabella.12') or die "die";
		
#   $smtp->mail();
#	$smtp->to('request.jurapida@gmail.com');
#	$smtp->data();
#	$smtp->datasend("From: ".$from."\n");
#	$smtp->datasend("To: request.jurapida\@gmail.com\n");
#	$smtp->datasend("Reply-To: ".$from."\n");
#	$smtp->datasend("Subject: Richiesta da ".$from."\n\n");
#	$smtp->datasend($body."\n");
#	$smtp->dataend;
#	$smtp->quit;
		
	print " </div>
            <p id=\"mail_sent\">Grazie! La ricontatteremo al pi&ugrave; presto!</p>";	
} else {
    print <<EOF;
		    <div id="form_email">
				<p>Oppure contattaci ora via <span lang="en">Email</span></p>
				<form id="contacts_form" action="../cgi-bin/contacts.cgi" method="post">
					<div class="form_email_element">
						<label for="form_email_name">Nome &#47; Azienda</label>
						<input tabindex="${tabindex()}" type="text" name="name" id="form_email_name"
EOF
print "value=\"".$name."\"/>";
if (%FORM && (!($name =~ /[a-zA-Z0-9]/) || length($name) < 2 || $name eq "Inserire Nome o Azienda")) {
    print "<h5 class=\"mail_form_error\">Inserisci Nome &#47; Azienda</h5>";
}
print <<EOF;
					</div>
					<div class="form_email_element">
						<label for="form_email_mail"><span lang="en">Email</span></label>
						<input tabindex="${tabindex()}" type="text" name="mail" id="form_email_mail"
EOF
print "value=\"".$from."\"/>";
if (%FORM && (!($from =~ /[a-zA-Z0-9]/) || length($from) < 4 || $from eq "Inserire propria Email")) {
    print "<h5 class=\"mail_form_error\">Inserisci la tua email</h5>";
} else {
    if (%FORM && $from =~ /[a-zA-Z0-9]/ && index($from, '@') == -1) {
        print "<h5 class=\"mail_form_error\">Email inserita non valida</h5>";
    }
}
print <<EOF;
					</div>
					<div class="form_email_element">
						<label for="form_email_mex">Messaggio</label>
						<textarea tabindex="${tabindex()}" name="mex" id="form_email_mex" rows="5" cols="5">
EOF
print $body."</textarea>";
if (%FORM && (!($body =~ /[a-zA-Z0-9]/) || length($body) < 4 || $body eq "Inserire messaggio")) {
    print "<h5 class=\"mail_form_error\">Inserisci un messaggio</h5>";
}
print <<EOF;
					</div>
					<div class="form_email_element">
						<input tabindex="${tabindex()}" type="submit" value="Invia" id="form_email_submit"/>
					</div>
				</form>
			</div>
		</div>
		
EOF
}
print <<EOF;
		<div id="footer">
			<div id="footer_top">
				<div id="maps">
					<ul id="maps_menu">
						<li><a tabindex="${tabindex()}" href="../cgi-bin/index.cgi"><span xml:lang="en">Home</span></a></li>
						<li><a tabindex="${tabindex()}" href="../pages/products.html">Prodotti</a></li>
						<li>Contatti</li>
						<li><a tabindex="${tabindex()}" href="../pages/about.html">Chi siamo</a></li>
					</ul>
					<ul id="maps_categories">
						<li><a tabindex="${tabindex()}" href="products.cgi?category=Calcio">Calcio</a></li>
						<li><a tabindex="${tabindex()}" href="products.cgi?category=Basket"><span xml:lang="en">Basket</span></a></li>
						<li><a tabindex="${tabindex()}" href="products.cgi?category=Volley"><span xml:lang="en">Volley</span></a></li>
						<li><a tabindex="${tabindex()}" href="products.cgi?category=Tennistavolo">Tennistavolo</a></li>
						<li><a tabindex="${tabindex()}" href="products.cgi?category=Nuoto">Nuoto</a></li>
						<li><a tabindex="${tabindex()}" href="products.cgi?category=Minigolf">Minigolf</a></li>
						<li><a tabindex="${tabindex()}" href="products.cgi?category=Calciobalilla">Calciobalilla</a></li>
						<li><a tabindex="${tabindex()}" href="products.cgi?category=Protezioni">Protezioni</a></li>
						<li><a tabindex="${tabindex()}" href="products.cgi?category=Accessori">Accessori</a></li>
					</ul>
				</div>
				<div id="admin_form_panel">
					<form id="admin_form" action="../cgi-bin/login.cgi" method="post">
						<fieldset>
							<legend><i class="material-icons md-18">&#xE853;</i>Area Riservata</legend>
							<label class="form_item" for="username">Username</label>
							<input tabindex="${tabindex()}" class="form_item" id="username" type="text" name="username"/>
							<label class="form_item" for="password">Password</label>
							<input tabindex="${tabindex()}" class="form_item" id="password" type="password" name="password"/>
							<input type="hidden" name="page" value="../cgi-bin/index.cgi" />
							<input tabindex="${tabindex()}" id="submit" type="submit" value="Login" />
						</fieldset>
					</form>
				</div>
			</div>
			<div id="copy_panel">
				<p id="copy">Copyright &copy; 2016 - All right reserved. Ju Rapida SNC - VIA F. PETRARCA, 14/31100 TREVISO ITALY - P. IVA: 01836040269</p>
				<p id="validation">
					<span id="xhtml_valid">
    					<a href="http://validator.w3.org/check?uri=referer"><img src="http://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0 Strict" height="31" width="88" /></a>
  					</span>
					<span id="css_valid">
						<a href="http://jigsaw.w3.org/css-validator/check/referer"><img style="border:0;width:88px;height:31px" src="http://jigsaw.w3.org/css-validator/images/vcss-blue" alt="Valid CSS3" /></a>
					</span>
				</p>
			</div>
		</div>
	</body>
</html>
EOF
