#!/usr/bin/perl
#!C:/xampp/perl/bin/perl.exe

# ATTENZIONE! IN BASE AL TUO O.S. CAMBIA LE RIGHE QUI SOPRA


getSession(); # Verifico che la sessione ci sia






sub getSession() {
	$sessione = CGI::Session->load() or die $!; #CGI::Session->errstr
	if ($sessione->is_expired || $sessione->is_empty) { # Se manca la sessione torno in home
		print redirect(-url=>'../');
	}
}