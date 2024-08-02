import os

current_script_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_script_path)

tools_path = os.path.join(current_directory, "tools")
wget_path = os.path.join(tools_path, "wget.exe")
zip_path = os.path.join(tools_path, "7z.exe")
git_path = os.path.join(tools_path, "git", "cmd", "git.exe")
setup_path = os.path.join(tools_path, "setup.exe")

mods_toml_path = os.path.join(current_directory, "mod", "mods.toml")
install_order_file_path = os.path.join(current_directory, "mod", "install_order.txt")
install_type = 15

# 构建 mod downloads 目录的路径
downloads_dir = os.path.join(current_directory, "mod", "downloads")
os.makedirs(downloads_dir, exist_ok=True)

bgt_path = os.path.join(
    current_directory, "Baldur's Gate Enhanced Edition Tetralogy.7z"
)

install_dir = os.path.join(
    current_directory,
    # f"Baldur's Gate Enhanced Edition Tetralogy {datetime.datetime.now().strftime('%Y%m%d')}",
    "Baldur's Gate Enhanced Edition Tetralogy 20240801",
)
