#!C:/Perl64/bin/perl.exe
#!/usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard Vars);
use CGI::Session;
use warnings;
use HTTP::BrowserDetect;
use XML::LibXML;

#Da usare il lab
#<link href="../tecwebproject/css/style_1024_max.css" rel="stylesheet" type="text/css" />
#<link href="../tecwebproject/css/style_768.css" rel="stylesheet" type="text/css" />
#<link href="../tecwebproject/css/style_480.css" rel="stylesheet" type="text/css" />
#<link href="../tecwebproject/css/style_1024_min.css" rel="stylesheet" type="text/css" />

my $tabIndexCount = 0;
sub tabindex {
    $tabIndexCount++;
    return (\$tabIndexCount); #ritorna il RIFERIMENTO alla variabile
}

sub getSession() {
	$sessione = CGI::Session->load() or die $!; #CGI::Session->errstr
	if ($sessione->is_expired || $sessione->is_empty) { # Se manca la sessione torno in home
		print redirect(-url=>'../');
	} else {
		print $sessione->param('pass');
		return $sessione;
	}
}

sub destroySession() {
	$session = CGI::Session->load() or die $!;
	#$SID = $session->id();
	$session->close() or die "errore close";
	$session->delete() or die "errore delete";
	$session->flush() or die "errore flush";
	print redirect(-url=>'../cgi-bin/index.cgi'); # Torno in home
}
	
my $session = getSession(); # Verifico che la sessione ci sia

my $cgi = CGI->new();

if (defined $cgi->param('tabindex') && $cgi->param('tabindex') ne '') {
    $tabIndexCount = $tabIndexCount - $cgi->param('tabindex');
}

my $app = $cgi->param('logout');
if ($app) { # LOGOUT - E' stato premuto il link per uscire
	destroySession();
} else {
	print "Content-Type: text/html\n\n";
	print <<EOF;
		<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
		<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
			<head>
				<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
				<title>Amministrazione - Ju Rapida</title>
				<meta name="title" content="Ju Rapida S.N.C." />
				<meta name="description" content="Pagina di amministrazione del sito Ju Rapida." />
				<meta name="author" content="Fabiano Tavallini, Marco Franceschini, Daniele Favaro" />
				<meta name="copyright" content="Ju Rapida S.N.C." />
				<meta name="viewport" content="width=device-width" />
				<link href="../css/style_1024_max.css" rel="stylesheet" type="text/css" />
				<link href="../css/style_768.css" rel="stylesheet" type="text/css" />
				<link href="../css/style_480.css" rel="stylesheet" type="text/css" />
				<link href="../css/style_1024_min.css" rel="stylesheet" type="text/css" />
                <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" type='text/css' />
				<link href='https://fonts.googleapis.com/css?family=Maven+Pro:400,700' rel='stylesheet' type='text/css' />
				<link rel="icon" type="image/png" href="../res/images/icon.png" />
			</head>
			<body>
EOF
    if ($cgi->param('compatibilityRead') ne "read") {
        my $bd = new HTTP::BrowserDetect($cgi->user_agent());
        my $browserName = $bd->browser_string();
        my $browserVersion = $bd->public_version();
        print $browserName." ".$browserVersion;
        if (($browserName eq "Chrome" && $browserVersion < 45) ||       #Verificato
        ($browserName eq "Safari" && $browserVersion < 9) ||            #Verificato
        ($browserName eq "IE" && $browserVersion < 9) ||                
        ($browserName eq "Firefox" && $browserVersion < 42) ||          #Verificato
        ($browserName eq "Opera" && $browserVersion < 34) ||            #Verificato
        ($browserName eq "iOsSafari" && $browserVersion < 8.4)) {
            print " <div id=\"compatibilityAlert\">
                        <form method=\"post\" action=\"admin.cgi\">
                            <p><span>Attenzione!</span> Il tuo browser non supporta pienamente le funzioni di questa pagina. Aggiornalo subito all'ultima versione per non avere problemi durante la navigazione.</p>
                            <input type=\"hidden\" name=\"compatibilityRead\" value=\"read\"/>  
                            <input tabindex=\"${tabindex()}\" type=\"submit\" class=\"button\" value=\"Ho capito\"/>
                    </div>";
        }
    }
     
    print <<EOF;
				<div id="header" class="fadeInDown">
					<div id="navbar_admin">
						<a tabindex="${tabindex()}" id="admin_back_icon" href="../cgi-bin/admin.cgi?logout=1"><img src="../res/images/ic_home.png" alt="Torna al sito"</img></a>
						<p><a tabindex="${tabindex()}" id="admin_back" href="../cgi-bin/admin.cgi?logout=1">Torna al sito</a></p>
						<p>Area Amministrativa</p>
					</div>
				</div>
				
				<div id="content_admin">
					<p>Benvenuti nell'amministrazione del sito, selezionare una delle seguenti opzioni per gestire novit&agrave; e prodotti.</p>
					<div id="admin_panel">
						<a tabindex="${tabindex()}" id="news" class="linked_box fadeInLeft" href="admin_news.cgi"><span class="admin_label">Novit&agrave;</span></a>	
						<a tabindex="${tabindex()}" id="products" class="linked_box fadeInRight" href="admin_products.cgi"><span class="admin_label">Prodotti</span></a>
					</div>
EOF
    
    #Verifica XML prodotti tramite XSD
    my $parser = XML::LibXML->new;
    my $schema = XML::LibXML::Schema->new(location => "../xml/db_schema.xsd");
    my $doc = $parser->parse_file("../xml/db.xml");
    my $result = eval { $schema->validate($doc); };
    if (defined $result) {
        print "<span id=\"info_msg\" class=\"admin_message\">Database XML prodotti valido =D</span>";
    } else {
        print "<span id=\"error_msg\" class=\"admin_message\">Database XML prodotti non valido =(</span>";
    }
    
    #Verifica XML admin tramite XSD
    $schema = XML::LibXML::Schema->new(location => "../xml/admin_db_schema.xsd");
    $doc = $parser->parse_file("../xml/admin_db.xml");
    $result = eval { $schema->validate($doc); };
    if (defined $result) {
        print "<span id=\"info_msg\" class=\"admin_message\">Database XML amministratori valido =D</span>";
    } else {
        print "<span id=\"error_msg\" class=\"admin_message\">Database XML amministratori non valido =(</span>";
    }
    
    print <<EOF;
				</div>
						
				<div id="footer">
					<div id="copy_panel">
						<p id="copy">Copyright &copy; 2016 - All right reserved. Ju Rapida SNC - VIA F. PETRARCA, 14/31100 TREVISO ITALY - P. IVA: 01836040269</p>
						<p id="validation">
							<span id="xhtml_valid">
								<a tabindex="${tabindex()}" href="http://validator.w3.org/check?uri=referer"><img src="http://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0 Strict" height="31" width="88" /></a>
							</span>
							<span id="css_valid">
								<a tabindex="${tabindex()}" href="http://jigsaw.w3.org/css-validator/check/referer"><img style="border:0;width:88px;height:31px" src="http://jigsaw.w3.org/css-validator/images/vcss-blue" alt="Valid CSS3" /></a>
							</span>
						</p>
					</div>
				</div>
			</body>
		</html>
EOF
}
