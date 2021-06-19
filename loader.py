from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from http.server import BaseHTTPRequestHandler, HTTPServer
from Bio.Phylo.TreeConstruction import DistanceCalculator 
from Bio.Align.Applications import MuscleCommandline
from urllib.parse import unquote
import matplotlib.pyplot as plt
from tkinter import filedialog
from Bio import AlignIO
from Bio import Entrez
from Bio import SeqIO
from Bio import Phylo
import tkinter as tk
import webbrowser
import matplotlib
import subprocess
import zipfile
import Bio
import os




#fase 1: unione delle sequenze FASTA date in input in un unico file

def letturaEntrez( mail, seqs ):                                                                                                                #metodo di lettura delle sequenze da NCBI, accession numbers specificati in seqs
    outfile = "res/out.fasta"                                                                                                                   #percorso del file di output
    data = "res/data.txt"                                                                                                                       #percorso del file di memorizzazione dati
    Entrez.email = mail                                                                                                                         #assegnazione della mail per la connessione al database 
    t=[]                                                                                                                                        #lista temporanea per il contenimento delle sequenze
    n=[]                                                                                                                                        #lista temporanea per il contenimento dei dati relativi alle sequenze
    for seq in seqs:                                                                                                                            #ripeti per ogni accession number specificato
        with Entrez.efetch( db = "nucleotide", id = seq, rettype = "fasta", retmode = "text") as handle:                                        #connessione al database e recupero files
                seq_record = SeqIO.parse(handle, "fasta")                                                                                       #lettura dei singoli files
                for record in seq_record:                                                                                                       #ripeti per ogni sequenza all'interno di un singolo file
                    record.id = record.description.replace(" ", "_")                                                                            #modifica l'ID della sequenza per avere chiarezza alla stampa
                    n.append( "id: " + record.id + " -> nome: " + record.name + " -> descrizione: " + record.description + "\n")                #memorizza i dati relativi alla sequenza
                    t.append( record )                                                                                                          #aggiungi la sequenza a t
    SeqIO.write( t, outfile, "fasta" )                                                                                                          #salva il contenuto di t nel file dedicato         
    f = open( data, "w" )                                                                                                                       #apri il file contenente i dati della sequenza
    for i in n:                                                                                                                                 #per ogni elemento di n
        f.write( i )                                                                                                                            #scrivilo sul file
    f.close()                                                                                                                                   #chiudi il file



def letturaManuale( seqs ):                                                                                                                     #metodo di lettura delle sequenze da file, percorso specificato in seqs
    outfile = "res/out.fasta"                                                                                                                   #percorso del file di output
    data = "res/data.txt"                                                                                                                       #percorso del file di memorizzazione dati
    t=[]                                                                                                                                        #lista temporanea per il contenimento delle sequenze
    n=[]                                                                                                                                        #lista temporanea per il contenimento dei dati relativi alle sequenze
    for seq in seqs:                                                                                                                            #ripeti per ogni percorso specificato
        with open( seq ) as handle:                                                                                                             #apri il file 
            for record in SeqIO.parse( handle, "fasta" ):                                                                                       #per ogni sequenza all'interno del singolo file
                n.append( "id: " + record.id + " -> nome: " + record.name + " -> descrizione: " + record.description + "\n")                    #memorizza i dati relativi alla sequenza
                t.append( record )                                                                                                              #aggiungi la sequenza a t
    SeqIO.write( t, outfile, "fasta" )                                                                                                          #salva il contenuto di t nel file dedicato
    f = open( data, "w" )                                                                                                                       #apri il file contenente i dati della sequenza
    for i in n:                                                                                                                                 #per ogni elemento di n
        f.write( i )                                                                                                                            #scrivilo sul file
    f.close()                                                                                                                                   #chiudi il file
    




#fase 2: allineamento delle sequenze

def allineamento():                                                                                                                             #metodo di allineamento
    in_file = "res/out.fasta"                                                                                                                   #percorso del file contenente le sequenze i formato FASTA
    out_file = "res/allineamento.fasta"                                                                                                         #percorso del file di output
    clust_file = "res/conversione.aln"                                                                                                          #percorso del file contenente le sequenze allineate in formato aln
    muscle_exe = "res/muscle.exe"                                                                                                               #percorso dell'eseguibile di MUSCLE per l'allineamento
    MuscleCommandline( muscle_exe, input = in_file, out = out_file )                                                                            #MUSCLE allinea i file di input e salva il risultato in quello di output(FASTA)
    subprocess.check_output( [muscle_exe, "-in", in_file, "-out", out_file] )                                                                   #avvia il processo per MUSCLE
    Bio.AlignIO.convert( out_file, "fasta", clust_file, "clustal" )                                                                             #converti l'allineamento da FASTA a CLUSTAL



                

