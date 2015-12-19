#!C:/xampp/perl/bin/perl.exe
#!/usr/bin/perl



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
		print redirect(-url=>'../');
	} else {
		print $sessione->param('pass');
		return $sessione;
	}
}

sub destroySession() {
	$session = CGI::Session->load() or die $!;
	#$SID = $session->id();
	$session->close() or die "errore close";
	$session->delete() or die "errore delete";
	$session->flush() or die "errore flush";
	print redirect(-url=>'../'); # Torno in home
}

	
my $session = getSession(); # Verifico che la sessione ci sia

my $cgi = CGI->new();
my $app = $cgi->param('appoggio');
if ($app) { # LOGOUT - E' stato premuto il link per uscire
	destroySession();
}else{
	print "Content-Type: text/html\n\n";
	print <<EOF;
		<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
		<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
			<head>
				<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
				<title>Amministrazione - Ju Rapida</title>
				<meta name="title" content="Ju Rapida S.N.C." />
				<meta name="description" content="Pagina di amministrazione del sito Ju Rapida." />
				<meta name="author" content="Fabiano Tavallini, Marco Franceschini, Daniele Favaro" />
				<meta name="copyright" content="Ju Rapida S.N.C." />
				<meta name="viewport" content="width=device-width">
				<link href="../css/style_1024_max.css" rel="stylesheet" type="text/css" />
				<link href="../css/style_768.css" rel="stylesheet" type="text/css" />
				<link href="../css/style_480.css" rel="stylesheet" type="text/css" />
				<link href="../css/style_1024_min.css" rel="stylesheet" type="text/css" />
				<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" />
				<link href='https://fonts.googleapis.com/css?family=Maven+Pro:400,700' rel='stylesheet' type='text/css' />
				<link rel="icon" type="image/png" href="res/images/icon.png" />
			</head>
			<body>
				<div id="header" class="fadeInDown">
					<div id="navbar_admin">
						<a id="admin_back_icon" href="../cgi-bin/admin.cgi?appoggio=1"><i class="material-icons md-24">&#xE88A;</i></a>
						<p><a id="admin_back" href="../cgi-bin/admin.cgi?appoggio=1">Torna al sito</a></p>
						<p>Area Amministrativa</p>
					</div>
				</div>
				
				<div id="content_admin">
					<p>Benvenuti nell'amministrazione del sito, selezionare una delle seguenti opzioni per gestire novit&agrave; e prodotti.</p>
					<div id="admin_panel">
						<a id="news" class="linked_box fadeInLeft" href="admin_news.cgi"><span class="admin_label">Novit&agrave;</span></a>	
						<a id="products" class="linked_box fadeInRight" href="admin_products.cgi"><span class="admin_label">Prodotti</span></a>
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