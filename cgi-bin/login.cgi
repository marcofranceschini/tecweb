#!/usr/bin/perl

print "Content-Type: text/html\n\n";

read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});

print $buffer;

@pairs = split(/&/, $buffer);
@username = split(/=/, @pairs[0]);
$username = @username[1];
@password = split(/=/, @pairs[1]);
$password = @password[1];

print "<br>".$username."<br>".$password;