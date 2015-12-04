#!/Applications/XAMPP/bin/perl

use Net::SMTP_auth;

$smtp = Net::SMTP_auth->new('smtp.gmail.com');
$smtp->auth('CRAM-MD5', 'dfavaro.guest@gmail.com', 'Bellabella.12');

$smtp->mail($ENV{USER});
$smtp->to('postmaster');

$smtp->data();
$smtp->datasend("To: postmaster\n");
$smtp->datasend("\n");
$smtp->datasend("A simple test message\n");
$smtp->dataend();

$smtp->quit;