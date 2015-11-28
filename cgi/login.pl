#!/usr/bin/perl
use strict;
use warnings;
use Encode;
use CGI ":standard";
use HTML::Entities;


my $cgi = CGI->new(); # create new CGI object
my $user = $cgi->param('username');
my $psw = $cgi->param('password');
#$user=form.getvalue("username");
#$psw=form.getvalue("password");
if($user=="admin" && $psw=="admin") {
	open(INF,"../pages/admin.html");
}
