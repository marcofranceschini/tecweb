#!C:/Perl64/bin/perl.exe
#!/usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard Vars);
use CGI::Session;
use XML::LibXML;
use warnings;

#Da usare il lab
#<link href="../tecwebproject/css/style_1024_max.css" rel="stylesheet" type="text/css" />
#<link href="../tecwebproject/css/style_768.css" rel="stylesheet" type="text/css" />
#<link href="../tecwebproject/css/style_480.css" rel="stylesheet" type="text/css" />
#<link href="../tecwebproject/css/style_1024_min.css" rel="stylesheet" type="text/css" />

sub getSession() {
	$sessione = CGI::Session->load() or die $!; #CGI::Session->errstr
	if ($sessione->is_expired || $sessione->is_empty) { # Se manca la sessione torno in home
		#print redirect(-url=>'../');
	}
}

sub destroySession() {
	$session = CGI::Session->load() or die $!;
	#$SID = $session->id();
	$session->close();
	$session->delete();
	$session->flush();
	#print redirect(-url=>'../'); # Torno in home
	print "Content-Type: text/html\n\n";
	print "prova";
	$sessione = CGI::Session->load() or die $!; #CGI::Session->errstr
	print $session->param('pass');
}

sub printPlaceholder() {
	# Da usare in lab: ../tecwebproject/res/images/empty_list.png
	$placeholder = "<div id=\"placeholder\">
						<p>Nessun prodotto ancora inserito</p>
						<img src=\"../res/images/empty_list.png\" alt=\"Immagina lista prodotti vuota\" \>
					</div>";
	return $placeholder;
}

getSession(); # Verifico che la sessione ci sia

