import os
import shutil
import subprocess
import time

from env import setup_path, zip_path


def run_command(command, input=None):
    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
    )

    if input is None or len(input) == 0:
        output, error = process.communicate()
    else:
        inputs = input.split(b"|")

        if len(inputs) == 1:
            output, error = process.communicate(input=inputs[0])
        else:
            for input in inputs:
                process.stdin.write(input + b"\n")
                process.stdin.flush()
                time.sleep(0.1)

            output = process.stdout.read()
            error = process.stderr.read()

    if process.returncode != 0:
        msg = error
        if not msg.strip():
            msg = output
    else:
        msg = output

    try:
        msg = msg.decode("utf-8")
    except UnicodeDecodeError:
        try:
            msg = msg.decode("gbk")
        except UnicodeDecodeError:
            try:
                msg = msg.decode("latin-1")
            except UnicodeDecodeError:
                msg = "无法解码"

    if process.returncode != 0:
        print(f"命令执行失败: {command}, {msg}")
        return msg, False

    return msg, True


def unzip(filepath, extract_path, move_dir=""):
    original_dir = extract_path
    if move_dir:
        extract_path = f"{extract_path}_tmp"
    command = f'{zip_path} x "{filepath}" -o"{extract_path}" -y'
    output, success = run_command(command)
    if move_dir:
        shutil.move(os.path.join(extract_path, move_dir), original_dir)
        os.rmdir(extract_path)
    if success and "Everything is Ok" in output:
        print(f"文件 '{filepath}' 已解压到 {extract_path}")
        return True
    else:
        print(f"警告: '{filepath}' 解压失败或不是有效的压缩文件")
        return False


def uninstall_mod(install_dir, mod_name, component=None):
    print(f"卸载模组: {mod_name}")
    uninstall_exe = os.path.join(install_dir, f"setup-{mod_name}.exe")
    if os.path.exists(uninstall_exe):
        if component:
            command = f'cd "{install_dir}" && "{uninstall_exe}" --no-exit-pause --noautoupdate --language 0 --force-uninstall-list {component} --skip-at-view'
        else:
            command = f'cd "{install_dir}" && "{uninstall_exe}" --no-exit-pause --noautoupdate --language 0 --uninstall --skip-at-view'
        print(f"执行命令: {command}")
        run_command(command)
        print(f"模组 '{mod_name}' 卸载成功")
    else:
        print(f"模组 '{mod_name}' 未安装")


def install_mod(install_dir, mod_name, component, language, input=None):
    print(f"安装模组: {mod_name}:{component}")
    install_exe = os.path.join(install_dir, f"setup-{mod_name}.exe")
    if not os.path.exists(install_exe):
        shutil.copy(setup_path, install_exe)

    command = f'cd "{install_dir}" && "{install_exe}"  --no-exit-pause --noautoupdate --language {language} --skip-at-view --force-install-list {component} --logapp'
    msg, result = run_command(command, input)
    if result:
        print(f"模组 '{mod_name}:{component}' 安装成功")
        return True
    else:
        if "INSTALLED WITH WARNINGS" in msg:
            print(f"模组 '{mod_name}:{component}' 安装成功（部分警告）")
            return True
        if "SUCCESSFULLY INSTALLED" in msg:
            print(f"模组 '{mod_name}:{component}' 安装成功")
            return True

    return False
