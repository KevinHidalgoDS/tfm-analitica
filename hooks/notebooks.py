from pathlib import Path

from mkdocs.exceptions import ConfigurationError
from mkdocs.plugins import event_priority
from mkdocs.structure.files import File


@event_priority(100)
def on_files(files, config):
    root = Path(config.config_file_path).resolve().parent
    notebook_dir = root / "notebook"

    if not notebook_dir.is_dir():
        raise ConfigurationError(f"No existe la carpeta: {notebook_dir}")

    for notebook in sorted(notebook_dir.rglob("*.ipynb")):
        if ".ipynb_checkpoints" in notebook.parts:
            continue

        uri = notebook.relative_to(root).as_posix()

        if files.get_file_from_path(uri) is not None:
            raise ConfigurationError(f"Ruta de notebook duplicada: {uri}")

        files.append(
            File(
                uri,
                src_dir=str(root),
                dest_dir=config.site_dir,
                use_directory_urls=config.use_directory_urls,
            )
        )

    return files