#!/usr/bin/perl
use strict;
use warnings;
use Encode;
use CGI ":standard";
use HTML::Entities;

sub createSession() { # Per creare una sessione
$session = new CGI::Session();
$session->param('user', $user);
$session->param('psw', $psw);
#print $session->header(-location=>"$base");
}

my $cgi = CGI->new(); # Create new CGI object
my $user = $cgi->param('username');
my $psw = $cgi->param('password');
#$user=form.getvalue("username");
#$psw=form.getvalue("password");
if($user=="admin" && $psw=="admin") {
	createSession();
	open(INF,"../pages/admin.html");
}
