#!/usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard Vars);
use XML::LibXML;
use warnings;

my $cgi = CGI->new();
my $category = $cgi->param('category');

# Lettura da file XML
my $file = '../xml/db.xml';
my $parser = XML::LibXML->new();
$parser->keep_blanks(0);
my $doc = $parser->parse_file($file) or die "Errore nel parsing";
my $radice = $doc->getDocumentElement or die "Errore elemento radice";
my $query = "/products/product[category=\"".$category."\"]";
my @prodotti = $doc->findnodes($query);

print CGI->header;
print <<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
        <title>$category - Ju Rapida</title>
        <meta name="title" content="$category - Ju Rapida S.N.C." />
        <meta name="description" content="Pagina dei prodotti nel mondo $category di JU RAPIDA" />
        <meta name="keywords" content="$category, ju rapida, articoli sportivi, prodotti, sport;" />
		<meta name="author" content="Fabiano Tavallini, Marco Franceschini, Daniele Favaro" />
		<meta name="copyright" content="Ju Rapida S.N.C." />
		<meta name="viewport" content="width=device-width" />
		<link href="../css/style_1024_max.css" rel="stylesheet" type="text/css" />
		<link href="../css/style_768.css" rel="stylesheet" type="text/css" />
		<link href="../css/style_480.css" rel="stylesheet" type="text/css" />
		<link href="../css/style_1024_min.css" rel="stylesheet" type="text/css" />
        <link href="../css/style_print.css" rel="stylesheet" type="text/css" />
        <!--[if lte IE 8]>
            <link rel="stylesheet" type="text/css" href="../css/style_ie8.css" />
        <![endif]-->
		<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" type='text/css' />
		<link href='https://fonts.googleapis.com/css?family=Maven+Pro:400,700' rel='stylesheet' type='text/css' />
		<link rel="icon" type="image/png" href="../res/images/icon.png" />
	</head>
	<body>
        <div><a class="skip_menu" href="#firstProduct">Salta la navigazione</a></div>
		<div id="header">
			<div id="contacts">
				<p><i class="material-icons md-18">&#xE0CD;</i> +39 0422 445566</p>
				<p><i class="material-icons md-18">&#xE0BE;</i> jurapida\@gmail.com</p>
			</div>
			<div id="navbar">
				<a href="index.cgi"><img id="logo" src="../res/images/logo_bianco.png" alt="Logo Ju Rapida" /></a>
				<ul id="menu"> 
					<li><a href="index.cgi"><span xml:lang="en">Home</span></a></li>
					<li><a href="../pages/products.html">Prodotti</a></li>
					<li><a href="contacts.cgi">Contatti</a></li>
					<li><a href="../pages/about.html">Chi siamo</a></li>
				</ul>
			</div>
			<div id="breadcrumb">
                <a href="index.cgi"><img src="../res/images/ic_home.png" alt="Home page"></img></a> &gt; <a href="../pages/products.html">Prodotti</a> &gt; $category
			</div>
		</div>
				
		<div id="content_products_cgi">
			<div id="products_navigator">
				<div id="category_navigator">
					<p class="navigator_title">Categoria</p>
					<ul class=\"navigator_list\">
EOF
my $isCategoryEmpty = 0;
if ($category ne "Calcio" && !@prodotti && $isCategoryEmpty == 0) {
    print "             <li><a id=\"firstProduct\" href=\"products.cgi?category=Calcio\">Calcio</a></li>\n";
    $isCategoryEmpty = 1;
} else {
    if ($category ne "Calcio") {
        print "			<li><a href=\"products.cgi?category=Calcio\">Calcio</a></li>\n";
    } else {
        print "			<li class=\"navigator_current\"><i class=\"material-icons md-24\">&#xE892;</i>Calcio</li>\n";
    }
}

if ($category ne "Basket" && !@prodotti && $isCategoryEmpty == 0) {
    print "             <li><a id=\"firstProduct\" href=\"products.cgi?category=Basket\"><span xml:lang=\"en\">Basket</span></a></li>\n";
    $isCategoryEmpty = true;
} else {
    if ($category ne "Basket") {
        print "         <li><a href=\"products.cgi?category=Basket\"><span xml:lang=\"en\">Basket</span></a></li>\n";
    } else {
        print "         <li class=\"navigator_current\"><i class=\"material-icons md-24\">&#xE892;</i><span xml:lang=\"en\">Basket</span></li>\n";
    }
}

