#!C:/xampp/perl/bin/perl.exe
#!/usr/bin/perl


# ATTENZIONE! SE USI WIN SCAMBIA L'ORDINE DELLE RIGHE QUI SOPRA
 
use CGI;
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
	print "<script>location.replace(\"../pages/admin.html\")</script>";		#attenzione agli slash e al percorso
	#$query = new CGI;

	#print $query->redirect('http://www.devdaily.com/');
	#print $query->header(-location => 'http://www.goolge.it');
	
	my $session = new CGI::Session("driver:File", undef, {Directory=>'/tmp'});
	$session->param('user', $username);
	$session->param('pass', $password);
	print $s->param('user');
	
	#print redirect(-url=>'../pages/admin.html');
	#$url = "../pages/admin.html";
	#open(FILE, $url) || die "errore nella open\n\n";
 } else {
 	print "ERROR";
 }