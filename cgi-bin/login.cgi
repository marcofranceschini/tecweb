#!/usr/bin/perl
#!C:/xampp/perl/bin/perl.exe

# ATTENZIONE! IN BASE AL TUO O.S. CAMBIA LE RIGHE QUI SOPRA
 
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use CGI::Cookie;
use CGI::Session;
use warnings;

my $q = new CGI;
print $q->header;

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
	$prova = createSession();
	print "".$prova->param('user');
	print "Ho fatto??";
	$sessione=getSession();
	print $sessione{'pass'};
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
 	if ($username eq "" and $password eq "") { # Username e password vuoti
		print "	<script>
    				alert(\"Riempi i campi per accedere\");
				</script>";
	} elsif ($username eq "") {	# Username vuoto
		print "	<script>
    				alert(\"Inserisci lo username\");
				</script>";
	} elsif ($password eq "") {	# Password vuota
		print "	<script>
    				alert(\"Inserisci la password\");
				</script>";
	} elsif ($username ne "admin") {	# Username errato
		print "	<script>
    				alert(\"Username errato\");
				</script>";
	} else {	# Password errata
		print "<script>
    				alert(\"Password errata\");
				</script>";
	}

	#Lasciamo temporaneamente perdere, sistemiamo quando facciamo la home in CGI
	print a({
		-href	=>	'../',
		-title	=>	'Redirect to Home Page'
	}, "Home Page");
	#print "<script>location.replace(\"../\")</script>";
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