if ($category ne "Volley" && !@prodotti && $isCategoryEmpty == 0) {
    print "             <li><a id=\"firstProduct\" href=\"products.cgi?category=Volley\"><span xml:lang=\"en\">Volley</span></a></li>\n";
    $isCategoryEmpty = true;
} else {
    if ($category ne "Volley") {
        print "			<li><a href=\"products.cgi?category=Volley\"><span xml:lang=\"en\">Volley</span></a></li>\n";
    } else {
        print "		   	<li class=\"navigator_current\"><i class=\"material-icons md-24\">&#xE892;</i><span xml:lang=\"en\">Volley</span></li>\n";
    }
}

if ($category ne "Tennistavolo" && !@prodotti && $isCategoryEmpty == 0) {
    print "             <li><a id=\"firstProduct\" href=\"products.cgi?category=Tennistavolo\">Tennistavolo</a></li>\n";
    $isCategoryEmpty = true;
} else {
    if ($category ne "Tennistavolo") {
        print "	        <li><a href=\"products.cgi?category=Tennistavolo\">Tennistavolo</a></li>\n";
    } else {
        print "			<li class=\"navigator_current\"><i class=\"material-icons md-24\">&#xE892;</i>Tennistavolo</li>\n";
    }
}

if ($category ne "Nuoto" && !@prodotti && $isCategoryEmpty == 0) {
    print "             <li><a id=\"firstProduct\" href=\"products.cgi?category=Nuoto\">Nuoto</a></li>\n";
    $isCategoryEmpty = true;
} else {
    if ($category ne "Nuoto") {
        print "			<li><a href=\"products.cgi?category=Nuoto\">Nuoto</a></li>\n";
    } else {
        print "			<li class=\"navigator_current\"><i class=\"material-icons md-24\">&#xE892;</i>Nuoto</li>\n";
    }
}

if ($category ne "Minigolf" && !@prodotti && $isCategoryEmpty == 0) {
    print "             <li><a id=\"firstProduct\" href=\"products.cgi?category=Minigolf\">Minigolf</a></li>\n";
    $isCategoryEmpty = true;
} else {
    if ($category ne "Minigolf") {
        print "			<li><a href=\"products.cgi?category=Minigolf\">Minigolf</a></li>\n";
    } else {
        print "			<li class=\"navigator_current\"><i class=\"material-icons md-24\">&#xE892;</i>Minigolf</li>\n";
    }
}

if ($category ne "Calciobalilla" && !@prodotti && $isCategoryEmpty == 0) {
    print "             <li><a id=\"firstProduct\" href=\"products.cgi?category=Calciobalilla\">Calciobalilla</a></li>\n";
    $isCategoryEmpty = true;
} else {
    if ($category ne "Calciobalilla") {
        print "         <li><a href=\"products.cgi?category=Calciobalilla\">Calciobalilla</a></li>\n";
    } else {
        print "			<li class=\"navigator_current\"><i class=\"material-icons md-24\">&#xE892;</i>Calciobalilla</li>\n";
    }
}

if ($category ne "Protezioni" && !@prodotti && $isCategoryEmpty == 0) {
    print "             <li><a id=\"firstProduct\" href=\"products.cgi?category=Protezioni\">Protezioni</a></li>\n";
    $isCategoryEmpty = true;
} else {
    if ($category ne "Protezioni") {
        print "			<li><a href=\"products.cgi?category=Protezioni\">Protezioni</a></li>\n";
    } else {
        print "			<li class=\"navigator_current\"><i class=\"material-icons md-24\">&#xE892;</i>Protezioni</li>\n";
    }
}

if ($category ne "Accessori" && !@prodotti && $isCategoryEmpty == 0) {
    print "             <li><a id=\"firstProduct\" href=\"products.cgi?category=Accessori\">Accessori</a></li>\n";
    $isCategoryEmpty = true;
} else {
    if ($category ne "Accessori") {
        print "			<li><a href=\"products.cgi?category=Accessori\">Accessori</a></li>\n";
    } else {
        print "			<li class=\"navigator_current\"><i class=\"material-icons md-24\">&#xE892;</i>Accessori</li>\n";
    }
}
print "	            </ul>
				</div>";

# Stampo i placeholder del menu
for(my $i=0; $i < scalar @prodotti; $i++) {
    print "<div class=\"navigator_placeholder";
    if(!($i % 2) && $i gt 1) {
        print " navigator_placeholder_block2";
    }
    if(!($i % 3) && $i gt 1) {
        print " navigator_placeholder_block3";
    }
    if(!($i % 4) && $i gt 1) {
        print " navigator_placeholder_block4";
    }
    print "\">";
    print " </div>";
}
print "     </div>\n";
print " <div id=\"products_displayer\">";
print " <div id=\"products_displayer_frame\">";

