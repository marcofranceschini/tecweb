#!/usr/bin/perl
#!C:/Perl64/bin/perl.exe

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
	$sessione = CGI::Session->load() or die $!; #CGI::Session->errstr
	print $session->param('pass');
}

sub printPlaceholder() {
	# Da usare in lab: ../tecwebproject/res/images/empty_list.png
	$placeholder = 
"				<div id=\"placeholder\">
					<p>Nessun prodotto ancora inserito</p>
					<img src=\"../res/images/empty_list.png\" alt=\"Immagina lista prodotti vuota\" \>
				</div>
			</div>\n";   #</content_admin>
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
    # Stampa l'hash ricevuto
    #foreach $key (keys %INPUT)
    #{
    #    print "$key: $INPUT{$key}\n";
    #}
	print <<EOF;
	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
		<head>
			<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
			<title>Gestione Prodotti - Amministrazione - Ju Rapida</title>
			<meta name="title" content="Ju Rapida S.N.C." />
			<meta name="description" content="Pagina di amministrazione delle novit&agrave; del sito Ju Rapida." />
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
					<p>Gestione Novit&agrave;</p>
				</div>
				<div id="admin_dashboard">
EOF
#print "					<span id=\"products_number\">Sono presenti ".scalar @prodotti." prodotti</span>\n";
print <<EOF;
					<form name="dashboard_form" id="dashboard_form" action="admin_news.cgi" method="post" enctype="multipart/form-data">
						<label class="form_item" for="display_category">Categoria:</label>
						<select class="form_item" name="display_category">
EOF
print "							<option value=\"Tutte\"";
                            if($display_category eq "Tutte"){ print " selected ";}
                            print ">Tutte</option>\n";
print "							<option value=\"Calcio\"";
                            if($display_category eq "Calcio"){ print " selected ";}
                            print ">Calcio</option>\n";
print "							<option value=\"Basket\"";
                            if($display_category eq "Basket"){ print " selected ";}
                            print "><span lang=\"en\">Basket</span></option>\n";
print "							<option value=\"Volley\"";
                            if($display_category eq "Volley"){ print " selected ";}
                            print "><span lang=\"en\">Volley</span></option>\n";
print "							<option value=\"Tennistavolo\"";
                            if($display_category eq "Tennistavolo"){ print " selected ";}
                            print">Tennistavolo</option>\n";
print "							<option value=\"Nuoto\"";
                            if($display_category eq "Nuoto"){ print " selected ";}
                            print ">Nuoto</option>\n";
print "							<option value=\"Minigolf\"";
                            if($display_category eq "Minigolf"){ print " selected ";}
                            print ">Minigolf</option>\n";
print "							<option value=\"Calciobalilla\"";
                            if($display_category eq "Calciobalilla"){ print " selected ";}
                            print ">Calciobalilla</option>\n";
print "							<option value=\"Protezioni\"";
                            if($display_category eq "Protezioni" ){ print " selected ";}
                            print ">Protezioni</option>\n";
print "							<option value=\"Accessori\"";
                            if($display_category eq "Accessori"){ print " selected ";}
                            print ">Accessori</option>\n";
                        print <<EOF;
						</select>
						<input id="submit_dashboard" type="submit" value="Aggiorna" />
					</form>
				</div>
			</div>
			<div id="content_admin">	
EOF

	if(%INPUT or $error) {  #se riceve dati in input o errori
        if($INPUT{'modify_wallpaper'}) {
            # Modal di modifica    
            my $code = $INPUT{'wallpaper_code'};
            my $query = "/products/product [code=\"".$code."\"]";
            my $prodotto = $doc->findnodes($query)->get_node(1) or die "Prodotto non trovato";
            my $category = $prodotto->findnodes("category/text()");
            my $description = $prodotto->findnodes("description/text()");
            my $shortDescription = $prodotto->findnodes("shortDescription/text()");
            my $sfondo = $prodotto->findnodes("backgroundImg/text()");
            print $sfondo;
            print <<EOF;
                    <div id="openWallpaper" class="modalDialog">
                        <div>
                            <a href="#close" title="Close" class="close">X</a>
                            <p>Modifica dello sfondo</p>
                            <form name="form_modal_wallpaper" id="form_modal_modify" action="admin_news.cgi" method="post" enctype="multipart/form-data">
                                <label class="form_item" for="product_category">Categoria</label>
EOF
                    print"      <input class=\"form_item\" id=\"product_category\" name=\"product_category\" value=\"".$category."\" disabled>";
                    print "<label class=\"form_item\" for=\"wallpaper_desc\">Descrizione dello sfondo</label>";
                    print "<textarea class=\"form_item\" id=\"wallpaper_desc\" name=\"wallpaper_desc\" >DESCRIZIONE DELLO SFONDO PER NON VEDENTI</textarea>";
                    print "<label class=\"form_item\" for=\"wallpaper_img\">Sfondo</label>";
                    print "<img src=\"../cgi-bin/".$sfondo."\" class=\"form_item\" id=\"wallpaper_img\" name\"wallpaper_img\" alt=\"Immagine di sfondo\" height=\"31\" width=\"88\" />";
                    print "<input type=\"hidden\" name=\"wallpaper_code\" value=\"".$code."\" />";
                    print <<EOF;
                            <label class="form_item" for="product_image">Nuovo sfondo</label>
                            <input class="form_item" id="wallpaper_new_img" type="file" name="image" />
                            <input class="submit_modal" id="submit_modal_wallpaper" name="modal_wallpaper" type="submit" value="Modifica" />
                        </form>
                    </div>
                </div>
EOF
        }
        if($error) {
            if($error =~ /413/) {     #errore: 413 Request entity too large
                print "<span id=\"error_msg\" class=\"admin_message\">L'immagine selezionata &egrave; troppo grande!</span>";
            }
        }
        if($INPUT{'modal_wallpaper'}) { # Inserisco i dati o verifico che siano stati modificati e poi inserisco quelli opportuni?
      		# Modifica del database 
            $codice_prodotto = $INPUT{'wallpaper_code'};
            #$code = $INPUT{'product_code'};
            $name = $INPUT{'product_name'};
            $desc = $INPUT{'product_desc'};
            $wallpaper_desc = $INPUT{'wallpaper_desc'};
			$image = $cgi->param("image");   
                     
            my $query = "/products/product [code=\"".$codice_prodotto."\"]";
            my $prodotto = $doc->findnodes($query)->get_node(1);
            if(!$prodotto){                
                print "<span id=\"error_msg\" class=\"admin_message\">Prodotto ".$codice_prodotto." non trovato, &egrave; possibile che sia stato rimosso</span>";
            } else {
                #my $old_description = $prodotto->findnodes("AAAA/text()")->get_node(1); # Descr per non vedenti
                my $old_image = $prodotto->findnodes("backgroundImg/text()")->get_node(1);
                # Modifica/Inserimento della descrizione
                #if($old_description ne $desc) {
                #    $old_description->setData($desc);
                #}
                # Modifica/Inserimento dello sfondo
                if ( $image ) {
                    if($old_image ne $image) {
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
                print "<span id=\"info_msg\" class=\"admin_message\">Prodotto ".$codice_prodotto." modificato correttamente</span>";
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
                print "<span id=\"info_msg\" class=\"admin_message\">Prodotto ".$codice_prodotto." \"nascosto\" correttamente</span>";
            }
        }
        if($INPUT{'evidence'}) {
            # Scrittura su file XML	
            my $code = $INPUT{'evidence_code'};
            # Verifico che l'immagine di sfondo ci sia
            my $query = "/products/product [code=\"".$code."\"]";
            my $prodotto = $doc->findnodes($query)->get_node(1);
            if(!$prodotto){                
                print "<span id=\"error_msg\" class=\"admin_message\">Prodotto ".$code." non trovato, &egrave; possibile che sia stato rimosso</span>";
            }else{
                my $image = $prodotto->findnodes("backgroundImg/text()")->get_node(1);
                if($image eq "") {
                    print "<span id=\"error_msg\" class=\"admin_message\">Prodotto ".$code." senza sfondo, inserirne uno</span>";
                }else{
                    my $evidenza = $prodotto->findnodes("inEvidence/text()")->get_node(1);
                    $evidenza->setData("true");
                    print "<span id=\"info_msg\" class=\"admin_message\">Prodotto ".$code." evidenziato correttamente</span>";
                }
            }
            
        }
        #serializzazione e chiusura del file
        open(OUT, ">$file");
        print OUT $doc->toString(2);    #2: indenta correttamente
        close(OUT);
	}
	# Lettura da file XML
    my $query = "/products/product [category=\"".$display_category."\"]";
    if($display_category eq "Tutte") {
        $query = "/products/product";
    }
    my @prodotti = $doc->findnodes($query);
	
    if (!@prodotti) {
	   	print printPlaceholder();
    } else {
        #stampa le card dei prodotti
        print <<EOF;
				<div id="products_container">
					<div id="products_label">
						<span>Codice</span><span id="product_name_label">Nome</span><span>Categoria</span>
					</div>
EOF
        for(my $i=0; $i < scalar @prodotti; $i++) {
            my $codice = $prodotti[$i]->findnodes("code/text()");
            my $nome = $prodotti[$i]->findnodes("name/text()");
            my $categoria = $prodotti[$i]->findnodes("category/text()");
            my $evidenza = $prodotti[$i]->findnodes("inEvidence/text()");
            print "					<div class=\"product_card\">\n";
            print "						<span class=\"product_code\">".$codice."</span>\n";
            print "						<span class=\"product_name\">".$nome."</span>\n";
            print "						<span class=\"product_category\">".$categoria."</span>\n";
			print "						<div class=\"product_buttons\">\n";
            print "							<form name=\"form_wallpaper\" id=\"form_modify\" class=\"form_modify\" action=\"admin_news.cgi#openWallpaper\" method=\"post\" enctype=\"multipart/form-data\">\n";
            print "								<input type=\"hidden\" name=\"wallpaper_display_category\" value=\"".$display_category."\" />\n";
            print "								<input type=\"hidden\" name=\"wallpaper_code\" value=\"".$codice."\" />\n";
            print "							    <input class=\"button\" type=\"submit\" name=\"modify_wallpaper\" value=\"Sfondo\" />\n";
            print "							</form>\n";
            print "							<form name=\"form_evidence\" id=\"form_remove\" class=\"form_remove\" action=\"admin_news.cgi\" method=\"post\" enctype=\"multipart/form-data\">\n";
            print "								<input type=\"hidden\" name=\"display_category_evidence\" value=\"".$display_category."\" />\n";
            print "								<input type=\"hidden\" name=\"evidence_code\" value=\"".$codice."\" />\n";
            if($evidenza eq "false") {
                print "							<input class=\"button\" type=\"submit\" name=\"evidence\" value=\"Evidenzia\" />\n";
            }else{
                print "							<input class=\"button\" type=\"submit\" name=\"hide_evidence\" value=\"Nascondi\" />\n";
            }
            print "							</form>\n";
            print "						</div>\n";
            print "					</div>\n";
        }
        print "				</div>\n";
        print "			</div>\n";    # </content_admin>
    }
    
	print <<EOF;
			<div id="openModal" class="modalDialog">
				<div>
					<a href="#close" title="Close" class="close">X</a>
					<p>Inserisci un nuovo prodotto</p>
					<form name="form_modal_insert" id="form_modal_insert" action="admin_news.cgi" method="post" enctype="multipart/form-data">
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
						<input class="form_item" id="product_code" type="text"  name="product_code" required />
						<label class="form_item" for="product_name">Nome</label>
						<input class="form_item" id="product_name" type="text" name="product_name" required />
						<label class="form_item" for="product_desc">Descrizione</label>
						<textarea class="form_item" id="product_desc" name="product_desc" required ></textarea>
						<label class="form_item" for="thumbnail_desc">Descrizione breve</label>
						<textarea class="form_item" id="thumbnail_desc"  name="thumbnail_desc" required ></textarea>
						<label class="form_item" for="product_image">Carica <span lang="en">thumbnail</span></label>
						<input class="form_item" id="product_image" type="file" name="image" required />
						<input class="submit_modal" id="submit_modal" type="submit" name="insert" value="Inserisci" />
					</form>
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