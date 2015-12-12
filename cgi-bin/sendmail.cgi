#!/usr/bin/perl

use CGI;
use CGI::Session;
use Net::SMTP;
use CGI qw(:standard Vars);

$q = CGI->new;
print $q->header();

$from = "";
$subject = "";
$body = "";

my %data = Vars();

$from = $data{"name"};
$subject = $data{"mail"};
$body = $data{"mex"};

if ($from ne '' && $subject ne '' && $body ne '') {
    my $smtp = Net::SMTP->new(
        'mail.smtp2go.com',
        Hello	=>	'mail.smtp2go.com',
        Port    =>  2525,
        Timeout =>  10,
        User    =>  'neneabc1@gmail.com',
        Password=>  'bellabella.12') or die;
	
    $smtp->mail($from);
    $smtp->to('neneabc1@gmail.com');
    $smtp->data;
    $smtp->datasend("Sent from perl! Fuck yeah!");
    $smtp->dataend;
    $smtp->quit;
    
    #Verificare con or die
    print " <script>
    			alert(\"Grazie! Verrai contatto al piu' presto!\");
			</script>";
    print " <script>location.replace(\"../pages/contacts.html\")</script>";
} else {
    print " <script>
    			alert(\"Compila tutti i campi correttamente!\");
			</script>";
    print " <script>location.replace(\"../pages/contacts.html\")</script>";
}