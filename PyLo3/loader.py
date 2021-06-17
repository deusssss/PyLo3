import webbrowser
import os
import letturaEsempio as le
import letturaManuale as lm
import letturaEntrez as lent
import allineamento as alli 
import maketree as mt
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import unquote
import tkinter as tk
from tkinter import filedialog

def Analisi(tipoLettura, mail="", seqs="", file=[]):
    if (tipoLettura=="prova"):
        file1=le.letturaEsempio()
        
    if (tipoLettura=="carica"):
        file1=lm.letturaManuale(file)  
        
    if (tipoLettura=="entrez"):
        seqs=seqs.replace(" ", "").split(",")
        file1=lent.letturaEntrez(mail, seqs)   
            
    file2=alli.allineamento(file1)
    return(mt.maketree(file2))


hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    
    def do_GET(self):
        pass
         
    def do_POST(self):
        
        content_len = int(self.headers.get('Content-Length').split("\n")[0])
        post_body = self.rfile.read(content_len)
        
        coms=post_body.decode('UTF-8')
        
        
        if("prova" in coms):
            URL=Analisi("prova")
            
            
        elif("carica" in coms):
            
            
            root = tk.Tk()
            root.withdraw()
            

            files = filedialog.askopenfilename(title = "Scegli i files FASTA",filetypes = [("fasta files","*.fasta")], multiple=True)
            URL=Analisi("carica", file=files)
                     
        elif("entrez" in coms):
            email = (((unquote(coms).replace("+", "")).split("&"))[0])[12:]
            accs = (((unquote(coms).replace("+", "")).split("&"))[1])[17:]
            
            URL=Analisi("entrez", mail=email, seqs=accs)
        
        
        
        self.send_response(200)
        
        self.send_header('Content-type', 'image/png')
        self.end_headers()
        self.wfile.write(open(URL, "rb").read())
        
        


def start():
    webbrowser.open("file://" + os.path.realpath("visualization/AnalisiFilogenetica.html") )
    
    if __name__ == "__main__":        
        webServer = HTTPServer((hostName, serverPort), MyServer)
        print("Server started http://%s:%s" % (hostName, serverPort))
    
        try:
            webServer.serve_forever()
        except KeyboardInterrupt:
            pass
    
        webServer.server_close()
        print("Server stopped.")
start()