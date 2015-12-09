#!/usr/bin/perl
#!C:/xampp/perl/bin/perl.exe


# ATTENZIONE! SE USI WIN SCAMBIA L'ORDINE DELLE RIGHE QUI SOPRA
 
use CGI;
use CGI::Session;
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
my $biscotto = $cgi->cookie("MY_SID") || undef;
#$session    = new CGI::Session("driver:File", $sid, {Directory=>'/tmp'});
$session = CGI::Session->load("driver:File", $cgi, {Directory=>'/tmp'});

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