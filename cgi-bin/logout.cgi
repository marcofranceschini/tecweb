#!/usr/bin/perl
#!C:/xampp/perl/bin/perl.exe



# ATTENZIONE! IN BASE AL TUO O.S. CAMBIA LE RIGHE QUI SOPRA

use CGI;
use CGI::Carp qw(fatalsToBrowser);	# Show errors in browser
use CGI::Session;
use CGI qw/:standard/;
use warnings;


my $sessione = destroySession(); 
print redirect(-url=>'../');

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