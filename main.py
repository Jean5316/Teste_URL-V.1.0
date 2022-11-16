## Já deixei instalado o package do Requests e também importado aqui para você. Está pronto para usar.
## E não se esquece de pesquisar sobre try: e except: para tratar erros do Request. (isso pode te ajudar)

## pode apagar esses comentários haha.

 
## Bom desafio!

import requests
def corrigir_nome(site):
        site =  site.lower().strip().replace(" ",'').split(',')
        return site

def inicia_novamente(atz_exc):
         
                if atz_exc == 's' or atz_exc == 'S':
                        sites = corrigir_nome(input('Qual site: '))
                        return sites
                elif atz_exc == 'n' or atz_exc == 'N':
                        fim = print("Programa Finalizado")
                        return fim
                else:
                        while atz_exc != 's' or 'n' or atz_exc != 'S' or 'N':
                                invalido = print("Opção invalida!")
                                inicia_novamente(input("Quer consultar mais site? "))
                                return invalido 
                                
    


        


status_code_informativa = [100,101,102,103]
status_code_sucesso = [200,201,202,203,204,205,206,207,208,226]
status_code_redirecionamento = [300,301,302,303,304,305,306,307,308]
status_code_erro_cliente = [400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,
                        416,417,418,421,422,423,424,425,426,428,429,431,451]
status_code_erro_servidor = [500,501,502,503,504,505,506,507,508,509,510,511]

sites = corrigir_nome(input("Qual o site(s): "))
urls = sites


for site in urls:
        
                #verifica o ponto
                if "." not in site:
                        print(f"Verifique a URL do {site}.")
                 #verifica http ou https       
                else: 
                        if "http"  not in site:
                                site = f"http://{site}." 

                        try: 
                                r = requests.get(site)
                                if r.status_code in status_code_sucesso or status_code_redirecionamento:
                                        site_on = print(f"{site} online, status code {r.status_code}.")
                                                                                        
                                elif r.status_code in status_code_erro_cliente or status_code_erro_servidor:
                                        site_off = print(f"{site} offline, status code {r.status_code}.") 
                                                                                       
                        except:
                                        nao_encontrou = print(f"{site} invalido ou sem resposta.")
        
inicia_novamente(input("Quer consultar mais site?(s/n)"))