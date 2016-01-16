#!/usr/bin/perl
#!C:/Perl64/bin/perl.exe
 
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard Vars);
use CGI::Session;
use XML::LibXML;
use warnings;
	
$username = "";	# Per il messaggio con user vuoto
$password = "";	# Per il messaggio con password vuota
$page = "";

my %data = Vars();
$username = $data{"username"};
$password = $data{"password"};
$page = $data{"page"};

# Leggo dati login da db
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file("../xml/admin_db.xml");

my @admins = $doc->findnodes('/administrators/user');
my $admin = $admins[0]; # In questo progetto esiste un solo amministratore

if ($username eq $admin->findnodes('./username')->to_literal && $password eq $admin->findnodes('./password')->to_literal) {	# Login corretto
	
	my $sessione = createSession();
	print $sessione->header(-location=>"admin.cgi");

} else {	# Login errato
    print "Content-Type: text/html\n\n";
	# Da usare in lab
	#<link href="../tecwebproject/css/style_1024_max.css" rel="stylesheet" type="text/css" />
	#<link href="../tecwebproject/css/style_768.css" rel="stylesheet" type="text/css" />
	#<link href="../tecwebproject/css/style_480.css" rel="stylesheet" type="text/css" />
	#<link href="../tecwebproject/css/style_1024_min.css" rel="stylesheet" type="text/css" />
	
	print <<EOF;
	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
		<head>
			<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
			<title>Errore - Amministrazione - Ju Rapida</title>
			<meta name="title" content="Ju Rapida S.N.C." />
			<meta name="description" content="Pagina di errore del sito Ju Rapida." />
			<!-- meta name="keywords" content="ju rapida, ammin, articoli sportivi, calcio, tennistavolo, volley, carlo tavallini, vendita;" -->
			<meta name="author" content="Fabiano Tavallini, Marco Franceschini, Daniele Favaro" />
			<meta name="copyright" content="Ju Rapida S.N.C." />
			<meta name="viewport" content="width=device-width">
			<link href="../css/style_1024_max.css" rel="stylesheet" type="text/css" />
			<link href="../css/style_768.css" rel="stylesheet" type="text/css" />
			<link href="../css/style_480.css" rel="stylesheet" type="text/css" />
			<link href="../css/style_1024_min.css" rel="stylesheet" type="text/css" />
			<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" type='text/css' />
			<link href='https://fonts.googleapis.com/css?family=Maven+Pro:400,700' rel='stylesheet' type='text/css' />
			<link rel="icon" type="image/png" href="../res/images/icon.png" />
		</head>
		<body>
			<div id="header">
				<div id="navbar_admin">
					<h3>Qualcosa &egrave; andato storto</h3>
				</div>
			</div>
			
			<div id="content_error">
				<img src="../res/images/error.png" alt="Immagine di errore" />
EOF
	if (!%data) {
		print "<h3>Riprova ad eseguire il login!</h3>";
		$page = "../cgi-bin/index.cgi";
	}elsif ($username eq "" and $password eq "") { # Username e password vuoti
		print "<h3>Username e password non inseriti!</h3>";
	} elsif ($username eq "") {	# Username vuoto
		print "<h3>Username non inserito!</h3>";
	} elsif ($password eq "") {	# Password vuota
		print "<h3>Password non inserita!</h3>";
	} elsif ($username ne "admin") {	# Username errato
		print "<h3>Username inserito non corretto!</h3>";
	} else {	# Password errata
		print "<h3>Password inserita non corretta!</h3>";
	} 
	print a({
		-id		=>	'previous_page',
		-href	=>	$page."#admin_form",
		-title	=>	'Redirect to previous page'
	}, "Riprova");
			
	print <<EOF;
			</div>
		</body>
	</html>
EOF

 	
 }
 
sub createSession() {
	$session = new CGI::Session();
	$session->param('user', $username);
	$session->param('pass', $password);
	return $session;
}
