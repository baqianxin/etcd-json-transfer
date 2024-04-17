import os
from datetime import datetime
import subprocess
from etcd import Client

# etcd 服务器备份地址和端口
etcd_host = '127.0.0.1'
etcd_port = 2379

# etcd 导出数据保存的本地目录
backup_dir = os.path.expanduser('~/etcd-backup')


def export_etcd_data():

    # 获取当前日期
    today_date = datetime.now().strftime('%Y-%m-%d')

    # 导出 etcd 数据到备份文件
    backup_filename = f'etcd_backup_{today_date}.json'
    backup_path = os.path.join(backup_dir, backup_filename)
    current_dumpfile = os.path.join("/Users/oom/", "etcd-json-converter/home-gateway.json")
    dump_cmd=f'/Users/oom/etcd-json-converter/etcd-json-transfer --endpoint=100.0.0.0:2379  export  --prefix="/apisix" --file={current_dumpfile}'
    reason=subprocess.run(dump_cmd.split())
    print(reason.returncode)
    if reason.returncode !=0:
        print(f'Exported etcd data to {backup_path} failed')
        os._exit(-1)
    if os.path.exists(current_dumpfile):
        print(f"文件存在 {current_dumpfile}")
        subprocess.run(["ls","-alh",current_dumpfile])
        subprocess.run(["mv",current_dumpfile,backup_path])
    else:
        print("文件不存在")
        subprocess.run(["ls","-alh",backup_path])

    print(f'Exported etcd data to {backup_path}')

def import_ectd_data():
    print("todo:::")

if __name__ == '__main__':
    export_etcd_data()
