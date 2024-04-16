import os
#全ファイル列挙
def enumfiles(path):
    if os.path.isdir(path):
        #ディレクトリの場合
        for i in os.listdir(path):
            ff=os.path.join(path,f)
            enumfiles(ff)#
    else:
        #ファイルの場合
        print(path)
        
if __name__=="__main__":
    #指定ディレクトリ以下の全ファイル列挙
    enumfiles('./test_dir')