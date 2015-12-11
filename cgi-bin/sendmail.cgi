#!/usr/bin/perl

use CGI;
use CGI::Session;
use Net::SMTP;

$q = CGI->new;
print $q->header();

$from = "";
$subject = "Request info from ";
$body = "";

use CGI qw(:standard Vars);
my %data = Vars();

$from = $data{"name"};
$subject = $data{"mail"};
$body = $data{"mex"};

if ($from ne '' && $subject ne '' && $body ne '') {
    my $mailer = new Net::SMTP(
        'mail.smtp2go.com',
        Hello	=>	'mail.smtp2go.com',
        Port    =>  2525,
        User    =>  'neneabc1@gmail.com',
        Password=>  'bellabella.12');
	
    $mailer->mail($from);
    $mailer->to('neneabc1@gmail.com');
    $mailer->data;
    $mailer->datasend("Sent from perl! Fuck yeah!");
    $mailer->dataend;
    $mailer->quit;
    
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