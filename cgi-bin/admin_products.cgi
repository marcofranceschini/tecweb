#!/usr/bin/perl
#!C:/xampp/perl/bin/perl.exe

use CGI;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard Vars);
use CGI::Session;
use warnings;

#Da usare il lab
#<link href="../tecwebproject/css/style_1024_max.css" rel="stylesheet" type="text/css" />
#<link href="../tecwebproject/css/style_768.css" rel="stylesheet" type="text/css" />
#<link href="../tecwebproject/css/style_480.css" rel="stylesheet" type="text/css" />
#<link href="../tecwebproject/css/style_1024_min.css" rel="stylesheet" type="text/css" />

sub getSession() {
	$sessione = CGI::Session->load() or die $!; #CGI::Session->errstr
	if ($sessione->is_expired || $sessione->is_empty) { # Se manca la sessione torno in home
		#print redirect(-url=>'../');
	}
}

sub destroySession() {
	$session = CGI::Session->load() or die $!;
	#$SID = $session->id();
	$session->close();
	$session->delete();
	$session->flush();
	#print redirect(-url=>'../'); # Torno in home
	print "Content-Type: text/html\n\n";
	print "prova";
	$sessione = CGI::Session->load() or die $!; #CGI::Session->errstr
	print $session->param('pass');
}

sub printPlaceholder() {
	# Da usare in lab: ../tecwebproject/res/images/empty_list.png
	$placeholder = "<div id=\"placeholder\">
						<p>Nessun prodotto ancora inserito</p>
						<img src=\"../res/images/empty_list.png\" alt=\"Immagina lista prodotti vuota\" \>
					</div>";
	return $placeholder;
}


getSession(); # Verifico che la sessione ci sia

my $cgi = CGI->new();
my $param = $cgi->param('param');
if ($param) { # LOGOUT - E' stato premuto il link per uscire
	destroySession();
} else {
	print "Content-Type: text/html\n\n";
	print <<EOF;
	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
		<head>
			<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
			<title>Gestione Prodotti - Amministrazione - Ju Rapida</title>
			<meta name="title" content="Ju Rapida S.N.C." />
			<meta name="description" content="Pagina di amministrazione dei prodotti del sito Ju Rapida." />
			<!-- meta name="keywords" content="ju rapida, ammin, articoli sportivi, calcio, tennistavolo, volley, carlo tavallini, vendita;" -->
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
				<div id="navbar_admin">
					<a id="admin_back_icon" href="../cgi-bin/admin.cgi?param=1"><i class="material-icons md-24">&#xE88A;</i></a>
					<p><a id="admin_back" href="../cgi-bin/admin.cgi?param=1">Torna al sito</a></p>
					<p>Gestione Prodotti</p>
				</div>
			</div>
			
			<div id="openModal" class="modalDialog">
				<div>
					<a href="#close" title="Close" class="close">X</a>
					<p>Inserisci un nuovo prodotto</p>
					<form action="admin_products.cgi" method="post">
						<label class="form_item" for="product_category">Categoria</label>
						<select class="form_item" id="product_category">
							<option value="calcio">Calcio</option>
							<option value="basket"><span lang="en">Basket</span></option>
							<option value="volley"><span lang="en">Volley</span></option>
							<option value="tennistavolo">Tennistavolo</option>
							<option value="nuoto">Nuoto</option>
							<option value="minigolf">Minigolf</option>
							<option value="calciobalilla">Calciobalilla</option>
							<option value="protezioni">Protezioni</option>
							<option value="accessori">Accessori</option>
						</select>
						<label class="form_item" for="product_code">Codice</label>
						<input class="form_item" id="product_code" type="text" />
						<label class="form_item" for="product_name">Nome</label>
						<input class="form_item" id="product_name" type="text" />
						<label class="form_item" for="product_desc">Descrizione</label>
						<textarea class="form_item" id="product_desc"></textarea>
						<label class="form_item" for="thumbnail_desc">Descrizione breve</label>
						<textarea class="form_item" id="thumbnail_desc"></textarea>
						<label class="form_item" for="product_image">Carica <span lang="en">thumbnail</span></label>
						<input class="form_item" id="product_image" type="file" />
						
						<input id="submit" type="submit" value="Inserisci" />
					</form>
				</div>
			</div>
			
			<div id="content_admin">	
EOF
	#salvare dati XML
	print %FORM;
	
	#prendere dati XML
	
	
	#if (lista prodotti vuota)
	print printPlaceholder();
	
	print <<EOF;
			</div>
			
			<div id="action_bar">
				<div id="action_box">
					<a id="action_back" class="linked_box fadeInLeft" href="admin.cgi">Indietro</a>
					<a id="action_add" class="linked_box fadeInRight" href="#openModal">Aggiungi</a>
				</div>
			</div>
					
			<div id="footer">
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

}
