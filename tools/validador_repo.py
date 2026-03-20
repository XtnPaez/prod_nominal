#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
validador_repo.py

Valida la estructura documental del repo según el marco de trabajo acordado.

Reglas que controla:
1. Debe existir un único README.md en la raíz.
2. Debe existir la carpeta templates/ con:
   - template_esquema.md
   - template_tabla.md
3. Debe existir la carpeta esquemas/
4. Cada carpeta dentro de esquemas/ debe tener:
   - un archivo principal con el mismo nombre de la carpeta
     (ej: esquemas/ddbb_alimentar/ddbb_alimentar.md)
   - 01_estructura.md
   - 02_tablas_clave.md
   - 03_relaciones_internas.md
   - 04_queries_base.md
   - 05_hallazgos.md
   - 06_pendientes.md
5. Opcionalmente controla si los archivos están vacíos.
6. Opcionalmente controla si hay README.md dentro de subcarpetas
   (según el criterio definido, eso se marca como problema).

Uso:
    python validador_repo.py /ruta/al/repo
    python validador_repo.py . --strict
    python validador_repo.py . --json

Salida:
- Resumen en consola
- Código de salida 0 si todo está bien
- Código de salida 1 si hay errores
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Dict


# =========================
# Configuración del validador
# =========================

REQUIRED_ROOT_FILES = [
    "README.md",
]

REQUIRED_TEMPLATE_FILES = [
    "template_esquema.md",
    "template_tabla.md",
]

REQUIRED_SCHEMA_FILES = [
    "01_estructura.md",
    "02_tablas_clave.md",
    "03_relaciones_internas.md",
    "04_queries_base.md",
    "05_hallazgos.md",
    "06_pendientes.md",
]


@dataclass
class Issue:
    level: str   # ERROR | WARN | INFO
    path: str
    message: str


@dataclass
class ValidationResult:
    ok: bool
    repo_path: str
    issues: List[Issue]
    stats: Dict[str, int]


def is_markdown_empty(path: Path) -> bool:
    """
    Considera 'vacío' un .md si:
    - no existe contenido
    - solo tiene espacios
    - solo tiene títulos muy mínimos sin texto real
    """
    text = path.read_text(encoding="utf-8", errors="ignore").strip()

    if not text:
        return True

    # Eliminamos líneas vacías
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return True

    # Si solo hay uno o dos headings y nada más, lo consideramos casi vacío
    heading_like = [line for line in lines if line.startswith("#")]
    if len(lines) <= 2 and len(heading_like) == len(lines):
        return True

    return False


def find_nested_readmes(repo_path: Path) -> List[Path]:
    """
    Busca README.md fuera de la raíz.
    """
    nested = []
    for p in repo_path.rglob("README.md"):
        if p.parent != repo_path:
            nested.append(p)
    return sorted(nested)


def validate_repo(repo_path: Path, strict: bool = False) -> ValidationResult:
    issues: List[Issue] = []

    # -------------------------
    # 1. README raíz
    # -------------------------
    for fname in REQUIRED_ROOT_FILES:
        fpath = repo_path / fname
        if not fpath.exists():
            issues.append(Issue("ERROR", str(fpath), "Falta archivo obligatorio en raíz."))

    # -------------------------
    # 2. templates/
    # -------------------------
    templates_dir = repo_path / "templates"
    if not templates_dir.exists() or not templates_dir.is_dir():
        issues.append(Issue("ERROR", str(templates_dir), "Falta carpeta obligatoria templates/."))
    else:
        for fname in REQUIRED_TEMPLATE_FILES:
            fpath = templates_dir / fname
            if not fpath.exists():
                issues.append(Issue("ERROR", str(fpath), "Falta template obligatorio."))
            elif strict and is_markdown_empty(fpath):
                issues.append(Issue("WARN", str(fpath), "El template existe pero está vacío o casi vacío."))

    # -------------------------
    # 3. esquemas/
    # -------------------------
    esquemas_dir = repo_path / "esquemas"
    if not esquemas_dir.exists() or not esquemas_dir.is_dir():
        issues.append(Issue("ERROR", str(esquemas_dir), "Falta carpeta obligatoria esquemas/."))
    else:
        schema_dirs = sorted([p for p in esquemas_dir.iterdir() if p.is_dir()])

        if not schema_dirs:
            issues.append(Issue("WARN", str(esquemas_dir), "La carpeta esquemas/ existe pero no contiene esquemas."))

        for schema_dir in schema_dirs:
            schema_name = schema_dir.name
            main_md = schema_dir / f"{schema_name}.md"

            # Archivo principal con nombre de carpeta
            if not main_md.exists():
                issues.append(
                    Issue(
                        "ERROR",
                        str(main_md),
                        "Falta archivo principal del esquema con el mismo nombre de la carpeta."
                    )
                )
            elif strict and is_markdown_empty(main_md):
                issues.append(Issue("WARN", str(main_md), "El archivo principal del esquema está vacío o casi vacío."))

            # Archivos estándar por esquema
            for fname in REQUIRED_SCHEMA_FILES:
                fpath = schema_dir / fname
                if not fpath.exists():
                    issues.append(Issue("ERROR", str(fpath), "Falta archivo obligatorio del esquema."))
                elif strict and is_markdown_empty(fpath):
                    issues.append(Issue("WARN", str(fpath), "El archivo existe pero está vacío o casi vacío."))

    # -------------------------
    # 4. README.md fuera de raíz
    # -------------------------
    nested_readmes = find_nested_readmes(repo_path)
    for p in nested_readmes:
        issues.append(
            Issue(
                "WARN",
                str(p),
                "Se encontró un README.md fuera de la raíz; según el criterio acordado, no debería existir."
            )
        )

    # -------------------------
    # 5. Armar resultado
    # -------------------------
    error_count = sum(1 for i in issues if i.level == "ERROR")
    warn_count = sum(1 for i in issues if i.level == "WARN")
    info_count = sum(1 for i in issues if i.level == "INFO")

    result = ValidationResult(
        ok=(error_count == 0),
        repo_path=str(repo_path),
        issues=issues,
        stats={
            "errors": error_count,
            "warnings": warn_count,
            "info": info_count,
            "total_issues": len(issues),
        },
    )
    return result


def print_result(result: ValidationResult) -> None:
    print(f"\nRepo: {result.repo_path}")
    print("-" * 80)

    if not result.issues:
        print("OK: no se detectaron problemas.")
    else:
        for issue in result.issues:
            print(f"[{issue.level}] {issue.path}")
            print(f"         {issue.message}")

    print("-" * 80)
    print(
        f"Resumen -> errores: {result.stats['errors']} | "
        f"warnings: {result.stats['warnings']} | "
        f"info: {result.stats['info']} | "
        f"total: {result.stats['total_issues']}"
    )

    if result.ok:
        print("Estado final: OK")
    else:
        print("Estado final: CON ERRORES")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validador de estructura documental del repo."
    )
    parser.add_argument(
        "repo",
        nargs="?",
        default=".",
        help="Ruta al repositorio. Por defecto: directorio actual."
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Además de la existencia, controla si ciertos .md están vacíos o casi vacíos."
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Imprime la salida en JSON."
    )

    args = parser.parse_args()

    repo_path = Path(args.repo).resolve()

    if not repo_path.exists() or not repo_path.is_dir():
        print(f"ERROR: la ruta no existe o no es un directorio: {repo_path}", file=sys.stderr)
        return 1

    result = validate_repo(repo_path, strict=args.strict)

    if args.json:
        payload = asdict(result)
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print_result(result)

    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
