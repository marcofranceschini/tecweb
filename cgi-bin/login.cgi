#!C:/xampp/perl/bin/perl.exe

#!/usr/bin/perl
 
use CGI;
use CGI::Session;
use warnings;

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
	
	my $s = new CGI::Session("driver:File", undef, {Directory=>'/tmp'});
	#my $ses_id = $session->id();
	#print $username;
	#$session = CGI::Session->new();
	    
	#$session = new CGI::Session("driver:File", $cgi, {Directory=>'/tmp'});

	#$s = CGI::Session->new();
    #$s = CGI::Session->new("driver:file", $sid);
    #$s = CGI::Session->new("driver:file", $sid, {Directory=>'/tmp'});
	#my $sid = $cgi->cookie("CGISESSID") || undef;
	#my $s = new CGI::Session(undef, $sid, {Directory=>'/tmp'});

	$s->param('user', $username);
	$s->param('pass', $password);
	print $s->param('user');
	
	#print "GG WP";
	#print "<script>location.replace(\"../pages/admin.html\")</script>";		#attenzione agli slash e al percorso
	#print redirect(-url=>'../pages/admin.html');
	#$url = "../pages/admin.html";
	#open(FILE, $url) || die "errore nella open\n\n";
 } else {
 	print "ERROR";
 }