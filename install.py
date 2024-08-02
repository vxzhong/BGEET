import json
import os
import shutil
import sys

import tomllib

from env import (
    bgt_path,
    downloads_dir,
    install_dir,
    install_order_file_path,
    install_type,
    mods_toml_path,
)
from utils import install_mod, uninstall_mod, unzip


def extract_bgt_zip(filepath):
    if os.path.exists(install_dir):
        print(f"目录 '{install_dir}' 已存在，跳过解压")
        return False

    unzip(filepath, install_dir)
    return True


def parse_mods_toml(toml_path):
    if not os.path.exists(toml_path):
        print(f"错误: 找不到 {toml_path} 文件")
        return None

    with open(toml_path, "rb") as toml_file:
        config = tomllib.load(toml_file)
        return config


def parse_install_order(toml_config, installed, order_file):
    if not os.path.exists(order_file):
        print(f"错误: 找不到 {order_file} 文件")
        return None

    copied = {}
    with open(order_file, "r", encoding="utf-8") as order_file:
        for line in order_file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            splits = line.split(";")
            if len(splits) < 5:
                print(f"错误: {line} 不是有效的安装顺序行")
                continue

            mod_name = splits[1]
            component = splits[2]
            install = int(splits[4]) & install_type
            input_text = None
            if len(splits) > 5 and splits[5]:
                input_text = splits[5].encode("utf-8")

            installed_key = f"{mod_name}_{component}"
            if installed.get(installed_key):
                # 已经安装
                print(f"模组 {mod_name}:{component} 已安装，跳过")
                continue

            if installed_key == "stratagems_1500":
                shutil.copy(
                    os.path.join(install_dir, "override", "bgee.lua"),
                    os.path.join(install_dir, "override", "bgee.lua.1500"),
                )
                if installed.get("stratagems_1510"):
                    # 恢复 1500 之前的bgee.lua，因为 1510或者1500的rebuild_spells只能调用一次
                    shutil.copy(
                        os.path.join(install_dir, "override", "bgee.lua.1510"),
                        os.path.join(install_dir, "override", "bgee.lua"),
                    )

            if installed_key == "stratagems_1510":
                shutil.copy(
                    os.path.join(install_dir, "override", "bgee.lua"),
                    os.path.join(install_dir, "override", "bgee.lua.1510"),
                )
                if installed.get("stratagems_1500"):
                    shutil.copy(
                        os.path.join(install_dir, "override", "bgee.lua.1500"),
                        os.path.join(install_dir, "override", "bgee.lua"),
                    )

            if mod_name.lower() == "eet_gui" or mod_name.lower() == "eet_end":
                if install:
                    if install_mod(install_dir, mod_name, component, 7):
                        installed[installed_key] = True
                continue

            mod_info = toml_config.get(mod_name, None)
            if mod_info is None:
                print(f"错误: 未找到模组 {mod_name} 的信息")
                continue

            name = mod_info["name"]
            mod_dir = os.path.join(downloads_dir, name)

            if not copied.get(mod_name):
                setup_exe = os.path.join(install_dir, f"setup-{mod_name}.exe")
                if not os.path.exists(setup_exe):
                    print(f"复制 {mod_dir} 到 {install_dir}")
                    shutil.copytree(
                        mod_dir,
                        install_dir,
                        dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns(".git"),
                    )
                copied[mod_name] = True

            language = 0
            if "tra" in mod_info:
                language = mod_info["tra"].get("CN", 0)

            if splits[0] == "STD":
                if not install:
                    continue

                if install_mod(install_dir, mod_name, component, language, input_text):
                    installed[installed_key] = True


def uninstall_mods_order(
    toml_config, installed: dict, mod_name="", all=False, mod_component=None
):
    # mod_names = ["EET_end"]  # "EET_gui"
    mod_names = []
    if mod_name:
        mod_names.append(mod_name)
    if all:
        mod_names = list(toml_config.keys())
        mod_names.reverse()
        # mod_names.append("EET_end")
    for mod_name in mod_names:
        uninstall_mod(install_dir, mod_name, mod_component)
        if mod_component:
            mods = mod_component.split(" ")
            for mod_component in mods:
                if len(mod_component) > 0:
                    installed.pop(f"{mod_name}_{mod_component}", None)
        else:
            for i in list(installed.keys()):
                if i.startswith(mod_name):
                    installed.pop(i)


first = extract_bgt_zip(bgt_path)
toml_config = parse_mods_toml(mods_toml_path)
installed_json_path = os.path.join(install_dir, "installed.json")
try:
    with open(installed_json_path) as f:
        installed = json.load(f)
except FileNotFoundError:
    installed = {}

if first:
    uninstall_mods_order(toml_config, installed, mod_name="EET_end")
    # rename bgee.lua
    if os.path.exists(os.path.join(install_dir, "override", "BGEE.LUA")):
        os.rename(
            os.path.join(install_dir, "override", "BGEE.LUA"),
            os.path.join(install_dir, "override", "bgee.lua"),
        )
        # copy backup bgee.lua
        if os.path.exists(os.path.join(install_dir, "override", "bgee.lua")):
            shutil.copy(
                os.path.join(install_dir, "override", "bgee.lua"),
                os.path.join(install_dir, "override", "bgee.lua.bak"),
            )


try:
    if len(sys.argv) > 1:
        if sys.argv[1] == "ua":
            uninstall_mods_order(toml_config, installed, all=True)
        elif sys.argv[1] == "u":
            uninstall_mods_order(toml_config, installed, all=False)
        else:
            mod_component = None
            if len(sys.argv) > 2:
                mod_component = " ".join(sys.argv[2:])
            uninstall_mods_order(
                toml_config,
                installed,
                all=False,
                mod_name=sys.argv[1],
                mod_component=mod_component,
            )
    else:
        parse_install_order(toml_config, installed, install_order_file_path)
finally:
    with open(installed_json_path, "w+") as f:
        json.dump(installed, f)
