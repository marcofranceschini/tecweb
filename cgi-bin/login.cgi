#!/usr/bin/perl

print "Content-Type: text/html\n\n";

read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});

print $buffer;

@pairs = split(/&/, $buffer);
foreach $pair (@pairs) {
	($username, $password) = split(/=/, $pair);
	print $username." ".$password;
}