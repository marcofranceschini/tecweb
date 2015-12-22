#!C:/Perl64/bin/perl.exe
#!/usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard Vars);
use CGI::Session;
use XML::LibXML;
use File::Basename;
use warnings;
$CGI::POST_MAX = 1024 * 5000;   #massimo upload
my $safe_filename_characters = "a-zA-Z0-9_.-";  #caratteri sicuri
my $upload_dir = "../res/images/products";

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

# Verifica della sessione
getSession();

my $cgi = CGI->new();
my $error = $cgi->cgi_error();

# Recupero i dati dall'input
my %INPUT = Vars();
    
# Apertura file XML
$file = '../xml/db.xml';
$parser = XML::LibXML->new();
$parser->keep_blanks(0);
$doc = $parser->parse_file($file) or die "Errore nel parsing";
$radice = $doc->getDocumentElement or die "Errore elemento radice";

my $cat = "Calcio";
if(%INPUT{'display_category'}) {
    print "prova";
    $cat = %INPUT{'display_category'};
}

# Lettura da file XML
my $query = "/products/product [category=\"".$cat."\"]";
my @prodotti = $doc->findnodes($query);

# Controllo logout e creazione pagina
my $logout = $cgi->param('logout');
if ($logout) {
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
					<a id="admin_back_icon" href="../cgi-bin/admin.cgi?logout=1"><i class="material-icons md-24">&#xE88A;</i></a>
					<p><a id="admin_back" href="../cgi-bin/admin.cgi?logout=1">Torna al sito</a></p>
					<p>Gestione Prodotti</p>
				</div>
                <div id="admin_dashboard">
EOF
print "<span id=\"products_number\">Sono presenti ".scalar @prodotti." prodotti</span>";
print <<EOF;
                    <form id="dashboard_form" action="admin_products.cgi" method="post">
                        <div class="form_item">
                            <span>nella</span>
                            <label for="display_category">categoria</label>
                        </div>
                        <select class="form_item" name="display_category">
EOF
print "<option value=\"".$cat."\">".$cat."</option>";
print <<EOF;
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
                        <input id="submit_dashboard" type="submit" value="Aggiorna" />
                </div>
			</div>
			<div id="content_admin">	
EOF

	if(%INPUT or $error) {  #se riceve dati in input o errori
        if(%INPUT{'modify_request'}) {
            # Modal di modifica    
            my $code = $INPUT{'modify_request'};
            my $query = "/products/product [code=\"".$code."\"]";
            my $prodotto = $doc->findnodes($query)->get_node(1) or die "Prodotto non trovato";
            my $name = $prodotto->findnodes("name/text()");
            my $category = $prodotto->findnodes("category/text()");
            my $description = $prodotto->findnodes("description/text()");
            my $shortDescription = $prodotto->findnodes("shortDescription/text()");
            print <<EOF;
                    <div id="openModify" class="modalDialog">
                        <div>
                            <a href="#close" title="Close" class="close">X</a>
                            <p>Modifica un prodotto</p>
                            <form action="admin_products.cgi" method="post">
                                <label class="form_item" for="product_category">Categoria</label>
                                <select class="form_item" id="product_category" name="product_category">
EOF
                    print "<option value=\"".$category."\">".$category."</option>";
                    print <<EOF;
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
EOF
                    print "<input class=\"form_item\" id=\"product_code\" type=\"text\"  name=\"product_code\" value=\"".$code."\" disabled />";
                    print "<label class=\"form_item\" for=\"product_name\">Nome</label>";
                    print "<input class=\"form_item\" id=\"product_name\" type=\"text\" name=\"product_name\" value=\"".$name."\" />";
                    print "<label class=\"form_item\" for=\"product_desc\">Descrizione</label>";
                    print "<textarea class=\"form_item\" id=\"product_desc\"  name=\"product_desc\" >".$description."</textarea>";
                    print "<label class=\"form_item\" for=\"thumbnail_desc\">Descrizione breve</label>";
                    print "<textarea class=\"form_item\" id=\"thumbnail_desc\"  name=\"thumbnail_desc\" >".$shortDescription."</textarea>";
                    print "<input type=\"hidden\" name=\"modify\" value=\"".$code."\" />";
                    print <<EOF;
                            <label class="form_item" for="product_image">Nuova <span lang="en">thumbnail</span></label>
                            <input class="form_item" id="product_image" type="file" name="image" />
                            <input class="submit_modal" id="submit_modal_modify" type="submit" value="Modifica" />
                        </form>
                    </div>
                </div>
EOF
        }
        if($error) {
            if($error =~ /413/) {     #errore: 413 Request entity too large
                print "<span id=\"error_msg\">L'immagine selezionata &egrave; troppo grande!</span>";
            }
        }
        if($INPUT{'modify'}) { # Inserisco i dati o verifico che siano stati modificati e poi inserisco quelli opportuni?
      		# Modifica del database 
            $codice_prodotto = $INPUT{'modify'};
            $category = $INPUT{'product_category'};
            #$code = $INPUT{'product_code'};
            $name = $INPUT{'product_name'};
            $desc = $INPUT{'product_desc'};
            $thumbnail_desc = $INPUT{'thumbnail_desc'};
			$image = $cgi->param("image");   
                     
            my $query = "/products/product [code=\"".$codice_prodotto."\"]";
            my $prodotto = $doc->findnodes($query)->get_node(1) or die "Prodotto non trovato";
            my $old_category = $prodotto->findnodes("category/text()")->get_node(1);
            my $old_name = $prodotto->findnodes("name/text()")->get_node(1);            
            my $old_description = $prodotto->findnodes("description/text()")->get_node(1);
            my $old_shortDescription = $prodotto->findnodes("shortDescription/text()")->get_node(1);
            my $old_image = $prodotto->findnodes("img/text()")->get_node(1);
            
            if($old_category ne $category) {
                $old_category->setData($category);
            }
            if($old_name ne $name) {
                $old_name->setData($name);
            }
            if($old_description ne $desc) {
                $old_description->setData($desc);
            }
            if($old_shortDescription ne $thumbnail_desc) {
                $old_shortDescription->setData($thumbnail_desc);
            }
            if ( $image ) {
                if($old_image ne $image) {
                    print "le immagini sono diverse";
                    my ( $name, $path, $extension ) = fileparse ( $image, '..*' );
                    $image = $name.$extension;
                    $image =~ tr/ /_/;
                    $image =~ s/[^$safe_filename_characters]//g;
                    my $upload_file_handle = $cgi->upload("image");
                    open ( UPLOADFILE, ">$upload_dir/$image" ) or die "$!";
                    binmode UPLOADFILE;
                    while ( <$upload_file_handle> ) {
                        print UPLOADFILE;
                    }
                    close UPLOADFILE;
                    $old_image->setData($image);
                }
            }
        }
        if($INPUT{'remove'}) {
            # Rimozione dal database
            my $codice_prodotto = $INPUT{'remove'};
            my $query = "/products/product [code=\"".$codice_prodotto."\"]";
            my $prodotto = $doc->findnodes($query)->get_node(1) or die "Prodotto non trovato";
            my $padre = $prodotto->parentNode;
            $padre->removeChild($prodotto);
        }
        if($INPUT{'insert'}) {
            # Scrittura su file XML	
            my $category = $INPUT{'product_category'};
            my $code = $INPUT{'product_code'};
            my $name = $INPUT{'product_name'};
            my $desc = $INPUT{'product_desc'};
            my $thumbnail_desc = $INPUT{'thumbnail_desc'};
            my $image = $cgi->param("image");  
            #upload dell'immagine
            if ( !$image ) {
                die $!;
            } else {
                my ( $name, $path, $extension ) = fileparse ( $image, '..*' );
                $image = $name.$extension;
                $image =~ tr/ /_/;
                $image =~ s/[^$safe_filename_characters]//g;
                my $upload_file_handle = $cgi->upload("image");
                open ( UPLOADFILE, ">$upload_dir/$image" ) or die "$!";
                binmode UPLOADFILE;
                while ( <$upload_file_handle> ) {
                    print UPLOADFILE;
                }
                close UPLOADFILE;
            }
            
            $new_product =
            "<product>".
            "<category>".$category."</category>".
            "<code>".$code."</code>".
            "<name>".$name."</name>".
            "<description>".$desc."</description>".
            "<shortDescription>".$thumbnail_desc."</shortDescription>".
            "<img>".$image."</img>".
            "<backgroundImg></backgroundImg>".
            "<inEvidence>false</inEvidence>".
            "</product>";
            $nodo = $parser->parse_balanced_chunk($new_product) or die "Frammento non ben formato\n";
            $padre = $doc->findnodes("/products")->get_node(1) or die "Errore nel padre\n";
            if($padre){
                $padre->appendChild($nodo);
            } else {
                print "<p>Database mal formato</p>";
            }
        }
        #serializzazione e chiusura del file
        open(OUT, ">$file");
        print OUT $doc->toString(2);    #2: indenta correttamente
        close(OUT);
	}
	
	if (!@prodotti) {
	   	print printPlaceholder();
    } else {
        #stampa le card dei prodotti
        print "<div id=\"products_container\">";
        print "<div id=\"products_label\"><span>Codice</span><span id=\"product_name_label\">Nome</span><span>Categoria</span></div>";
        for(my $i=0; $i < scalar @prodotti; $i++)
        {
            my $codice = $prodotti[$i]->findnodes("code/text()");
            my $nome = $prodotti[$i]->findnodes("name/text()");
            my $categoria = $prodotti[$i]->findnodes("category/text()");
            print "<div class=\"product_card\">";
            print "<span class=\"product_code\">".$codice."</span>";
            print "<span class=\"product_name\">".$nome."</span>";
            print "<span class=\"product_category\">".$categoria."</span>";
           #<a id=\"action_add\" href=\"#openModify?value=\"".$codice."\">Modifica</a> 
		  
			print "<div class=\"product_buttons\">
                 <form class=\"form_modify\" action=\"admin_products.cgi#openModify\" method=\"post\">
                        <input type=\"hidden\" name=\"display_category\" value=\"".$cat."\" />
                        <input type=\"hidden\" name=\"modify_request\" value=\"".$codice."\" />
                        <input class=\"button\" type=\"submit\" value=\"Modifica\" />
                </form>
                <form class=\"form_remove\" action=\"admin_products.cgi\" method=\"post\">
                        <input type=\"hidden\" name=\"remove\" value=\"".$codice."\" />
                        <input class=\"button\" type=\"submit\" value=\"Rimuovi\" />
                </form>
            </div>";
            print "</div>";
        }
        print "</div>";
    }
    
	print <<EOF;
            <div id="openModal" class="modalDialog">
				<div>
					<a href="#close" title="Close" class="close">X</a>
					<p>Inserisci un nuovo prodotto</p>
					<form action="admin_products.cgi" method="post" enctype="multipart/form-data">
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
						<input class="submit_modal" id="submit_modal" type="submit" value="Inserisci" />
					</form>
				</div>
			</div>
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