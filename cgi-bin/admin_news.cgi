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
my $upload_dir = "../res/images/";
my $file = '../data/xml/db.xml';

my $cgi = CGI->new();
my $error = $cgi->cgi_error();
my %INPUT = Vars();

my $tabIndexCount = 0;
sub tabIndex {
    if ($INPUT{'add_wallpaper'}) {
        $tabIndexCount = -1;
    } else {
        $tabIndexCount++;
    } 
    return (\$tabIndexCount);
}

sub getSession() {
	my $session = CGI::Session->load() or die "Errore"; #CGI::Session->errstr
	if ($session->is_expired || $session->is_empty) { # Se manca la sessione torno in home
		print redirect(-url=>'index.cgi');
	}
}

sub destroySession() {
	my $session = CGI::Session->load() or die "Errore";
	$session->close();
	$session->delete();
	$session->flush();
	print redirect(-url=>'index.cgi'); # Torno in home
}

sub printPlaceholder() {
	$placeholder = "<div id=\"placeholder\">
					   <p>Nessun prodotto ancora inserito</p>
					   <img src=\"../res/images/empty_list.png\" alt=\"Immagina lista prodotti vuota\" \>
				    </div>
			</div>\n";   #</content_admin>
	return $placeholder;
}

# Verifica della sessione
getSession();
    
# Apertura file XML
$parser = XML::LibXML->new();
$parser->keep_blanks(0);
$doc = $parser->parse_file($file) or die "Errore nel parsing";
$radice = $doc->getDocumentElement or die "Errore elemento radice";

my $display_category = "Tutte";
if($INPUT{'display_category'}) {
    $display_category = $INPUT{'display_category'};
}
if($INPUT{'display_category_modify'}) {
    $display_category = $INPUT{'display_category_modify'};
}
if($INPUT{'display_category_remove'}) {
    $display_category = $INPUT{'display_category_remove'};
}

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
			<meta name="description" content="Pagina di amministrazione delle novit&agrave; del sito Ju Rapida." />
			<meta name="author" content="Fabiano Tavallini, Marco Franceschini, Daniele Favaro" />
			<meta name="copyright" content="Ju Rapida S.N.C." />
			<meta name="viewport" content="width=device-width"/>
			<link href="../css/style_1024_max.css" rel="stylesheet" type="text/css" />
			<link href="../css/style_768.css" rel="stylesheet" type="text/css" />
			<link href="../css/style_480.css" rel="stylesheet" type="text/css" />
			<link href="../css/style_1024_min.css" rel="stylesheet" type="text/css" />
            <!--[if lte IE 8]>
                <link rel="stylesheet" type="text/css" href="../css/style_ie8.css" />
            <![endif]-->
            <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" type='text/css' />
			<link href='https://fonts.googleapis.com/css?family=Maven+Pro:400,700' rel='stylesheet' type='text/css' />
			<link rel="icon" type="image/png" href="../res/images/icon.png" />
			<script type="text/javascript" src="../js/admin_news.js"></script>
		</head>
		<body>
			<div id="header">
				<div id="navbar_admin">
					<a tabindex="${tabIndex()}" id="admin_back_icon" href="admin.cgi?logout=1"><i class="material-icons md-24">&#xE88A;</i></a>
					<p><a tabindex="${tabIndex()}" id="admin_back" href="admin.cgi?logout=1">Torna al sito</a></p>
					<p>Gestione Novit&agrave;</p>
				</div>