if(!@prodotti) {
    print " <span id=\"error_msg\" class=\"client_message\">Nessun prodotto da visualizzare</span>";
} else {
    # Stampa le card dei prodotti
    for(my $i=0; $i < scalar @prodotti; $i++) {
        my $codice = $prodotti[$i]->findnodes("code/text()");
        my $nome = $prodotti[$i]->findnodes("name/text()");
        my $thumbnail = $prodotti[$i]->findnodes("thumbnail/text()");
        my $descrizione_corta = $prodotti[$i]->findnodes("shortDescription/text()");
        print " <div class=\"product_card\">";
        print " <div class=\"product_image\">";
        print "     <img src=\"../res/images/products/thumbnails/".$thumbnail."\" alt=\"".$descrizione_corta."\"/>";
        print " </div>"; 
        # Stampo abbreviate le parole dopo la prima se il nome e' troppo lungo
        my $nome_originale = $nome;
        if(length($nome) > 15) {
            @parole = split / /, $nome;
            $nome = $parole[0];
            if($parole[1]) {
                $nome = $nome." ";
            }
            for(my $i=1; $i < scalar @parole; $i++) {
                # Se contiene "con" stampo la prossima parola per intera
                if(($parole[$i] eq "con") or ($parole[$i] eq "Con")){
                    $nome = $nome.$parole[$i+1];
                    $i++;
                } else {
                    my @lettere = split //, $parole[$i];
                    $nome = $nome.$lettere[0].".";
                }
            }
        }
        print " <span class=\"product_name\">".$nome."</span>";
        print " <span class=\"product_code\">Codice ".$codice."</span>";
        print " <p class=\"product_short_description\">".$descrizione_corta."</p>";
        print " <div class=\"product_display_button\">
                    <form class=\"form_display\" action=\"product_displayer.cgi#content_products_displayer_cgi\" method=\"post\">
                        <div>";
        print "             <input type=\"hidden\" name=\"display_code\" value=\"".$codice."\" />
                            <input type=\"hidden\" name=\"display_name\" value=\"".$nome_originale."\" />
                            <input type=\"hidden\" name=\"display_category\" value=\"".$category."\" />";
        if ($i == 0) {
            print "         <input id=\"firstProduct\" class=\"button\" type=\"submit\" value=\"Apri\" />";
        } else {
            print "         <input class=\"button\" type=\"submit\" value=\"Apri\" />";
        }
        print "         </div>
                    </form>
                </div>";
        print " </div>";
    }
}
print <<EOF;
                </div>
            </div>	
		</div>
		
		<div id="footer">
			<div id="footer_top">
				<div id="maps">
					<ul id="maps_menu">
						<li><a href="index.cgi"><span xml:lang="en">Home</span></a></li>
						<li><a href="../pages/products.html">Prodotti</a></li>
						<li><a href="contacts.cgi">Contatti</a></li>
						<li><a href="../pages/about.html">Chi siamo</a></li>
					</ul>
					<ul id="maps_categories">
EOF
if ($category ne "Calcio") { 
    print "             <li><a href=\"products.cgi?category=Calcio\">Calcio</a></li>";
} else {
    print "             <li>Calcio</li>";
}
if ($category ne "Basket") { 
    print "				<li><a href=\"products.cgi?category=Basket\"><span xml:lang=\"en\">Basket</span></a></li>";
} else {
    print "             <li><span xml:lang=\"en\">Basket</span></li>";
}
if ($category ne "Volley") { 
    print "				<li><a href=\"products.cgi?category=Volley\"><span xml:lang=\"en\">Volley</span></a></li>";
} else {
    print "             <li><span xml:lang=\"en\">Volley</span></li>";
}
if ($category ne "Tennistavolo") { 
    print "				<li><a href=\"products.cgi?category=Tennistavolo\">Tennistavolo</a></li>";
} else {
    print "             <li>Tennistavolo</li>";
}
if ($category ne "Nuoto") { 
    print "				<li><a href=\"products.cgi?category=Nuoto\">Nuoto</a></li>";
} else {
    print "             <li>Nuoto</li>";
}
if ($category ne "Minigolf") { 
    print "				<li><a href=\"products.cgi?category=Minigolf\">Minigolf</a></li>";
} else {
    print "             <li>Minigolf</li>";
}
if ($category ne "Calciobalilla") { 
    print "				<li><a href=\"products.cgi?category=Calciobalilla\">Calciobalilla</a></li>";
} else {
    print "             <li>Calciobalilla</li>";
}
if ($category ne "Protezioni") { 
    print "				<li><a href=\"products.cgi?category=Protezioni\">Protezioni</a></li>";
} else {
    print "             <li>Protezioni</li>";
}
if ($category ne "Accessori") { 
    print "				<li><a href=\"products.cgi?category=Accessori\">Accessori</a></li>";
} else {
    print "             <li>Accessori</li>";
}
print <<EOF;
					</ul>
				</div>
				<div id="admin_form_panel">
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
