#!/usr/bin/perl

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
		<meta name="viewport" content="width=device-width">
		<link href="../css/style_1024_max.css" rel="stylesheet" type="text/css" />
		<link href="../css/style_768.css" rel="stylesheet" type="text/css" />
		<link href="../css/style_480.css" rel="stylesheet" type="text/css" />
		<link href="../css/style_1024_min.css" rel="stylesheet" type="text/css" />
		<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" />
		<link href='https://fonts.googleapis.com/css?family=Maven+Pro:400,700' rel='stylesheet' type='text/css' />
		<link rel="icon" type="image/png" href="../res/images/icon.png" />
	</head>
	<body>
		<div id="header">
			<div id="contacts">
				<p><i class="material-icons md-18">&#xE0CD;</i> +39 0422 445566</p>
				<p><i class="material-icons md-18">&#xE0BE;</i> jurapida@gmail.com</p>
			</div>
			<div id="navbar">
				<a href="../index.html"><img id="logo" src="../res/images/logo_bianco.png" alt="Logo Ju Rapida" /></a>
				<ul id="menu"> 
					<li><a href="../index.html"><span xml:lang="en">Home</span></a></li>
					<li><a href="../pages/products.html">Prodotti</a></li> <!--Comprese le offerte-->
					<li><span id="current">Contatti</span></li>
					<li><a href="../pages/about.html">Chi siamo</a></li>
				</ul>
			</div>
			<div id="breadcrumb">
				<a href="../index.html"><i class="material-icons md-18" >&#xE88A;</i></a> <span>&gt; Contatti</span>
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
			<div id="form_email">
				<p>Oppure contattaci ora via <span lang="en">Email</span></p>
				<form id="contacts_form" action="../cgi-bin/contacts.cgi" method="post">
					<div class="form_email_element">
						<label for="form_email_name">Nome &#47; Societ&agrave;</label>
						<input type="text" name="name" id="form_email_name"
EOF
if ($FORM{'name'}) {
	print "value=\"".$FORM{'name'}."\"";
} 
print "/>";
print <<EOF;
						<h5 class="mail_form_error" id="error_name">Inserire Nome &#47; Societ&agrave;</h5>
					</div>
					<div class="form_email_element">
						<label for="form_email_mail"><span lang="en">Email</span></label>
						<input type="text" name="mail" id="form_email_mail"
EOF
if ($FORM{'mail'}) {
	print "value=\"".$FORM{'mail'}."\"";
}
print "/>";
print <<EOF;
						<h5 class="mail_form_error" id="error_mail">Inserisci la tua email</h5>
					</div>
					<div class="form_email_element">
						<label for="form_email_mex">Messaggio</label>
						<textarea name="mex" id="form_email_mex" rows="5" cols="5">
EOF
print $FORM{'mex'}."</textarea>";
print <<EOF;
						<h5 class="mail_form_error" id="error_mex">Inserisci un messaggio</h5>
					</div>
					<div class="form_email_element">
						<input type="submit" value="Invia" id="form_email_submit" />
					</div>
				</form>
			</div>
		</div>
		
EOF
if (%FORM) {
	if ($name ne '' && $from ne '' && index($from, '@') != -1 && $body ne '') {
		my $smtp = new Net::SMTP::TLS(
        	'smtp.gmail.com',
			Port    =>  587,
			User    => 	'request.jurapida',
			Password=> 	'bellabella.12') or die "die";
		
		$smtp->mail();
		$smtp->to('request.jurapida@gmail.com');
		$smtp->data();
		$smtp->datasend("From: ".$from."\n");
		$smtp->datasend("To: request.jurapida\@gmail.com\n");
		$smtp->datasend("Reply-To: ".$from."\n");
		$smtp->datasend("Subject: Richiesta da ".$from."\n\n");
		$smtp->datasend($body."\n");
		$smtp->dataend;
		$smtp->quit;
		
		print <<EOF;
		<script type="text/javascript">
			document.getElementById('form_email').style.display = "none";
			location.hash = "#mail_sent";
		</script>
		<p id="mail_sent">Grazie! La ricontatteremo al pi&ugrave; presto!</p>		
EOF
	} else {
		if ($name eq '') {
			print "	<script type=\"text/javascript\">
						document.getElementById(\"error_name\").style.display = \"block\";
						location.hash = \"#contacts_form\";
					</script>";
		} 
		if ($from eq '') {
			print "	<script type=\"text/javascript\">
						document.getElementById(\"error_mail\").style.display = \"block\";
						location.hash = \"#contacts_form\";
					</script>";
		} elsif (index($from, '@') == -1) {
			print "	<script type=\"text/javascript\">
						document.getElementById(\"error_mail\").style.display = \"block\";
						document.getElementById(\"error_mail\").innerHTML = \"Email inserita non valida\";
						location.hash = \"#contacts_form\";
					</script>";
		}
		if ($body eq '') {
			print "	<script type=\"text/javascript\">
						document.getElementById(\"error_mex\").style.display = \"block\";
						location.hash = \"#contacts_form\";
					</script>";
		}
	}	
}
print <<EOF;
		<div id="footer">
			<div id="footer_top">
				<div id="maps">
					<ul id="maps_menu">
						<li><a href="../index.html"><span xml:lang="en">Home</span></a></li>
						<li><a href="../pages/products.html">Prodotti</a></li>
						<li><a href="contacts.cgi">Contatti</a></li>
						<li><a href="../pages/about.html">Chi siamo</a></li>
					</ul>
					<ul id="maps_categories">
						<li><a href="">Calcio</a></li>
						<li><a href=""><span xml:lang="en">Basket</span></a></li>
						<li><a href=""><span xml:lang="en">Volley</span></a></li>
						<li><a href="">Tennistavolo</a></li>
						<li><a href="">Nuoto</a></li>
						<li><a href="">Minigolf</a></li>
						<li><a href="">Calciobalilla</a></li>
						<li><a href="">Protezioni</a></li>
						<li><a href="">Accessori</a></li>
					</ul>
				</div>
				<div id="admin_form_panel">
					<form id="admin_form" action="../cgi-bin/login.cgi" method="post">
						<fieldset>
							<legend><i class="material-icons md-18">&#xE853;</i>Area Riservata</legend>
							<label class="form_item" for="username">Username</label>
							<input class="form_item" id="username" type="text" name="username"/>
							<label class="form_item" for="password">Password</label>
							<input class="form_item" id="password" type="password" name="password"/>
							<input type="hidden" name="page" value="../pages/contacts.html" />
							<input id="submit" type="submit" value="Login" />
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
