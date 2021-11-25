#使用zipfile和itertools进行zip文件的暴力破解
import zipfile
import itertools
import time
def extractFiles(zFile,password):
    try:
        zFile.extractall(pwd=password)
        return f"Correct Password is {password}"
    except:
        return f"Bad Password {password},Retrying!"
def main():
    zFile= zipfile.ZipFile("../files/test.zip")
    chars = "1234567890"
    for try_pass in itertools.permutations(chars,4):
        password = "".join(try_pass)
        guess = extractFiles(zFile=zFile,password=password.encode('utf-8'))
        print(guess)
        time.sleep(1)
if __name__ == "__main__":
    main()