EOF
#print "					<span id=\"products_number\">Sono presenti ".scalar @prodotti." prodotti</span>\n";

    print "     </div>
            <div id=\"content_admin\">";	

	if(%INPUT or $error) {  # Se riceve dati in input o errori
        if($INPUT{'add_wallpaper'}) {
            # Modal di modifica    
            my $code = $INPUT{'evidence_code'};
            my $query = "/products/product [code=\"".$code."\"]";
            my $prodotto = $doc->findnodes($query)->get_node(1) or die "Prodotto non trovato";
            my $category = $prodotto->findnodes("category/text()");
            my $description = $prodotto->findnodes("description/text()");
            my $shortDescription = $prodotto->findnodes("shortDescription/text()");
            my $sfondo = $prodotto->findnodes("backgroundImg/text()");
            print <<EOF;
                    <div id="openWallpaper" class="modalDialog">
                        <div>
                            <a tabindex="1" href="admin_news.cgi" title="Close" class="close">X</a>
                            <p>Evidenzia prodotto</p>
                            <form id="form_modal_modify" action="admin_news.cgi" method="post" enctype="multipart/form-data">
                                <div>
                                    <label class="form_item">Categoria: $category</label>
EOF
				if ($sfondo ne "none") {
                    print "         <label class=\"form_item\" for=\"wallpaper_img\">Sfondo</label>";
                    print "         <img src=\"../res/images/".$sfondo."\" class=\"form_item\" id=\"wallpaper_img\" alt=\"Immagine di sfondo\" />";
                }
                print <<EOF;             
                                    <input type="hidden" name="evidence_code" value="$code" />				
                                    <label class="form_item" for="wallpaper_new_img">Nuovo sfondo</label>
                                    <input tabindex="2" class="form_item" id="wallpaper_new_img" type="file" name="image"/>
EOF
									if ($sfondo ne "none") {
										print "<input tabindex=\"3\" accept=\"image/*\" class=\"submit_modal\" id=\"submit_modal_wallpaper\" name=\"add_evidence\" type=\"submit\" value=\"Aggiorna\"/>";
									} else {
                                    	print "<input tabindex=\"3\" accept=\"image/*\" class=\"submit_modal\" id=\"submit_modal_wallpaper\" name=\"add_evidence\" type=\"submit\" value=\"Aggiungi\"/>";
        		                    }
                print <<EOF;
                
                                </div>
                            </form>
                        </div>
                   </div>
EOF
        }
        if($error) {
            if($error =~ /413/) {     # Errore: 413 Request entity too large
                print "<span id=\"error_msg\" class=\"admin_message\">L'immagine selezionata &egrave; troppo grande!</span>";
            }
        }
        if($INPUT{'add_evidence'}) { # Inserisco i dati o verifico che siano stati modificati e poi inserisco quelli opportuni?
            $codice_prodotto = $INPUT{'evidence_code'};
            $name = $INPUT{'product_name'};
            $desc = $INPUT{'product_desc'};
            $wallpaper_desc = $INPUT{'wallpaper_desc'};
            my $query = "/products/product [code=\"".$codice_prodotto."\"]";
            my $prodotto = $doc->findnodes($query)->get_node(1);
            if(!$prodotto){                
                print "<span id=\"error_msg\" class=\"admin_message\">Prodotto ".$codice_prodotto." non trovato, &egrave; possibile che sia stato rimosso</span>";
            } else {
                $image = $cgi->param("image");
                my $old_image = $prodotto->findnodes("backgroundImg/text()")->get_node(1);
                if (!$image) {
                    if ($old_image eq "none") {
                        print "<span id=\"error_msg\" class=\"admin_message\">Immagine di sfondo non inserita</span>";
                    } else {
                        my $evidenza = $prodotto->findnodes("inEvidence/text()")->get_node(1);
                        $evidenza->setData("true");
                        print "<span id=\"info_msg\" class=\"admin_message\">Prodotto ".$codice_prodotto." evidenziato correttamente</span>";
                    }
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
                    $old_image->setData($image);
                    my $evidenza = $prodotto->findnodes("inEvidence/text()")->get_node(1);
                    $evidenza->setData("true");
                    print "<span id=\"info_msg\" class=\"admin_message\">Prodotto ".$code." evidenziato correttamente</span>";
                }
            }
        }
        if($INPUT{'hide_evidence'}) {
            # Rimozione "evidenza"
            my $codice_prodotto = $INPUT{'evidence_code'};
            my $query = "/products/product [code=\"".$codice_prodotto."\"]";
            my $prodotto = $doc->findnodes($query)->get_node(1);
            if(!$prodotto) {
                print "<span id=\"error_msg\" class=\"admin_message\">Prodotto ".$codice_prodotto." non trovato, &egrave; possibile che sia stato rimosso</span>";
            } else {
                my $evidenza = $prodotto->findnodes("inEvidence/text()")->get_node(1);
                $evidenza->setData("false");
                print "<span id=\"info_msg\" class=\"admin_message\">Prodotto ".$codice_prodotto." nascosto correttamente</span>";
            }
        }
        # Serializzazione e chiusura del file
        open(OUT, ">$file");
        print OUT $doc->toString(1);    # 1: indenta correttamente
        close(OUT);
	}
	# Lettura da file XML
    my $queryLimitata = "/products/product [category=\"".$display_category."\"]"; # Query per i prodotti selezionati
    if($display_category eq "Tutte") {
        $queryLimitata = "/products/product";
    }
    my @prodottiLimitati = $doc->findnodes($queryLimitata);
    
    my $query = "/products/product"; # Query per tutti i prodotti
    my @prodotti = $doc->findnodes($query);
    
	
    if (!@prodotti) {
	   	print printPlaceholder();
    } else {        
        # Stampa le card dei prodotti
        print <<EOF;
                <div id="products_container_news">
                    <div class="products_label_news">
                        <span>Codice</span><span class="product_name_label">Nome</span><span>Categoria</span>
                    </div>
EOF
        foreach my $product (@prodotti) { # Stampo i prodotti che sono in evidenza
            my $evidenza = $product->findnodes("./inEvidence");
            if($evidenza eq "true") {
                my $codice = $product->findnodes("code/text()");
                my $nome = $product->findnodes("name/text()");
                my $categoria = $product->findnodes("category/text()");
                print "					<div class=\"product_card\">\n";
                print "						<span class=\"product_code\">".$codice."</span>\n";
                print "						<span class=\"product_name\">".$nome."</span>\n";
                print "						<span class=\"product_category\">".$categoria."</span>\n";
                print "				        <div class=\"product_buttons\">\n";
                print "							<form class=\"form_remove\" action=\"admin_news.cgi\" method=\"post\" enctype=\"multipart/form-data\">\n";
                print "								<div>
                                                        <input type=\"hidden\" name=\"display_category_evidence\" value=\"".$display_category."\" />\n";
                print "								    <input type=\"hidden\" name=\"evidence_code\" value=\"".$codice."\" />\n";
                print "							        <input tabindex=\"${tabIndex()}\" class=\"button\" type=\"submit\" name=\"hide_evidence\" value=\"Rimuovi\" />\n";
                print "							    </div>
                                                </form>\n";
                print "						</div>\n";
                print "					</div>\n";
                $index_tab=$index_tab+1;
            }
        }
        print "</div>"; # products_container_news        
    }
    
    # Due cicli for utili solo alla stampa della linea di separazione
    foreach my $product (@prodotti) {
        if ($product->findnodes("./inEvidence") eq "false") {
            push @notInEvidence, $product;
        }
    }
    foreach my $product (@prodotti) {
        if ($product->findnodes("./inEvidence") eq "true") {
            push @inEvidence, $product;
        }
    }
    if (@notInEvidence && @inEvidence) {
        print "<hr />";
    }
    
    print <<EOF;
					<form id="dashboard_form_news" action="admin_news.cgi" method="post">
                        <div>
                            <label class="form_item_news" for="display_category">Categoria:</label>
                            <select tabindex=\"${tabIndex()}\" class="form_item_news" id="display_category" name="display_category">
                                <option value="Tutte"
