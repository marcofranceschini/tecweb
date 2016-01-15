#!/usr/bin/perl
#!C:/Perl64/bin/perl.exe

use CGI;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard Vars);
use XML::LibXML;
use warnings;

my $cgi = CGI->new();
my $codice = $cgi->param('display_code');
my $nome = $cgi->param('display_name');
my $categoria = $cgi->param('display_category');

# Lettura da file XML
my $file = '../xml/db.xml';
my $parser = XML::LibXML->new();
$parser->keep_blanks(0);
my $doc = $parser->parse_file($file) or die "Errore nel parsing";
my $radice = $doc->getDocumentElement or die "Errore elemento radice";
my $query = "/products/product[code=\"".$codice."\"]";
my $prodotto = $doc->findnodes($query)->get_node(1);
if (!$prodotto) {
    print redirect(-url=>'../pages/products.html'); 
}
print CGI->header;
print <<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
EOF
print "<title>".$nome." - ".$categoria." - Ju Rapida</title>";
print "<meta name=\"title\" content=\"".$nome." - ".$categoria." - Ju Rapida S.N.C.\" />";
print "<meta name=\"description\" content=\"Pagina descrittiva del prodotto ".$nome." del mondo ".$categoria."\" di JU RAPIDA />";
print "<meta name=\"keywords\" content=\"".$nome.", ".$categoria.", ".$codice.", ju rapida, articoli sportivi, prodotti, sport;\" />";
print <<EOF;
		<meta name="author" content="Fabiano Tavallini, Marco Franceschini, Daniele Favaro" />
		<meta name="copyright" content="Ju Rapida S.N.C." />
		<meta name="viewport" content="width=device-width">
		<link href="../css/style_1024_max.css" rel="stylesheet" type="text/css" />
		<link href="../css/style_768.css" rel="stylesheet" type="text/css" />
		<link href="../css/style_480.css" rel="stylesheet" type="text/css" />
		<link href="../css/style_1024_min.css" rel="stylesheet" type="text/css" />
        <link href="../css/style_print.css" rel="stylesheet" type="text/css" />
		<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" />
		<link href='https://fonts.googleapis.com/css?family=Maven+Pro:400,700' rel='stylesheet' type='text/css' />
		<link rel="icon" type="image/png" href="../res/images/icon.png" />
	</head>
	<body>
        <a class="skip_menu" href="#content_products_displayer_cgi" tabindex="1">Salta la navigazione</a> 
		<div id="header">
			<div id="contacts">
				<p><i class="material-icons md-18">&#xE0CD;</i> +39 0422 445566</p>
				<p><i class="material-icons md-18">&#xE0BE;</i> jurapida@gmail.com</p>
			</div>
			<div id="navbar">
				<a href="index.cgi" tabindex=\"2\"><img id="logo" src="../res/images/logo_bianco.png" alt="Logo Ju Rapida" /></a>
				<ul id="menu"> 
					<li><a href="index.cgi" tabindex=\"3\"><span xml:lang="en">Home</span></a></li>
					<li><a href="../pages/products.html" tabindex=\"4\">Prodotti</a></li>
					<li><a href="../cgi-bin/contacts.cgi" tabindex=\"5\">Contatti</a></li>
					<li><a href="../pages/about.html" tabindex=\"6\">Chi siamo</a></li>
				</ul>
			</div>
			<div id="breadcrumb">
EOF
print "				<a href=\"index.cgi\" tabindex=\"7\"><i class=\"material-icons md-18\" >&#xE88A;</i></a> &gt; <a href=\"../pages/products.html\" tabindex=\"8\">Prodotti</a> &gt; <a href=\"products.cgi?category=".$categoria."\" tabindex=\"9\">".$categoria."</a> &gt; ".$nome."\n";
print "				<a href=\"../cgi-bin/index.cgi\"><img src=\"../res/images/ic_home.png\" alt=\"Home page\"</img></a> &gt; <a href=\"../pages/products.html\">Prodotti</a> &gt; <a href=\"products.cgi?category=".$categoria."\">".$categoria."</a> &gt; ".$nome."\n";
print <<EOF;
			</div>
		</div>
				
		<div id="content_products_displayer_cgi">
EOF

