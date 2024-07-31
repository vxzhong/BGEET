import os
from urllib.parse import urlparse

import tomllib

from env import downloads_dir, git_path, mods_toml_path, wget_path
from utils import run_command, unzip


def get_latest_commit_sha(repo_path):
    command = f"cd {repo_path} && {git_path} rev-parse HEAD"
    output, _ = run_command(command)
    return output.strip()


def download_and_extract(mod_name, mod_info):
    name = mod_info["name"]
    url = mod_info.get("down", "file://local")
    version = mod_info.get("version", "")
    parsed_url = urlparse(url)
    is_git = parsed_url.path.endswith(".git")

    if is_git:
        # 使用 git 克隆仓库
        repo_path = os.path.join(downloads_dir, mod_info.get("save", name))
        command = f"git clone {url} {repo_path}"
        if os.path.exists(repo_path) and os.path.exists(
            os.path.join(repo_path, ".git")
        ):
            current_sha = get_latest_commit_sha(repo_path)
            if current_sha == version:
                print(f"Git 仓库 '{mod_name}' 已是最新版本 (SHA: {version})，跳过更新")
                return

            # 如果目录已存在，执行 git pull
            print(f"更新现有的 Git 仓库 '{mod_name}'")
            command = f"cd {repo_path} && {git_path} pull"
            output, success = run_command(command)
            if success:
                print(
                    f"Git 仓库 '{mod_name}' 更新到： {get_latest_commit_sha(repo_path)}"
                )
        else:
            # 如果目录不存在，执行 git clone
            print(f"克隆新的 Git 仓库 '{mod_name}'")
            command = f"{git_path} clone {url} {repo_path}"
            output, success = run_command(command)
            if success:
                print(f"Git 仓库 '{mod_name}' 已克隆到 {repo_path}")
    else:
        # 使用 wget 下载文件
        filename = os.path.basename(parsed_url.path)
        save = mod_info.get("save")
        if save:
            filename = f"{save}"
        filepath = os.path.join(downloads_dir, filename)
        if os.path.exists(filepath):
            print(f"文件 '{filename}' 已存在，跳过下载")
        else:
            command = f"{wget_path} -O {filepath} {url}"
            output, success = run_command(command)
            if not success:
                print(f"文件 '{filename}' 下载失败")
            else:
                print(f"文件 '{filename}' 已下载到 {filepath}")

        move_dir = mod_info.get("move_dir", "")
        unzip_dir = os.path.join(downloads_dir, name)

        if not os.path.exists(unzip_dir):
            unzip(filepath, unzip_dir, move_dir=move_dir)


if os.path.exists(mods_toml_path):
    with open(mods_toml_path, "rb") as toml_file:
        config = tomllib.load(toml_file)

    for mod_name, mod_info in config.items():
        print(f"处理模组: {mod_name}")
        download_and_extract(mod_name, mod_info)
else:
    print(f"错误: 在 {mods_toml_path} 找不到 mods.toml 文件")
