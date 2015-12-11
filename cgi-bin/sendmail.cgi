#!/Users/danielef/perl5/perlbrew/perls/perl-5.16.0/bin/perl

use CGI;
use Net::SMTP::SSL;
   
$q = CGI->new;
print $q->header();


my $to = 'neneabc1@gmail.com';
my $subject = 'Test subject';
my $body = 'Test body';
my $from = 'dfavaro.guest@gmail.com';
my $password = 'Bellabella.12';

my $smtp;
if (not $smtp = Net::SMTP::SSL->new(
	'smtp.gmail.com',
    Port => 465,
    Debug => 1)) {
   	die "Could not connect to server\n";
}

$smtp->data();
$smtp->datasend("From: " . $from . "\n");
$smtp->datasend("To: " . $to . "\n");
$smtp->datasend("Subject: " . $subject . "\n");
$smtp->datasend("\n");
$smtp->datasend($body . "\n");
$smtp->dataend();
$smtp->quit;

$smtp->auth($from, $password) or die "Authentication failed!\n";
$smtp->mail('dfavaro.guest@gmail.com');
$smtp->to('neneabc1@gmail.com');