# ----------------------------------------------------------
# サーバーへの接続情報を設定
IP_ADDRESS = '127.0.0.1' # 追記するリモート接続先 IP_address
USER_NAME = 'username'#追記するリモート接続先のユーザー
KEY_PATH = ''#keyの絶対パス
PUBLIC_KEY = ""# 追記する公開鍵文字列
# ----------------------------------------------------------

# paramikoのインポート
import paramiko


def add_ssh_key(ipaddress:str,username:str,keypath:str,publickey:str):
    cmd = f'cd /home/{username}/.ssh ; echo {publickey} >>authorized_keys'
    client = paramiko.SSHClient()
    try:
        client.set_missing_host_key_policy(paramiko.WarningPolicy()) # またはparamiko.AutoAddPolicy()

        # 上記で設定したIPアドレス、ユーザー名、キーファイルを渡す
        client.connect(ipaddress,
        username=username,
        key_filename=keypath,
        timeout=5.0)

        # コマンドの実行
        stdin, stdout, stderr = client.exec_command(cmd)
        #　エラーが存在するなら出力させる
        if len(stderr.read()) > 0:

            cmd_errresult = ''
            for line in stderr:
                cmd_errresult += line
            print(cmd_errresult)

    except Exception as e:

        print(e.__str__())

    finally:
        client.close()




if __name__ == "__main__":
    add_ssh_key(
        IP_ADDRESS,
        USER_NAME,
        KEY_PATH,
        PUBLIC_KEY        
    )
