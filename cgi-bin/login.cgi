#!C:/xampp/perl/bin/perl.exe
#!/usr/bin/perl


# ATTENZIONE! IN BASE AL TUO O.S. CAMBIA LE RIGHE QUI SOPRA
 
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard Vars);
use CGI::Session;
use warnings;

#print "Content-Type: text/html\n\n";
	
$username = "";	# Per il messaggio con user vuoto
$password = "";	# Per il messaggio con password vuota
$page = "";

my %data = Vars();
$username = $data{"username"};
$password = $data{"password"};
$page = $data{"page"};
 
if ($username eq "admin" && $password eq "admin") {	# Login corretto
	#print "GG WP";
	#$query = new CGI;
	#print $query->redirect('http://www.devdaily.com/');
	#print $query->header(-location => 'http://www.goolge.it');
	
	#$CGI::Session::Driver::file::FileName = "sessione"; # Cambio nome al file contenente la sessione
	#$session = new CGI::Session(undef, {Directory=>'/tmp'});
	
	#$session = new CGI::Session("driver:File", undef, {Directory=>'/tmp'});
	#$session->name("PROVA");
	#$sid = $session->id();
	$sessione = createSession();
	#print $sessione->param('user')."<br>".$sessione->param('pass')."<br />";
	
	
	print $sessione->header(-location=>"admin.cgi");
	
	
	#$s = getSession();
	#print "<br>La password dopo load &egrave; ".$s{'pass'};
	#print redirect(-url => 'admin.cgi');
	
	#print "ID SESSIONE=".$sid;
	
	#$cgi = CGI.new("html4")
	#$prova = CGI::Session.new($cgi,'session_key' => '111');
	#$sid = $prova->id();
	
	#$biscotto = CGI::Cookie->new(-name=>'ID',-value=>$sid);
	#print header(-cookie=>$biscotto);

	#$cookie = $cgi->cookie(CGISESSID => $sid);
	#print $cgi->header( -cookie=>$cookie );
	
	#$session->param('user', $username);
	#$session->param('pass', $password);
	#print "USERNAME=".$session->param('user');

	#print "<script>location.replace(\"../pages/admin.html\")</script>";	# Attenzione agli slash e al percorso
	
	#print redirect(-url=>'../pages/admin.html');
	#$url = "../pages/admin.html";
	#open(FILE, $url) || die "errore nella open\n\n";

 } else {	# Login errato
	#print CGI->header;			#usiamo il nostro header
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
			<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" />
			<link href='https://fonts.googleapis.com/css?family=Maven+Pro:400,700' rel='stylesheet' type='text/css' />
			<link rel="icon" type="image/png" href="res/images/icon.png" />
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
		$page = "../index.html";
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
 
sub getSession() {
	$session = CGI::Session->load() or die CGI::Session->errstr;
	if ($session->is_expired) {
		print "Non c'&egrave; nulla da caricare";
	} else {
		print $session->param('pass');
		#my %ritorno=('user', $session->param('user'), 'pass', $session->param('pass'));
		#print $ritorno{'user'};
		#return $ritorno;
	}
}
