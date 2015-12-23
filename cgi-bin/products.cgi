#!C:/Perl64/bin/perl.exe
#!/usr/bin/perl




use CGI;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard Vars);
use XML::LibXML;
use warnings;

my $cgi = CGI->new();
my $category = $cgi->param('category');
print $category;

print "Content-Type: text/html\n\n";
print <<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
EOF
print "<title>".$category." - Ju Rapida</title>";
print "<meta name=\"title\" content=\"".$category." - Ju Rapida S.N.C.\" />";
print "<meta name=\"description\" content=\"Pagina dei prodotti nel mondo ".$category."\" di JU RAPIDA />";
print "<meta name=\"keywords\" content=\"".$category.", ju rapida, articoli sportivi, prodotti, sport;\" />";
print <<EOF;
		<meta name="author" content="Fabiano Tavallini, Marco Franceschini, Daniele Favaro" />
		<meta name="copyright" content="Ju Rapida S.N.C." />
		<meta name="viewport" content="width=device-width">
		<link href="../css/style_1024_max.css" rel="stylesheet" type="text/css" />
		<link href="../css/style_768.css" rel="stylesheet" type="text/css" />
		<link href="../css/style_480.css" rel="stylesheet" type="text/css" />
		<link href="../css/style_1024_min.css" rel="stylesheet" type="text/css" />
		<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" />
		<link href='https://fonts.googleapis.com/css?family=Maven+Pro:400,700' rel='stylesheet' type='text/css' />
		<link rel="icon" type="image/png" href="../res/images/icon.png" />
	</head>
	<body>
		<div id="header">
			<div id="contacts">
				<p><i class="material-icons md-18">&#xE0CD;</i> +39 0422 445566</p>
				<p><i class="material-icons md-18">&#xE0BE;</i> jurapida@gmail.com</p>
			</div>
			<div id="navbar">
				<a href="../index.html"><img id="logo" src="../res/images/logo_bianco.png" alt="Logo Ju Rapida" /></a>
				<ul id="menu"> 
					<li><a href="../index.html"><span xml:lang="en">Home</span></a></li>
					<li><span id="current">Prodotti</span></li> <!--Comprese le offerte-->
					<li><a href="../cgi-bin/contacts.cgi">Contatti</a></li>
					<li><a href="about.html">Chi siamo</a></li>
				</ul>
			</div>
			<div id="breadcrumb">
EOF
print "<a href=\"../index.html\"><i class=\"material-icons md-18\" >&#xE88A;</i></a> &gt; <a href=\"../pages/products.html\">Prodotti</a> &gt; ".$category;
print <<EOF;
			</div>
		</div>
				
		<div id="content_products_cgi">
            <div id="products_navigator">
                <!-- selettore di categorie e filtri per i prodotti -->
            </div>
EOF

#lettura da file XML
my $file = '../xml/db.xml';
my $parser = XML::LibXML->new();
$parser->keep_blanks(0);
my $doc = $parser->parse_file($file) or die "Errore nel parsing";
my $radice = $doc->getDocumentElement or die "Errore elemento radice";
#my @prodotti = $radice->getElementsByTagName('product') or die "Errore prodotti\n";
my $query = "/products/product[category=\"".$category."\"]";
my @prodotti = $doc->findnodes($query) or die "<p>Non &egrave; stato possibile reperire la lista dei prodotti</p>";
	
#stampa le card dei prodotti
print "<div id=\"products_displayer\">";
print " <div id=\"products_displayer_frame\">";
for(my $i=0; $i < scalar @prodotti; $i++)
{
    my $codice = $prodotti[$i]->findnodes("code/text()");
    my $nome = $prodotti[$i]->findnodes("name/text()");
    my $categoria = $prodotti[$i]->findnodes("category/text()");
    my $immagine = $prodotti[$i]->findnodes("img/text()");
    my $descrizione = $prodotti[$i]->findnodes("description/text()");
    my $descrizione_corta = $prodotti[$i]->findnodes("shortDescription/text()");
    print "<div class=\"product_card\">";
    print "<div class=\"product_image\">";
    print " <img src=\"../res/images/products/".$immagine."\" alt=\"".$descrizione_corta."\"/>";
    print "</div>";
    print "<span class=\"product_name\">".$nome."</span>";
    print "<span class=\"product_code\">Codice ".$codice."</span>";
    print "<p class=\"product_short_description\">".$descrizione_corta."</p>";
    print
    "<div class=\"product_display_button\">
        <form class=\"form_display\" action=\"product_displayer.cgi\" method=\"post\">
               <input type=\"hidden\" name=\"display\" value=\"".$codice."\" />
               <input class=\"button\" type=\"submit\" value=\"Apri\" />
        </form>
    </div>";
    print "</div>";
}
print " </div>";
print "</div>";
    
print <<EOF;	
		</div>
		
		<div id="footer">
			<div id="footer_top">
				<div id="maps">
					<ul id="maps_menu">
						<li><a href="../index.html"><span xml:lang="en">Home</span></a></li>
						<li><a href="products.html">Prodotti</a></li>
						<li><a href="../cgi-bin/contacts.cgi">Contatti</a></li>
						<li><a href="about.html">Chi siamo</a></li>
					</ul>
					<ul id="maps_categories">
						<li><a href="../cgi-bin/products.cgi?category=Calcio">Calcio</a></li>
						<li><a href="../cgi-bin/products.cgi?category=Basket"><span xml:lang="en">Basket</span></a></li>
						<li><a href="../cgi-bin/products.cgi?category=Volley"><span xml:lang="en">Volley</span></a></li>
						<li><a href="../cgi-bin/products.cgi?category=Tennistavolo">Tennistavolo</a></li>
						<li><a href="../cgi-bin/products.cgi?category=Nuoto">Nuoto</a></li>
						<li><a href="../cgi-bin/products.cgi?category=Minigolf">Minigolf</a></li>
						<li><a href="../cgi-bin/products.cgi?category=Calciobalilla">Calciobalilla</a></li>
						<li><a href="../cgi-bin/products.cgi?category=Protezioni">Protezioni</a></li>
						<li><a href="../cgi-bin/products.cgi?category=Accessori">Accessori</a></li>
					</ul>
				</div>
				<div id="admin_form_panel">
					<form id="admin_form" action="../cgi-bin/login.cgi" method="post">
						<fieldset>
							<legend><i class="material-icons md-18">&#xE853;</i>Area Riservata</legend>
							<label class="form_item" for="username">Username</label>
							<input class="form_item" id="username" type="text" name="username"/>
							<label class="form_item" for="password">Password</label>
							<input class="form_item" id="password" type="password" name="password"/>
							<input type="hidden" name="page" value="../pages/products.html" />
							<input id="submit" type="submit" value="Login" />
						</fieldset>
					</form>
				</div>
			</div>
			<div id="copy_panel">
				<p id="copy">Copyright &copy; 2016 - All right reserved. Ju Rapida SNC - VIA F. PETRARCA, 14/31100 TREVISO ITALY - P. IVA: 01836040269</p>
				<p id="validation">
					<span id="xhtml_valid">
    					<a href="http://validator.w3.org/check?uri=referer"><img src="http://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0 Strict" height="31" width="88" /></a>
  					</span>
					<span id="css_valid">
						<a href="http://jigsaw.w3.org/css-validator/check/referer"><img style="border:0;width:88px;height:31px" src="http://jigsaw.w3.org/css-validator/images/vcss-blue" alt="Valid CSS3" /></a>
					</span>
				</p>
			</div>
		</div>
	</body>
</html>
EOF
