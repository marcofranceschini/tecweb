#!/usr/bin/perl

print "Content-Type: text/html\n\n";

read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});

@pairs = split(/&/, $buffer);
foreach $pair (@pairs) {
	
}