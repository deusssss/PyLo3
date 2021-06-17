from Bio import SeqIO
import datetime
from Bio import Entrez

def letturaEntrez( mail, seqs, db_="nucleotide", rettype_="fasta", outf="", n=""):
    
    stamp=str(datetime.datetime.now()).replace(" ", "").replace(".", "").replace(":", "") 
    Entrez.email = mail
    
    if(n==""):
        nome="entrez" + stamp + "."+rettype_
    else:
        nome=n
    
    
    if(outf==""):
        outfile = "res/FASTAunited/"+nome
    else:
        outfile=outf
        
    t=[]
    for seq in seqs:
        with Entrez.efetch(db=db_, id=seq, rettype=rettype_, retmode="text") as handle:
                seq_record = SeqIO.parse(handle, rettype_)
                for record in seq_record:
                    t.append(record)
    
    SeqIO.write(t, outfile, rettype_)
    return(outfile)