my $cgi = CGI->new();
my $param = $cgi->param('param');
if ($param) { # LOGOUT - E' stato premuto il link per uscire
	destroySession();
} else {
	print "Content-Type: text/html\n\n";
	print <<EOF;
	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
		<head>
			<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
			<title>Gestione Prodotti - Amministrazione - Ju Rapida</title>
			<meta name="title" content="Ju Rapida S.N.C." />
			<meta name="description" content="Pagina di amministrazione dei prodotti del sito Ju Rapida." />
			<!-- meta name="keywords" content="ju rapida, ammin, articoli sportivi, calcio, tennistavolo, volley, carlo tavallini, vendita;" -->
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
				<div id="navbar_admin">
					<a id="admin_back_icon" href="../cgi-bin/admin.cgi?param=1"><i class="material-icons md-24">&#xE88A;</i></a>
					<p><a id="admin_back" href="../cgi-bin/admin.cgi?param=1">Torna al sito</a></p>
					<p>Gestione Prodotti</p>
				</div>
			</div> 
			
			<div id="openModal" class="modalDialog">
				<div>
					<a href="#close" title="Close" class="close">X</a>
					<p>Inserisci un nuovo prodotto</p>
					<form action="admin_products.cgi" method="post">
						<label class="form_item" for="product_category">Categoria</label>
						<select class="form_item" id="product_category" name="product_category">
							<option value="Calcio">Calcio</option>
							<option value="Basket"><span lang="en">Basket</span></option>
							<option value="Volley"><span lang="en">Volley</span></option>
							<option value="Tennistavolo">Tennistavolo</option>
							<option value="Nuoto">Nuoto</option>
							<option value="Minigolf">Minigolf</option>
							<option value="Calciobalilla">Calciobalilla</option>
							<option value="Protezioni">Protezioni</option>
							<option value="Accessori">Accessori</option>
						</select>
						<label class="form_item" for="product_code">Codice</label>
						<input class="form_item" id="product_code" type="text"  name="product_code" />
						<label class="form_item" for="product_name">Nome</label>
						<input class="form_item" id="product_name" type="text" name="product_name" />
						<label class="form_item" for="product_desc">Descrizione</label>
						<textarea class="form_item" id="product_desc"  name="product_desc" ></textarea>
						<label class="form_item" for="thumbnail_desc">Descrizione breve</label>
						<textarea class="form_item" id="thumbnail_desc"  name="thumbnail_desc" ></textarea>
						<label class="form_item" for="product_image">Carica <span lang="en">thumbnail</span></label>
						<input class="form_item" id="product_image" type="file" name="image" />
						<input type="hidden" name="insert" value="true" />
						<input id="submit_modal" type="submit" value="Inserisci" />
					</form>
				</div>
			</div>
			
			<div id="content_admin">	
EOF

    #apertura file XML
    my $file = '../xml/db.xml';
    my $parser = XML::LibXML->new();
    my $doc = $parser->parse_file($file) or die "Errore nel parsing";
    my $radice = $doc->getDocumentElement or die "Errore elemento radice";
    
	my %INPUT = Vars();
	if (%INPUT) {
        
        if($INPUT{'modify'}) {
            print "MODIFICA SELEZIONATA";
        }
        if($INPUT{'remove'}) {
            print "RIMOZIONE SELEZIONATA";
        }
        if($INPUT{'insert'}) {
            #scrittura su file XML	
            my $category = $INPUT{'product_category'};
            my $code = $INPUT{'product_code'};
            my $name = $INPUT{'product_name'};
            my $desc = $INPUT{'product_desc'};
            my $thumbnail_desc = $INPUT{'thumbnail_desc'};
            #my image =  = $INPUT{'product_image'};        
            
            $new_product =
            "\t<product>\n".
            "\t\t<category>".$category."</category>\n".
            "\t\t<code>".$code."</code>\n".
            "\t\t<name>".$name."</name>\n".
            "\t\t<description>".$desc."</description>\n".
            "\t\t<shortDescription>".$thumbnail_desc."</shortDescription>\n".
            "\t\t<backgroundImg></backgroundImg>\n".
            "\t\t<inEvidence>false</inEvidence>\n".
            "\t</product>\n";
            $nodo = $parser->parse_balanced_chunk($new_product) or die "Frammento non ben formato\n";
            $padre = $doc->findnodes("/products")->get_node(1) or die "Errore nel padre\n";
            $padre->appendChild($nodo);
            
            #serializzazione e chiusura del file
            open(OUT, ">$file");
            print OUT $doc->toString;
            close(OUT);
        }
	}
    
	#lettura da file XML
	#my @prodotti = $radice->getElementsByTagName('product') or die "Errore prodotti\n";
    my @prodotti = $doc->findnodes("/products/product") or die "Errore prodotti\n";
	
	if (!@prodotti) {
	   	print printPlaceholder();
    } else {
        print "<p id=\"products_number\">Sono presenti: ".scalar @prodotti." prodotti</p>";
        print "<div id=\"products_container\">";
        print "<div id=\"products_label\"><span>Codice</span><span id=\"product_name_label\">Nome</span><span>Categoria</span></div>";
        for(my $i=0; $i < scalar @prodotti; $i++)
        {
            print "<div class=\"product_card\">";
            print "<span class=\"product_code\">".$prodotti[$i]->findnodes("code/text()")."</span>";
            print "<span class=\"product_name\">".$prodotti[$i]->findnodes("name/text()")."</span>";
            print "<span class=\"product_category\">".$prodotti[$i]->findnodes("category/text()")."</span>";
            print <<EOF;
            <div id="product_buttons">
                <form id="form_modify" action="admin_products.cgi" method="post">
                        <input type="hidden" name="modify" value="true" />
                        <input class="button" type="submit" value="Modifica" />
                </form>
                <form id="form_remove" action="admin_products.cgi" method="post">
                        <input type="hidden" name="remove" value="true" />
                        <input class="button" type="submit" value="Rimuovi" />
                </form>
            </div>
EOF
            print "</div>";
        }
        print "</div>";
    }
    
    
    
	print <<EOF;
			</div>
			
			<div id="action_bar">
				<div id="action_box">
					<a id="action_back" class="linked_box" href="admin.cgi">Indietro</a>
					<a id="action_add" class="linked_box" href="#openModal">Aggiungi</a>
				</div>
			</div>
					
			<div id="footer">
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

}