#fase 3: allineamento della matrice delle distanze
#fase 4: creazione dell'albero filogenetico

def maketree():                                                                                                                                 #metodo per la creazione dell'albero filogenetico a partire dal file clustal
    in_file = "res/conversione.aln"                                                                                                             #percorso del file contenente l'allineamento 
    xml_file = "res/xml.xml"                                                                                                                    #percorso del file contenente il codice XML dell'albero
    tree_file = "res/tree.png"                                                                                                                  #percorso del file contenente l'albero
    with open( in_file, "r" ) as aln:                                                                                                           #apri il file di input
        align = AlignIO.read( aln,"clustal" )                                                                                                   #mettine il contenuto in una variabile
    calculator = DistanceCalculator( 'blosum62' )                                                                                               #usa la matrice BLOSUM per calcolare la distanza fra le sequenze
    constructor = DistanceTreeConstructor( calculator , "upgma")                                                                                         #dal calcolo precedente calcola le posizioni dei rami dell'albero
    albero = constructor.build_tree( align )                                                                                                    #usa i calcoli precedenti per costruire l'albero filogenetico  
    Phylo.write( albero, xml_file, "phyloxml" )                                                                                                 #salva il codice XML dell'albero nel percorso specificato
    fig = plt.figure( figsize = ( 50, 25 ) )                                                                                                    #tramite matplotlib disegna uno schema vuoto
    matplotlib.rc( 'font', size = 12 )                                                                                                          #font di nodi e foglie
    matplotlib.rc( 'xtick', labelsize = 10 )                                                                                                    #font dell' etichetta dell'asse x
    matplotlib.rc( 'ytick', labelsize = 10 )                                                                                                    #font dell' etichetta dell'asse y
    axes = fig.add_subplot( 1, 1, 1 )                                                                                                           #aggiungi un sottografico per creare una cornice
    Phylo.draw( albero, axes = axes, do_show = False )                                                                                          #disegna l'albero filogenetico  come descritto dal file XML
    fig.savefig( tree_file )                                                                                                                    #salva la figura in un file .png
    
    

                
                
#fase 0: esecuzione dell'analisi
                
def Analisi( tipoLettura, mail="", seqs="", file=[] ):                                                                                          #metodo per l'esecuzione dell'analisi filogenetica
    if (tipoLettura == "carica"):                                                                                                               #se è stata scelta un'analisi da files caricati manualmente
        letturaManuale( file )                                                                                                                  #esegui una lettura dai files specificati
    elif ( tipoLettura == "entrez" ):                                                                                                           #se è stata scelta un'analisi da accession number di NCBI
        seqs = seqs.replace( " ", "" ).split( "," )                                                                                             #rimuovi eventuali spazi dalla stringa e trasformala in un arraydi singole stringhe
        letturaEntrez( mail, seqs )                                                                                                             #esegui download e lettura dai files specificati          
    allineamento()                                                                                                                              #esegui l'allineamento delle sequenze
    maketree()                                                                                                                                  #crea l'albero filogenetico





#classe Server

