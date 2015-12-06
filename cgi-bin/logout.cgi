#!/usr/bin/perl

#!C:/xampp/perl/bin/perl.exe
 
use CGI;
use CGI:Session;
use warnings;

$session = CGI::Session->load() or die CGI::Session->errstr();
if ( $s->is_expired ) {
	print "oi oi";
}

if ( $s->is_empty ) {
	print "vuota";
}