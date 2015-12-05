#!/usr/bin/perl

#!C:/xampp/perl/bin/perl.exe
 
use CGI;
use warnings;

#sub createSession($name, $value) {
#	$session = new CGI::Session();
#	$session->param($name, $value);
#	print $session->header(-location=>"$base");
#}

#sub getSession($name) {
#	$session = CGI::Session->load() or die $!;
#	if ($session->is_expired || $session->is_empty ) {
#		return undef;
#	} else {
#		my $app = $session->param($name);
#		return $app;
#	}
#}

#sub destroySession() {
#	$session = CGI::Session->load() or die $!;
#	$SID = $session->id();
#	$session->close();
#	$session->delete();
#	$session->flush();
#}

print "Content-Type: text/html\n\n";
 
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
 
@pairs = split(/&/, $buffer);
@username = split(/=/, @pairs[0]);
$username = @username[1];
@password = split(/=/, @pairs[1]);
$password = @password[1];
 
 if ($username eq "admin" && $password eq "admin") {
	#print "GG WP";
	#print "<script>location.replace(\"../pages/admin.html\")</script>";		#attenzione agli slash e al percorso
	#$query = new CGI;
	#print $query->redirect('http://www.devdaily.com/');
	#print $query->header(-location => 'http://www.goolge.it');
	
	#my $session = new CGI::Session("driver:File", undef, {Directory=>'/tmp'});
	#my $ses_id = $session->id();
	print $username;
	$session = CGI::Session->new();
	$session->param('user', ''+$username);
	$session->param('pass', ''+$password);
	print ""+$session->param('user');



	
	#$page = new CGI;
	#$nome_utente = $page->param('user', $username),
	#createSession('user', $username);
	#$page = new CGI;
	#ricava il contenuto del widget ‘utente’
	#$nome_utente = $page->param('pass', $password),
	#createSession('pass', $password);
	
	#print "GG WP";
	#print "<script>location.replace(\"../pages/admin.html\")</script>";		#attenzione agli slash e al percorso
	#print redirect(-url=>'../pages/admin.html');
	#$url = "../pages/admin.html";
	#open(FILE, $url) || die "errore nella open\n\n";
 } else {
 	print "ERROR";
 }