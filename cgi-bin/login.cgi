#!/usr/bin/perl
#!C:/xampp/perl/bin/perl.exe


# ATTENZIONE! SE USI WIN SCAMBIA L'ORDINE DELLE RIGHE QUI SOPRA
 
use CGI;
use CGI qw/:standard/;
use CGI::Cookie;
use CGI::Session;
use warnings;

print "Content-Type: text/html\n\n";
 
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
 
@pairs = split(/&/, $buffer);
@username = split(/=/, @pairs[0]);
$username = @username[1];
@password = split(/=/, @pairs[1]);
$password = @password[1];
 

if ($username eq "admin" && $password eq "admin") {
	#print "GG WP";
	#$query = new CGI;
	#print $query->redirect('http://www.devdaily.com/');
	#print $query->header(-location => 'http://www.goolge.it');
	
	$session = new CGI::Session("driver:File", undef, {Directory=>'/tmp'});
	$session->name("PROVA");
	$sid = $session->id();
	print $sid;
	$biscotto = CGI::Cookie->new(-name=>'ID',-value=>$sid);
	print header(-cookie=>$biscotto);

	#$cookie = $cgi->cookie(CGISESSID => $sid);
    	#print $cgi->header( -cookie=>$cookie );
	
	$session->param('user', $username);
	$session->param('pass', $password);
	$session->flush(); 

	#print "<script>location.replace(\"../pages/admin.html\")</script>";	#attenzione agli slash e al percorso
	
	#print redirect(-url=>'../pages/admin.html');
	#$url = "../pages/admin.html";
	#open(FILE, $url) || die "errore nella open\n\n";
 } else {
 	print "ERROR";
 }