class MyServer( BaseHTTPRequestHandler ):                                                                                                       #creazione di un server locale per la comunicazione con la pagina di visualizzazione HTML
                                                                                                       
    def do_GET( self ):                                                                                                                         #metodo per la gestione delle richieste in formato GET
        self.send_response( 200 )                                                                                                               #rispondi 200:OK
        if self.path.endswith( 'albero' ):                                                                                                      #se è richiesto un albero
            self.send_header( 'Content-type', 'image/png' )                                                                                     #imposta l'header per trasmetter un immagine
            self.end_headers()                                                                                                                  #fine degli header
            self.wfile.write( open( "res/tree.png", "rb" ).read() )                                                                             #apri il file dell'albero, leggilo ed invialo
        elif self.path.endswith( 'sequenze' ):                                                                                                  #se è richiesta una sequenza
            self.send_header( 'Content-type', 'text/fasta' )                                                                                    #imposta l'header per trasmetter un file FASTA
            self.end_headers()                                                                                                                  #fine degli header
            self.wfile.write(open( "res/out.fasta", "rb" ).read() )                                                                             #apri il file delle sequenze, leggilo e invialo
        elif self.path.endswith( 'allineamento' ):                                                                                              #se è richiesto un allineamento
            self.send_header( 'Content-type', 'text/aln' )                                                                                      #imposta l'header per trasmetter un file aln
            self.end_headers()                                                                                                                  #fine degli header
            self.wfile.write( open( "res/conversione.aln", "rb" ).read() )                                                                      #apri il file dell'allineamento, leggilo ed invialo
        elif self.path.endswith( 'data' ):                                                                                                      #se è richiesto un file di dati
            self.send_header( 'Content-type', 'text/txt' )                                                                                      #imposta l'header per trasmetter un file txt
            self.end_headers()                                                                                                                  #fine degli header
            self.wfile.write( open( "res/data.txt", "rb" ).read() )                                                                             #apri il file dei dati, leggilo ed invialo
        elif self.path.endswith( 'zip' ):                                                                                                       #se sono richiesi tutti i dati
            self.send_header( 'Content-type', 'application/zip' )                                                                               #imposta l'header per trasmetter un file zip
            self.end_headers()                                                                                                                  #fine degli header
            zf = zipfile.ZipFile( "res/zip.zip", mode="w" )                                                                                     #crea un file zip
            zf.write( "res/tree.png", compress_type=0)                                                                                          #aggiungi all'archivio l'albero
            zf.write( "res/out.fasta", compress_type=0)                                                                                         #aggiungi all'archivio le sequenze
            zf.write( "res/conversione.aln", compress_type=0)                                                                                   #aggiungi all'archivio l'allineamento
            zf.write( "res/data.txt", compress_type=0)                                                                                          #aggiungi all'archivio i dati
            zf.close()                                                                                                                          #chiudi il file zip
            self.wfile.write( open( "res/zip.zip", "rb" ).read() )                                                                              #apri il file compresso, leggilo ed invialo
                        
    def do_POST( self ):                                                                                                                        #metodo per la gestione delle richieste in formato POST
        content_len = int( self.headers.get( 'Content-Length' ).split( "\n" )[0] )                                                              #recupera l'header della richiesta
        post_body = self.rfile.read( content_len )                                                                                              #leggi la lunghezza dell'header
        coms=post_body.decode( 'UTF-8' )                                                                                                        #decodifica il contenuto dell'header in una stringa
        self.send_response( 200 )                                                                                                               #rispondi 200:OK
        if( "carica" in coms ):                                                                                                                 #se è stata richiesta una lettura di files locali
            root = tk.Tk()                                                                                                                      #crea una finestra
            root.withdraw()                                                                                                                     #nascondi la finestra vuota     
            files = filedialog.askopenfilename( title = "Scegli i files FASTA", filetypes = [( "fasta files","*.fasta" )], multiple = True )    #imposta la finestra per richiedere l'inserimento di files FASTA
            Analisi( "carica", file=files )                                                                                                     #avvia l'analisi per files locali
        elif( "entrez" in coms ):                                                                                                               #se è stata richiesta una lettura di files remoti
            email = ( ( ( unquote( coms ).replace( "+", "" ) ).split( "&" ) )[0] )[12:]                                                         #recupera l'email dalla richiesta
            accs = ( ( ( unquote( coms ).replace( "+", "") ) .split( "&" ) )[1] )[17:]                                                          #recupera gli accession number dalla richiesta            
            Analisi( "entrez", mail = email, seqs = accs )                                                                                      #avvia l'analisi per files remoti
        self.send_response( 200 )                                                                                                               #rispondi 200:OK
        self.send_header( 'Content-type', "text/html" )                                                                                         #imposta l'header per trasmetter un file HTML
        self.end_headers()                                                                                                                      #fine degli header
        self.wfile.write( open( "visualization/response.html", "rb" ).read() )                                                                  #apri la pagina html di risposta, leggila ed inviala
            
        



#avvio:

def start():                                                                                                                                    #metodo per l'avvio del software
    hostName = "localhost"                                                                                                                      #hostname:localhost, server sulla macchina locale
    serverPort = 8080                                                                                                                           #porta 8080
    webbrowser.open( "file://" + os.path.realpath( "visualization/AnalisiFilogenetica.html" ) )                                                 #apri nel browser la pagina principale del software    
    webServer = HTTPServer( ( hostName, serverPort), MyServer )                                                                                 #avvia il server web locale
    print( "Server started http://%s:%s" % ( hostName, serverPort ) )                                                                           #stampa indirizzo e porta per conferma
    try:                                                                                                                                        #esegui
        webServer.serve_forever()                                                                                                               #resta in ascolto di richieste
    except KeyboardInterrupt:                                                                                                                   #all'eccezione KeyboardInterrupt(interruzione forzata)
        pass                                                                                                                                    #interrompi l'esecuzione
    webServer.server_close()                                                                                                                    #arresta il server
    print( "Server stopped." )                                                                                                                  #stampa un feedback dellachiusura del server
        
    
    
    
    
#avvio del programma    
    
start()                                                                                                                                         #richiama il metodo avvio e dai inizio all'esecuzione
