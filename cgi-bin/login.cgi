#!C:/xampp/perl/bin/perl.exe

#!/usr/bin/perl

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
} else {
	print "ERROR";
}