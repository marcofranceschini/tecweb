#!/usr/bin/perl

#!C:/xampp/perl/bin/perl.exe

#use warnings;

#my $filename = "../pages/admin.html";  #whatever
#system("start file://$filename");

#$file = "filehandle";
#$FileName = "../pages/admin.html";
#open(file, $FileName) or die "cannot open < input.txt: $!";

#use CGI;
#$query=../pages/admin.html;
#print $query->redirect('../pages/admin.html'); #deve essere la prima cosa che si stampa altrimenti non funziona


read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});

@pairs = split(/&/, $buffer);
@username = split(/=/, @pairs[0]);
$username = @username[1];
@password = split(/=/, @pairs[1]);
$password = @password[1];

if ($username eq "admin" && $password eq "admin") {
	print "GG WP";
	#print "<script>location.replace(\"../pages/admin.html\")</script>";	
		#attenzione agli slash e al percorso
}else{
	print "ERROR";
}