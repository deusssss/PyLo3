import datetime
from Bio.Align.Applications import MuscleCommandline
import subprocess
import Bio

def allineamento(in_file, musf="", outf="", clustf="", nall="", nconv=""):
    
    stamp=str(datetime.datetime.now()).replace(" ", "").replace(".", "").replace(":", "") 
    
    if(nall==""):
        nomeAll= "allineamento" + stamp + ".fasta"
    else:
        nomeAll=nall
        
    if(nconv==""):
        nomeClust= "conversione" + stamp + ".aln"
    else:
        nomeClust=nconv
    
    
    if(musf==""):
        muscle_exe= "res/muscle.exe"
    else:
        muscle_exe=musf
    
    
    if(outf==""):
        out_file="res/alligned/"+nomeAll
    else:
        out_file=outf
        
    if(clustf==""):
        clust_file="res/clustal/"+nomeClust
    else:
        clust_file=clustf
    
    
    
    MuscleCommandline(muscle_exe, input=in_file, out=out_file)
    subprocess.check_output([muscle_exe, "-in", in_file, "-out", out_file])

    Bio.AlignIO.convert(out_file, "fasta", clust_file, "clustal")
        
    return(clust_file)