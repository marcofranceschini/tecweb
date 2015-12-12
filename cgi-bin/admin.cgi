#!/usr/bin/perl
#!C:/xampp/perl/bin/perl.exe

use CGI;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use CGI::Cookie;
use CGI::Session;
use warnings;

print CGI->header;

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
	$sessione = createSession();
	
	#stampa admin.html	
	

} else {	# Login errato
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