# Stampa la scheda del prodotto
print "		<div id=\"product_card_displayer\">\n";
my $immagine = $prodotto->findnodes("img/text()");
my $descrizione = $prodotto->findnodes("description/text()");
print "			<div class=\"product_card\">\n";
print "				<div class=\"product_image\">\n";
print "					<img src=\"../res/images/products/".$immagine."\" alt=\"".$descrizione_corta."\"/>\n";
print "				</div>\n";
print "				<div class=\"product_data\">\n";
print "		      		<span class=\"product_name\">".$nome."</span>\n";
print "			      	<span class=\"product_code\">Codice ".$codice."</span>\n";
print "		           	<p class=\"product_description\">".$descrizione."</p>\n";
print "                 <div class=\"product_back_button\">
                            <form action=\"products.cgi?\" method=\"post\">
                                <input type=\"hidden\" name=\"category\" value=\"".$categoria."\" />
                                <input class=\"button\" type=\"submit\" value=\"Torna ai prodotti\" tabindex=\"1\" />
                            </form>
                        </div>\n";
print "		       </div>\n";  
print "         </div>\n";
print "     </div>\n";
    
print <<EOF;	
		</div>
		
		<div id="footer">
			<div id="footer_top">
				<div id="maps">
					<ul id="maps_menu">
						<li><a href="index.cgi" tabindex=\"10\"><span xml:lang="en">Home</span></a></li>
						<li><a href="products.html" tabindex=\"11\">Prodotti</a></li>                        
						<li><a href="contacts.cgi" tabindex=\"12\">Contatti</a></li>
						<li><a href="about.html" tabindex=\"13\">Chi siamo</a></li>
						<li><a href="../cgi-bin/index.cgi"><span xml:lang="en">Home</span></a></li>
						<li><a href="../pages/products.html">Prodotti</a></li>                        
						<li><a href="../cgi-bin/contacts.cgi">Contatti</a></li>
						<li><a href="about.html">Chi siamo</a></li>
					</ul>
					<ul id="maps_categories">
						<li><a href="products.cgi?category=Calcio" tabindex=\"14\">Calcio</a></li>
						<li><a href="products.cgi?category=Basket" tabindex=\"15\"><span xml:lang="en">Basket</span></a></li>
						<li><a href="products.cgi?category=Volley" tabindex=\"16\"><span xml:lang="en">Volley</span></a></li>
						<li><a href="products.cgi?category=Tennistavolo" tabindex=\"17\">Tennistavolo</a></li>
						<li><a href="products.cgi?category=Nuoto" tabindex=\"18\">Nuoto</a></li>
						<li><a href="products.cgi?category=Minigolf" tabindex=\"19\">Minigolf</a></li>
						<li><a href="products.cgi?category=Calciobalilla" tabindex=\"20\">Calciobalilla</a></li>
						<li><a href="products.cgi?category=Protezioni" tabindex=\"21\">Protezioni</a></li>
						<li><a href="products.cgi?category=Accessori" tabindex=\"22\">Accessori</a></li>
					</ul>
				</div>
				<div id="admin_form_panel">
					<form id="admin_form" action="login.cgi" method="post">
						<fieldset>
							<legend><i class="material-icons md-18">&#xE853;</i>Area Riservata</legend>
							<label class="form_item" for="username">Username</label>
							<input class="form_item" id="username" type="text" name="username" tabindex=\"23\" />
							<label class="form_item" for="password">Password</label>
							<input class="form_item" id="password" type="password" name="password" tabindex=\"24\" />
							<input type="hidden" name="page" value="../cgi-bin/index.cgi" />
							<input id="submit" type="submit" value="Login" tabindex=\"25\" />
						</fieldset>
					</form>
				</div>
			</div>
			<div id="copy_panel">
				<p id="copy">Copyright &copy; 2016 - All right reserved. Ju Rapida SNC - VIA F. PETRARCA, 14/31100 TREVISO ITALY - P. IVA: 01836040269</p>
				<p id="validation">
					<span id="xhtml_valid">
    					<a href="http://validator.w3.org/check?uri=referer" tabindex=\"26\"><img src="http://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0 Strict" height="31" width="88" /></a>
  					</span>
					<span id="css_valid">
						<a href="http://jigsaw.w3.org/css-validator/check/referer" tabindex=\"27\"><img style="border:0;width:88px;height:31px" src="http://jigsaw.w3.org/css-validator/images/vcss-blue" alt="Valid CSS3" /></a>
					</span>
				</p>
			</div>
		</div>
	</body>
</html>
EOF
