#!/usr/bin/perl
#!C:/xampp/perl/bin/perl.exe


# ATTENZIONE! SE USI WIN SCAMBIA L'ORDINE DELLE RIGHE QUI SOPRA
 
use CGI;
use CGI::Session;
use CGI qw/:standard/;
use CGI::Cookie;
use warnings;

print "Content-Type: text/html\n\n";

#sub destroySession() {
#	$session = CGI::Session->load() or die $!;
#	$SID = $session->id();
#	$session->close();
#	$session->delete();
#	$session->flush();
#}


#$user = getSession('user');
#$biscotto = $cgi->cookie("driver:File") || undef;
#$sid = $biscotto->param('user', $username);

%cookies = CGI::Cookie->fetch;
$id = $cookies{'ID'}->value;
print $id;
$session = CGI::Session->load($id, undef, {Directory=>'/tmp'});


#if ( $s->is_expired ) {
#	print "oi oi";
#}

#if ( $s->is_empty ) {
	#print "vuota";
#}
$password = $session->param('pass');
print $password;

sub getSession($name) {
	$session = CGI::Session->load("driver:File", undef, {Directory=>'/tmp'}) or die $!;
	if ($session->is_expired || $session->is_empty ) {
		return undef;
	} else {
		my $app = $session->param($name);
		return $app;
	}
}
