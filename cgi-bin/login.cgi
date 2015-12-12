#!/usr/bin/perl
#!C:/xampp/perl/bin/perl.exe

# ATTENZIONE! IN BASE AL TUO O.S. CAMBIA LE RIGHE QUI SOPRA
 
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use CGI::Cookie;
use CGI::Session;
use warnings;

read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});

$username = "";	# Per il popup con user vuoto
$password = "";	# Per il popup con password vuota
@pairs = split(/&/, $buffer);
# Rivedere l'aggiunta della riga $value =~ tr/+/ /; per compatibilità con vecchi browser
@username = split(/=/, @pairs[0]);
$username = @username[1];
@password = split(/=/, @pairs[1]);
$password = @password[1];
 
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
	print $sessione->param('user')."<br>".$sessione->param('pass')."<br>";
	print "Ho fatto??";
	$s = getSession();
	print $s{'pass'};
	
	print redirect(-url => '../pages/admin.html');
	
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
 	#in ogni login form dobbiamo usare un campo hidden con valore il nome della pagine html
	#dove risiede in modo da saper tornarci qui sotto
	print CGI->header;
	print "<h1>Qualcosa &egrave; andato storto :(</h1>";
 	if ($username eq "" and $password eq "") { # Username e password vuoti
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
		-href	=>	'../',
		-title	=>	'Redirect to Home Page'
	}, "Clicca qui per tornare alla Home Page e riprovare");
 }
 
sub createSession() {
	$session = new CGI::Session();
	$session->param('user', $username);
	$session->param('pass', $password);
	return $session;
}
 
sub getSession() {
	$session = CGI::Session->load() or die CGI::Session->errstr;
	if ($session->is_expired || $session->is_empty) {
		print "NON GHE SE NIENTE DA CARICAR";
	} else {
		my %ritorno=('user', $session->param('user'), 'pass', $session->param('pass'));
		return $ritorno;
	}
}