EOF
                                if($display_category eq "Tutte"){ print " selected=\"selected\" ";}
                                print ">Tutte</option>\n";
    print "							<option value=\"Calcio\"";
                                if($display_category eq "Calcio"){ print " selected=\"selected\" ";}
                                print ">Calcio</option>\n";
    print "							<option lang=\"en\" value=\"Basket\"";
                                if($display_category eq "Basket"){ print " selected=\"selected\" ";}
                                print ">Basket</option>\n";
    print "							<option lang=\"en\" value=\"Volley\"";
                                if($display_category eq "Volley"){ print " selected=\"selected\" ";}
                                print ">Volley</option>\n";
    print "							<option value=\"Tennistavolo\"";
                                if($display_category eq "Tennistavolo"){ print " selected=\"selected\" ";}
                                print">Tennistavolo</option>\n";
    print "							<option value=\"Nuoto\"";
                                if($display_category eq "Nuoto"){ print " selected=\"selected\" ";}
                                print ">Nuoto</option>\n";
    print "							<option value=\"Minigolf\"";
                                if($display_category eq "Minigolf"){ print " selected=\"selected\" ";}
                                print ">Minigolf</option>\n";
    print "							<option value=\"Calciobalilla\"";
                                if($display_category eq "Calciobalilla"){ print " selected=\"selected\" ";}
                                print ">Calciobalilla</option>\n";
    print "							<option value=\"Protezioni\"";
                                if($display_category eq "Protezioni" ){ print " selected=\"selected\" ";}
                                print ">Protezioni</option>\n";
    print "							<option value=\"Accessori\"";
                                if($display_category eq "Accessori"){ print " selected=\"selected\" ";}
                                print ">Accessori</option>\n";
                     print "</select>
						    <input tabindex=\"${tabIndex()}\" id=\"submit_dashboard_news\" type=\"submit\" value=\"Aggiorna\" />
					   </div>
                    </form>
					<div id=\"products_container\">";

    my $cont=0;
    for(my $i=0; $i < scalar @prodottiLimitati && $cont!=1; $i++) { # Verifico se ci sono prodotti che non sono in evidenza
        my $evidenza = $prodottiLimitati[$i]->findnodes("./inEvidence");
        if($evidenza ne "true") {
            $cont=1;
        }
    }
    if($cont!=0) { # Ho almeno 1 prodotto non in evidenza
        # Stampa le card dei prodotti
        print <<EOF;
                    <div class="products_label_news">
                        <span>Codice</span><span class="product_name_label">Nome</span><span>Categoria</span>
                    </div>
EOF
        for(my $i=0; $i < scalar @prodottiLimitati; $i++) { # Stampo i prodotti che non sono in evidenza
            my $evidenza = $prodottiLimitati[$i]->findnodes("./inEvidence");
            if($evidenza ne "true") {
                my $codice = $prodottiLimitati[$i]->findnodes("code/text()");
                my $nome = $prodottiLimitati[$i]->findnodes("name/text()");
                my $categoria = $prodottiLimitati[$i]->findnodes("category/text()");        
                print "					<div class=\"product_card\">\n";
                print "						<span class=\"product_code\">".$codice."</span>\n";
                print "						<span class=\"product_name\">".$nome."</span>\n";
                print "						<span class=\"product_category\">".$categoria."</span>\n";
                print "				        <div class=\"product_buttons\">\n";
                print "							<form class=\"form_add\" action=\"admin_news.cgi#openWallpaper\" method=\"post\" enctype=\"multipart/form-data\">\n";
                print "								<div>
                                                        <input type=\"hidden\" name=\"display_category_evidence\" value=\"".$display_category."\" />\n";
                print "								    <input type=\"hidden\" name=\"evidence_code\" value=\"".$codice."\" />\n";
                print "							        <input tabindex=\"${tabIndex()}\" class=\"button\" type=\"submit\" name=\"add_wallpaper\" value=\"Evidenzia\" />\n";
                print "							    </div>
                                                </form>\n";
                print "						</div>\n";
                print "					</div>\n";
            }
        }        
    }
    print "	</div>\n"; # products_container
	print <<EOF;
			<div id="action_bar">
				<div id="action_box_news">
                    <a tabindex="${tabIndex()}" id="action_back_news" class="linked_box" href="admin.cgi">Indietro</a>
                </div>
			</div>
		</div>		
		<div id="footer">
            <div id="copy_panel">
                <p id="copy">Copyright &copy; 2016 - All right reserved. Ju Rapida SNC - VIA F. PETRARCA, 14/31100 TREVISO ITALY - P. IVA: 01836040269</p>
                <p id="validation">
                    <span id="xhtml_valid">
                        <a tabindex="${tabIndex()}" href=\"http://validator.w3.org/check?uri=referer\"><img src=\"http://www.w3.org/Icons/valid-xhtml10\" alt=\"Valid XHTML 1.0 Strict\" height=\"31\" width=\"88\" /></a>
                    </span>
                    <span id=\"css_valid\">
                        <a tabindex="${tabIndex()}" href=\"http://jigsaw.w3.org/css-validator/check/referer\"><img style=\"border:0;width:88px;height:31px\" src=\"http://jigsaw.w3.org/css-validator/images/vcss-blue\" alt=\"Valid CSS3\" /></a>
                    </span>
                </p>
            </div>
        </div>
    </body>
</html>
EOF
}
