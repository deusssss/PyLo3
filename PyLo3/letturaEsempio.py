from Bio import SeqIO
import datetime

def letturaEsempio(outf="", n=""):
    
    
    stamp=str(datetime.datetime.now()).replace(" ", "").replace(".", "").replace(":", "") 
    seqpath="res/SequenzeEsempio"
     
    if(n==""):
        nome="prova" + stamp + ".fasta"
    else:
        nome=n
    
    if(outf==""):
        outfile = "res/FASTAunited/"+nome
    else:
        outfile=outf
        
    t1 = SeqIO.read(seqpath+"/seq1.fasta", "fasta")
    t2 = SeqIO.read(seqpath+"/seq2.fasta", "fasta")
    t3 = SeqIO.read(seqpath+"/seq3.fasta", "fasta")
    t4 = SeqIO.read(seqpath+"/seq4.fasta", "fasta")
    t5 = SeqIO.read(seqpath+"/seq5.fasta", "fasta")
    t6 = SeqIO.read(seqpath+"/seq6.fasta", "fasta")

    t1.id = 'Seq1'
    t2.id = 'Seq2'
    t3.id = 'Seq3'
    t4.id = 'Seq4'
    t5.id = 'Seq5'
    t6.id = 'Seq6'

    SeqIO.write([t1,t2,t3,t4,t5,t6], outfile, "fasta")
    return(outfile)




