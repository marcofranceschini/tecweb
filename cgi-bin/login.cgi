#!/usr/bin/perl

#!C:/xampp/perl/bin/perl.exe
 

 
use CGI;
use warnings;

print "Content-Type: text/html\n\n";
 
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
 
@pairs = split(/&/, $buffer);
@username = split(/=/, @pairs[0]);
$username = @username[1];
@password = split(/=/, @pairs[1]);
$password = @password[1];
 
 if ($username eq "admin" && $password eq "admin") {
	print "GG WP";
	print "<script>location.replace(\"../pages/admin.html\")</script>";		#attenzione agli slash e al percorso
	$query = new CGI;
	#print $query->redirect('http://www.devdaily.com/');
	print $query->header(-location => 'http://www.goolge.it');
	
	
	#print "GG WP";
	#print "<script>location.replace(\"../pages/admin.html\")</script>";		#attenzione agli slash e al percorso
	#print redirect(-url=>'../pages/admin.html');
	#$url = "../pages/admin.html";
	#open(FILE, $url) || die "errore nella open\n\n";
 } else {
 	print "ERROR";
 }