#!C:/xampp/perl/bin/perl.exe
#!/usr/bin/perl


# ATTENZIONE! IN BASE AL TUO O.S. CAMBIA LE RIGHE QUI SOPRA

use CGI;
use CGI::Carp qw(fatalsToBrowser);	# Show errors in browser
use CGI::Session;
use CGI qw/:standard/;
use CGI::Cookie;
use warnings;

print "Content-Type: text/html\n\n";

#$user = getSession('user');
#$biscotto = $cgi->cookie("driver:File") || undef;
#$sid = $biscotto->param('user', $username);

#%cookies = CGI::Cookie->fetch;
#$id = $cookies{'ID'}->value;
#print $id;
#$session = CGI::Session->load($id, undef, {Directory=>'/tmp'});

#$CGI::Session::Driver::file::FileName = "sessione"; # Cambio nome al file contenente la sessione
#$session = CGI::Session->load("driver:File", undef, {Directory=>'/tmp'});
#$sid = $session->id();
#print "ID SESSIONE=".$sid;


#if ( $s->is_expired ) {
#	print "oi oi";
#}

#if ( $s->is_empty ) {
	#print "vuota";
#}
#$password = $session->param('pass');

$sessione=getSession();
print $sessione{'pass'};

#$session->flush(); 

sub getSession() {
	$session = CGI::Session->load() or die $!; #CGI::Session->errstr
	if ($session->is_expired) { # Entra nell'if con la condizione is_empty
		print "expired";
	} elsif ($session->is_empty) {
		print "empty";
	} else {
		print $session->param('pass');
	}
}

sub destroySession() {
	$session = CGI::Session->load() or die $!;
	$SID = $session->id();
	$session->close();
	$session->delete();
	$session->flush();
}