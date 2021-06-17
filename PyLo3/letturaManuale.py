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
        with open(seq) as handle:
            for record in SeqIO.parse(handle, "fasta"):
                t.append(record)
    

    SeqIO.write(t, outfile, "fasta")
    return(outfile)




