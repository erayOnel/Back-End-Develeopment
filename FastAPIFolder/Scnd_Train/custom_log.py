from fastapi.requests import Request

def log(tag="Rise", message="Null", request: Request = None):
    # default request degerini 'None' olarak atadik
    with open("log.txt", "w+") as for_log:
        # 'w+' belirtilen dosya eger bulunmuyorsa olusturmasini soyler
        for_log.write(f"{tag} : {message}")
        for_log.write(f"\t{request.url}\n")


