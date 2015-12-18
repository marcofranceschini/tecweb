#!/usr/bin/perl
#!C:/xampp/perl/bin/perl.exe



# ATTENZIONE! IN BASE AL TUO O.S. CAMBIA LE RIGHE QUI SOPRA

use CGI;
use CGI::Carp qw(fatalsToBrowser);	# Show errors in browser
use CGI::Session;
use CGI qw/:standard/;
use warnings;


destroySession(); 
print redirect(-url=>'../');

sub destroySession() {
	$session = CGI::Session->load() or die $!;
	$SID = $session->id();
	$session->close();
	$session->delete();
	$session->flush();
}
