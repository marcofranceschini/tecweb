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
print <<EOF;
		<meta name="title" content="Prodotti - Ju Rapida S.N.C." />
		<meta name="description" content="Vendiamo una vasta gamma di articoli per ogni genere sportivo" />
		<meta name="keywords" content="ju rapida, articoli sportivi, prodotti, sport;" />
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
				
		<div id="content_products">
			<ul id="categories" class="fadeInDown">
				<li><a id="cat_calcio" class="linked_box" href="../cgi-bin/products.cgi?category=calcio"><span class="cat_label">Calcio</span></a></li>	<!-- Compresi parastinchi -->
				<li><a id="cat_basket" class="linked_box" href="../cgi-bin/products.cgi?category=basket"><span class="cat_label">Basket</span></a></li>
				<li><a id="cat_volley" class="linked_box" href="../cgi-bin/products.cgi?category=volley"><span class="cat_label">Volley</span></a></li>
				<li><a id="cat_tennistavolo" class="linked_box" href="../cgi-bin/products.cgi?category=tennistavolo"><span class="cat_label">Tennistavolo</span></a></li>
				<li><a id="cat_nuoto" class="linked_box" href="../cgi-bin/products.cgi?category=nuoto"><span class="cat_label">Nuoto</span></a></li>
				<li><a id="cat_minigolf" class="linked_box" href="../cgi-bin/products.cgi?category=minigolf"><span class="cat_label">Minigolf</span></a></li>
				<li><a id="cat_calciobalilla" class="linked_box" href="../cgi-bin/products.cgi?category=calciobalilla"><span class="cat_label">Calciobalilla</span></a></li>
				<li><a id="cat_protezioni" class="linked_box" href="../cgi-bin/products.cgi?category=protezioni"><span class="cat_label">Protezioni</span></a></li>
				<li><a id="cat_accessori" class="linked_box" href="../cgi-bin/products.cgi?category=accessori"><span class="cat_label">Accessori</span></a></li>	<!-- Cronometri, Fischi, Paradenti -->
			</ul>
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
						<li><a href="../cgi-bin/products.cgi?category=calcio">Calcio</a></li>
						<li><a href="../cgi-bin/products.cgi?category=basket"><span xml:lang="en">Basket</span></a></li>
						<li><a href="../cgi-bin/products.cgi?category=volley"><span xml:lang="en">Volley</span></a></li>
						<li><a href="../cgi-bin/products.cgi?category=tennistavolo">Tennistavolo</a></li>
						<li><a href="../cgi-bin/products.cgi?category=nuoto">Nuoto</a></li>
						<li><a href="../cgi-bin/products.cgi?category=minigolf">Minigolf</a></li>
						<li><a href="../cgi-bin/products.cgi?category=calciobalilla">Calciobalilla</a></li>
						<li><a href="../cgi-bin/products.cgi?category=protezioni">Protezioni</a></li>
						<li><a href="../cgi-bin/products.cgi?category=accessori">Accessori</a></li>
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
