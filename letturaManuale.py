from Bio import SeqIO
import datetime

def letturaManuale( seqs, outf="", n=""):
    
    stamp=str(datetime.datetime.now()).replace(" ", "").replace(".", "").replace(":", "") 
    
    if(n==""):
        nome="manual" + stamp + ".fasta"
    else:
        nome=n
    
    if(outf==""):
        outfile = "res/FASTAunited/"+nome
    else:
        outfile=outf
        
    t=[]
    for seq in seqs:
        t.append(SeqIO.read(seq, "fasta"))
    

    SeqIO.write(t, outfile, "fasta")
    return(outfile)




