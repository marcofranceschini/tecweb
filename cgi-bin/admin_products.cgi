#!/Users/danielef/perl5/perlbrew/perls/perl-5.16.0/bin/perl
#!/usr/bin/perl
#!C:/xampp/perl/bin/perl.exe

# ATTENZIONE! IN BASE AL TUO O.S. CAMBIA LE RIGHE QUI SOPRA

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
		<link href="../tecwebproject/css/style_1024_max.css" rel="stylesheet" type="text/css" />
		<link href="../tecwebproject/css/style_768.css" rel="stylesheet" type="text/css" />
		<link href="../tecwebproject/css/style_480.css" rel="stylesheet" type="text/css" />
		<link href="../tecwebproject/css/style_1024_min.css" rel="stylesheet" type="text/css" />
		<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" />
		<link href='https://fonts.googleapis.com/css?family=Maven+Pro:400,700' rel='stylesheet' type='text/css' />
		<link rel="icon" type="image/png" href="res/images/icon.png" />
	</head>
	<body>
		<div id="header">
			<div id="navbar_admin">
				<a id="admin_back_icon" href="../index.html"><i class="material-icons md-24">&#xE88A;</i></a>
				<p><a id="admin_back" href="../index.html">Torna al sito</a></p>
				<p>Gestione Prodotti</p>
			</div>
		</div>
		
		<div id="content_admin">
EOF


#<!-- -------------- CGI - MODAL ------------ -->
			
						
print <<EOF;
		</div>
		
		<div id="action_bar">
			<div id="action_box">
				<a id="action_back" class="linked_box fadeInLeft" href="admin.html">Indietro</a>
				<a id="action_add" class="linked_box fadeInRight" href="">Aggiungi</a>
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
