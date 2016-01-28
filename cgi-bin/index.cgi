#!C:/Perl64/bin/perl.exe
#!/usr/bin/perl
 
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use XML::LibXML;
use warnings;

my $cgi = CGI->new();

print CGI->header;
print <<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<title>Ju Rapida</title>
		<meta name="title" content="Ju Rapida S.N.C." />
		<meta name="description" content="Only Sport Only Quality, JU RAPIDA mette in vendita articoli sportivi di qualit&agrave; dal 1949." />
		<meta name="keywords" content="ju rapida, palloni, articoli sportivi, calcio, tennistavolo, volley, carlo tavallini, vendita;" />
		<meta name="author" content="Fabiano Tavallini, Marco Franceschini, Daniele Favaro" />
		<meta name="copyright" content="Ju Rapida S.N.C." />
		<meta name="viewport" content="width=device-width" />
		<link href="../css/style_1024_max.css" rel="stylesheet" type="text/css" />
		<link href="../css/style_768.css" rel="stylesheet" type="text/css" />
		<link href="../css/style_480.css" rel="stylesheet" type="text/css" />
		<link href="../css/style_1024_min.css" rel="stylesheet" type="text/css" />
   		<link href="../css/style_print.css" rel="stylesheet" type="text/css" />
		<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" type='text/css' />
		<link href='https://fonts.googleapis.com/css?family=Maven+Pro:400,700' rel='stylesheet' type='text/css' />
		<link rel="icon" type="image/png" href="../res/images/icon.png" />
		<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.min.js"></script>
		<script type="text/javascript" src="../js/index.js"></script>
	</head>
	<body>
        <div><a class="skip_menu" href="#firstProduct">Salta la navigazione</a></div>
        <div id="header">
			<div id="contacts">
				<p><i class="material-icons md-18">&#xE0CD;</i> +39 0422 445566</p>
				<p><i class="material-icons md-18">&#xE0BE;</i> jurapida\@gmail.com</p>
			</div>
			<div id="navbar">
				<img id="logo" src="../res/images/logo_bianco.png" alt="Logo Ju Rapida" />
				<ul id="menu">
					<li><span id="current" xml:lang="en">Home</span></li>
					<li><a href="../pages/products.html">Prodotti</a></li>
					<li><a href="contacts.cgi">Contatti</a></li>
					<li id="menu_last"><a href="../pages/about.html">Chi siamo</a></li>
				</ul>
			</div>
            <div id="breadcrumb_home"></div>
		</div>
		
		<div id="content_home">
            <div id="panes">
EOF
$parser = XML::LibXML->new();
my $doc = $parser->parse_file("../xml/db.xml");
my $home_vuota = "true";
my @products = $doc->findnodes('/products/product');
for (my $i = 0; $i < scalar @products; $i++) {
    if ($products[$i]->findnodes('./inEvidence') eq "true") {
        $home_vuota = "false";
        print " <div class=\"pane\" style=\"background-image: url('../res/images/".$products[$i]->findnodes('./backgroundImg')."')\">
                    <div class=\"pane_content\">
                    <img src=\"../res/images/products/thumbnails/".$products[$i]->findnodes('./thumbnail')."\" alt=\"".$products[$i]->findnodes('./shortDescription')."\"/>";
        if ($i == 0) {
            print "         <p><a id=\"firstProduct\" href=\"product_displayer.cgi?display_category=".$products[$i]->findnodes('./category')."&amp;display_code=".$products[$i]->findnodes('./code')."&amp;display_name=".$products[$i]->findnodes('./name')."\">".$products[$i]->findnodes('./shortDescription')."</a></p>";
        } else {
            print "         <p><a href=\"product_displayer.cgi?display_category=".$products[$i]->findnodes('./category')."&amp;display_code=".$products[$i]->findnodes('./code')."&amp;display_name=".$products[$i]->findnodes('./name')."\">".$products[$i]->findnodes('./shortDescription')."</a></p>";
        }
        print " </div>
                </div>";
    }
}
print "     </div>";
if($home_vuota eq "true") {
    print <<EOF;
            <div id="home_placeholder">
                <div id="welcome_message">
                    <p id="welcome_title">Benvenuto in <span class="ju_rapida">Ju Rapida</span></p>
                    <p>Qui puoi trovare subito i prodotti che stai cercando!</p>
                    <p>Inizia subito un tour</p>
                    <a href="../pages/products.html">Vai ai prodotti</a>
                </div>
            </div>
EOF
} else {
    print <<EOF;
            <a id="backTop" href="#header">
				<i class="material-icons">&#xE316;</i>
                Torna in alto alla pagina
				<i class="material-icons">&#xE316;</i>
			</a>
EOF
}
print <<EOF;
		</div>

		<div id="footer">
			<div id="footer_top">
				<div id="maps">
					<ul id="maps_menu">
						<li><span xml:lang="en">Home</span></li>
						<li><a href="../pages/products.html">Prodotti</a></li>
						<li><a href="contacts.cgi">Contatti</a></li>
						<li><a href="../pages/about.html">Chi siamo</a></li>
					</ul>
					<ul id="maps_categories">
						<li><a href="products.cgi?category=Calcio">Calcio</a></li>
						<li><a href="products.cgi?category=Basket"><span xml:lang="en">Basket</span></a></li>
						<li><a href="products.cgi?category=Volley"><span xml:lang="en">Volley</span></a></li>
						<li><a href="products.cgi?category=Tennistavolo">Tennistavolo</a></li>
						<li><a href="products.cgi?category=Nuoto">Nuoto</a></li>
						<li><a href="products.cgi?category=Minigolf">Minigolf</a></li>
						<li><a href="products.cgi?category=Calciobalilla">Calciobalilla</a></li>
						<li><a href="products.cgi?category=Protezioni">Protezioni</a></li>
						<li><a href="products.cgi?category=Accessori">Accessori</a></li>
					</ul>
				</div>
				<div id="admin_form_panel">
					<!-- Da usare in lab:   ../cgi-bin/login.cgi-->
					<form id="admin_form" action="login.cgi" method="post">
						<fieldset>
							<legend><i class="material-icons md-18">&#xE853;</i>Area Riservata</legend>
							<label class="form_item" for="username">Username</label>
							<input class="form_item" id="username" type="text" name="username"/>
							<label class="form_item" for="password">Password</label>
							<input class="form_item" id="password" type="password" name="password"/>
							<input type="hidden" name="page" value="index.cgi" />
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
