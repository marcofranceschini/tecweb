#!/usr/bin/perl
#!C:/Perl64/bin/perl.exe

# ATTENZIONE! IN BASE AL TUO O.S. CAMBIA LE RIGHE QUI SOPRA

use CGI;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard Vars);
use CGI::Session;
use warnings;

getSession(); # Verifico che la sessione ci sia



sub getSession() {
	$sessione = CGI::Session->load() or die $!; #CGI::Session->errstr
	if ($sessione->is_expired || $sessione->is_empty) { # Se manca la sessione torno in home
		print redirect(-url=>'../');
	}else{
		print "Content-Type: text/html\n\n";
	}
}