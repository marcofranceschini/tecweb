#!/Users/danielef/perl5/perlbrew/perls/perl-5.16.0/bin/perl

use CGI;
use Net::SMTP;
   
$q = CGI->new;
print $q->header();

$mail = '/usr/sbin/sendmail';

$smtp = Net::SMTP->new(
	"smtp.gmail.com",
	Hello => 'smtp.gmail.com',
    Timeout => 2);
	
$smtp->mail('neneabc1@gmail.com');
$smtp->to('neneabc1@gmail.com');
$smtp->data;
$smtp->datasend('From: neneabc1@gmail.com\nTo: neneabc1@gmail.com');
$smtp->dataend;
$smtp->quit;
