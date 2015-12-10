#!C:/xampp/perl/bin/perl.exe
#!/usr/bin/perl
#!/Users/danielef/perl5/perlbrew/perls/perl-5.16.0/bin/perl


# ATTENZIONE! IN BASE AL TUO O.S. CAMBIA LE RIGHE QUI SOPRA
 
use CGI;
use CGI::Carp qw(fatalsToBrowser); # show errors in browser
use CGI qw/:standard/;
use CGI::Cookie;
use CGI::Session;

use CGI::Session::Driver::file;

use warnings;

print "Content-Type: text/html\n\n";
 
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
 
@pairs = split(/&/, $buffer);
# Rivedere l'aggiunta della riga $value =~ tr/+/ /; per compatibilità con vecchi browser
@username = split(/=/, @pairs[0]);
$username = @username[1];
@password = split(/=/, @pairs[1]);
$password = @password[1];
 

if ($username eq "admin" && $password eq "admin") {
	#print "GG WP";
	#$query = new CGI;
	#print $query->redirect('http://www.devdaily.com/');
	#print $query->header(-location => 'http://www.goolge.it');
	
	$CGI::Session::Driver::file::FileName = "sessione"; # Cambio nome al file contenente la sessione
	#$session = new CGI::Session(undef, {Directory=>'/tmp'});
	
	$session = new CGI::Session("driver:File", undef, {Directory=>'/tmp'});
	$session->name("PROVA");
	$sid = $session->id();
	print "ID SESSIONE=".$sid;
	
	$cgi = CGI.new("html4")
	$prova = CGI::Session.new($cgi,'session_key' => '111');
	$sid = $prova->id();
	
	$biscotto = CGI::Cookie->new(-name=>'ID',-value=>$sid);
	#print header(-cookie=>$biscotto);

	#$cookie = $cgi->cookie(CGISESSID => $sid);
    #print $cgi->header( -cookie=>$cookie );
	
	$session->param('user', $username);
	$session->param('pass', $password);
	print "".$session->param('user');
	#$session->flush(); 

	#print "<script>location.replace(\"../pages/admin.html\")</script>";	#attenzione agli slash e al percorso
	
	#print redirect(-url=>'../pages/admin.html');
	#$url = "../pages/admin.html";
	#open(FILE, $url) || die "errore nella open\n\n";
 } else {
 	print "ERROR";
 }
