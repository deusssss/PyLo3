from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator 
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
import datetime
from Bio import Phylo
import matplotlib
import matplotlib.pyplot as plt

def maketree(in_file, xml="", tree="", ntree="", nxml=""):
    
    stamp=str(datetime.datetime.now()).replace(" ", "").replace(".", "").replace(":", "") 
    
    if(ntree==""):
        nomeAlbero= "tree" + stamp + ".png"
    else:
        nomeAlbero=ntree
        
    if(nxml==""):
        nomeXML= "xml" + stamp + ".xml"
    else:
        nomeXML=nxml
        
    
    
    if(xml==""):
        xml_file="res/xml/"+nomeXML
  
    else:
        xml_file=xml
        
    if(tree==""):
        tree_file="res/trees/"+nomeAlbero
  
    else:
        tree_file=tree
    
    with open(in_file,"r") as aln: 
        align = AlignIO.read(aln,"clustal")
    
    calculator = DistanceCalculator('blosum62')
    
    constructor = DistanceTreeConstructor(calculator)
    
    albero = constructor.build_tree(align)
    albero.rooted = True
     
    Phylo.write(albero, xml_file, "phyloxml")
    
    
    
    
    
    
    
    fig = plt.figure(figsize=(13, 5), dpi=100) # create figure & set the size 
    matplotlib.rc('font', size=12)              # fontsize of the leaf and node labels 
    matplotlib.rc('xtick', labelsize=10)       # fontsize of the tick labels
    matplotlib.rc('ytick', labelsize=10)       # fontsize of the tick labels
    axes = fig.add_subplot(1, 1, 1)
    Phylo.draw(albero, axes=axes,do_show=False)
    fig.savefig(tree_file)
    return (tree_file)
    
    
    
